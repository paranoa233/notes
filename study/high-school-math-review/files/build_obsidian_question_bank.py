# -*- coding: utf-8 -*-
from __future__ import annotations

import bisect
import csv
import datetime as dt
import html
import json
import re
import shutil
import unicodedata
import urllib.parse
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "分类版"
STUDENT_PDF_DIR = SOURCE_DIR / "01_学生版-讲义"
ZIP_NAME = "学生版讲义合集_含目录-20260527171204.zip"
VAULT = ROOT / "Obsidian题库"
TODAY = dt.date.today().isoformat()
CHAPTER_FORMULA_DIR = VAULT / "07_章节题目合集_Obsidian公式版"
MD_OPEN_SCHEME = "mdopen"


PROBLEM_TOKENS = [
    "已知",
    "若",
    "设",
    "求",
    "证明",
    "求证",
    "则",
    "下列",
    "问",
    "为___",
    "___",
    "( )",
    "（ ）",
    "多选",
    "函数",
    "方程",
    "不等式",
    "取值范围",
    "最大",
    "最小",
    "概率",
    "个数",
    "正确",
    "满足",
    "如图",
    "袋",
    "随机",
    "椭圆",
    "双曲线",
    "抛物线",
    "直线",
    "圆",
    "数列",
    "三角形",
    "四面体",
    "正方体",
    "定义",
]


