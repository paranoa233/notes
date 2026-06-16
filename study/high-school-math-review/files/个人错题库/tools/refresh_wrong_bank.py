from __future__ import annotations

import csv
import datetime as dt
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRONG_DIR = ROOT / "01_错题"
CONTROL_DIR = ROOT / "00_控制台"
DASHBOARD = CONTROL_DIR / "错题看板.html"
STATS = CONTROL_DIR / "错题统计.md"
HEALTH = CONTROL_DIR / "系统体检.md"
CALENDAR = CONTROL_DIR / "复习日历.md"
CLASSIFICATION_CSV = CONTROL_DIR / "分类清单.csv"
DATA_JSON = CONTROL_DIR / "wrong_bank_data.json"

REQUIRED_FIELDS = [
    "type",
    "wrong_id",
    "lesson_id",
    "module_id",
    "module",
    "topic",
    "priority",
    "status",
    "mastery",
    "wrong_reason",
    "knowledge_points",
    "methods",
    "anti_mistake_tip",
    "created",
]
VALID_STATUS = {"待复习", "一刷通过", "仍错", "二刷通过", "已掌握"}
VALID_PRIORITY = {"P1", "P2", "P3"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str] | None:
    value = value.strip()
    if value == "[]":
        return []
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [strip_quotes(item.strip()) for item in inner.split(",") if item.strip()]


def parse_frontmatter(text: str) -> dict[str, object] | None:
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return None

    lines = match.group(1).splitlines()
    data: dict[str, object] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            i += 1
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value:
            inline_list = parse_inline_list(raw_value)
            data[key] = inline_list if inline_list is not None else strip_quotes(raw_value)
            i += 1
            continue

        values: list[str] = []
        i += 1
        while i < len(lines):
            child = lines[i]
            stripped = child.strip()
            if not stripped:
                i += 1
                continue
            if not child.startswith((" ", "\t")):
                break
            if stripped.startswith("- "):
                values.append(strip_quotes(stripped[2:]))
            i += 1
        data[key] = values
    return data


def as_list(value: object) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)]


def as_int(value: object, default: int = 0) -> int:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def parse_date(value: object) -> dt.date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return dt.date.fromisoformat(text[:10])
    except ValueError:
        return None


def md_escape(value: object) -> str:
    return html.escape(str(value)).replace("|", "\\|")


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    if not rows:
        return "暂无数据\n"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(cell) for cell in row) + " |")
    return "\n".join(lines) + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def load_classification() -> dict[str, str]:
    if not CLASSIFICATION_CSV.exists():
        return {}
    result: dict[str, str] = {}
    with CLASSIFICATION_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            lesson_id = str(row.get("lesson_id") or "").strip()
            folder = str(row.get("folder") or "").strip()
            if lesson_id and folder:
                result[lesson_id] = folder.replace("\\", "/")
    return result


def load_wrong_notes() -> list[dict[str, object]]:
    notes: list[dict[str, object]] = []
    for path in WRONG_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        data = parse_frontmatter(text)
        if not data or data.get("type") != "wrong_problem":
            continue
        rel = path.relative_to(ROOT).as_posix()
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        title = title_match.group(1).strip() if title_match else path.stem
        data["_file"] = rel
        data["_path"] = path
        data["_title"] = title
        data["_body"] = text
        notes.append(data)
    return notes


def priority_key(note: dict[str, object]) -> tuple[str, int, int, str]:
    status = str(note.get("status") or "")
    return (
        str(note.get("priority") or "P2"),
        0 if status == "仍错" else 1,
        as_int(note.get("mastery"), 9),
        str(note.get("next_review") or "9999-12-31"),
    )


