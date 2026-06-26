# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / "04_原始资料" / "problems.json"
CHAPTER_ROOT = VAULT / "07_章节题目合集_Obsidian公式版"
DONE_STATUS = {"done", "submitted"}
REVIEW_STATUS = {"review"}


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
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def is_done(status: str) -> bool:
    return status in DONE_STATUS


def is_review(status: str) -> bool:
    return status in REVIEW_STATUS


def render_dashboard(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>题库进度看板</title>
<style>
  :root {{
    --ink:#17202a;
    --muted:#667085;
    --line:#d9dee7;
    --bg:#f6f7f9;
    --panel:#ffffff;
    --teal:#2f9e8f;
    --teal-soft:#e7f5f2;
    --gold:#b98520;
    --coral:#d86b5b;
    --shadow:0 10px 30px rgba(20, 28, 38, .07);
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--ink); }}
  a {{ color:inherit; text-decoration:none; }}
  main {{ max-width:1220px; margin:0 auto; padding:24px; }}
  header {{
    display:grid;
    grid-template-columns:minmax(0,1fr) auto;
    gap:18px;
    align-items:end;
    margin-bottom:16px;
  }}
  h1 {{ margin:0; font-size:30px; letter-spacing:0; }}
  .stamp,.label,.module-meta,.hint {{ color:var(--muted); }}
  .quick-links {{ display:flex; flex-wrap:wrap; gap:8px; justify-content:flex-end; }}
  .quick-link {{
    display:inline-flex;
    align-items:center;
    gap:6px;
    min-height:36px;
    padding:8px 12px;
    border:1px solid var(--line);
    border-radius:8px;
    background:var(--panel);
    font-size:13px;
    font-weight:650;
  }}
  .quick-link.primary {{ background:var(--teal); color:#fff; border-color:var(--teal); }}
  .quick-link:hover,.module:hover {{ box-shadow:var(--shadow); transform:translateY(-1px); }}
  .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; margin-bottom:14px; }}
  .card,section,.module {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; }}
  .card {{ padding:14px; min-height:102px; }}
  .num {{ font-size:30px; font-weight:750; margin-top:4px; }}
  .bar {{ height:10px; background:#e7ebf1; border-radius:999px; overflow:hidden; margin-top:8px; }}
  .fill {{ height:100%; background:var(--teal); }}
  section {{ padding:14px; margin-bottom:14px; box-shadow:0 1px 0 rgba(20,28,38,.02); }}
  .section-head {{ display:flex; justify-content:space-between; gap:12px; align-items:center; margin-bottom:10px; }}
  h2 {{ font-size:16px; margin:0; }}
  .search {{
    width:min(360px,100%);
    height:36px;
    border:1px solid var(--line);
    border-radius:8px;
    padding:0 11px;
    font:inherit;
    background:#fff;
  }}
  .module-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }}
  .module {{ display:block; padding:10px; transition:.16s ease; }}
  .module-title {{ font-weight:700; font-size:14px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .module-meta {{ font-size:12px; margin-top:3px; }}
  .pill {{ display:inline-flex; align-items:center; justify-content:center; min-width:48px; padding:3px 8px; border-radius:999px; background:var(--teal-soft); color:#17685e; font-weight:700; font-size:12px; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; }}
  th,td {{ border-bottom:1px solid var(--line); padding:8px 6px; text-align:left; }}
  th {{ color:var(--muted); font-weight:650; }}
  tbody tr:hover {{ background:#f9fafb; }}
  .lesson-link {{ font-weight:650; color:#17685e; }}
  .empty {{ color:var(--muted); text-align:center; padding:18px 0; }}
  @media(max-width:860px) {{
    main {{ padding:14px; }}
    header {{ grid-template-columns:1fr; align-items:start; }}
    .quick-links {{ justify-content:flex-start; }}
    .cards {{ grid-template-columns:repeat(2,minmax(0,1fr)); }}
    .section-head {{ display:block; }}
    .search {{ margin-top:10px; }}
  }}
  @media(max-width:560px) {{ .cards {{ grid-template-columns:1fr; }} table {{ font-size:12px; }} }}
</style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>题库进度看板</h1>
      <div class="stamp" id="stamp"></div>
    </div>
    <nav class="quick-links">
      <a class="quick-link primary" id="chapterIndex" href="#">章节题库</a>
      <a class="quick-link" id="detailIndex" href="#">细分题库</a>
    </nav>
  </header>
  <div class="cards" id="cards"></div>
  <section>
    <div class="section-head">
      <h2>章节入口</h2>
      <span class="hint">点击章节进入题目合集</span>
    </div>
    <div class="module-grid" id="modules"></div>
  </section>
  <section>
    <div class="section-head">
      <h2>讲义进度</h2>
      <input class="search" id="lessonSearch" placeholder="筛选讲义或章节编号">
    </div>
    <table>
      <thead><tr><th>讲义</th><th>模块</th><th>进度</th><th>完成</th></tr></thead>
      <tbody id="lessons"></tbody>
    </table>
    <div class="empty" id="empty" hidden>没有匹配的讲义</div>
  </section>
</main>
<script>
const data = {payload};
const done = data.done || data.modules.reduce((sum, m) => sum + m.done, 0);
const review = data.review || data.modules.reduce((sum, m) => sum + (m.review || 0), 0);
const handled = data.handled || done + review;
const pct = data.total ? Math.round(done / data.total * 100) : 0;
const handledPct = data.total ? Math.round(handled / data.total * 100) : 0;
const chapterFiles = {{
  "1":"01_基本不等式.md","2":"02_函数.md","3":"03_新定义.md","4":"04_导数选填.md",
  "5":"05_导数大题.md","6":"06_三角函数.md","7":"07_解三角形.md","8":"08_向量.md",
  "9":"09_立体几何.md","10":"10_数列.md","11":"11_复数.md","12":"12_直线和圆.md",
  "13":"13_圆锥曲线(难点).md","14":"14_圆锥曲线(小题).md","15":"15_概率统计.md","16":"16_排列组合.md"
}};
function bar(pct) {{ return `<div class="bar"><div class="fill" style="width:${{pct}}%"></div></div>`; }}
function moduleId(name) {{ return String(name).split(" ")[0]; }}
function readerHref(relPath) {{ return `../../reader.html?file=${{encodeURIComponent(relPath)}}`; }}
function vaultMarkdownHref(relPath) {{ return readerHref(`Obsidian题库/${{relPath}}`); }}
function chapterMarkdownHref(file) {{ return readerHref(`Obsidian题库/07_章节题目合集_Obsidian公式版/${{file}}`); }}
function chapterHref(name) {{
  const id = moduleId(name);
  return chapterMarkdownHref(chapterFiles[id] || "README.md");
}}
function lessonHref(lesson) {{
  const id = lesson.id.split("-")[0];
  const chapter = chapterFiles[id] || "README.md";
  return chapterMarkdownHref(chapter);
}}
document.getElementById("chapterIndex").href = chapterMarkdownHref("README.md");
document.getElementById("detailIndex").href = vaultMarkdownHref("00_控制台/题目浏览.md");
document.getElementById("stamp").textContent = `生成时间：${{data.generated_at}}`;
document.getElementById("cards").innerHTML = [
  ["总题数", data.total, ""],
  ["正式完成", done, ""],
  ["待核对", review, ""],
  ["待处理", data.total - handled, ""],
  ["已处理", `${{handledPct}}%`, bar(handledPct)]
].map(([label,value,extra])=>`<div class="card"><div class="label">${{label}}</div><div class="num">${{value}}</div>${{extra}}</div>`).join("");
document.getElementById("modules").innerHTML = data.modules.map(m=>`<a class="module" href="${{chapterHref(m.name)}}"><div class="module-title" title="${{m.name}}">${{m.name}}</div><div class="module-meta">完成 ${{m.done}}，待核对 ${{m.review || 0}}，已处理 ${{m.handled || m.done}} / ${{m.total}}</div>${{bar(m.handled_pct || m.pct)}}</a>`).join("");
const lessonsBody = document.getElementById("lessons");
const empty = document.getElementById("empty");
function renderLessons(keyword = "") {{
  const q = keyword.trim().toLowerCase();
  const rows = data.lessons.filter(l => !q || `${{l.id}} ${{l.title}} ${{l.module}}`.toLowerCase().includes(q));
  lessonsBody.innerHTML = rows.map(l=>`<tr><td><a class="lesson-link" href="${{lessonHref(l)}}">${{l.id}} ${{l.title}}</a></td><td>${{l.module}}</td><td>${{bar(l.handled_pct || l.pct)}} <span class="pill">${{l.handled_pct || l.pct}}%</span></td><td>${{l.done}} 完成，${{l.review || 0}} 待核对，${{l.handled || l.done}} / ${{l.total}}</td></tr>`).join("");
  empty.hidden = rows.length > 0;
}}
renderLessons();
document.getElementById("lessonSearch").addEventListener("input", event => renderLessons(event.target.value));
</script>
</body>
</html>
"""


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = data["problems"]
    lessons = data["lessons"]
    status_by_id = {}
    missing_notes: list[str] = []
    for problem in problems:
        note = VAULT / problem["note_path"]
        fm = read_frontmatter(note) if note.exists() else {}
        if not note.exists():
            missing_notes.append(problem["problem_id"])
        status_by_id[problem["problem_id"]] = fm.get("status", problem.get("status", "todo"))
        problem["status"] = status_by_id[problem["problem_id"]]

    chapter_files = {
        "1": "01_基本不等式.md",
        "2": "02_函数.md",
        "3": "03_新定义.md",
        "4": "04_导数选填.md",
        "5": "05_导数大题.md",
        "6": "06_三角函数.md",
        "7": "07_解三角形.md",
        "8": "08_向量.md",
        "9": "09_立体几何.md",
        "10": "10_数列.md",
        "11": "11_复数.md",
        "12": "12_直线和圆.md",
        "13": "13_圆锥曲线(难点).md",
        "14": "14_圆锥曲线(小题).md",
        "15": "15_概率统计.md",
        "16": "16_排列组合.md",
    }
    by_lesson: dict[str, list[dict]] = defaultdict(list)
    for problem in problems:
        by_lesson[problem["lesson_id"]].append(problem)

    status_counts = Counter(status_by_id.values())
    total_done = sum(1 for status in status_by_id.values() if is_done(status))
    total_review = sum(1 for status in status_by_id.values() if is_review(status))
    total_handled = total_done + total_review

    module_order: dict[str, dict] = {}
    out = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "total": len(problems),
        "done": total_done,
        "review": total_review,
        "handled": total_handled,
        "done_pct": round(total_done / len(problems) * 100) if problems else 0,
        "handled_pct": round(total_handled / len(problems) * 100) if problems else 0,
        "status_counts": dict(status_counts),
        "missing_note_count": len(missing_notes),
        "missing_notes": missing_notes[:100],
        "modules": [],
        "lessons": [],
    }
    for lesson in lessons:
        module_key = f"{lesson['module_id']} {lesson['module']}"
        module_order.setdefault(module_key, {"name": module_key, "total": 0, "done": 0, "review": 0, "handled": 0, "chapter_file": chapter_files.get(str(lesson["module_id"]), "README.md")})
        rows = by_lesson[lesson["lesson_id"]]
        total = len(rows)
        done = sum(1 for p in rows if is_done(status_by_id.get(p["problem_id"], "")))
        review = sum(1 for p in rows if is_review(status_by_id.get(p["problem_id"], "")))
        handled = done + review
        module_order[module_key]["total"] += total
        module_order[module_key]["done"] += done
        module_order[module_key]["review"] += review
        module_order[module_key]["handled"] += handled
        out["lessons"].append({"id": lesson["lesson_id"], "title": lesson["display_title"], "module": module_key, "chapter_file": chapter_files.get(str(lesson["module_id"]), "README.md"), "total": total, "done": done, "review": review, "handled": handled, "pct": round(done / total * 100) if total else 0, "handled_pct": round(handled / total * 100) if total else 0})
    for module in module_order.values():
        total = module["total"]
        done = module["done"]
        handled = module["handled"]
        module["pct"] = round(done / total * 100) if total else 0
        module["handled_pct"] = round(handled / total * 100) if total else 0
        out["modules"].append(module)

    (VAULT / "04_原始资料" / "progress.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    write_text(VAULT / "00_控制台" / "进度看板.html", render_dashboard(out))
    print("进度看板已刷新。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