START_OVERRIDES = {
    # These lessons have generic cover text near the page boundary; explicit starts keep
    # the first numbered problem from being assigned to the previous lesson.
    "5-1": 5817,
    "6-1": 7985,
    # The converted Markdown contains a duplicated "第二定义" block. The second copy
    # aligns with the TOC page and avoids duplicate problem notes.
    "14-2": 12707,
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def read_zip_markdown(zip_path: Path) -> tuple[str, list[str]]:
    with zipfile.ZipFile(zip_path) as zf:
        md_name = next(info.filename for info in zf.infolist() if info.filename.lower().endswith(".md"))
        text = zf.read(md_name).decode("utf-8", errors="replace")
    return text, text.splitlines()


def parse_lessons(text: str, lines: list[str]) -> list[dict]:
    lessons: list[tuple[int, str, int]] = []
    for match in re.finditer(r"<tr><td>(\d{2})</td><td>([^<]+)</td><td>(\d+)</td></tr>", text):
        lessons.append((int(match.group(1)), html.unescape(match.group(2)), int(match.group(3))))

    for line in lines[:120]:
        match = re.match(r"\s*(\d{1,2})\s+(.+?)\s+(\d+)\s*$", line)
        if not match:
            continue
        serial = int(match.group(1))
        title = match.group(2)
        if 1 <= serial <= 78 and re.match(r"\d+-\d+", title):
            lessons.append((serial, title, int(match.group(3))))

    by_serial = {serial: (serial, title, page) for serial, title, page in lessons}
    result: list[dict] = []
    for serial in sorted(by_serial):
        _, raw_title, start_page = by_serial[serial]
        lesson_id, module_name, topic = parse_lesson_title(raw_title)
        display_title = f"{module_name}：{topic}" if module_name else topic
        module_id = lesson_id.split("-", 1)[0]
        result.append(
            {
                "serial": serial,
                "lesson_id": lesson_id,
                "raw_title": raw_title,
                "module_id": module_id,
                "module": module_name or topic,
                "topic": topic,
                "display_title": display_title,
                "start_page": start_page,
            }
        )
    return result


def parse_lesson_title(title: str) -> tuple[str, str, str]:
    match = re.match(r"(?P<lesson_id>\d+-\d+)(?P<rest>.+)", title)
    if not match:
        return title, "", title
    lesson_id = match.group("lesson_id")
    rest = match.group("rest").strip().replace(":", "：")
    if "：" in rest:
        module_name, topic = rest.split("：", 1)
    else:
        module_name, topic = "", rest
    return lesson_id, module_name, topic


def file_uri(path) -> str:
    return Path(path).resolve().as_uri()


def md_open_url(path) -> str:
    encoded = urllib.parse.quote(str(Path(path).resolve()), safe="")
    return f"{MD_OPEN_SCHEME}://open?path={encoded}"


def find_student_pdf(lesson: dict) -> Path | None:
    lesson_id = str(lesson["lesson_id"])
    matches: list[Path] = []
    if STUDENT_PDF_DIR.exists():
        for pdf in sorted(STUDENT_PDF_DIR.glob(f"{lesson_id}*.pdf")):
            remainder = pdf.stem[len(lesson_id) :]
            if remainder and remainder[0].isdigit():
                continue
            matches.append(pdf)
    if matches:
        return matches[0]

    fallback = SOURCE_DIR / "学生版讲义合集_含目录.pdf"
    return fallback if fallback.exists() else None


def attach_lesson_source_pdfs(lessons: list[dict]) -> None:
    for lesson in lessons:
        pdf = find_student_pdf(lesson)
        if not pdf:
            lesson["source_pdf"] = ""
            lesson["source_pdf_uri"] = ""
            lesson["source_pdf_name"] = ""
            continue
        lesson["source_pdf"] = str(pdf.resolve())
        lesson["source_pdf_uri"] = file_uri(pdf)
        lesson["source_pdf_name"] = pdf.name


def normalize_for_match(text: str) -> str:
    remove_chars = "[]【】()（）<>《》“”\"'，,。.．、:：;；!！?？&-—_/\\ "
    value = unicodedata.normalize("NFKC", text).lower().translate(str.maketrans("", "", remove_chars))
    for token in [
        "讲义",
        "专题",
        "模块",
        "第",
        "十一",
        "十二",
        "十三",
        "十四",
        "十五",
        "十六",
        "一",
        "二",
        "三",
        "四",
        "五",
        "六",
        "七",
        "八",
        "九",
        "十",
        "选学",
    ]:
        value = value.replace(token, "")
    return value


def estimate_page_line(lines: list[str], page0: int) -> int:
    first_by_page: dict[int, int] = {}
    for line_no, line in enumerate(lines, 1):
        match = re.search(r"images/(\d+)_", line)
        if match:
            first_by_page.setdefault(int(match.group(1)), line_no)

    anchors = sorted(first_by_page.items())
    pages = [page for page, _ in anchors]
    pos = bisect.bisect_left(pages, page0)
    if pos < len(anchors) and anchors[pos][0] == page0:
        return anchors[pos][1]

    before = anchors[pos - 1] if pos > 0 else None
    after = anchors[pos] if pos < len(anchors) else None
    if before and after:
        page_a, line_a = before
        page_b, line_b = after
        return round(line_a + (page0 - page_a) * (line_b - line_a) / (page_b - page_a))
    return (after or before or (0, 115))[1]


def compute_lesson_boundaries(lessons: list[dict], lines: list[str]) -> None:
    candidates: list[tuple[int, str, str, bool]] = []
    for line_no, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped in {"---", "--"}:
            continue
        if stripped.startswith("#") or (len(stripped) <= 45 and not re.match(r"^[A-D][.．]", stripped)):
            normalized = normalize_for_match(stripped)
            if len(normalized) >= 2:
                candidates.append((line_no, stripped, normalized, stripped.startswith("#")))

    starts: list[int] = []
    for lesson in lessons:
        lesson_id = lesson["lesson_id"]
        estimate = estimate_page_line(lines, int(lesson["start_page"]) - 1)
        keyword = lesson["topic"] or lesson["module"] or lesson["display_title"]
        normalized_keyword = normalize_for_match(keyword)
        matches: list[tuple[int, int, str]] = []
        for line_no, text, normalized, is_heading in candidates:
            if abs(line_no - estimate) > 360:
                continue
            if not normalized_keyword or (normalized_keyword not in normalized and normalized not in normalized_keyword):
                continue
            score = abs(line_no - estimate)
            if is_heading:
                score -= 25
            if "专题" in text or "模块" in text:
                score -= 20
            if keyword.replace(" ", "") in text.replace(" ", ""):
                score -= 15
            if line_no < estimate:
                score -= 3
            if abs(line_no - estimate) > 90 and not (
                "专题" in text or "模块" in text or keyword.replace(" ", "") in text.replace(" ", "")
            ):
                score += 160
            matches.append((score, line_no, text))

        start = min(matches)[1] if matches else estimate
        starts.append(START_OVERRIDES.get(lesson_id, start))

    for index, lesson in enumerate(lessons):
        lesson["start_line"] = starts[index]
        lesson["end_line"] = starts[index + 1] if index + 1 < len(starts) else len(lines) + 1


def section_kind(heading: str) -> str:
    if "作业" in heading:
        return "作业"
    if "挑战" in heading:
        return "挑战自我"
    if "经典例题" in heading or "例题" in heading:
        return "经典例题"
    if "专项练习" in heading or "实战演练" in heading or "习题" in heading:
        return "练习"
    if "知识清单" in heading:
        return "知识清单"
    if "前言" in heading or "重点笔记" in heading or "补充知识" in heading or "通法" in heading:
        return "讲义"
    return ""


def looks_like_problem(text: str) -> bool:
    return any(token in text for token in PROBLEM_TOKENS) or len(text) > 70


def convert_images_to_obsidian_links(text: str) -> str:
    return re.sub(r"!\[[^\]]*\]\(images/([^)]+)\)", r"![[05_附件/images/\1]]", text)


def clean_block(block: list[str]) -> str:
    raw = "\n".join(block).strip()
    raw = convert_images_to_obsidian_links(raw)
    return raw.strip() + "\n"


def parse_problem_blocks(lessons: list[dict], lines: list[str]) -> list[dict]:
    raw_items: list[tuple[int, int, str]] = []
    headings: list[tuple[int, str]] = []
    heading_lines: list[int] = []

    number_re = re.compile(r"^\s*(\d{1,3})[\.．、]\s*(\S.*)$")
    for line_no, line in enumerate(lines, 1):
        stripped = line.strip()
        if re.match(r"^#{1,6}\s+", stripped):
            headings.append((line_no, re.sub(r"^#+\s*", "", stripped)))
            heading_lines.append(line_no)
        match = number_re.match(line)
        if match:
            raw_items.append((line_no, int(match.group(1)), match.group(2).strip()))

    heading_numbers = [line_no for line_no, _ in headings]
    problems: list[dict] = []

    for lesson in lessons:
        lesson_order = 0
        for raw_index, (line_no, original_number, first_line) in enumerate(raw_items):
            if not (lesson["start_line"] <= line_no < lesson["end_line"]):
                continue

            heading_index = bisect.bisect_right(heading_numbers, line_no) - 1
            section = headings[heading_index][1] if heading_index >= 0 else ""
            kind = section_kind(section)
            if not kind:
                for lookback in range(heading_index - 1, max(-1, heading_index - 5), -1):
                    inherited = section_kind(headings[lookback][1])
                    if inherited:
                        kind = inherited
                        break

            problem_like = looks_like_problem(first_line)
            include = kind in {"作业", "挑战自我", "经典例题", "练习"} or problem_like
            if kind in {"讲义", ""} and not problem_like:
                include = False
            if kind == "知识清单" and not problem_like:
                include = False
            if not include:
                continue

            next_raw = raw_items[raw_index + 1][0] if raw_index + 1 < len(raw_items) else len(lines) + 1
            next_heading_pos = bisect.bisect_right(heading_lines, line_no)
            next_heading = heading_lines[next_heading_pos] if next_heading_pos < len(heading_lines) else len(lines) + 1
            block_end = min(next_raw, next_heading, lesson["end_line"])
            block = clean_block(lines[line_no - 1 : block_end - 1])

            lesson_order += 1
            problem_id = f"{lesson['lesson_id']}-{lesson_order}"
            problems.append(
                {
                    "problem_id": problem_id,
                    "lesson_id": lesson["lesson_id"],
                    "lesson_title": lesson["display_title"],
                    "module_id": lesson["module_id"],
                    "module": lesson["module"],
                    "topic": lesson["topic"],
                    "source_order": lesson_order,
                    "original_number": original_number,
                    "section": section,
                    "kind": kind or "题目",
                    "source_line": line_no,
                    "source_end_line": block_end,
                    "content": block,
                }
            )

    return problems


def slug(value: str) -> str:
    value = value.replace(":", "：").strip()
    value = re.sub(r'[<>:"/\\|?*]', "-", value)
    value = re.sub(r"\s+", "", value)
    return value[:80]


def lesson_dir(lesson: dict) -> Path:
    module_folder = f"{lesson['module_id']}_{slug(lesson['module'])}"
    lesson_folder = f"{lesson['lesson_id']}_{slug(lesson['topic'])}"
    return Path("01_题目") / module_folder / lesson_folder


def lesson_index_path(lesson: dict) -> Path:
    module_folder = f"{lesson['module_id']}_{slug(lesson['module'])}"
    return Path("03_讲义索引") / module_folder / f"{lesson['lesson_id']}_{slug(lesson['topic'])}.md"


def solution_dir_for(problem: dict) -> Path:
    module_folder = f"{problem['module_id']}_{slug(problem['module'])}"
    lesson_folder = f"{problem['lesson_id']}_{slug(problem['topic'])}"
    return Path("02_我的解答") / module_folder / lesson_folder


def frontmatter_from_existing(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def yaml_scalar(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str], indent: str = "") -> str:
    return "\n".join(f"{indent}- {yaml_scalar(value)}" for value in values)


def problem_note(problem: dict, lesson_note_rel: Path, solution_rel: Path, existing: dict[str, str]) -> str:
    status = existing.get("status", "todo") or "todo"
    solution_link = existing.get("solution", f"[[{solution_rel.as_posix()}|我的解答]]")
    tags = ["题库", "高中数学", f"module/{problem['module_id']}", f"lesson/{problem['lesson_id']}"]
    source_pdf_uri = problem.get("source_pdf_uri", "")
    source_pdf_path = problem.get("source_pdf", "")
    source_pdf_block = ""
    frontmatter = [
        "---",
        'type: "problem"',
        f"problem_id: {yaml_scalar(problem['problem_id'])}",
        f"lesson_id: {yaml_scalar(problem['lesson_id'])}",
        f"lesson_title: {yaml_scalar(problem['lesson_title'])}",
        f"module_id: {yaml_scalar(problem['module_id'])}",
        f"module: {yaml_scalar(problem['module'])}",
        f"topic: {yaml_scalar(problem['topic'])}",
        f"source_order: {problem['source_order']}",
        f"original_number: {problem['original_number']}",
        f"section: {yaml_scalar(problem['section'])}",
        f"kind: {yaml_scalar(problem['kind'])}",
        f"status: {yaml_scalar(status)}",
        f"solution: {yaml_scalar(solution_link)}",
        f"source_line: {problem['source_line']}",
    ]
    if source_pdf_uri:
        frontmatter.extend(
            [
                f"source_pdf: {yaml_scalar(source_pdf_uri)}",
                f"source_pdf_path: {yaml_scalar(source_pdf_path)}",
                f"source_pdf_name: {yaml_scalar(problem.get('source_pdf_name', ''))}",
            ]
        )
    frontmatter.extend(
        [
            f"created: {yaml_scalar(TODAY)}",
            'generated_by: "question_bank_builder"',
            "tags:",
            yaml_list(tags, "  "),
            "---",
            "",
        ]
    )
    return (
        "\n".join(frontmatter)
        + f"# {problem['problem_id']}\n\n"
        + f"> 讲义：[[{lesson_note_rel.as_posix()}|{problem['lesson_id']} {problem['lesson_title']}]]  \n"
        + f"> 来源：{problem['kind']} / {problem['section']}  \n"
        + source_pdf_block
        + f"> 原始题号：{problem['original_number']}  \n"
        + f"> 状态：`{status}`\n\n"
        + "## 题目\n\n"
        + problem["content"]
        + "\n## 我的解答\n\n"
        + f"{solution_link}\n\n"
        + "> 把文件名以本题编号开头的 Markdown、图片、PDF 或 Word 文档放进 `99_上传入口`，再运行导入工具，系统会自动关联到这里。\n"
    )


def lesson_note(lesson: dict, count: int) -> str:
    lesson_folder = lesson_dir(lesson).as_posix()
    source_pdf_uri = lesson.get("source_pdf_uri", "")
    source_pdf_path = lesson.get("source_pdf", "")
    source_pdf_frontmatter = ""
    source_pdf_line = ""
    if source_pdf_uri:
        source_pdf_frontmatter = (
            f"source_pdf: {yaml_scalar(source_pdf_uri)}\n"
            f"source_pdf_path: {yaml_scalar(source_pdf_path)}\n"
            f"source_pdf_name: {yaml_scalar(lesson.get('source_pdf_name', ''))}\n"
        )
    return f"""---
type: "lesson"
lesson_id: {yaml_scalar(lesson["lesson_id"])}
lesson_title: {yaml_scalar(lesson["display_title"])}
module_id: {yaml_scalar(lesson["module_id"])}
module: {yaml_scalar(lesson["module"])}
topic: {yaml_scalar(lesson["topic"])}
start_page: {lesson["start_page"]}
problem_count: {count}
{source_pdf_frontmatter}generated_by: "question_bank_builder"
tags:
  - "讲义索引"
  - "题库"
---
# {lesson["lesson_id"]} {lesson["display_title"]}

[[00_控制台/总览|返回总览]]

- 题目数：{count}
- 原合集起始页：{lesson["start_page"]}
{source_pdf_line}- 题目目录：`{lesson_folder}`

```dataview
TABLE problem_id AS 编号, kind AS 类型, section AS 板块, status AS 状态, file.link AS 题目, solution AS 解答
FROM "{lesson_folder}"
WHERE type = "problem"
SORT source_order ASC
```
"""


def root_readme(total: int) -> str:
    return f"""# 高中数学 Obsidian 题库

这个 vault 已经把学生版讲义拆成独立题目笔记，共 `{total}` 题。题号按原讲义编号扩展，例如 `10-3-3` 表示 `10-3 数列：特征根` 的第 3 题。

建议先打开：

- [[00_控制台/总览]]
- [[00_控制台/上传解答]]
- [[00_控制台/题目浏览]]

后续上传解答时，把文件放进 `99_上传入口`，文件名以题号开头，例如 `10-3-3.png`、`10-3-3.md`、`10-3-3 我的解答.pdf`，再运行 `tools/import_solutions.py`。
"""


def overview_note(total: int) -> str:
    return f"""# 总览

共 `{total}` 道题。这个页面使用 Dataview 展示进度；如果你还没装 Dataview，也可以打开同目录下的 `进度看板.html`。

```dataviewjs
const problems = dv.pages('"01_题目"').where(p => p.type === "problem");
const total = problems.length;
const done = problems.where(p => ["done", "submitted"].includes(String(p.status))).length;
const pct = total ? Math.round(done / total * 100) : 0;
function bar(value) {{
  return `<div style="height:10px;background:#e5e7eb;border-radius:999px;overflow:hidden"><div style="height:10px;width:${{value}}%;background:#2f9e8f"></div></div>`;
}}
dv.paragraph(`<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:10px 0 18px">
  <div style="border:1px solid #e5e7eb;border-radius:8px;padding:12px"><b>总题数</b><div style="font-size:28px">${{total}}</div></div>
  <div style="border:1px solid #e5e7eb;border-radius:8px;padding:12px"><b>已上传/完成</b><div style="font-size:28px">${{done}}</div></div>
  <div style="border:1px solid #e5e7eb;border-radius:8px;padding:12px"><b>总进度</b><div style="font-size:28px">${{pct}}%</div>${{bar(pct)}}</div>
</div>`);
const modules = problems.groupBy(p => p.module_id + " " + p.module)
  .map(g => {{
    const c = g.rows.length;
    const d = g.rows.where(p => ["done", "submitted"].includes(String(p.status))).length;
    return [g.key, c, d, Math.round(d / c * 100), bar(Math.round(d / c * 100))];
  }});
dv.table(["模块", "题数", "已上传/完成", "进度", ""], modules);
```

## 快捷入口

- [[00_控制台/上传解答]]
- [[00_控制台/题目浏览]]
- [[00_控制台/最近上传]]
- [[00_控制台/可视化进度]]
"""


def upload_note() -> str:
    return """# 上传解答

把你的解答文件放到 `99_上传入口`。文件名要以题号开头：

- `10-3-3.md`
- `10-3-3.png`
- `10-3-3 我的解答.pdf`
- `10-3-3 二刷.docx`

然后运行 `tools/import_solutions.py`。系统会把文件移入对应题目的解答附件夹，创建或更新“我的解答”笔记，并把题目状态改为 `submitted`。

Markdown 解答也可以写 frontmatter：

```yaml
---
problem_id: 10-3-3
status: done
---
```

可用状态：`todo`、`submitted`、`done`、`review`、`stuck`。
"""


def browser_note() -> str:
    return """# 题目浏览

```dataview
TABLE problem_id AS 编号, lesson_title AS 讲义, kind AS 类型, section AS 板块, status AS 状态, file.link AS 题目, solution AS 解答
FROM "01_题目"
WHERE type = "problem"
SORT module_id ASC, lesson_id ASC, source_order ASC
```
"""


def recent_note() -> str:
    return """# 最近上传

```dataview
TABLE problem_id AS 编号, status AS 状态, updated AS 更新时间, file.link AS 解答
FROM "02_我的解答"
WHERE type = "solution"
SORT updated DESC
LIMIT 50
```
"""


def visual_note() -> str:
    return """# 可视化进度

如果 Obsidian 没有直接显示下面的页面，可以在文件管理器中打开 `00_控制台/进度看板.html`。

<iframe src="进度看板.html" style="width:100%; height:760px; border:0; border-radius:8px;"></iframe>
"""


def inbox_readme() -> str:
    return """# 上传入口

把解答文件放在这个文件夹里，文件名以题号开头，例如：

- `10-3-3.md`
- `10-3-3.png`
- `10-3-3 我的解答.pdf`

放好之后运行 `tools/import_solutions.py`。导入成功后，文件会被移动到对应题目的附件文件夹。
"""


def solution_template() -> str:
    return """---
type: "solution"
problem_id: ""
status: "submitted"
confidence: ""
updated: ""
tags:
  - "我的解答"
---
# 我的解答

## 思路

## 过程

## 复盘
"""


def problem_template() -> str:
    return """---
type: "problem"
problem_id: ""
lesson_id: ""
status: "todo"
tags:
  - "题库"
---
# 题目

## 我的解答
"""


def render_dashboard(problems: list[dict], lessons: list[dict]) -> str:
    data = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "total": len(problems),
        "modules": [],
        "lessons": [],
    }
    status_by_id = {p["problem_id"]: p.get("status", "todo") for p in problems}
    module_order: dict[str, dict] = {}
    for lesson in lessons:
        module_key = f"{lesson['module_id']} {lesson['module']}"
        module_order.setdefault(module_key, {"name": module_key, "total": 0, "done": 0})
        lesson_problems = [p for p in problems if p["lesson_id"] == lesson["lesson_id"]]
        total = len(lesson_problems)
        done = sum(1 for p in lesson_problems if status_by_id[p["problem_id"]] in {"submitted", "done"})
        module_order[module_key]["total"] += total
        module_order[module_key]["done"] += done
        data["lessons"].append(
            {
                "id": lesson["lesson_id"],
                "title": lesson["display_title"],
                "module": module_key,
                "total": total,
                "done": done,
                "pct": round(done / total * 100) if total else 0,
            }
        )
    for module in module_order.values():
        total = module["total"]
        done = module["done"]
        module["pct"] = round(done / total * 100) if total else 0
        data["modules"].append(module)

    payload = json.dumps(data, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>题库进度看板</title>
<style>
  :root {{
    color-scheme: light;
    --ink: #17202a;
    --muted: #667085;
    --line: #d9dee7;
    --bg: #f7f8fb;
    --panel: #ffffff;
    --teal: #2f9e8f;
    --gold: #c7922b;
    --coral: #d86b5b;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
    background: var(--bg);
    color: var(--ink);
  }}
  main {{ max-width: 1180px; margin: 0 auto; padding: 24px; }}
  header {{ display:flex; justify-content:space-between; gap:16px; align-items:flex-end; margin-bottom:18px; }}
  h1 {{ margin:0; font-size:28px; letter-spacing:0; }}
  .stamp {{ color:var(--muted); font-size:13px; }}
  .cards {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-bottom:18px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px; }}
  .label {{ color:var(--muted); font-size:13px; }}
  .num {{ font-size:32px; font-weight:750; margin-top:4px; }}
  .bar {{ height:10px; background:#e7ebf1; border-radius:999px; overflow:hidden; margin-top:8px; }}
  .fill {{ height:100%; width:0; background:var(--teal); }}
  section {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px; margin-bottom:14px; }}
  h2 {{ font-size:16px; margin:0 0 10px; }}
  .module-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }}
  .module {{ border:1px solid var(--line); border-radius:8px; padding:10px; }}
  .module-title {{ font-weight:700; font-size:14px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .module-meta {{ color:var(--muted); font-size:12px; margin-top:3px; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; }}
  th, td {{ border-bottom:1px solid var(--line); padding:8px 6px; text-align:left; }}
  th {{ color:var(--muted); font-weight:650; }}
  @media (max-width: 760px) {{
    main {{ padding:14px; }}
    header {{ display:block; }}
    .cards {{ grid-template-columns:1fr; }}
    table {{ font-size:12px; }}
  }}
</style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>题库进度看板</h1>
      <div class="stamp" id="stamp"></div>
    </div>
  </header>
  <div class="cards" id="cards"></div>
  <section>
    <h2>模块进度</h2>
    <div class="module-grid" id="modules"></div>
  </section>
  <section>
    <h2>讲义进度</h2>
    <table>
      <thead><tr><th>讲义</th><th>模块</th><th>进度</th><th>完成</th></tr></thead>
      <tbody id="lessons"></tbody>
    </table>
  </section>
</main>
<script>
const data = {payload};
const done = data.modules.reduce((sum, m) => sum + m.done, 0);
const pct = data.total ? Math.round(done / data.total * 100) : 0;
function bar(pct) {{
  return `<div class="bar"><div class="fill" style="width:${{pct}}%"></div></div>`;
}}
document.getElementById("stamp").textContent = `生成时间：${{data.generated_at}}`;
document.getElementById("cards").innerHTML = [
  ["总题数", data.total],
  ["已上传/完成", done],
  ["总进度", `${{pct}}%`]
].map(([label, value], idx) => `<div class="card"><div class="label">${{label}}</div><div class="num">${{value}}</div>${{idx===2 ? bar(pct) : ""}}</div>`).join("");
document.getElementById("modules").innerHTML = data.modules.map(m => `
  <div class="module">
    <div class="module-title" title="${{m.name}}">${{m.name}}</div>
    <div class="module-meta">${{m.done}} / ${{m.total}}，${{m.pct}}%</div>
    ${{bar(m.pct)}}
  </div>
`).join("");
document.getElementById("lessons").innerHTML = data.lessons.map(l => `
  <tr>
    <td>${{l.id}} ${{l.title}}</td>
    <td>${{l.module}}</td>
    <td>${{bar(l.pct)}}</td>
    <td>${{l.done}} / ${{l.total}}</td>
  </tr>
`).join("");
</script>
</body>
</html>
"""


IMPORT_SOLUTIONS_SCRIPT = r'''# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
INBOX = VAULT / "99_上传入口"
MANIFEST = VAULT / "04_原始资料" / "problems.json"
ATTACH_ROOT = VAULT / "05_附件" / "解答附件"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    data: dict[str, str] = {}
    if not match:
        return data, text
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data, text[match.end():]


def find_problem_id(path: Path, text: str | None = None) -> tuple[str | None, str]:
    name_match = re.search(r"(\d{1,2}-\d{1,2}-\d{1,3})", path.stem)
    if name_match:
        return name_match.group(1), "filename"
    if text:
        fm, _ = strip_frontmatter(text)
        for key in ("problem_id", "题号", "编号"):
            if key in fm:
                return fm[key], "frontmatter"
        body_match = re.search(r"(?:problem_id|题号|编号)\s*[:：]\s*(\d{1,2}-\d{1,2}-\d{1,3})", text)
        if body_match:
            return body_match.group(1), "body"
    return None, "missing"


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = strip_frontmatter(text)
    return fm, body, text


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_text(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def update_problem_status(problem_note: Path, status: str, solution_link: str) -> None:
    text = problem_note.read_text(encoding="utf-8", errors="replace")
    now = dt.datetime.now().isoformat(timespec="seconds")
    if not text.startswith("---\n"):
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        return
    fm = text[4:end].splitlines()
    body = text[end + 5 :]
    wanted = {
        "status": yaml_quote(status),
        "solution": yaml_quote(solution_link),
        "updated": yaml_quote(now),
    }
    seen: set[str] = set()
    new_lines: list[str] = []
    for line in fm:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in wanted and not line.startswith(" "):
            new_lines.append(f"{key}: {wanted[key]}")
            seen.add(key)
        else:
            new_lines.append(line)
    for key, value in wanted.items():
        if key not in seen:
            new_lines.append(f"{key}: {value}")
    write_text(problem_note, "---\n" + "\n".join(new_lines) + "\n---\n" + body)


def append_solution_note(solution_note: Path, problem_id: str, problem_note: Path, content: str, status: str) -> None:
    now = dt.datetime.now().isoformat(timespec="seconds")
    header = (
        "---\n"
        'type: "solution"\n'
        f"problem_id: {yaml_quote(problem_id)}\n"
        f"status: {yaml_quote(status)}\n"
        f"updated: {yaml_quote(now)}\n"
        'tags:\n'
        '  - "我的解答"\n'
        "---\n"
        f"# {problem_id} 我的解答\n\n"
        f"对应题目：[[{rel(problem_note)}|{problem_id}]]\n\n"
    )
    if solution_note.exists():
        existing = solution_note.read_text(encoding="utf-8", errors="replace").rstrip()
        write_text(solution_note, existing + f"\n\n## 上传 {now}\n\n" + content.strip() + "\n")
    else:
        solution_note.parent.mkdir(parents=True, exist_ok=True)
        write_text(solution_note, header + "## 上传 " + now + "\n\n" + content.strip() + "\n")


def import_one(path: Path, problems: dict) -> tuple[bool, str]:
    suffix = path.suffix.lower()
    text = None
    fm: dict[str, str] = {}
    body = ""
    if suffix in {".md", ".markdown", ".txt"}:
        fm, body, text = parse_frontmatter(path)
    problem_id, source = find_problem_id(path, text)
    if not problem_id:
        return False, f"未识别题号：{path.name}"
    if problem_id not in problems:
        return False, f"题号不存在：{problem_id} ({path.name})"

    problem = problems[problem_id]
    problem_note = VAULT / problem["note_path"]
    solution_dir = VAULT / problem["solution_dir"]
    solution_note = VAULT / problem["solution_note"]
    attach_dir = ATTACH_ROOT / problem_id
    attach_dir.mkdir(parents=True, exist_ok=True)
    solution_dir.mkdir(parents=True, exist_ok=True)

    status = fm.get("status", "submitted")
    if status not in {"todo", "submitted", "done", "review", "stuck"}:
        status = "submitted"

    if suffix in {".md", ".markdown", ".txt"}:
        archive_path = attach_dir / path.name
        if archive_path.exists():
            archive_path = attach_dir / f"{path.stem}-{dt.datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        shutil.move(str(path), archive_path)
        content = body.strip() or f"[[{rel(archive_path)}]]"
    else:
        target = attach_dir / path.name
        if target.exists():
            target = attach_dir / f"{path.stem}-{dt.datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        shutil.move(str(path), target)
        if suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}:
            content = f"![[{rel(target)}]]"
        else:
            content = f"[[{rel(target)}|{target.name}]]"

    append_solution_note(solution_note, problem_id, problem_note, content, status)
    solution_link = f"[[{rel(solution_note)}|我的解答]]"
    update_problem_status(problem_note, status, solution_link)
    return True, f"{problem_id} <- {path.name} ({source})"


def main() -> int:
    if not MANIFEST.exists():
        print("找不到 problems.json，请先生成题库。")
        return 1
    data = read_json(MANIFEST)
    problems = {item["problem_id"]: item for item in data["problems"]}
    files = [
        path
        for path in INBOX.rglob("*")
        if path.is_file()
        and not path.name.startswith("README")
        and path.suffix.lower() in {".md", ".markdown", ".txt", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".pdf", ".docx"}
    ]
    if not files:
        print("上传入口里暂时没有可导入的文件。")
        return 0

    ok = 0
    for path in files:
        success, message = import_one(path, problems)
        print(message)
        ok += int(success)

    refresh = VAULT / "tools" / "refresh_progress.py"
    if refresh.exists():
        subprocess.run([sys.executable, str(refresh)], check=False)

    print(f"完成：成功导入 {ok} 个文件，剩余 {len(files) - ok} 个需要检查。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


REFRESH_PROGRESS_SCRIPT = r'''# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / "04_原始资料" / "problems.json"


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    data: dict[str, str] = {}
    if not match:
        return data
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def write_text(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def render_dashboard(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>题库进度看板</title>
<style>
  :root {{ --ink:#17202a; --muted:#667085; --line:#d9dee7; --bg:#f7f8fb; --panel:#fff; --teal:#2f9e8f; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--ink); }}
  main {{ max-width:1180px; margin:0 auto; padding:24px; }}
  header {{ display:flex; justify-content:space-between; gap:16px; align-items:flex-end; margin-bottom:18px; }}
  h1 {{ margin:0; font-size:28px; letter-spacing:0; }}
  .stamp,.label,.module-meta {{ color:var(--muted); }}
  .cards {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-bottom:18px; }}
  .card,section,.module {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; }}
  .card {{ padding:14px; }}
  .num {{ font-size:32px; font-weight:750; margin-top:4px; }}
  .bar {{ height:10px; background:#e7ebf1; border-radius:999px; overflow:hidden; margin-top:8px; }}
  .fill {{ height:100%; background:var(--teal); }}
  section {{ padding:14px; margin-bottom:14px; }}
  h2 {{ font-size:16px; margin:0 0 10px; }}
  .module-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }}
  .module {{ padding:10px; }}
  .module-title {{ font-weight:700; font-size:14px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .module-meta {{ font-size:12px; margin-top:3px; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; }}
  th,td {{ border-bottom:1px solid var(--line); padding:8px 6px; text-align:left; }}
  th {{ color:var(--muted); font-weight:650; }}
  @media(max-width:760px) {{ main {{ padding:14px; }} header {{ display:block; }} .cards {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<main>
  <header><div><h1>题库进度看板</h1><div class="stamp" id="stamp"></div></div></header>
  <div class="cards" id="cards"></div>
  <section><h2>模块进度</h2><div class="module-grid" id="modules"></div></section>
  <section><h2>讲义进度</h2><table><thead><tr><th>讲义</th><th>模块</th><th>进度</th><th>完成</th></tr></thead><tbody id="lessons"></tbody></table></section>
</main>
<script>
const data = {payload};
const done = data.modules.reduce((sum, m) => sum + m.done, 0);
const pct = data.total ? Math.round(done / data.total * 100) : 0;
function bar(pct) {{ return `<div class="bar"><div class="fill" style="width:${{pct}}%"></div></div>`; }}
document.getElementById("stamp").textContent = `生成时间：${{data.generated_at}}`;
document.getElementById("cards").innerHTML = [["总题数",data.total],["已上传/完成",done],["总进度",`${{pct}}%`]].map(([label,value],idx)=>`<div class="card"><div class="label">${{label}}</div><div class="num">${{value}}</div>${{idx===2?bar(pct):""}}</div>`).join("");
document.getElementById("modules").innerHTML = data.modules.map(m=>`<div class="module"><div class="module-title" title="${{m.name}}">${{m.name}}</div><div class="module-meta">${{m.done}} / ${{m.total}}，${{m.pct}}%</div>${{bar(m.pct)}}</div>`).join("");
document.getElementById("lessons").innerHTML = data.lessons.map(l=>`<tr><td>${{l.id}} ${{l.title}}</td><td>${{l.module}}</td><td>${{bar(l.pct)}}</td><td>${{l.done}} / ${{l.total}}</td></tr>`).join("");
</script>
</body>
</html>
"""


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = data["problems"]
    lessons = data["lessons"]
    status_by_id = {}
    for problem in problems:
        note = VAULT / problem["note_path"]
        fm = read_frontmatter(note) if note.exists() else {}
        status_by_id[problem["problem_id"]] = fm.get("status", problem.get("status", "todo"))
        problem["status"] = status_by_id[problem["problem_id"]]

    module_order: dict[str, dict] = {}
    out = {"generated_at": dt.datetime.now().isoformat(timespec="seconds"), "total": len(problems), "modules": [], "lessons": []}
    for lesson in lessons:
        module_key = f"{lesson['module_id']} {lesson['module']}"
        module_order.setdefault(module_key, {"name": module_key, "total": 0, "done": 0})
        rows = [p for p in problems if p["lesson_id"] == lesson["lesson_id"]]
        total = len(rows)
        done = sum(1 for p in rows if status_by_id.get(p["problem_id"]) in {"submitted", "done"})
        module_order[module_key]["total"] += total
        module_order[module_key]["done"] += done
        out["lessons"].append({"id": lesson["lesson_id"], "title": lesson["display_title"], "module": module_key, "total": total, "done": done, "pct": round(done / total * 100) if total else 0})
    for module in module_order.values():
        total = module["total"]
        done = module["done"]
        module["pct"] = round(done / total * 100) if total else 0
        out["modules"].append(module)

    (VAULT / "04_原始资料" / "progress.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    write_text(VAULT / "00_控制台" / "进度看板.html", render_dashboard(out))
    print("进度看板已刷新。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def extract_images(zip_path: Path) -> int:
    image_count = 0
    image_root = VAULT / "05_附件" / "images"
    ensure_dir(image_root)
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if not info.filename.startswith("images/") or info.is_dir():
                continue
            target = image_root / Path(info.filename).name
            with zf.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            image_count += 1
    return image_count


def copy_source_markdown(zip_path: Path, md_name: str, text: str) -> None:
    source_root = VAULT / "04_原始资料"
    write_text(source_root / md_name, convert_images_to_obsidian_links(text))


def write_manifest(lessons: list[dict], problems: list[dict]) -> None:
    manifest = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_zip": str((SOURCE_DIR / ZIP_NAME).resolve()),
        "student_pdf_dir": str(STUDENT_PDF_DIR.resolve()),
        "vault": str(VAULT.resolve()),
        "lessons": lessons,
        "problems": problems,
    }
    write_text(VAULT / "04_原始资料" / "problems.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    csv_path = VAULT / "04_原始资料" / "problems.csv"
    ensure_dir(csv_path.parent)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "lesson_id",
                "lesson_title",
                "module",
                "topic",
                "source_order",
                "original_number",
                "kind",
                "section",
                "note_path",
                "solution_note",
                "status",
                "source_pdf_name",
                "source_pdf",
                "source_pdf_uri",
            ],
        )
        writer.writeheader()
        for problem in problems:
            writer.writerow({key: problem.get(key, "") for key in writer.fieldnames})


def configure_obsidian() -> None:
    write_text(
        VAULT / ".obsidian" / "app.json",
        json.dumps({"attachmentFolderPath": "05_附件/images", "alwaysUpdateLinks": True}, ensure_ascii=False, indent=2),
    )
    write_text(
        VAULT / ".obsidian" / "core-plugins.json",
        json.dumps(["file-explorer", "global-search", "switcher", "graph", "backlink", "outgoing-link", "tag-pane", "page-preview", "templates"], ensure_ascii=False, indent=2),
    )
    write_text(
        VAULT / ".obsidian" / "templates.json",
        json.dumps({"folder": "90_模板"}, ensure_ascii=False, indent=2),
    )


def build_vault() -> None:
    zip_path = SOURCE_DIR / ZIP_NAME
    if not zip_path.exists():
        raise FileNotFoundError(zip_path)

    text, lines = read_zip_markdown(zip_path)
    with zipfile.ZipFile(zip_path) as zf:
        md_name = next(info.filename for info in zf.infolist() if info.filename.lower().endswith(".md"))

    lessons = parse_lessons(text, lines)
    attach_lesson_source_pdfs(lessons)
    compute_lesson_boundaries(lessons, lines)
    problems = parse_problem_blocks(lessons, lines)

    for lesson in lessons:
        lesson["note_path"] = lesson_index_path(lesson).as_posix()
        lesson["question_dir"] = lesson_dir(lesson).as_posix()
        lesson["problem_count"] = sum(1 for problem in problems if problem["lesson_id"] == lesson["lesson_id"])

    for problem in problems:
        matching_lesson = next(lesson for lesson in lessons if lesson["lesson_id"] == problem["lesson_id"])
        note_rel = lesson_dir(matching_lesson) / f"{problem['problem_id']}.md"
        solution_rel = solution_dir_for(problem) / f"{problem['problem_id']}_我的解答.md"
        problem["note_path"] = note_rel.as_posix()
        problem["solution_dir"] = solution_dir_for(problem).as_posix()
        problem["solution_note"] = solution_rel.as_posix()
        problem["status"] = "todo"
        problem["source_pdf"] = matching_lesson.get("source_pdf", "")
        problem["source_pdf_uri"] = matching_lesson.get("source_pdf_uri", "")
        problem["source_pdf_name"] = matching_lesson.get("source_pdf_name", "")

    ensure_dir(VAULT)
    ensure_dir(VAULT / "02_我的解答")
    ensure_dir(VAULT / "05_附件" / "解答附件")
    configure_obsidian()
    image_count = extract_images(zip_path)
    copy_source_markdown(zip_path, md_name, text)

    counts_by_lesson = {lesson["lesson_id"]: lesson["problem_count"] for lesson in lessons}
    for lesson in lessons:
        write_text(VAULT / lesson["note_path"], lesson_note(lesson, counts_by_lesson[lesson["lesson_id"]]))

    for problem in problems:
        lesson = next(lesson for lesson in lessons if lesson["lesson_id"] == problem["lesson_id"])
        note_path = VAULT / problem["note_path"]
        existing = frontmatter_from_existing(note_path)
        lesson_note_rel = Path(lesson["note_path"])
        solution_rel = Path(problem["solution_note"])
        write_text(note_path, problem_note(problem, lesson_note_rel, solution_rel, existing))

    write_text(VAULT / "README.md", root_readme(len(problems)))
    write_text(VAULT / "00_控制台" / "总览.md", overview_note(len(problems)))
    write_text(VAULT / "00_控制台" / "上传解答.md", upload_note())
    write_text(VAULT / "00_控制台" / "题目浏览.md", browser_note())
    write_text(VAULT / "00_控制台" / "最近上传.md", recent_note())
    write_text(VAULT / "00_控制台" / "可视化进度.md", visual_note())
    write_text(VAULT / "99_上传入口" / "README_把解答放这里.md", inbox_readme())
    write_text(VAULT / "90_模板" / "我的解答模板.md", solution_template())
    write_text(VAULT / "90_模板" / "题目模板.md", problem_template())
    write_text(VAULT / "tools" / "import_solutions.py", IMPORT_SOLUTIONS_SCRIPT)
    refresh_progress_tool = VAULT / "tools" / "refresh_progress.py"
    if not refresh_progress_tool.exists():
        write_text(refresh_progress_tool, REFRESH_PROGRESS_SCRIPT)
    write_manifest(lessons, problems)

    dashboard = render_dashboard(problems, lessons)
    write_text(VAULT / "00_控制台" / "进度看板.html", dashboard)

    print(f"Vault: {VAULT}")
    print(f"Lessons: {len(lessons)}")
    print(f"Problems: {len(problems)}")
    print(f"Images: {image_count}")


if __name__ == "__main__":
    build_vault()
