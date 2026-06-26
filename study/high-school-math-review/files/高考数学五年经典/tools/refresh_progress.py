# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / "04_原始资料" / "problems.json"
DASHBOARD = VAULT / "00_控制台" / "进度看板.html"
PROGRESS_JSON = VAULT / "04_原始资料" / "progress.json"
CHAPTER_ROOT = VAULT / "06_章节题目合集"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def is_done(status: str) -> bool:
    return status in {"done", "submitted"}


def is_review(status: str) -> bool:
    return status == "review"


def render_dashboard(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>高考数学五年经典题库进度</title>
<style>
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;background:#f6f7f9;color:#17202a}}
a{{color:inherit;text-decoration:none}}a:hover{{text-decoration:underline}}
main{{max-width:1180px;margin:0 auto;padding:24px}}
h1{{font-size:28px;margin:0 0 6px}}h2{{font-size:17px}}
.top{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:end;margin-bottom:18px}}
.links{{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end}}
.quick{{display:inline-flex;align-items:center;min-height:36px;border:1px solid #d9dee7;border-radius:8px;background:#fff;padding:8px 12px;font-size:13px;font-weight:700}}
.quick.primary{{background:#2f9e8f;color:#fff;border-color:#2f9e8f}}
.muted{{color:#667085}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:18px 0}}
.card,section{{background:#fff;border:1px solid #d9dee7;border-radius:8px;padding:14px}}section{{margin-top:14px}}
.module{{display:block;transition:.16s ease}}.module:hover{{box-shadow:0 10px 28px rgba(20,28,38,.08);transform:translateY(-1px);text-decoration:none}}
.num{{font-size:30px;font-weight:750}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}
.bar{{height:10px;background:#e7ebf1;border-radius:999px;overflow:hidden;margin-top:8px}}.fill{{height:100%;background:#2f9e8f}}
.review{{background:#b7791f}}
input{{height:36px;border:1px solid #d9dee7;border-radius:8px;padding:0 10px;font:inherit;width:min(360px,100%);margin:8px 0 10px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}th,td{{border-bottom:1px solid #d9dee7;padding:8px;text-align:left}}th{{color:#667085}}
@media(max-width:700px){{main{{padding:14px}}.top{{display:block}}.links{{justify-content:flex-start;margin-top:10px}}.cards{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<main>
<div class="top">
  <div>
    <h1>高考数学五年经典题库进度</h1>
    <div class="muted">刷新时间：{data.get("generated_at", dt.datetime.now().isoformat(timespec="seconds"))}</div>
  </div>
  <nav class="links">
    <a class="quick primary" href="../../reader.html?file=高考数学五年经典/07_章节题目合集_Obsidian公式版/README.md">章节合集</a>
    <a class="quick" href="../../reader.html?file=高考数学五年经典/00_控制台/题目浏览.md">题目浏览</a>
    <a class="quick" href="../../reader.html?file=高考数学五年经典/00_控制台/内容地图.md">内容地图</a>
  </nav>
</div>
<div id="app"></div>
</main>
<script type="application/json" id="data">{payload}</script>
<script>
const data = JSON.parse(document.getElementById('data').textContent);
function bar(pct) {{ return `<div class="bar"><div class="fill" style="width:${{pct}}%"></div></div>`; }}
function readerHref(path) {{ return `../../reader.html?file=${{encodeURIComponent(path)}}`; }}
function chapterHref(file) {{ return readerHref('高考数学五年经典/07_章节题目合集_Obsidian公式版/' + (file || 'README.md')); }}
document.getElementById('app').innerHTML = `
<div class="cards">
  <div class="card"><div class="muted">总题数</div><div class="num">${{data.total}}</div></div>
  <div class="card"><div class="muted">正式完成</div><div class="num">${{data.done}}</div></div>
  <div class="card"><div class="muted">待核对</div><div class="num">${{data.review}}</div></div>
  <div class="card"><div class="muted">待处理</div><div class="num">${{data.total - data.handled}}</div></div>
  <div class="card"><div class="muted">已处理</div><div class="num">${{data.handled}} / ${{data.total}}</div>${{bar(data.handled_pct)}}</div>
</div>
<section><h2>章节</h2><div class="grid">${{data.modules.map(m => `<a class="card module" href="${{chapterHref(m.chapter_file)}}"><b>${{m.name}}</b><div class="muted">完成 ${{m.done}}，待核对 ${{m.review}}，已处理 ${{m.handled}} / ${{m.total}}</div>${{bar(m.handled_pct)}}</a>`).join('')}}</div></section>
<section><h2>题组</h2><input id="search" placeholder="筛选编号、题组或章节"><table><thead><tr><th>编号</th><th>题组</th><th>章节</th><th>完成</th><th>待核对</th><th>已处理</th></tr></thead><tbody id="lessonRows"></tbody></table></section>`;
function renderLessons(keyword = '') {{
  const q = keyword.trim().toLowerCase();
  const rows = data.lessons.filter(l => !q || `${{l.id}} ${{l.title}} ${{l.module}}`.toLowerCase().includes(q));
  document.getElementById('lessonRows').innerHTML = rows.map(l => `<tr><td><a href="${{chapterHref(l.chapter_file)}}">${{l.id}}</a></td><td><a href="${{chapterHref(l.chapter_file)}}">${{l.title}}</a></td><td>${{l.module}}</td><td>${{l.done}}</td><td>${{l.review}}</td><td>${{l.handled}} / ${{l.total}}（${{l.handled_pct}}%）</td></tr>`).join('');
}}
renderLessons();
document.getElementById('search').addEventListener('input', event => renderLessons(event.target.value));
</script>
</body>
</html>
"""


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = data["problems"]
    lessons = data["lessons"]
    chapter_files = {
        "1": "01_集合与常用逻辑用语.md",
        "2": "02_不等式.md",
        "3": "03_函数.md",
        "4": "04_导数.md",
        "5": "05_三角函数与解三角形.md",
        "6": "06_平面向量与复数.md",
        "7": "07_数列.md",
        "8": "08_立体几何与空间向量.md",
        "9": "09_直线与圆.md",
        "10": "10_圆锥曲线.md",
        "11": "11_概率与统计.md",
        "12": "12_新高考创新题型.md",
    }

    statuses: dict[str, str] = {}
    missing_notes: list[str] = []
    for problem in problems:
        note = VAULT / problem["note_path"]
        fm = read_frontmatter(note) if note.exists() else {}
        if not note.exists():
            missing_notes.append(problem["problem_id"])
        statuses[problem["problem_id"]] = fm.get("status", problem.get("status", "todo"))

    total = len(problems)
    done = sum(1 for status in statuses.values() if is_done(status))
    review = sum(1 for status in statuses.values() if is_review(status))
    handled = done + review
    payload = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "total": total,
        "done": done,
        "review": review,
        "handled": handled,
        "done_pct": round(done / total * 100) if total else 0,
        "handled_pct": round(handled / total * 100) if total else 0,
        "status_counts": dict(Counter(statuses.values())),
        "missing_note_count": len(missing_notes),
        "missing_notes": missing_notes[:100],
        "modules": [],
        "lessons": [],
    }

    by_module: dict[str, list[dict]] = defaultdict(list)
    by_lesson: dict[str, list[dict]] = defaultdict(list)
    for problem in problems:
        by_module[problem["module_id"]].append(problem)
        by_lesson[problem["lesson_id"]].append(problem)

    module_names = {lesson["module_id"]: lesson["module"] for lesson in lessons}
    for module_id in sorted(by_module, key=lambda value: int(value)):
        rows = by_module[module_id]
        count = len(rows)
        module_done = sum(1 for p in rows if is_done(statuses[p["problem_id"]]))
        module_review = sum(1 for p in rows if is_review(statuses[p["problem_id"]]))
        module_handled = module_done + module_review
        payload["modules"].append(
            {
                "name": f"{module_id} {module_names.get(module_id, '')}",
                "total": count,
                "done": module_done,
                "review": module_review,
                "handled": module_handled,
                "handled_pct": round(module_handled / count * 100) if count else 0,
                "chapter_file": chapter_files.get(str(module_id), "README.md"),
            }
        )

    for lesson in lessons:
        rows = by_lesson[lesson["lesson_id"]]
        count = len(rows)
        lesson_done = sum(1 for p in rows if is_done(statuses[p["problem_id"]]))
        lesson_review = sum(1 for p in rows if is_review(statuses[p["problem_id"]]))
        lesson_handled = lesson_done + lesson_review
        payload["lessons"].append(
            {
                "id": lesson["lesson_id"],
                "title": lesson["topic"],
                "module": lesson["module"],
                "total": count,
                "done": lesson_done,
                "review": lesson_review,
                "handled": lesson_handled,
                "handled_pct": round(lesson_handled / count * 100) if count else 0,
                "chapter_file": chapter_files.get(str(lesson.get("module_id") or ""), "README.md"),
            }
        )

    write_text(PROGRESS_JSON, json.dumps(payload, ensure_ascii=False, indent=2))
    write_text(DASHBOARD, render_dashboard(payload))
    print(f"已刷新进度看板：正式完成 {done}/{total}，待核对 {review}，已处理 {done + review}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