def validate_notes(notes: list[dict[str, object]], classification: dict[str, str]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    seen_ids: dict[str, str] = {}

    for note in notes:
        file = str(note.get("_file") or "")
        wrong_id = str(note.get("wrong_id") or "").strip()

        for field in REQUIRED_FIELDS:
            value = note.get(field)
            if value in (None, "", []) or value == "待补充":
                issues.append({"level": "P1", "file": file, "field": field, "message": "必填字段缺失或待补充"})

        if wrong_id:
            if wrong_id in seen_ids:
                issues.append({"level": "P1", "file": file, "field": "wrong_id", "message": f"编号重复，已出现在 {seen_ids[wrong_id]}"})
            else:
                seen_ids[wrong_id] = file

        status = str(note.get("status") or "")
        if status and status not in VALID_STATUS:
            issues.append({"level": "P2", "file": file, "field": "status", "message": f"状态不在推荐集合中：{status}"})

        priority = str(note.get("priority") or "")
        if priority and priority not in VALID_PRIORITY:
            issues.append({"level": "P2", "file": file, "field": "priority", "message": f"优先级应为 P1/P2/P3：{priority}"})

        confidence = str(note.get("classification_confidence") or "")
        if confidence and confidence not in VALID_CONFIDENCE:
            issues.append({"level": "P2", "file": file, "field": "classification_confidence", "message": f"分类置信度应为 high/medium/low：{confidence}"})
        if confidence == "low":
            issues.append({"level": "P2", "file": file, "field": "classification_confidence", "message": "分类置信度低，需要人工确认"})

        mastery = as_int(note.get("mastery"), -1)
        if mastery < 1 or mastery > 5:
            issues.append({"level": "P2", "file": file, "field": "mastery", "message": "掌握度应为 1 到 5"})

        for date_field in ["created", "updated", "last_review", "next_review"]:
            value = str(note.get(date_field) or "").strip()
            if value and not parse_date(value):
                issues.append({"level": "P2", "file": file, "field": date_field, "message": "日期应使用 YYYY-MM-DD"})

        lesson_id = str(note.get("lesson_id") or "").strip()
        expected_folder = classification.get(lesson_id)
        if expected_folder and not file.startswith(expected_folder + "/"):
            issues.append({"level": "P2", "file": file, "field": "lesson_id", "message": f"文件不在分类清单对应目录：{expected_folder}"})

        body = str(note.get("_body") or "")
        for heading in ["## 题目", "## 我的错误答案", "## 标准答案", "## 错因定位", "## 正确解法", "## 防错提醒"]:
            if heading not in body:
                issues.append({"level": "P2", "file": file, "field": "body", "message": f"缺少正文小节：{heading}"})

        quality_flags = as_list(note.get("quality_flags"))
        for flag in quality_flags:
            issues.append({"level": "P3", "file": file, "field": "quality_flags", "message": flag})

    return issues


def build_calendar(notes: list[dict[str, object]], days: int = 14) -> list[dict[str, object]]:
    today = dt.date.today()
    buckets: list[dict[str, object]] = []
    for offset in range(days):
        day = today + dt.timedelta(days=offset)
        rows: list[dict[str, str]] = []
        for note in notes:
            next_review = parse_date(note.get("next_review"))
            if next_review == day:
                rows.append(
                    {
                        "title": str(note.get("_title") or note.get("wrong_id") or "未命名错题"),
                        "file": str(note.get("_file") or ""),
                        "priority": str(note.get("priority") or "P2"),
                        "module": str(note.get("module") or "未分类"),
                        "status": str(note.get("status") or "待复习"),
                        "nextReview": str(note.get("next_review") or ""),
                        "_sort": priority_key(note),
                    }
                )
        rows = sorted(rows, key=lambda item: item["_sort"])
        for row in rows:
            row.pop("_sort", None)
        buckets.append({"date": day.isoformat(), "items": rows})
    return buckets


def build_data(notes: list[dict[str, object]], issues: list[dict[str, str]]) -> dict[str, object]:
    today = dt.date.today()
    status_counts = Counter(str(note.get("status") or "待复习") for note in notes)
    priority_counts = Counter(str(note.get("priority") or "P2") for note in notes)
    module_counts = Counter(str(note.get("module") or "未分类") for note in notes)
    reason_counts: Counter[str] = Counter()
    method_counts: Counter[str] = Counter()
    knowledge_counts: Counter[str] = Counter()

    due_notes = []
    overdue_notes = []
    for note in notes:
        reason_counts.update(as_list(note.get("wrong_reason")) or ["待补充"])
        method_counts.update(as_list(note.get("methods")) or ["待补充"])
        knowledge_counts.update(as_list(note.get("knowledge_points")) or ["待补充"])

        status = str(note.get("status") or "")
        due = parse_date(note.get("next_review"))
        if status in {"待复习", "仍错"} or (due and due <= today):
            due_notes.append(note)
        if due and due < today and status != "已掌握":
            overdue_notes.append(note)

    due_count = len(due_notes)
    overdue_count = len(overdue_notes)
    due_notes = sorted(due_notes, key=priority_key)[:20]
    return {
        "generatedAt": today.isoformat(),
        "total": len(notes),
        "pending": status_counts["待复习"],
        "wrongAgain": status_counts["仍错"],
        "mastered": status_counts["已掌握"],
        "due": due_count,
        "overdue": overdue_count,
        "issueCount": len(issues),
        "statusCounts": [{"name": k, "count": v} for k, v in status_counts.most_common()],
        "priorityCounts": [{"name": k, "count": v} for k, v in priority_counts.most_common()],
        "modules": [{"name": k, "count": v} for k, v in module_counts.most_common()],
        "reasons": [{"name": k, "count": v} for k, v in reason_counts.most_common(12)],
        "methods": [{"name": k, "count": v} for k, v in method_counts.most_common(10)],
        "knowledge": [{"name": k, "count": v} for k, v in knowledge_counts.most_common(10)],
        "priority": [
            {
                "title": str(note.get("_title") or note.get("wrong_id") or "未命名错题"),
                "file": str(note.get("_file") or ""),
                "priority": str(note.get("priority") or "P2"),
                "module": str(note.get("module") or "未分类"),
                "status": str(note.get("status") or "待复习"),
                "nextReview": str(note.get("next_review") or ""),
            }
            for note in due_notes
        ],
        "calendar": build_calendar(notes),
    }


def export_note(note: dict[str, object]) -> dict[str, object]:
    return {
        "title": str(note.get("_title") or note.get("wrong_id") or "未命名错题"),
        "file": str(note.get("_file") or ""),
        "wrong_id": str(note.get("wrong_id") or ""),
        "lesson_id": str(note.get("lesson_id") or ""),
        "module_id": str(note.get("module_id") or ""),
        "module": str(note.get("module") or ""),
        "topic": str(note.get("topic") or ""),
        "priority": str(note.get("priority") or "P2"),
        "status": str(note.get("status") or "待复习"),
        "mastery": as_int(note.get("mastery"), 0),
        "wrong_reason": as_list(note.get("wrong_reason")),
        "knowledge_points": as_list(note.get("knowledge_points")),
        "methods": as_list(note.get("methods")),
        "created": str(note.get("created") or ""),
        "last_review": str(note.get("last_review") or ""),
        "next_review": str(note.get("next_review") or ""),
    }


def render_dashboard(data: dict[str, object]) -> str:
    data_json = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>个人错题库看板</title>
  <style>
    :root {{
      --bg: #f7f7f4;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #637083;
      --line: #dfe3e8;
      --accent: #2f8f83;
      --warn: #b65f34;
      --blue: #536d9e;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Microsoft YaHei", "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.55;
    }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 28px 18px 42px; }}
    header {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 16px;
      align-items: flex-end;
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
      margin-bottom: 18px;
    }}
    h1 {{ margin: 0; font-size: 28px; letter-spacing: 0; }}
    h2 {{ margin: 0 0 12px; font-size: 18px; letter-spacing: 0; }}
    .muted {{ color: var(--muted); }}
    .links {{ display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end; }}
    .quick {{
      display: inline-flex;
      align-items: center;
      min-height: 36px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 12px;
      background: #fff;
      color: var(--text);
      font-size: 13px;
      font-weight: 700;
    }}
    .quick.primary {{ background: var(--accent); border-color: var(--accent); color: #fff; }}
    .toolbar {{ margin: 0 0 10px; }}
    input {{
      width: min(340px, 100%);
      height: 36px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0 11px;
      font: inherit;
      background: #fff;
    }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin: 18px 0; }}
    .card, section {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; }}
    .card b {{ display: block; color: var(--muted); font-size: 13px; font-weight: 600; }}
    .value {{ font-size: 30px; font-weight: 750; margin-top: 4px; }}
    .layout {{ display: grid; grid-template-columns: 1.1fr .9fr; gap: 14px; margin-top: 14px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ text-align: left; border-bottom: 1px solid var(--line); padding: 9px 6px; vertical-align: top; }}
    th {{ color: var(--muted); font-weight: 650; }}
    a {{ color: var(--blue); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .bar {{ height: 10px; background: #ecefeb; border-radius: 999px; overflow: hidden; margin-top: 8px; }}
    .fill {{ height: 100%; width: 0%; background: var(--accent); }}
    .pill {{ display: inline-block; border: 1px solid var(--line); border-radius: 999px; padding: 2px 8px; font-size: 12px; color: var(--muted); background: #fbfbf9; }}
    .empty {{ padding: 26px; text-align: center; color: var(--muted); border: 1px dashed var(--line); border-radius: 8px; background: #fbfbf9; }}
    code {{ background: #eef1f3; border-radius: 4px; padding: 2px 5px; font-family: Consolas, monospace; }}
    @media (max-width: 900px) {{ header {{ display: block; }} .links {{ justify-content: flex-start; margin-top: 10px; }} .grid, .layout {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>个人错题库看板</h1>
      <div class="muted">错题、复习、体检和薄弱点一屏看清</div>
    </div>
    <nav class="links">
      <a class="quick primary" href="今日学习路线.md">今日路线</a>
      <a class="quick" href="错题统计.md">错题统计</a>
      <a class="quick" href="系统体检.md">系统体检</a>
      <a class="quick" href="相似题推荐.md">相似题</a>
      <a class="quick" href="错题关联笔记.md">关联笔记</a>
    </nav>
  </header>
  <div class="muted">更新日期：<span id="generatedAt"></span></div>

  <div class="grid">
    <div class="card"><b>总错题</b><div class="value" id="total">0</div></div>
    <div class="card"><b>待复习</b><div class="value" id="pending">0</div></div>
    <div class="card"><b>今日队列</b><div class="value" id="due">0</div></div>
    <div class="card"><b>仍错</b><div class="value" id="wrongAgain">0</div></div>
    <div class="card"><b>已掌握</b><div class="value" id="mastered">0</div></div>
    <div class="card"><b>逾期</b><div class="value" id="overdue">0</div></div>
    <div class="card"><b>体检问题</b><div class="value" id="issueCount">0</div></div>
  </div>

  <div class="layout">
    <section>
      <h2>优先复习</h2>
      <div class="toolbar"><input id="prioritySearch" placeholder="筛选错题、专题或状态"></div>
      <div id="priorityEmpty" class="empty">优先显示 P1、待复习、仍错或到期的题。</div>
      <table id="priorityTable" hidden>
        <thead><tr><th>错题</th><th>优先级</th><th>专题</th><th>状态</th><th>下次复习</th></tr></thead>
        <tbody></tbody>
      </table>
    </section>

    <section>
      <h2>高频错因</h2>
      <div id="reasonEmpty" class="empty">导入错题后，这里用于查看重复出现的错误类型。</div>
      <table id="reasonTable" hidden>
        <thead><tr><th>错因</th><th>次数</th></tr></thead>
        <tbody></tbody>
      </table>
    </section>
  </div>

  <div class="layout">
    <section>
      <h2>专题分布</h2>
      <div id="moduleEmpty" class="empty">暂无错题。</div>
      <table id="moduleTable" hidden>
        <thead><tr><th>专题</th><th>数量</th><th>占比</th></tr></thead>
        <tbody></tbody>
      </table>
    </section>

    <section>
      <h2>接下来 14 天</h2>
      <div id="calendarEmpty" class="empty">暂无已安排日期的复习。</div>
      <table id="calendarTable" hidden>
        <thead><tr><th>日期</th><th>题数</th><th>题目</th></tr></thead>
        <tbody></tbody>
      </table>
    </section>
  </div>
</main>

<script>
const data = {data_json};
function text(id, value) {{ document.getElementById(id).textContent = value; }}
function renderTable(tableId, emptyId, rows, cells) {{
  const table = document.getElementById(tableId);
  const empty = document.getElementById(emptyId);
  const body = table.querySelector("tbody");
  body.innerHTML = "";
  if (!rows.length) {{ table.hidden = true; empty.hidden = false; return; }}
  table.hidden = false;
  empty.hidden = true;
  for (const row of rows) {{
    const tr = document.createElement("tr");
    for (const cell of cells(row)) {{
      const td = document.createElement("td");
      if (cell && cell.html) td.innerHTML = cell.html;
      else td.textContent = cell ?? "";
      tr.appendChild(td);
    }}
    body.appendChild(tr);
  }}
}}
text("generatedAt", data.generatedAt);
text("total", data.total);
text("pending", data.pending);
text("due", data.due);
text("wrongAgain", data.wrongAgain);
text("mastered", data.mastered);
text("overdue", data.overdue);
text("issueCount", data.issueCount);
function renderPriority(keyword = "") {{
  const q = keyword.trim().toLowerCase();
  const rows = data.priority.filter(row => !q || `${{row.title}} ${{row.module}} ${{row.status}} ${{row.priority}}`.toLowerCase().includes(q));
  renderTable("priorityTable", "priorityEmpty", rows, row => [
    row.file ? {{html: `<a href="../${{row.file}}">${{row.title}}</a>`}} : row.title,
    {{html: `<span class="pill">${{row.priority}}</span>`}},
    row.module,
    row.status,
    row.nextReview
  ]);
}}
renderPriority();
document.getElementById("prioritySearch").addEventListener("input", event => renderPriority(event.target.value));
renderTable("reasonTable", "reasonEmpty", data.reasons, row => [row.name, row.count]);
renderTable("moduleTable", "moduleEmpty", data.modules, row => [row.name, row.count, data.total ? Math.round(row.count / data.total * 100) + "%" : "0%"]);
const calendarRows = data.calendar.filter(day => day.items.length);
renderTable("calendarTable", "calendarEmpty", calendarRows, row => [
  row.date,
  row.items.length,
  row.items.map(item => item.title).join("；")
]);
</script>
</body>
</html>
"""


def render_stats(data: dict[str, object]) -> str:
    module_rows = [[item["name"], item["count"]] for item in data["modules"]]
    reason_rows = [[item["name"], item["count"]] for item in data["reasons"]]
    method_rows = [[item["name"], item["count"]] for item in data["methods"]]
    knowledge_rows = [[item["name"], item["count"]] for item in data["knowledge"]]
    status_rows = [[item["name"], item["count"]] for item in data["statusCounts"]]
    priority_rows = [[item["name"], item["count"]] for item in data["priorityCounts"]]
    review_rows = [[item["title"], item["priority"], item["module"], item["status"], item["nextReview"]] for item in data["priority"]]
    return f"""# 错题统计

本页由 `tools/refresh_wrong_bank.py` 生成。

## 本次统计日期

{data["generatedAt"]}

## 总量概览

- 总错题数：{data["total"]}
- 待复习：{data["pending"]}
- 仍错：{data["wrongAgain"]}
- 已掌握：{data["mastered"]}
- 逾期复习：{data["overdue"]}
- 系统体检问题：{data["issueCount"]}

## 状态分布

{markdown_table(["状态", "题数"], status_rows)}
## 优先级分布

{markdown_table(["优先级", "题数"], priority_rows)}
## 专题分布

{markdown_table(["专题", "错题数"], module_rows)}
## 高频错因

{markdown_table(["错因", "次数"], reason_rows)}
## 高频知识点

{markdown_table(["知识点", "次数"], knowledge_rows)}
## 高频方法

{markdown_table(["方法", "次数"], method_rows)}
## 优先复习清单

{markdown_table(["错题", "优先级", "专题", "状态", "下次复习"], review_rows)}
## 本周建议

- 先处理 `P1`、`仍错` 和逾期题。
- 每次复习后更新 `mastery`、`status`、`last_review` 和 `next_review`。
- 如果某个错因连续出现，单独建立一页方法复盘。
"""


def render_health(issues: list[dict[str, str]]) -> str:
    level_counts = Counter(issue["level"] for issue in issues)
    rows = [[issue["level"], issue["file"], issue["field"], issue["message"]] for issue in issues]
    return f"""# 系统体检

本页由 `tools/refresh_wrong_bank.py` 生成。

## 体检结果

- P1 问题：{level_counts["P1"]}
- P2 问题：{level_counts["P2"]}
- P3 提醒：{level_counts["P3"]}

## 问题清单

{markdown_table(["级别", "文件", "字段", "说明"], rows)}
## 修复建议

- P1：会影响统计或检索，优先修。
- P2：会影响复习体验，尽量修。
- P3：是质量提醒，不一定阻塞使用。
"""


def render_calendar(data: dict[str, object]) -> str:
    sections = []
    for day in data["calendar"]:
        items = day["items"]
        if not items:
            continue
        rows = [
            [item["title"], item["priority"], item["module"], item["status"], item["nextReview"]]
            for item in items
        ]
        sections.append(f"## {day['date']}\n\n{markdown_table(['错题', '优先级', '专题', '状态', '复习日'], rows)}")
    body = "\n".join(sections) if sections else "未来 14 天暂无已安排复习的题。\n"
    return f"""# 复习日历

本页由 `tools/refresh_wrong_bank.py` 生成。

{body}
"""


def main() -> None:
    notes = load_wrong_notes()
    classification = load_classification()
    issues = validate_notes(notes, classification)
    data = build_data(notes, issues)
    write_text(DASHBOARD, render_dashboard(data))
    write_text(STATS, render_stats(data))
    write_text(HEALTH, render_health(issues))
    write_text(CALENDAR, render_calendar(data))
    write_text(
        DATA_JSON,
        json.dumps(
            {
                "generatedAt": data["generatedAt"],
                "summary": data,
                "issues": issues,
                "notes": [export_note(note) for note in sorted(notes, key=priority_key)],
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    print(f"refreshed {len(notes)} wrong problems; issues: {len(issues)}")


if __name__ == "__main__":
    main()
