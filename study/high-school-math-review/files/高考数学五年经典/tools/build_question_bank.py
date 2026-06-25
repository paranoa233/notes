# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import zipfile
from collections import defaultdict
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
WORKSPACE = VAULT.parent
SOURCE_ZIP = VAULT / "高考数学五年经典_原书顺序合并版-20260529035403.zip"
SOURCE_PDF = VAULT / "高考数学五年经典_原书顺序合并版.pdf"
TODAY = dt.date.today().isoformat()


CHAPTERS = {
    1: "集合与常用逻辑用语",
    2: "不等式",
    3: "函数",
    4: "导数",
    5: "三角函数与解三角形",
    6: "平面向量与复数",
    7: "数列",
    8: "立体几何与空间向量",
    9: "直线与圆",
    10: "圆锥曲线",
    11: "概率与统计",
    12: "新高考创新题型",
}

CN_NUM = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "十一": 11,
    "十二": 12,
}

CN_BY_NUM = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十",
    11: "十一",
    12: "十二",
}

TRAIN_SECTIONS = {"模拟集训", "真题集训", "新高考真题", "全国卷真题"}
GENERATED_DIRS = [
    ".obsidian",
    "00_控制台",
    "01_题目",
    "02_我的解答",
    "03_讲义索引",
    "04_原始资料",
    "05_附件",
    "06_章节题目合集",
    "07_章节题目合集_Obsidian公式版",
    "90_模板",
    "99_上传入口",
]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def read_zip_markdown(zip_path: Path) -> tuple[str, list[str], zipfile.ZipFile]:
    zf = zipfile.ZipFile(zip_path)
    md_name = next(name for name in zf.namelist() if name.lower().endswith(".md"))
    text = zf.read(md_name).decode("utf-8", errors="replace")
    return md_name, text.splitlines(), zf


def slug(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]', "-", value.strip())
    value = re.sub(r"\s+", "", value)
    return value[:90]


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def file_uri(path: Path) -> str:
    return path.resolve().as_uri() if path.exists() else ""


