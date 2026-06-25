# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OVERVIEW_MD = ROOT / "系统总控台.md"
OVERVIEW_JSON = ROOT / "系统总控台.json"
WORKBENCH_MD = ROOT / "学习工作台.md"
WORKBENCH_HTML = ROOT / "学习工作台.html"


TASKS = [
    {
        "key": "question_bank",
        "name": "二轮 Obsidian 题库进度",
        "cwd": ROOT / "Obsidian题库",
        "args": ["tools/refresh_progress.py"],
    },
    {
        "key": "ai_notes",
        "name": "AI 笔记索引",
        "cwd": ROOT / "Obsidian题库",
        "args": ["tools/ai_note_manager.py", "index"],
    },
    {
        "key": "wrong_bank",
        "name": "个人错题库",
        "cwd": ROOT / "个人错题库",
        "args": ["tools/refresh_wrong_bank.py"],
    },
    {
        "key": "classic_bank",
        "name": "高考数学五年经典题库",
        "cwd": ROOT / "高考数学五年经典",
        "args": ["tools/refresh_progress.py"],
    },
    {
        "key": "content_optimizer",
        "name": "内容复习建议",
        "cwd": ROOT,
        "args": ["tools/content_optimizer.py"],
    },
]

POST_TASKS = [
    {
        "key": "llm_wiki",
        "name": "LLM 知识库编译",
        "cwd": ROOT,
        "args": ["tools/llm_wiki_maintain.py", "refresh"],
    },
]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"_load_error": f"{path}: {exc}"}


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "暂无数据\n"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        cells = [str(cell).replace("|", "\\|").replace("\n", " ") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def rel_link(path: Path, label: str) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return f"[{label}]({rel})"


def rel_link_value(path_value: Any, label: Any, fallback: str = "暂无") -> str:
    text = str(label or "").strip()
    raw_path = str(path_value or "").strip()
    if not raw_path or not text:
        return fallback
    path = Path(raw_path)
    if not path.is_absolute():
        path = ROOT / path
    try:
        return rel_link(path, text)
    except ValueError:
        return text


def run_task(task: dict[str, Any]) -> dict[str, Any]:
    started = dt.datetime.now()
    script = task["cwd"] / task["args"][0]
    if not script.exists():
        return {
            "key": task["key"],
            "name": task["name"],
            "status": "missing",
            "seconds": 0,
            "message": f"脚本不存在：{script}",
        }
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    proc = subprocess.run(
        [sys.executable, *task["args"]],
        cwd=str(task["cwd"]),
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    seconds = round((dt.datetime.now() - started).total_seconds(), 2)
    output = (proc.stdout or "").strip()
    error = (proc.stderr or "").strip()
    return {
        "key": task["key"],
        "name": task["name"],
        "status": "ok" if proc.returncode == 0 else "failed",
        "returncode": proc.returncode,
        "seconds": seconds,
        "message": output.splitlines()[-1] if output else error.splitlines()[-1] if error else "",
        "stdout": output,
        "stderr": error,
    }


def run_tasks(tasks: list[dict[str, Any]], jobs: int) -> list[dict[str, Any]]:
    if not tasks:
        return []
    worker_count = max(1, min(jobs, len(tasks)))
    if worker_count == 1:
        return [run_task(task) for task in tasks]

    results_by_key: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        future_map = {executor.submit(run_task, task): task for task in tasks}
        for future in concurrent.futures.as_completed(future_map):
            task = future_map[future]
            try:
                result = future.result()
            except Exception as exc:  # noqa: BLE001
                result = {
                    "key": task["key"],
                    "name": task["name"],
                    "status": "failed",
                    "returncode": -1,
                    "seconds": 0,
                    "message": f"{type(exc).__name__}: {exc}",
                    "stdout": "",
                    "stderr": f"{type(exc).__name__}: {exc}",
                }
            results_by_key[task["key"]] = result
    return [results_by_key[task["key"]] for task in tasks]


def question_bank_row(name: str, root: Path, data: dict[str, Any]) -> list[Any]:
    total = int(data.get("total") or 0)
    done = int(data.get("done") or 0)
    review = int(data.get("review") or 0)
    handled = int(data.get("handled") or done + review)
    handled_pct = int(data.get("handled_pct") or (round(handled / total * 100) if total else 0))
    missing = int(data.get("missing_note_count") or 0)
    return [
        name,
        total,
        done,
        review,
        f"{handled} / {total} ({handled_pct}%)" if total else "0",
        missing,
        rel_link(root / "00_控制台" / "进度看板.html", "看板"),
    ]


def render_overview(results: list[dict[str, Any]], data: dict[str, Any]) -> str:
    generated_at = dt.datetime.now().isoformat(timespec="seconds")
    question = data.get("question_bank", {})
    classic = data.get("classic_bank", {})
    wrong = data.get("wrong_bank", {}).get("summary", {})
    ai = data.get("ai_notes", {})
    content = data.get("content", {})
    llm = data.get("llm_wiki", {}).get("summary", {})
    learning_path = content.get("learningPath", [])

    bank_rows = [
        question_bank_row("二轮 Obsidian 题库", ROOT / "Obsidian题库", question),
        question_bank_row("高考数学五年经典", ROOT / "高考数学五年经典", classic),
    ]

    wrong_rows = [
        ["总错题", wrong.get("total", 0)],
        ["今日队列", wrong.get("due", 0)],
        ["仍错", wrong.get("wrongAgain", 0)],
        ["逾期", wrong.get("overdue", 0)],
        ["体检问题", wrong.get("issueCount", 0)],
    ]

    ai_rows = [
        ["标准笔记", ai.get("total", 0)],
        ["待整理材料", ai.get("inbox", {}).get("pending", 0)],
        ["转化待处理", sum((ai.get("conversion", {}).get("summary") or {}).values())],
        ["需要检查的问题", ai.get("issueCount", 0)],
        ["ready", ai.get("statusCounts", {}).get("ready", 0)],
        ["review", ai.get("statusCounts", {}).get("review", 0)],
    ]

    content_rows = [
        ["错题总数", content.get("wrong", {}).get("total", 0)],
        ["今日队列", content.get("wrong", {}).get("due", 0)],
        ["二轮题库题量", content.get("questionBank", {}).get("total", 0)],
        ["五年经典题量", content.get("classicBank", {}).get("total", 0)],
        ["AI 标准笔记", content.get("aiNotes", {}).get("total", ai.get("total", 0))],
        ["今日学习路线", len(learning_path)],
        ["LLM Wiki 主题页", llm.get("topicTotal", 0)],
        ["LLM Wiki 检查项", llm.get("issueTotal", 0)],
    ]

    learning_rows = []
    for item in learning_path[:8]:
        ai_note = item.get("ai_note") or {}
        two_round = item.get("two_round") or {}
        classic_problem = item.get("classic") or {}
        learning_rows.append(
            [
                item.get("order", ""),
                rel_link_value(item.get("file"), item.get("title")),
                f"{item.get('priority', '')} / {item.get('status', '')}",
                rel_link_value(ai_note.get("file"), ai_note.get("title"), item.get("ai_note_action", "建议补笔记")),
                rel_link_value(two_round.get("note_path"), two_round.get("problem_id")),
                rel_link_value(classic_problem.get("note_path"), classic_problem.get("problem_id")),
            ]
        )

    task_rows = [
        [
            item["name"],
            item["status"],
            item.get("seconds", 0),
            item.get("message", ""),
        ]
        for item in results
    ]

    return f"""# 系统总控台

本页由 `tools/maintain_study_systems.py` 生成，用来统一查看题库、错题库和 AI 笔记管理系统。

## 更新时间

{generated_at}

## 一键维护

在当前总目录运行：

```powershell
.\\tools\\maintain_study_systems.ps1
```

## 快速入口

- {rel_link(WORKBENCH_HTML, "互动工作台")}
- {rel_link(ROOT / "学习工作台.md", "学习工作台")}
- {rel_link(ROOT / "Obsidian题库" / "00_控制台" / "总览.md", "二轮题库总览")}
- {rel_link(ROOT / "Obsidian题库" / "00_控制台" / "进度看板.html", "二轮题库进度看板")}
- {rel_link(ROOT / "内容优化总览.md", "内容优化总览")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "今日学习路线.md", "今日学习路线")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "相似题推荐.md", "错题相似题推荐")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "错题关联笔记.md", "错题关联笔记")}
- {rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "AI学习流水线.md", "AI 学习流水线")}
- {rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "对话导入清单.md", "AI 对话导入清单")}
- {rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "AI笔记转化看板.md", "AI 笔记转化看板")}
- {rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "标准笔记索引.md", "AI 笔记索引")}
- {rel_link(ROOT / "LLM知识库" / "README.md", "LLM 知识库")}
- {rel_link(ROOT / "LLM知识库" / "wiki" / "00_Index.md", "LLM Wiki 索引")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "学习工作台.md", "个人错题库学习工作台")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "错题看板.html", "个人错题库看板")}
- {rel_link(ROOT / "高考数学五年经典" / "00_控制台" / "总览.md", "五年经典总览")}
- {rel_link(ROOT / "高考数学五年经典" / "00_控制台" / "进度看板.html", "五年经典进度看板")}

## 题库快照

{markdown_table(["系统", "总题数", "正式完成", "待核对", "已处理", "缺失笔记", "入口"], bank_rows)}
## 错题库快照

{markdown_table(["指标", "数量"], wrong_rows)}
## AI 笔记快照

{markdown_table(["指标", "数量"], ai_rows)}
## 内容优化快照

{markdown_table(["指标", "数量"], content_rows)}
## 今日学习闭环

{markdown_table(["顺序", "错题", "优先状态", "AI笔记", "二轮题", "五年题"], learning_rows)}
## 本次维护结果

{markdown_table(["任务", "状态", "耗时秒", "结果"], task_rows)}
## 建议动作

- 先看错题库的“今日队列”和“仍错”，这是最直接影响复习收益的部分。
- 题库中 `review` 状态表示已经处理但需要人工核对，优先级高于普通 `todo`。
- AI 笔记体检有问题时，先修缺失字段和小节顺序，再继续批量整理。
"""


def render_workbench(results: list[dict[str, Any]], data: dict[str, Any]) -> str:
    generated_at = dt.datetime.now().isoformat(timespec="seconds")
    question = data.get("question_bank", {})
    classic = data.get("classic_bank", {})
    wrong_bank = data.get("wrong_bank", {})
    wrong = wrong_bank.get("summary", {})
    ai = data.get("ai_notes", {})
    content = data.get("content", {})
    llm = data.get("llm_wiki", {}).get("summary", {})
    learning_path = content.get("learningPath", [])
    failed_tasks = [item for item in results if item.get("status") not in {"ok", None}]

    today_rows = [
        [
            "1",
            "按路线完成今日闭环",
            f"{len(learning_path)} 条",
            rel_link(ROOT / "个人错题库" / "00_控制台" / "今日学习路线.md", "今日学习路线"),
            "每条做到：原错题重做 -> 笔记复盘 -> 二轮同类题 -> 五年迁移题",
        ],
        [
            "2",
            "处理仍错和逾期题",
            f"{wrong.get('wrongAgain', 0)} 仍错 / {wrong.get('overdue', 0)} 逾期",
            rel_link(ROOT / "个人错题库" / "00_控制台" / "错题统计.md", "错题统计"),
            "更新 status、mastery、last_review、next_review",
        ],
        [
            "3",
            "补齐错题对应笔记",
            f"{ai.get('total', 0)} 张标准笔记",
            rel_link(ROOT / "个人错题库" / "00_控制台" / "错题关联笔记.md", "错题关联笔记"),
            "没有匹配笔记的错题，整理成一张方法卡",
        ],
        [
            "4",
            "查看 LLM 知识库队列",
            f"{llm.get('topicTotal', 0)} 个主题 / {llm.get('issueTotal', 0)} 个检查项",
            rel_link(ROOT / "LLM知识库" / "wiki" / "00_Index.md", "LLM Wiki"),
            "先看待编译队列，再补标准笔记或修复结构问题",
        ],
        [
            "5",
            "检查系统健康",
            f"{wrong.get('issueCount', 0)} 个错题体检问题",
            rel_link(ROOT / "个人错题库" / "00_控制台" / "系统体检.md", "系统体检"),
            "先修 P1，再看 P2/P3 提醒",
        ],
    ]

    path_rows = []
    for item in learning_path[:6]:
        ai_note = item.get("ai_note") or {}
        two_round = item.get("two_round") or {}
        classic_problem = item.get("classic") or {}
        path_rows.append(
            [
                item.get("order", ""),
                rel_link_value(item.get("file"), item.get("title")),
                f"{item.get('priority', '')} / {item.get('status', '')} / 掌握度{item.get('mastery', '')}",
                item.get("review_reason", ""),
                item.get("timebox", ""),
                item.get("anti_mistake_tip", ""),
                rel_link_value(ai_note.get("file"), ai_note.get("title"), item.get("ai_note_action", "建议补笔记")),
                rel_link_value(two_round.get("note_path"), two_round.get("problem_id")),
                rel_link_value(classic_problem.get("note_path"), classic_problem.get("problem_id")),
            ]
        )

    health_rows = [
        ["维护任务", "异常" if failed_tasks else "正常", "；".join(item.get("name", "") for item in failed_tasks) or "全部通过"],
        ["错题库体检", wrong.get("issueCount", 0), rel_link(ROOT / "个人错题库" / "00_控制台" / "系统体检.md", "查看体检")],
        ["二轮题库缺失笔记", question.get("missing_note_count", 0), rel_link(ROOT / "Obsidian题库" / "00_控制台" / "进度看板.html", "查看看板")],
        ["五年经典缺失笔记", classic.get("missing_note_count", 0), rel_link(ROOT / "高考数学五年经典" / "00_控制台" / "进度看板.html", "查看看板")],
        ["AI 笔记检查问题", ai.get("issueCount", 0), rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "系统体检.md", "AI 体检")],
        ["LLM Wiki 检查项", llm.get("issueTotal", 0), rel_link(ROOT / "LLM知识库" / "wiki" / "04_Health_Check.md", "Wiki 体检")],
    ]

    bank_rows = [
        [
            "二轮题库",
            question.get("total", 0),
            f"{question.get('handled', 0)} / {question.get('total', 0)} ({question.get('handled_pct', 0)}%)",
            rel_link(ROOT / "Obsidian题库" / "00_控制台" / "内容地图.md", "内容地图"),
        ],
        [
            "五年经典",
            classic.get("total", 0),
            f"{classic.get('handled', 0)} / {classic.get('total', 0)} ({classic.get('handled_pct', 0)}%)",
            rel_link(ROOT / "高考数学五年经典" / "00_控制台" / "内容地图.md", "内容地图"),
        ],
    ]

    return f"""# 学习工作台

本页由 `tools/maintain_study_systems.py` 生成。日常复习建议先打开这里，再进入对应题库或错题库。

## 更新时间

{generated_at}

## 今天先做

{markdown_table(["顺序", "任务", "数量", "入口", "完成标准"], today_rows)}
## 今日学习闭环

{markdown_table(["顺序", "错题", "优先状态", "为什么今天做", "建议用时", "防错口令", "AI笔记/整理方向", "二轮题", "五年题"], path_rows)}
## 系统健康

{markdown_table(["项目", "状态/数量", "入口或说明"], health_rows)}
## 题库资源

{markdown_table(["题库", "总题数", "已处理", "内容入口"], bank_rows)}
## 常用入口

- {rel_link(WORKBENCH_HTML, "互动工作台")}
- {rel_link(ROOT / "系统总控台.md", "系统总控台")}
- {rel_link(ROOT / "内容优化总览.md", "内容优化总览")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "学习工作台.md", "个人错题库学习工作台")}
- {rel_link(ROOT / "个人错题库" / "00_控制台" / "错题看板.html", "个人错题库看板")}
- {rel_link(ROOT / "Obsidian题库" / "08_AI笔记管理" / "AI学习流水线.md", "AI 学习流水线")}
- {rel_link(ROOT / "LLM知识库" / "wiki" / "00_Index.md", "LLM Wiki 索引")}
"""


def render_workbench_html(results: list[dict[str, Any]], data: dict[str, Any]) -> str:
    generated_at = dt.datetime.now().isoformat(timespec="seconds")
    question = data.get("question_bank", {})
    classic = data.get("classic_bank", {})
    wrong = data.get("wrong_bank", {}).get("summary", {})
    ai = data.get("ai_notes", {})
    content = data.get("content", {})
    llm = data.get("llm_wiki", {}).get("summary", {})
    payload = json.dumps(
        {
            "generatedAt": generated_at,
            "results": results,
            "question": question,
            "classic": classic,
            "wrong": wrong,
            "ai": ai,
            "content": content,
            "llm": llm,
            "learningPath": content.get("learningPath", []),
            "links": {
                "workbenchMd": "学习工作台.md",
                "overview": "系统总控台.md",
                "content": "内容优化总览.md",
                "wrongDashboard": "个人错题库/00_控制台/错题看板.html",
                "wrongRoute": "个人错题库/00_控制台/今日学习路线.md",
                "wrongHealth": "个人错题库/00_控制台/系统体检.md",
                "questionDashboard": "Obsidian题库/00_控制台/进度看板.html",
                "questionMap": "Obsidian题库/00_控制台/内容地图.md",
                "classicDashboard": "高考数学五年经典/00_控制台/进度看板.html",
                "classicMap": "高考数学五年经典/00_控制台/内容地图.md",
                "aiPipeline": "Obsidian题库/08_AI笔记管理/AI学习流水线.md",
                "aiConversion": "Obsidian题库/08_AI笔记管理/AI笔记转化看板.md",
                "aiIndex": "Obsidian题库/08_AI笔记管理/标准笔记索引.md",
                "llmWiki": "LLM知识库/wiki/00_Index.md",
                "llmHealth": "LLM知识库/wiki/04_Health_Check.md",
                "llmQueue": "LLM知识库/wiki/05_Compile_Queue.md",
            },
        },
        ensure_ascii=False,
    ).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>高中数学复习</title>
<style>
  :root {{
    --bg:#f5f6f3;
    --panel:#ffffff;
    --ink:#18232d;
    --muted:#65707f;
    --line:#dce1e7;
    --teal:#2f8f83;
    --teal-soft:#e8f4f1;
    --blue:#425f9c;
    --gold:#a66d22;
    --red:#b65342;
    --shadow:0 12px 30px rgba(20, 28, 38, .08);
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0;
    background:var(--bg);
    color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;
    line-height:1.5;
  }}
  a {{ color:var(--blue); text-decoration:none; }}
  a:hover {{ text-decoration:underline; }}
  .shell {{ max-width:1280px; margin:0 auto; padding:24px; }}
  header {{
    display:grid;
    grid-template-columns:minmax(0,1fr) auto;
    gap:18px;
    align-items:end;
    margin-bottom:16px;
  }}
  h1 {{ margin:0; font-size:30px; letter-spacing:0; }}
  h2 {{ margin:0; font-size:17px; }}
  .muted,.sub,.small {{ color:var(--muted); }}
  .sub {{ margin-top:4px; }}
  .small {{ font-size:12px; }}
  .actions {{ display:flex; flex-wrap:wrap; gap:8px; justify-content:flex-end; }}
  .action {{
    min-height:36px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:8px 12px;
    border:1px solid var(--line);
    border-radius:8px;
    background:var(--panel);
    color:var(--ink);
    font-size:13px;
    font-weight:700;
  }}
  .action.primary {{ background:var(--teal); border-color:var(--teal); color:#fff; }}
  .metrics {{ display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:12px; margin:14px 0; }}
  .card,section {{
    background:var(--panel);
    border:1px solid var(--line);
    border-radius:8px;
  }}
  .card {{ min-height:104px; padding:14px; }}
  .card b {{ display:block; font-size:13px; color:var(--muted); font-weight:650; }}
  .value {{ margin-top:3px; font-size:30px; font-weight:780; }}
  .card.focus {{ border-color:#e1c58e; background:#fffaf0; }}
  .card.warn {{ border-color:#e4b5aa; background:#fff7f5; }}
  section {{ padding:14px; margin-top:14px; }}
  .section-head {{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    margin-bottom:10px;
  }}
  .grid-2 {{ display:grid; grid-template-columns:minmax(0,1.1fr) minmax(340px,.9fr); gap:14px; }}
  .table-wrap {{ overflow:auto; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; min-width:720px; }}
  th,td {{ border-bottom:1px solid var(--line); padding:8px 7px; text-align:left; vertical-align:top; }}
  th {{ color:var(--muted); font-weight:700; }}
  tr:hover td {{ background:#fafbfc; }}
  .pill {{
    display:inline-flex;
    align-items:center;
    min-height:24px;
    padding:2px 8px;
    border-radius:999px;
    background:#eef1f3;
    color:#334155;
    font-size:12px;
    font-weight:700;
    white-space:nowrap;
  }}
  .pill.ok {{ background:var(--teal-soft); color:#17685e; }}
  .pill.warn {{ background:#fff1d6; color:#7a4a0a; }}
  .pill.bad {{ background:#ffe5df; color:#963b2f; }}
  .progress {{ height:10px; background:#e7ebf1; border-radius:999px; overflow:hidden; margin-top:6px; }}
  .fill {{ height:100%; background:var(--teal); width:0; }}
  .module-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:10px; }}
  .module {{
    padding:10px;
    border:1px solid var(--line);
    border-radius:8px;
    background:#fff;
    min-height:86px;
  }}
  .module-title {{ font-weight:750; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .controls {{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; }}
  .segmented {{ display:inline-flex; border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; }}
  .segmented button {{
    border:0;
    background:#fff;
    padding:8px 11px;
    font:inherit;
    font-size:13px;
    font-weight:700;
    color:var(--muted);
    cursor:pointer;
  }}
  .segmented button.active {{ background:var(--teal); color:#fff; }}
  .search {{
    width:min(300px,100%);
    height:36px;
    border:1px solid var(--line);
    border-radius:8px;
    padding:0 11px;
    font:inherit;
    background:#fff;
  }}
  .chips {{ display:flex; flex-wrap:wrap; gap:8px; }}
  .chip {{ border:1px solid var(--line); border-radius:999px; padding:6px 10px; background:#fff; font-size:13px; }}
  .empty {{ color:var(--muted); padding:18px; border:1px dashed var(--line); border-radius:8px; text-align:center; }}
  @media(max-width:1040px) {{
    .metrics {{ grid-template-columns:repeat(3,minmax(0,1fr)); }}
    .grid-2 {{ grid-template-columns:1fr; }}
  }}
  @media(max-width:720px) {{
    .shell {{ padding:14px; }}
    header {{ grid-template-columns:1fr; }}
    .actions {{ justify-content:flex-start; }}
    .metrics {{ grid-template-columns:repeat(2,minmax(0,1fr)); }}
    .section-head {{ align-items:flex-start; flex-direction:column; }}
  }}
  @media(max-width:500px) {{
    .metrics {{ grid-template-columns:1fr; }}
    h1 {{ font-size:25px; }}
  }}
</style>
<link rel="stylesheet" href="assets/open-design/workbench.css?v=20260625-2">
</head>
<body>
<main class="shell">
  <header class="topbar">
    <a class="brand" href="学习工作台.html" aria-label="高中数学复习索引">
      <span class="brand-mark">∑</span>
      <span>高中数学复习</span>
    </a>
    <nav class="actions" id="actions"></nav>
  </header>

  <section class="hero">
    <div class="hero-copy">
      <p class="eyebrow">复习索引</p>
      <h1>高中数学复习</h1>
      <div class="sub">更新：<span id="generatedAt"></span></div>
      <div class="hero-actions">
        <a id="heroRouteLink" class="action primary" href="#">今日路线</a>
        <a id="heroDashboardLink" class="action" href="#">错题看板</a>
        <a id="heroWikiLink" class="action" href="#">LLM Wiki</a>
      </div>
    </div>
    <aside class="focus-panel" id="focusPanel">
      <div class="panel-kicker">今日焦点</div>
      <a class="focus-title" id="focusTitle" href="#">读取中</a>
      <div class="small" id="focusMeta"></div>
      <p class="focus-tip" id="focusTip"></p>
      <a class="action primary" id="focusAction" href="#">打开错题</a>
    </aside>
  </section>

  <div class="metrics" id="metrics"></div>

  <section class="panel route-panel">
    <div class="section-head">
      <h2>今日学习闭环</h2>
      <a id="routeLink" class="action" href="#">打开路线</a>
    </div>
    <div class="table-wrap route-table">
      <table>
        <thead><tr><th>错题</th><th>优先状态</th><th>建议</th><th>关联笔记</th><th>二轮题</th><th>五年题</th></tr></thead>
        <tbody id="routeRows"></tbody>
      </table>
    </div>
    <div id="routeEmpty" class="empty" hidden>当前没有待执行路线。</div>
  </section>

  <div class="grid-2">
    <section class="panel">
      <div class="section-head">
        <h2>题库进度</h2>
        <div class="controls">
          <div class="segmented">
            <button type="button" class="active" data-bank="question">二轮</button>
            <button type="button" data-bank="classic">五年经典</button>
          </div>
          <input class="search" id="moduleSearch" placeholder="筛选章节">
        </div>
      </div>
      <div class="module-grid" id="moduleGrid"></div>
    </section>

    <section class="panel">
      <div class="section-head">
        <h2>系统健康</h2>
        <a class="action" id="healthLink" href="#">体检</a>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>项目</th><th>状态</th><th>说明</th></tr></thead>
          <tbody id="healthRows"></tbody>
        </table>
      </div>
    </section>
  </div>

  <div class="grid-2">
    <section class="panel">
      <div class="section-head">
        <h2>高频信号</h2>
        <a class="action" id="contentLink" href="#">内容总览</a>
      </div>
      <div class="chips" id="signalChips"></div>
    </section>

    <section class="panel">
      <div class="section-head">
        <h2>本次维护</h2>
        <a class="action" id="overviewLink" href="#">总控台</a>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>任务</th><th>状态</th><th>耗时</th></tr></thead>
          <tbody id="taskRows"></tbody>
        </table>
      </div>
    </section>
  </div>
</main>

<script type="application/json" id="data">{payload}</script>
<script>
const data = JSON.parse(document.getElementById("data").textContent);
const links = data.links || {{}};
let activeBank = "question";

function h(value) {{
  return String(value ?? "").replace(/[&<>"']/g, ch => ({{
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  }}[ch]));
}}
function href(value) {{
  const raw = String(value || "");
  if (!raw) return "";
  if (/^(https?:)?\\/\\//.test(raw) || raw.startsWith("mailto:")) return raw;
  const hashIndex = raw.indexOf("#");
  const path = hashIndex >= 0 ? raw.slice(0, hashIndex) : raw;
  const hash = hashIndex >= 0 ? raw.slice(hashIndex) : "";
  if (/\\.md(?:$|[?#])/.test(path)) {{
    return `reader.html?file=${{encodeURIComponent(path)}}${{hash}}`;
  }}
  return encodeURI(raw).replace(/#/g, "%23");
}}
function link(target, label, className = "") {{
  if (!target || !label) return h(label || "暂无");
  const cls = className ? ` class="${{h(className)}}"` : "";
  return `<a${{cls}} href="${{h(href(target))}}">${{h(label)}}</a>`;
}}
function num(value) {{ return Number(value || 0); }}
function pct(done, total) {{ return total ? Math.round(done / total * 100) : 0; }}
function statusPill(status) {{
  const kind = status === "ok" || status === "正常" ? "ok" : status === "failed" || status === "异常" ? "bad" : "warn";
  return `<span class="pill ${{kind}}">${{h(status || "未运行")}}</span>`;
}}
function progressBar(value) {{
  const safe = Math.max(0, Math.min(100, num(value)));
  return `<div class="progress"><div class="fill" style="width:${{safe}}%"></div></div>`;
}}

document.getElementById("generatedAt").textContent = data.generatedAt || "";
document.getElementById("routeLink").href = href(links.wrongRoute);
document.getElementById("heroRouteLink").href = href(links.wrongRoute);
document.getElementById("heroDashboardLink").href = href(links.wrongDashboard);
document.getElementById("heroWikiLink").href = href(links.llmWiki);
document.getElementById("healthLink").href = href(links.wrongHealth);
document.getElementById("contentLink").href = href(links.content);
document.getElementById("overviewLink").href = href(links.overview);

document.getElementById("actions").innerHTML = [
  ["今日路线", links.wrongRoute, "primary"],
  ["错题看板", links.wrongDashboard, ""],
  ["二轮看板", links.questionDashboard, ""],
  ["五年看板", links.classicDashboard, ""],
  ["笔记转化", links.aiConversion, ""],
  ["LLM Wiki", links.llmWiki, ""],
  ["Markdown", links.workbenchMd, ""]
].map(([label, target, kind]) => link(target, label, `action ${{kind}}`.trim())).join("");

const wrong = data.wrong || {{}};
const ai = data.ai || {{}};
const question = data.question || {{}};
const classic = data.classic || {{}};
const content = data.content || {{}};
const llm = data.llm || {{}};
const failedTasks = (data.results || []).filter(item => item.status && item.status !== "ok");

function renderFocus() {{
  const item = (data.learningPath || [])[0];
  const title = document.getElementById("focusTitle");
  const meta = document.getElementById("focusMeta");
  const tip = document.getElementById("focusTip");
  const action = document.getElementById("focusAction");
  if (!item) {{
    title.textContent = "当前没有待执行路线";
    title.removeAttribute("href");
    meta.textContent = "错题队列暂时清空";
    tip.textContent = "可以查看系统健康或继续整理标准笔记。";
    action.href = href(links.wrongRoute);
    action.textContent = "查看路线";
    return;
  }}
  title.textContent = item.title || "未命名错题";
  title.href = href(item.file || links.wrongRoute);
  meta.textContent = [item.priority, item.status, item.mastery ? `掌握度 ${{item.mastery}}` : ""].filter(Boolean).join(" / ");
  tip.textContent = item.anti_mistake_tip || item.review_reason || item.timebox || "";
  action.href = href(item.file || links.wrongRoute);
  action.textContent = "打开错题";
}}

document.getElementById("metrics").innerHTML = [
  ["今日队列", wrong.due, `${{num(wrong.wrongAgain)}} 仍错 / ${{num(wrong.overdue)}} 逾期`, "focus"],
  ["二轮已处理", `${{num(question.handled)}} / ${{num(question.total)}}`, `${{num(question.handled_pct)}}%`, ""],
  ["五年待核对", num(classic.review), `正式完成 ${{num(classic.done)}}`, num(classic.review) ? "warn" : ""],
  ["标准笔记", ai.total, `待整理 ${{num(ai.inbox && ai.inbox.pending)}}`, ""],
  ["知识主题", num(llm.topicTotal), `${{num(llm.issueTotal)}} 个 Wiki 检查项`, num(llm.issueTotal) ? "warn" : ""],
  ["系统问题", num(wrong.issueCount) + num(ai.issueCount) + num(llm.issueTotal) + failedTasks.length, failedTasks.length ? "维护异常" : "体检通过", failedTasks.length ? "warn" : ""],
  ["今日路线", (data.learningPath || []).length, "错题 -> 笔记 -> 迁移题", ""]
].map(([label, value, detail, kind]) => `<div class="card ${{h(kind)}}"><b>${{h(label)}}</b><div class="value">${{h(value)}}</div><div class="small">${{h(detail)}}</div></div>`).join("");

function renderRoute() {{
  const rows = (data.learningPath || []).slice(0, 12);
  const body = document.getElementById("routeRows");
  document.getElementById("routeEmpty").hidden = rows.length > 0;
  body.innerHTML = rows.map(item => {{
    const aiNote = item.ai_note || {{}};
    const twoRound = item.two_round || {{}};
    const classicProblem = item.classic || {{}};
    return `<tr>
      <td data-label="错题">${{link(item.file, item.title)}}<div class="small">${{h(item.review_reason || "")}}</div></td>
      <td data-label="优先状态"><span class="pill ${{item.priority === "P1" ? "bad" : "warn"}}">${{h(item.priority || "")}} / ${{h(item.status || "")}}</span><div class="small">掌握度 ${{h(item.mastery || "")}}</div></td>
      <td data-label="建议">${{h(item.timebox || "")}}<div class="small">${{h(item.anti_mistake_tip || "")}}</div></td>
      <td data-label="关联笔记">${{link(aiNote.file, aiNote.title || item.ai_note_action || "建议补笔记")}}</td>
      <td data-label="二轮题">${{link(twoRound.note_path, twoRound.problem_id || "暂无")}}<div class="small">${{h(twoRound.reason || "")}}</div></td>
      <td data-label="五年题">${{link(classicProblem.note_path, classicProblem.problem_id || "暂无")}}<div class="small">${{h(classicProblem.reason || "")}}</div></td>
    </tr>`;
  }}).join("");
}}

function renderModules() {{
  const bank = activeBank === "classic" ? classic : question;
  const basePath = activeBank === "classic"
    ? "高考数学五年经典/07_章节题目合集_Obsidian公式版/"
    : "Obsidian题库/07_章节题目合集_Obsidian公式版/";
  const fallback = activeBank === "classic" ? links.classicDashboard : links.questionDashboard;
  const keyword = document.getElementById("moduleSearch").value.trim().toLowerCase();
  const rows = (bank.modules || []).filter(item => !keyword || String(item.name || "").toLowerCase().includes(keyword));
  document.getElementById("moduleGrid").innerHTML = rows.map(item => {{
    const handledPct = num(item.handled_pct ?? item.pct);
    const target = item.chapter_file ? `${{basePath}}${{item.chapter_file}}` : fallback;
    return `<a class="module" href="${{h(href(target))}}">
      <div class="module-title" title="${{h(item.name)}}">${{h(item.name)}}</div>
      <div class="small">完成 ${{num(item.done)}}，待核对 ${{num(item.review)}}，已处理 ${{num(item.handled)}} / ${{num(item.total)}}</div>
      ${{progressBar(handledPct)}}
      <div class="module-row"><span class="pill ${{handledPct >= 100 ? "ok" : handledPct >= 60 ? "warn" : ""}}">${{handledPct}}%</span><span class="small">打开章节</span></div>
    </a>`;
  }}).join("") || `<div class="empty">没有匹配章节。</div>`;
}}

function renderHealth() {{
  const rows = [
    ["维护任务", failedTasks.length ? "异常" : "正常", failedTasks.map(item => item.name).join("；") || "全部通过"],
    ["错题库体检", num(wrong.issueCount) ? "异常" : "正常", `${{num(wrong.issueCount)}} 个问题`],
    ["笔记体检", num(ai.issueCount) ? "异常" : "正常", `${{num(ai.issueCount)}} 个问题`],
    ["LLM Wiki 体检", num(llm.issueTotal) ? "异常" : "正常", `${{num(llm.issueTotal)}} 个检查项`],
    ["二轮题库缺失笔记", num(question.missing_note_count) ? "异常" : "正常", `${{num(question.missing_note_count)}} 个缺失`],
    ["五年经典缺失笔记", num(classic.missing_note_count) ? "异常" : "正常", `${{num(classic.missing_note_count)}} 个缺失`]
  ];
  document.getElementById("healthRows").innerHTML = rows.map(([name, status, detail]) =>
    `<tr><td>${{h(name)}}</td><td>${{statusPill(status)}}</td><td>${{h(detail)}}</td></tr>`
  ).join("");
}}

function renderSignals() {{
  const wrongSignals = Object.entries((content.wrong && content.wrong.reasons) || {{}}).map(([name, count]) => ["错因", name, count]);
  const methodSignals = Object.entries((content.questionBank && content.questionBank.methods) || {{}}).slice(0, 8).map(([name, count]) => ["二轮方法", name, count]);
  const classicSignals = Object.entries((content.classicBank && content.classicBank.methods) || {{}}).slice(0, 6).map(([name, count]) => ["五年方法", name, count]);
  const signals = [...wrongSignals, ...methodSignals, ...classicSignals];
  document.getElementById("signalChips").innerHTML = signals.map(([kind, name, count]) =>
    `<span class="chip"><b>${{h(kind)}}</b> ${{h(name)}} <span class="small">${{h(count)}}</span></span>`
  ).join("") || `<div class="empty">暂无内容信号。</div>`;
}}

function renderTasks() {{
  const rows = data.results || [];
  document.getElementById("taskRows").innerHTML = rows.map(item =>
    `<tr><td>${{h(item.name)}}</td><td>${{statusPill(item.status)}}</td><td>${{h(item.seconds || 0)}} 秒<div class="small">${{h(item.message || "")}}</div></td></tr>`
  ).join("") || `<tr><td colspan="3" class="muted">本次只重建了工作台，没有运行维护任务。</td></tr>`;
}}

document.querySelectorAll("[data-bank]").forEach(button => {{
  button.addEventListener("click", () => {{
    activeBank = button.dataset.bank;
    document.querySelectorAll("[data-bank]").forEach(item => item.classList.toggle("active", item === button));
    renderModules();
  }});
}});
document.getElementById("moduleSearch").addEventListener("input", renderModules);

renderFocus();
renderRoute();
renderModules();
renderHealth();
renderSignals();
renderTasks();
</script>
</body>
</html>
"""


def collect_data() -> dict[str, Any]:
    return {
        "question_bank": load_json(ROOT / "Obsidian题库" / "04_原始资料" / "progress.json"),
        "classic_bank": load_json(ROOT / "高考数学五年经典" / "04_原始资料" / "progress.json"),
        "wrong_bank": load_json(ROOT / "个人错题库" / "00_控制台" / "wrong_bank_data.json"),
        "ai_notes": load_json(ROOT / "Obsidian题库" / "08_AI笔记管理" / "notes_index.json"),
        "content": load_json(ROOT / "内容优化总览.json"),
        "llm_wiki": load_json(ROOT / "LLM知识库" / "wiki_index.json"),
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh and summarize all local study systems.")
    parser.add_argument("--skip-refresh", action="store_true", help="only rebuild the root overview from existing json")
    parser.add_argument("--jobs", type=int, default=4, help="parallel maintenance jobs; use 1 for serial debugging")
    parser.add_argument(
        "--only",
        choices=["all", "question_bank", "classic_bank", "wrong_bank", "ai_notes", "content_optimizer", "llm_wiki"],
        default="all",
        help="refresh only one system before rebuilding the overview",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.only == "all":
        selected = TASKS
        post_selected = POST_TASKS
    elif args.only == "llm_wiki":
        selected = []
        post_selected = POST_TASKS
    else:
        selected = [task for task in TASKS if task["key"] == args.only]
        post_selected = []
    if args.skip_refresh:
        results = []
    else:
        results = run_tasks(selected, args.jobs)
        if post_selected:
            results.extend(run_tasks(post_selected, 1))
    data = collect_data()
    write_text(OVERVIEW_MD, render_overview(results, data))
    write_text(WORKBENCH_MD, render_workbench(results, data))
    write_text(WORKBENCH_HTML, render_workbench_html(results, data))
    write_text(
        OVERVIEW_JSON,
        json.dumps(
            {
                "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
                "results": results,
                "data": data,
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    print(f"系统总控台已刷新：{OVERVIEW_MD}")
    return 0 if all(item.get("status") == "ok" for item in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