def yaml_quote(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def strip_hash(value: str) -> str:
    return re.sub(r"^#+\s*", "", value.strip()).strip()


def parse_cn_number(value: str) -> int | None:
    value = re.sub(r"\s+", "", value)
    if value in CN_NUM:
        return CN_NUM[value]
    if value.startswith("十") and len(value) > 1:
        return 10 + CN_NUM.get(value[1:], 0)
    if value.endswith("十") and len(value) > 1:
        return CN_NUM.get(value[:-1], 0) * 10
    return None


def chapter_from_line(line: str) -> int | None:
    text = strip_hash(line)
    if text.startswith("高考数学"):
        return None
    match = re.match(r"^第\s*([一二三四五六七八九十]+)\s*章\s*(.*)$", text)
    if not match:
        return None
    chapter = parse_cn_number(match.group(1))
    if chapter and 1 <= chapter <= 12:
        return chapter
    return None


def group_from_line(line: str) -> tuple[int, str] | None:
    text = strip_hash(line)
    match = re.match(r"^题组\s*[,，]?\s*(\d{1,2})\s*(.*)$", text)
    if not match:
        return None
    return int(match.group(1)), match.group(2).strip()


def section_from_line(line: str) -> str | None:
    text = re.sub(r"\s+", " ", strip_hash(line)).strip()
    for section in ["新高考真题", "全国卷真题", "真题集训", "模拟集训", "核心笔记"]:
        if text.startswith(section) and len(text) <= len(section) + 8:
            return section
    return None


def clean_answer_marker(line: str) -> str:
    line = re.sub(r"答案\s*\\\(\s*\\mathrm\{P\}\s*\d+\s*\\\)", "", line)
    line = re.sub(r"答案\s*P\s*\d+", "", line, flags=re.I)
    return line


def rewrite_images(text: str) -> str:
    def replace(match: re.Match) -> str:
        name = Path(match.group(1)).name
        return f"![[05_附件/images/{name}]]"

    return re.sub(r"!\[[^\]]*\]\(images/([^)]+)\)", replace, text)


def split_embedded_question_starts(line: str) -> list[str]:
    value = line
    if re.match(r"^##\s*\d{1,3}\s*[.．]", value.strip()):
        value = re.sub(r"^##\s*", "", value.strip())
    return re.split(
        r"(?<=\S)\s+(?=\d{1,3}\s*[.．]\s*(?:[（(]?\s*(?:19|20)\d{2}|[（(]?\s*多选题))",
        value,
    )


def question_start(part: str) -> tuple[int | None, str] | None:
    text = strip_hash(part)
    match = re.match(r"^(\d{1,3})\s*[.．、]\s*(.*)$", text)
    if match:
        return int(match.group(1)), text
    if re.match(r"^[（(]?\s*(?:19|20)\d{2}", text):
        return None, text
    return None


def parse_toc(lines: list[str]) -> dict[tuple[int, int], dict]:
    result: dict[tuple[int, int], dict] = {}
    chapter: int | None = None
    for line in lines[:340]:
        stripped = line.strip()
        chapter_match = re.match(r"^第\s*([一二三四五六七八九十]+)\s*章\s*(.+?)\s*$", stripped)
        if chapter_match:
            parsed = parse_cn_number(chapter_match.group(1))
            if parsed:
                chapter = parsed
            continue
        group_match = re.match(r"^题组\s*[,，]?\s*(\d{1,2})\s+(.+?)\s+(\d+)\s*$", stripped)
        if chapter and group_match:
            group = int(group_match.group(1))
            title = group_match.group(2).strip()
            page = int(group_match.group(3))
            result[(chapter, group)] = {"title": title, "start_page": page}
    return result


def parse_problems(lines: list[str]) -> tuple[list[dict], list[dict]]:
    toc = parse_toc(lines)
    problems: list[dict] = []
    current_lines: list[str] = []
    current_meta: dict | None = None
    chapter: int | None = None
    group: int | None = None
    group_title = ""
    section: str | None = None
    sequence_by_group: dict[tuple[int, int], int] = defaultdict(int)
    last_original_number = 0
    lessons_seen: dict[tuple[int, int], dict] = {}

    def finish_problem() -> None:
        nonlocal current_lines, current_meta
        if current_meta and current_lines:
            content = rewrite_images("\n".join(current_lines).strip())
            content = re.sub(r"\n{3,}", "\n\n", content)
            if content:
                problems.append({**current_meta, "content": content})
        current_lines = []
        current_meta = None

    for line_no, line in enumerate(lines, 1):
        chapter_match = chapter_from_line(line)
        if chapter_match:
            finish_problem()
            chapter = chapter_match
            group = None
            section = None
            last_original_number = 0
            continue

        group_match = group_from_line(line)
        if group_match and chapter:
            finish_problem()
            group, detected_title = group_match
            toc_item = toc.get((chapter, group), {})
            group_title = toc_item.get("title") or detected_title
            section = None
            last_original_number = 0
            lessons_seen[(chapter, group)] = {
                "lesson_id": f"{chapter}-{group}",
                "module_id": str(chapter),
                "module": CHAPTERS[chapter],
                "topic": group_title,
                "lesson_title": f"{CHAPTERS[chapter]}：{group_title}",
                "start_page": toc_item.get("start_page", ""),
                "source_line": line_no,
            }
            continue

        section_match = section_from_line(line)
        if section_match:
            finish_problem()
            section = section_match
            last_original_number = 0
            continue

        if not (chapter and group and section in TRAIN_SECTIONS):
            continue

        cleaned_line = clean_answer_marker(line)
        if not cleaned_line.strip():
            if current_lines and current_lines[-1].strip():
                current_lines.append("")
            continue

        for part in split_embedded_question_starts(cleaned_line):
            if part != cleaned_line:
                part = part.strip()
            if not part.strip():
                continue
            start = question_start(part)
            if start:
                original_number, question_line = start
                if original_number is None:
                    if current_meta is None:
                        continue
                    finish_problem()
                    last_original_number += 1
                    original_number = last_original_number
                else:
                    finish_problem()
                    last_original_number = original_number

                key = (chapter, group)
                sequence_by_group[key] += 1
                problem_id = f"{chapter}-{group}-{sequence_by_group[key]}"
                current_meta = {
                    "problem_id": problem_id,
                    "lesson_id": f"{chapter}-{group}",
                    "lesson_title": f"{CHAPTERS[chapter]}：{group_title}",
                    "module_id": str(chapter),
                    "module": CHAPTERS[chapter],
                    "topic": group_title,
                    "source_order": sequence_by_group[key],
                    "original_number": original_number,
                    "section": section,
                    "kind": section,
                    "source_line": line_no,
                }
                current_lines = [question_line]
            elif current_meta is not None:
                current_lines.append(part)

    finish_problem()
    lessons = sorted(lessons_seen.values(), key=lambda item: (int(item["module_id"]), int(item["lesson_id"].split("-")[1])))
    return lessons, problems


def chapter_pdf_map() -> dict[int, Path]:
    result: dict[int, Path] = {}
    for chapter, cn in CN_BY_NUM.items():
        matches = sorted(VAULT.glob(f"第{cn}章*.pdf"))
        if matches:
            result[chapter] = matches[0]
    return result


def attach_pdf_sources(lessons: list[dict], problems: list[dict]) -> None:
    pdfs = chapter_pdf_map()
    for item in lessons + problems:
        chapter = int(item["module_id"])
        chapter_pdf = pdfs.get(chapter)
        item["source_pdf_path"] = str(SOURCE_PDF.resolve()) if SOURCE_PDF.exists() else ""
        item["source_pdf_uri"] = file_uri(SOURCE_PDF)
        item["source_pdf_name"] = SOURCE_PDF.name if SOURCE_PDF.exists() else ""
        item["chapter_pdf_path"] = str(chapter_pdf.resolve()) if chapter_pdf and chapter_pdf.exists() else ""
        item["chapter_pdf_uri"] = file_uri(chapter_pdf) if chapter_pdf else ""
        item["chapter_pdf_name"] = chapter_pdf.name if chapter_pdf and chapter_pdf.exists() else ""


def prepare_vault() -> None:
    for name in GENERATED_DIRS:
        target = VAULT / name
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
    readme = VAULT / "README.md"
    if readme.exists():
        readme.unlink()

    source_obsidian = WORKSPACE / "Obsidian题库" / ".obsidian"
    if source_obsidian.exists():
        shutil.copytree(source_obsidian, VAULT / ".obsidian")
        workspace_file = VAULT / ".obsidian" / "workspace.json"
        if workspace_file.exists():
            workspace_file.unlink()
    else:
        (VAULT / ".obsidian").mkdir(parents=True, exist_ok=True)
        write_text(VAULT / ".obsidian" / "app.json", '{\n  "alwaysUpdateLinks": true\n}\n')


def extract_images(zf: zipfile.ZipFile) -> list[str]:
    image_dir = VAULT / "05_附件" / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    names: list[str] = []
    for info in zf.infolist():
        if not info.filename.lower().startswith("images/"):
            continue
        if not info.filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
            continue
        target = image_dir / Path(info.filename).name
        with zf.open(info) as source, target.open("wb") as dest:
            shutil.copyfileobj(source, dest)
        names.append(target.name)
    return names


def problem_paths(problem: dict) -> tuple[Path, Path, str, str]:
    module_dir = f"{problem['module_id']}_{slug(problem['module'])}"
    lesson_dir = f"{problem['lesson_id']}_{slug(problem['topic'])}"
    problem_note = VAULT / "01_题目" / module_dir / lesson_dir / f"{problem['problem_id']}.md"
    solution_note = VAULT / "02_我的解答" / module_dir / lesson_dir / f"{problem['problem_id']}_我的解答.md"
    return problem_note, solution_note, module_dir, lesson_dir


def render_problem(problem: dict, lesson_link: str, solution_link: str) -> str:
    source_pdf = problem.get("source_pdf_uri", "")
    chapter_pdf = problem.get("chapter_pdf_uri", "")
    pdf_line = ""
    chapter_line = ""
    fm = [
        "---",
        'type: "problem"',
        f"problem_id: {yaml_quote(problem['problem_id'])}",
        f"lesson_id: {yaml_quote(problem['lesson_id'])}",
        f"lesson_title: {yaml_quote(problem['lesson_title'])}",
        f"module_id: {yaml_quote(problem['module_id'])}",
        f"module: {yaml_quote(problem['module'])}",
        f"topic: {yaml_quote(problem['topic'])}",
        f"source_order: {problem['source_order']}",
        f"original_number: {problem['original_number']}",
        f"section: {yaml_quote(problem['section'])}",
        f"kind: {yaml_quote(problem['kind'])}",
        'status: "todo"',
        f"solution: {yaml_quote(solution_link)}",
        f"source_line: {problem['source_line']}",
        f"source_pdf: {yaml_quote(problem.get('source_pdf_uri', ''))}",
        f"source_pdf_path: {yaml_quote(problem.get('source_pdf_path', ''))}",
        f"source_pdf_name: {yaml_quote(problem.get('source_pdf_name', ''))}",
        f"chapter_pdf: {yaml_quote(problem.get('chapter_pdf_uri', ''))}",
        f"chapter_pdf_path: {yaml_quote(problem.get('chapter_pdf_path', ''))}",
        f"chapter_pdf_name: {yaml_quote(problem.get('chapter_pdf_name', ''))}",
        f"created: {yaml_quote(TODAY)}",
        'generated_by: "gaokao_five_years_question_bank_builder"',
        "tags:",
        '  - "题库"',
        '  - "高中数学"',
        '  - "高考数学五年经典"',
        f'  - "module/{problem["module_id"]}"',
        f'  - "lesson/{problem["lesson_id"]}"',
        "---",
    ]
    return (
        "\n".join(fm)
        + f"\n# {problem['problem_id']}\n\n"
        + f"> 题组：{lesson_link}  \n"
        + f"> 来源：{problem['section']} / 原始题号 {problem['original_number']}  \n"
        + pdf_line
        + chapter_line
        + "> 状态：`todo`\n\n"
        + "## 题目\n\n"
        + problem["content"].strip()
        + "\n\n## 我的解答\n\n"
        + solution_link
        + "\n\n> 把文件名以本题编号开头的 Markdown、图片、PDF 或 Word 文档放进 `99_上传入口`，再运行导入工具，系统会自动关联到这里。\n"
    )


def render_solution(problem: dict, problem_rel: str) -> str:
    return (
        "---\n"
        'type: "solution"\n'
        f"problem_id: {yaml_quote(problem['problem_id'])}\n"
        'status: "todo"\n'
        "tags:\n"
        '  - "我的解答"\n'
        "---\n"
        f"# {problem['problem_id']} 我的解答\n\n"
        f"对应题目：[[{problem_rel}|{problem['problem_id']}]]\n\n"
        "## 解答\n"
    )


def write_problem_notes(lessons: list[dict], problems: list[dict]) -> None:
    lesson_rel_by_id: dict[str, str] = {}
    lesson_lookup = {lesson["lesson_id"]: lesson for lesson in lessons}
    for lesson in lessons:
        module_dir = f"{lesson['module_id']}_{slug(lesson['module'])}"
        lesson_file = VAULT / "03_讲义索引" / module_dir / f"{lesson['lesson_id']}_{slug(lesson['topic'])}.md"
        lesson_rel_by_id[lesson["lesson_id"]] = rel(lesson_file)

    for problem in problems:
        problem_note, solution_note, _, _ = problem_paths(problem)
        lesson = lesson_lookup[problem["lesson_id"]]
        lesson_link = f"[[{lesson_rel_by_id[problem['lesson_id']]}|{problem['lesson_id']} {problem['topic']}]]"
        solution_link = f"[[{rel(solution_note)}|我的解答]]"
        write_text(problem_note, render_problem(problem, lesson_link, solution_link))
        write_text(solution_note, render_solution(problem, rel(problem_note)))

        problem["note_path"] = rel(problem_note)
        problem["solution_note"] = rel(solution_note)
        problem["solution_dir"] = rel(solution_note.parent)
        problem["status"] = "todo"


def write_lesson_indices(lessons: list[dict], problems: list[dict]) -> None:
    counts = defaultdict(int)
    for problem in problems:
        counts[problem["lesson_id"]] += 1

    for lesson in lessons:
        module_dir = f"{lesson['module_id']}_{slug(lesson['module'])}"
        lesson_path = VAULT / "03_讲义索引" / module_dir / f"{lesson['lesson_id']}_{slug(lesson['topic'])}.md"
        source_pdf = lesson.get("source_pdf_uri", "")
        chapter_pdf = lesson.get("chapter_pdf_uri", "")
        source_line = ""
        chapter_line = ""
        question_dir = f"01_题目/{lesson['module_id']}_{slug(lesson['module'])}/{lesson['lesson_id']}_{slug(lesson['topic'])}"
        body = f"""---
type: "lesson"
lesson_id: {yaml_quote(lesson['lesson_id'])}
lesson_title: {yaml_quote(lesson['lesson_title'])}
module_id: {yaml_quote(lesson['module_id'])}
module: {yaml_quote(lesson['module'])}
topic: {yaml_quote(lesson['topic'])}
start_page: {yaml_quote(lesson.get('start_page', ''))}
problem_count: {counts[lesson['lesson_id']]}
source_pdf: {yaml_quote(lesson.get('source_pdf_uri', ''))}
source_pdf_path: {yaml_quote(lesson.get('source_pdf_path', ''))}
source_pdf_name: {yaml_quote(lesson.get('source_pdf_name', ''))}
chapter_pdf: {yaml_quote(lesson.get('chapter_pdf_uri', ''))}
chapter_pdf_path: {yaml_quote(lesson.get('chapter_pdf_path', ''))}
chapter_pdf_name: {yaml_quote(lesson.get('chapter_pdf_name', ''))}
generated_by: "gaokao_five_years_question_bank_builder"
tags:
  - "讲义索引"
  - "题库"
  - "高考数学五年经典"
---
# {lesson['lesson_id']} {lesson['topic']}

[[00_控制台/总览|返回总览]]

- 题目数：{counts[lesson['lesson_id']]}
- 原书起始页：{lesson.get('start_page', '')}
{source_line}
{chapter_line}
- 题目目录：`{question_dir}`

```dataview
TABLE problem_id AS 编号, kind AS 类型, section AS 板块, status AS 状态, file.link AS 题目, solution AS 解答
FROM "{question_dir}"
WHERE type = "problem"
SORT source_order ASC
```
"""
        write_text(lesson_path, body)


def write_control_pages(total: int) -> None:
    overview = f"""# 总览

共 `{total}` 道题。题号按原书结构生成，例如 `10-3-7` 表示第 10 章第 3 个题组的第 7 题。

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
dv.table(["章节", "题数", "已上传/完成", "进度", ""], modules);
```

## 快捷入口

- [[00_控制台/上传解答]]
- [[00_控制台/题目浏览]]
- [[00_控制台/最近上传]]
- [[00_控制台/可视化进度]]
"""
    browser = """# 题目浏览

```dataview
TABLE module AS 章节, topic AS 题组, kind AS 类型, section AS 板块, status AS 状态, solution AS 解答
FROM "01_题目"
WHERE type = "problem"
SORT module_id ASC, lesson_id ASC, source_order ASC
```
"""
    upload = """# 上传解答

把文件名以题号开头的 Markdown、图片、PDF 或 Word 文档放进 `99_上传入口`。

示例：

- `10-3-7.png`
- `10-3-7 我的解答.pdf`
- `10-3-7.md`

然后运行 `tools/import_solutions.py`，系统会把文件归档到对应题目的“我的解答”笔记里。
"""
    recent = """# 最近上传

```dataview
TABLE updated AS 更新时间, status AS 状态, file.link AS 解答
FROM "02_我的解答"
WHERE type = "solution" AND updated
SORT updated DESC
LIMIT 30
```
"""
    progress = """# 可视化进度

打开同目录下的 [[进度看板.html]] 可以看离线版进度看板；在 Obsidian 中也可以直接查看 [[总览]] 的 Dataview 统计。
"""
    formula_test = """# 公式兼容测试

行内公式：\( a^2+b^2=c^2 \)

块公式：

\[
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
\]
"""
    write_text(VAULT / "00_控制台" / "总览.md", overview)
    write_text(VAULT / "00_控制台" / "题目浏览.md", browser)
    write_text(VAULT / "00_控制台" / "上传解答.md", upload)
    write_text(VAULT / "00_控制台" / "最近上传.md", recent)
    write_text(VAULT / "00_控制台" / "可视化进度.md", progress)
    write_text(VAULT / "00_控制台" / "公式兼容测试.md", formula_test)


def write_templates() -> None:
    write_text(
        VAULT / "90_模板" / "题目模板.md",
        '---\ntype: "problem"\nproblem_id: ""\nlesson_id: ""\nstatus: "todo"\ntags:\n  - "题库"\n---\n# 题目\n\n## 我的解答\n',
    )
    write_text(
        VAULT / "90_模板" / "我的解答模板.md",
        '---\ntype: "solution"\nproblem_id: ""\nstatus: "todo"\ntags:\n  - "我的解答"\n---\n# 我的解答\n\n## 解答\n',
    )
    write_text(VAULT / "99_上传入口" / "README_把解答放这里.md", "# 上传入口\n\n把文件名以题号开头的解答文件放在这里。\n")


def write_chapter_collections(problems: list[dict]) -> None:
    for out_dir_name in ["06_章节题目合集", "07_章节题目合集_Obsidian公式版"]:
        out_dir = VAULT / out_dir_name
        index = ["# 章节题目合集", ""]
        by_chapter: dict[str, list[dict]] = defaultdict(list)
        for problem in problems:
            by_chapter[problem["module_id"]].append(problem)
        for module_id in sorted(by_chapter, key=lambda item: int(item)):
            module_name = CHAPTERS[int(module_id)]
            filename = f"{int(module_id):02d}_{slug(module_name)}.md"
            index.append(f"- [[{out_dir_name}/{filename}|第{module_id}章 {module_name}]]")
            output = [f"# 第{module_id}章 {module_name}", ""]
            current_lesson = None
            for problem in sorted(by_chapter[module_id], key=lambda p: (int(p["lesson_id"].split("-")[1]), p["source_order"])):
                if problem["lesson_id"] != current_lesson:
                    output.extend([f"## {problem['lesson_id']} {problem['topic']}", ""])
                    current_lesson = problem["lesson_id"]
                output.extend([f"### {problem['problem_id']}", "", problem["content"].strip(), ""])
            write_text(out_dir / filename, "\n".join(output).rstrip() + "\n")
        write_text(out_dir / "README.md", "\n".join(index).rstrip() + "\n")


def write_manifest(md_name: str, lessons: list[dict], problems: list[dict], images: list[str]) -> None:
    manifest = {
        "name": "高考数学五年经典",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_zip": str(SOURCE_ZIP.resolve()),
        "source_markdown": md_name,
        "source_pdf": str(SOURCE_PDF.resolve()) if SOURCE_PDF.exists() else "",
        "problem_count": len(problems),
        "lesson_count": len(lessons),
        "image_count": len(images),
        "lessons": lessons,
        "problems": problems,
        "images": images,
    }
    write_text(VAULT / "04_原始资料" / "problems.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    source_readme = f"""# 原始资料

- 转换 Markdown：`{md_name}`，来源压缩包：`{SOURCE_ZIP.name}`
- 原书合并 PDF：[[{SOURCE_PDF.name}]]
- 已提取图片：`{len(images)}` 张，位于 [[05_附件/images]]
- 已生成题目：`{len(problems)}` 道
"""
    write_text(VAULT / "04_原始资料" / "README.md", source_readme)


def write_import_tool() -> None:
    source = WORKSPACE / "Obsidian题库" / "tools" / "import_solutions.py"
    target = VAULT / "tools" / "import_solutions.py"
    if source.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def write_dashboard(total: int, lessons: list[dict], problems: list[dict]) -> None:
    by_module = []
    for module_id, module_name in CHAPTERS.items():
        count = sum(1 for p in problems if p["module_id"] == str(module_id))
        by_module.append({"name": f"{module_id} {module_name}", "total": count, "done": 0, "pct": 0})
    lesson_rows = []
    for lesson in lessons:
        count = sum(1 for p in problems if p["lesson_id"] == lesson["lesson_id"])
        lesson_rows.append(
            {
                "id": lesson["lesson_id"],
                "title": lesson["topic"],
                "module": lesson["module"],
                "total": count,
                "done": 0,
                "pct": 0,
            }
        )
    payload = html.escape(json.dumps({"total": total, "modules": by_module, "lessons": lesson_rows}, ensure_ascii=False))
    page = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>高考数学五年经典题库进度</title>
<style>
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;background:#f6f7f9;color:#17202a}}
main{{max-width:1100px;margin:0 auto;padding:24px}}
h1{{font-size:28px;margin:0 0 6px}}
.muted{{color:#667085}}
.cards{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0}}
.card,section{{background:#fff;border:1px solid #d9dee7;border-radius:8px;padding:14px}}
.num{{font-size:30px;font-weight:750}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}
.bar{{height:10px;background:#e7ebf1;border-radius:999px;overflow:hidden;margin-top:8px}}
.fill{{height:100%;background:#2f9e8f}}
table{{width:100%;border-collapse:collapse;font-size:13px}}th,td{{border-bottom:1px solid #d9dee7;padding:8px;text-align:left}}th{{color:#667085}}
@media(max-width:700px){{main{{padding:14px}}.cards{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<main>
<h1>高考数学五年经典题库进度</h1>
<div class="muted">生成时间：{dt.datetime.now().isoformat(timespec="seconds")}</div>
<div id="app"></div>
</main>
<script type="application/json" id="data">{payload}</script>
<script>
const data = JSON.parse(document.getElementById('data').textContent);
function bar(pct) {{ return `<div class="bar"><div class="fill" style="width:${{pct}}%"></div></div>`; }}
document.getElementById('app').innerHTML = `
<div class="cards">
  <div class="card"><div class="muted">总题数</div><div class="num">${{data.total}}</div></div>
  <div class="card"><div class="muted">已完成</div><div class="num">0</div></div>
  <div class="card"><div class="muted">总进度</div><div class="num">0%</div>${{bar(0)}}</div>
</div>
<section><h2>章节</h2><div class="grid">${{data.modules.map(m => `<div class="card"><b>${{m.name}}</b><div class="muted">${{m.total}} 题</div>${{bar(0)}}</div>`).join('')}}</div></section>
<section style="margin-top:14px"><h2>题组</h2><table><thead><tr><th>编号</th><th>题组</th><th>章节</th><th>题数</th></tr></thead><tbody>${{data.lessons.map(l => `<tr><td>${{l.id}}</td><td>${{l.title}}</td><td>${{l.module}}</td><td>${{l.total}}</td></tr>`).join('')}}</tbody></table></section>`;
</script>
</body>
</html>
"""
    write_text(VAULT / "00_控制台" / "进度看板.html", page)


def write_readme(total: int) -> None:
    readme = f"""# 高考数学五年经典

这个 vault 已经把《高考数学 5 年经典》的题目拆成独立题目笔记，共 `{total}` 题。

建议先打开：

- [[00_控制台/总览]]
- [[00_控制台/题目浏览]]
- [[06_章节题目合集/README]]
- [[00_控制台/上传解答]]
"""
    write_text(VAULT / "README.md", readme)


def main() -> int:
    if not SOURCE_ZIP.exists():
        raise FileNotFoundError(SOURCE_ZIP)

    md_name, lines, zf = read_zip_markdown(SOURCE_ZIP)
    try:
        lessons, problems = parse_problems(lines)
        attach_pdf_sources(lessons, problems)
        prepare_vault()
        images = extract_images(zf)
        write_text(VAULT / "04_原始资料" / md_name, "\n".join(lines) + "\n")
        write_problem_notes(lessons, problems)
        write_lesson_indices(lessons, problems)
        write_control_pages(len(problems))
        write_templates()
        write_chapter_collections(problems)
        write_manifest(md_name, lessons, problems, images)
        write_import_tool()
        write_dashboard(len(problems), lessons, problems)
        write_readme(len(problems))
    finally:
        zf.close()

    print(f"已生成高考数学五年经典 Obsidian 题库：{len(problems)} 题，{len(lessons)} 个题组，{len(images)} 张图片。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
