# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
KB_ROOT = ROOT / "LLM知识库"
WIKI_ROOT = KB_ROOT / "wiki"
TOPIC_DIR = WIKI_ROOT / "topics"
METHOD_DIR = WIKI_ROOT / "methods"
SOURCE_DIR = WIKI_ROOT / "sources"
DATA_JSON = KB_ROOT / "wiki_index.json"
LOG_MD = WIKI_ROOT / "log.md"

QUESTION_ROOT = ROOT / "Obsidian题库"
CLASSIC_ROOT = ROOT / "高考数学五年经典"
WRONG_ROOT = ROOT / "个人错题库"
AI_ROOT = QUESTION_ROOT / "08_AI笔记管理"
AI_NOTE_DIR = AI_ROOT / "02_标准笔记"


METHOD_PATTERNS = {
    "基本不等式": ["基本不等式", "均值不等式"],
    "换元": ["换元", "代换", "设a=", "设b=", "令a=", "令b="],
    "整体结构识别": ["整体结构", "结构识别", "对称结构", "配凑"],
    "代入消元": ["代入", "消元"],
    "分类讨论": ["分类讨论", "分情况", "讨论"],
    "构造函数": ["构造函数", "设函数", "导数"],
    "导数单调性": ["导数", "f'(", "单调区间"],
    "数形结合": ["数形结合", "图象", "图像"],
    "特征方程": ["特征方程", "特征根", "二阶递推", "a_{n+2}"],
    "递推验证": ["递推", "通项", "前几项", "等差", "等比"],
    "空间向量": ["空间向量", "法向量", "二面角", "线面角"],
    "圆锥曲线定义": ["椭圆", "双曲线", "抛物线", "焦点", "准线"],
    "概率递推": ["概率", "递推", "随机过程", "条件概率"],
    "选项排除": ["选项", "多选", "判断", "正确的是"],
}


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


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return {}, text
    data: dict[str, Any] = {}
    lines = match.group(1).splitlines()
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
    return data, text[match.end() :]


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def as_int(value: Any, default: int = 0) -> int:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def parse_date(value: Any) -> dt.date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return dt.date.fromisoformat(text[:10])
    except ValueError:
        return None


def normalize(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\\[a-zA-Z]+", "", value)
    value = re.sub(r"[{}\[\]()（）【】\s，。；：、,.!?:;`'\"<>|/\\-]", "", value)
    return value


def slug(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*\r\n\t]', "-", str(value)).strip()
    value = re.sub(r"\s+", "", value)
    value = value.strip(". ")
    return value[:90] or "untitled"


def rel_link(base_file: Path, target: str | Path | None, label: Any, fallback: str = "暂无") -> str:
    text = str(label or "").strip()
    raw = str(target or "").strip()
    if not raw or not text:
        return fallback
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    try:
        rel = os.path.relpath(path, start=base_file.parent).replace("\\", "/")
        return f"[{text}]({rel})"
    except ValueError:
        return text


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


def searchable_problem_text(problem: dict[str, Any]) -> str:
    fields = [
        problem.get("problem_id", ""),
        problem.get("lesson_id", ""),
        problem.get("lesson_title", ""),
        problem.get("module", ""),
        problem.get("topic", ""),
        problem.get("section", ""),
        problem.get("kind", ""),
        problem.get("content", ""),
    ]
    return " ".join(str(item) for item in fields)


def detect_methods(text: str) -> list[str]:
    normalized = normalize(text)
    hits = []
    for method, patterns in METHOD_PATTERNS.items():
        if any(normalize(pattern) and normalize(pattern) in normalized for pattern in patterns):
            hits.append(method)
    return hits


def load_bank(bank_id: str, bank_label: str, root: Path) -> dict[str, Any]:
    manifest_path = root / "04_原始资料" / "problems.json"
    progress_path = root / "04_原始资料" / "progress.json"
    manifest = load_json(manifest_path)
    progress = load_json(progress_path)
    problems = []
    for raw in manifest.get("problems", []):
        problem = dict(raw)
        problem["_bank_id"] = bank_id
        problem["_bank_label"] = bank_label
        problem["_root"] = str(root)
        problem["_file"] = ""
        if problem.get("note_path"):
            problem["_file"] = (root / str(problem["note_path"])).relative_to(ROOT).as_posix()
        text = searchable_problem_text(problem)
        problem["_search"] = normalize(text)
        problem["_methods"] = detect_methods(text)
        problems.append(problem)
    return {
        "id": bank_id,
        "label": bank_label,
        "root": root.relative_to(ROOT).as_posix(),
        "manifest": manifest_path.relative_to(ROOT).as_posix(),
        "progress": progress_path.relative_to(ROOT).as_posix(),
        "manifest_loaded": bool(manifest) and "_load_error" not in manifest,
        "progress_loaded": bool(progress) and "_load_error" not in progress,
        "lessons": manifest.get("lessons", []),
        "problems": problems,
        "progress_data": progress,
    }


def load_wrong_notes() -> list[dict[str, Any]]:
    notes = []
    wrong_dir = WRONG_ROOT / "01_错题"
    if not wrong_dir.exists():
        return notes
    for path in sorted(wrong_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if fm.get("type") != "wrong_problem":
            continue
        title_match = re.search(r"^#\s+(.+)$", body, re.M)
        fm["_title"] = title_match.group(1).strip() if title_match else path.stem
        fm["_file"] = path.relative_to(ROOT).as_posix()
        fm["_body"] = body
        fm["_search"] = normalize(" ".join([body, str(fm.get("anti_mistake_tip", "")), str(fm.get("lesson_title", ""))]))
        notes.append(fm)
    return notes


def load_ai_notes() -> list[dict[str, Any]]:
    notes = []
    if not AI_NOTE_DIR.exists():
        return notes
    for path in sorted(AI_NOTE_DIR.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if fm.get("type") != "standard_note":
            continue
        title_match = re.search(r"^#\s+(.+)$", body, re.M)
        fm["_title"] = str(fm.get("title") or (title_match.group(1).strip() if title_match else path.stem))
        fm["_file"] = path.relative_to(ROOT).as_posix()
        fm["_body"] = body
        fm["_search"] = normalize(
            " ".join(
                [
                    fm.get("_title", ""),
                    fm.get("module", ""),
                    fm.get("topic", ""),
                    fm.get("lesson_id", ""),
                    " ".join(as_list(fm.get("knowledge_points"))),
                    " ".join(as_list(fm.get("methods"))),
                    " ".join(as_list(fm.get("related_problem_ids"))),
                    body,
                ]
            )
        )
        notes.append(fm)
    return notes


def topic_identity(module_id: Any, lesson_id: Any, module: Any, topic: Any) -> tuple[str, str]:
    module_id = str(module_id or "").strip()
    lesson_id = str(lesson_id or "").strip()
    module = str(module or "未分类").strip()
    topic = str(topic or module or "未分类").strip()
    label = f"{module} / {lesson_id} {topic}".strip()
    return slug(f"{module_id}_{lesson_id}_{module}_{topic}"), label


def empty_topic(topic_id: str, label: str, module_id: Any, lesson_id: Any, module: Any, topic: Any) -> dict[str, Any]:
    return {
        "id": topic_id,
        "label": label,
        "module_id": str(module_id or ""),
        "lesson_id": str(lesson_id or ""),
        "module": str(module or "未分类"),
        "topic": str(topic or module or "未分类"),
        "page": f"LLM知识库/wiki/topics/{topic_id}.md",
        "problem_counts": Counter(),
        "status_counts": Counter(),
        "methods": Counter(),
        "knowledge": Counter(),
        "wrong_reasons": Counter(),
        "wrong_items": [],
        "ai_notes": [],
        "samples": [],
    }


def get_topic(topics: dict[str, dict[str, Any]], module_id: Any, lesson_id: Any, module: Any, topic: Any) -> dict[str, Any]:
    topic_id, label = topic_identity(module_id, lesson_id, module, topic)
    if topic_id not in topics:
        topics[topic_id] = empty_topic(topic_id, label, module_id, lesson_id, module, topic)
    return topics[topic_id]


def add_sample(topic: dict[str, Any], item: dict[str, Any]) -> None:
    if len(topic["samples"]) >= 10:
        return
    topic["samples"].append(item)


def build_topics(banks: list[dict[str, Any]], wrong_notes: list[dict[str, Any]], ai_notes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    topics: dict[str, dict[str, Any]] = {}
    for bank in banks:
        for problem in bank["problems"]:
            topic = get_topic(
                topics,
                problem.get("module_id"),
                problem.get("lesson_id"),
                problem.get("module"),
                problem.get("topic"),
            )
            topic["problem_counts"][bank["id"]] += 1
            topic["status_counts"][str(problem.get("status") or "todo")] += 1
            topic["methods"].update(problem.get("_methods") or [])
            if len(topic["samples"]) < 6 or str(problem.get("status") or "") in {"todo", "review"}:
                add_sample(
                    topic,
                    {
                        "type": "problem",
                        "bank": bank["label"],
                        "problem_id": problem.get("problem_id", ""),
                        "file": problem.get("_file", ""),
                        "section": problem.get("section", ""),
                        "status": problem.get("status", ""),
                    },
                )
    for note in wrong_notes:
        topic = get_topic(topics, note.get("module_id"), note.get("lesson_id"), note.get("module"), note.get("topic"))
        topic["wrong_items"].append(
            {
                "wrong_id": note.get("wrong_id", ""),
                "title": note.get("_title", ""),
                "file": note.get("_file", ""),
                "priority": note.get("priority", ""),
                "status": note.get("status", ""),
                "mastery": note.get("mastery", ""),
                "methods": as_list(note.get("methods")),
                "anti_mistake_tip": note.get("anti_mistake_tip", ""),
            }
        )
        topic["wrong_reasons"].update(as_list(note.get("wrong_reason")) or ["待补充"])
        topic["knowledge"].update(as_list(note.get("knowledge_points")))
        topic["methods"].update(as_list(note.get("methods")))
    for note in ai_notes:
        topic = get_topic(topics, note.get("module_id"), note.get("lesson_id"), note.get("module"), note.get("topic"))
        topic["ai_notes"].append(
            {
                "note_id": note.get("note_id", ""),
                "title": note.get("_title", ""),
                "file": note.get("_file", ""),
                "kind": note.get("note_kind", ""),
                "status": note.get("status", ""),
                "confidence": note.get("classification_confidence", ""),
                "methods": as_list(note.get("methods")),
            }
        )
        topic["knowledge"].update(as_list(note.get("knowledge_points")))
        topic["methods"].update(as_list(note.get("methods")))
    return topics


def topic_score(topic: dict[str, Any]) -> int:
    wrong_weight = len(topic["wrong_items"]) * 100
    ai_weight = len(topic["ai_notes"]) * 20
    review_weight = topic["status_counts"].get("review", 0) * 2 + topic["status_counts"].get("todo", 0)
    problem_weight = sum(topic["problem_counts"].values())
    return wrong_weight + ai_weight + review_weight + problem_weight


def build_methods(topics: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    methods: dict[str, dict[str, Any]] = {}
    for topic in topics.values():
        for method, count in topic["methods"].items():
            node = methods.setdefault(
                method,
                {
                    "name": method,
                    "page": f"LLM知识库/wiki/methods/{slug(method)}.md",
                    "count": 0,
                    "wrong_count": 0,
                    "ai_note_count": 0,
                    "topics": [],
                    "samples": [],
                },
            )
            node["count"] += count
            node["wrong_count"] += sum(1 for item in topic["wrong_items"] if method in as_list(item.get("methods")))
            node["ai_note_count"] += sum(1 for item in topic["ai_notes"] if method in as_list(item.get("methods")))
            node["topics"].append({"label": topic["label"], "page": topic["page"], "score": topic_score(topic)})
            for sample in topic["samples"][:2]:
                if len(node["samples"]) < 8:
                    node["samples"].append(sample)
    for node in methods.values():
        node["topics"] = sorted(node["topics"], key=lambda item: (-int(item["score"]), item["label"]))[:12]
    return methods


def content_learning_path() -> list[dict[str, Any]]:
    content = load_json(ROOT / "内容优化总览.json")
    path = content.get("learningPath", [])
    return path if isinstance(path, list) else []


def build_lint(
    banks: list[dict[str, Any]],
    wrong_notes: list[dict[str, Any]],
    ai_notes: list[dict[str, Any]],
    topics: dict[str, dict[str, Any]],
) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    today = dt.date.today()
    for bank in banks:
        if not bank["manifest_loaded"]:
            issues.append({"level": "P1", "area": bank["label"], "item": bank["manifest"], "message": "题库 manifest 缺失或无法读取"})
        if not bank["progress_loaded"]:
            issues.append({"level": "P2", "area": bank["label"], "item": bank["progress"], "message": "进度数据缺失或无法读取"})
        progress = bank.get("progress_data") or {}
        if as_int(progress.get("missing_note_count"), 0):
            issues.append({"level": "P1", "area": bank["label"], "item": "missing_note_count", "message": f"缺失题目笔记 {progress.get('missing_note_count')} 个"})
        if as_int(progress.get("review"), 0):
            issues.append({"level": "P3", "area": bank["label"], "item": "review", "message": f"仍有 {progress.get('review')} 个 review 状态题目需要人工核对"})

    ai_by_problem: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    ai_by_lesson: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for note in ai_notes:
        for problem_id in as_list(note.get("related_problem_ids")):
            ai_by_problem[problem_id].append(note)
        if note.get("lesson_id"):
            ai_by_lesson[str(note.get("lesson_id"))].append(note)
        if str(note.get("status") or "") != "ready":
            issues.append({"level": "P2", "area": "AI笔记", "item": str(note.get("_file") or ""), "message": "标准笔记不是 ready 状态"})
        if str(note.get("classification_confidence") or "") == "low":
            issues.append({"level": "P2", "area": "AI笔记", "item": str(note.get("_file") or ""), "message": "分类置信度低，需要人工核对"})

    for note in wrong_notes:
        wrong_id = str(note.get("wrong_id") or "")
        source_problem_id = str(note.get("source_problem_id") or "")
        lesson_id = str(note.get("lesson_id") or "")
        if not note.get("anti_mistake_tip"):
            issues.append({"level": "P1", "area": "错题库", "item": wrong_id, "message": "缺少防错口令，无法形成复习触发器"})
        due = parse_date(note.get("next_review"))
        if due and due < today and str(note.get("status") or "") != "已掌握":
            issues.append({"level": "P3", "area": "错题库", "item": wrong_id, "message": f"复习已逾期 {(today - due).days} 天"})
        if source_problem_id and not ai_by_problem.get(source_problem_id) and not ai_by_lesson.get(lesson_id):
            issues.append({"level": "P2", "area": "错题库", "item": wrong_id, "message": "没有同题或同讲次 AI 标准笔记"})

    for topic in topics.values():
        if topic["wrong_items"] and not topic["ai_notes"]:
            issues.append({"level": "P2", "area": "知识主题", "item": topic["label"], "message": "有错题但没有标准笔记承接"})
    return issues


def serializable_counter(counter: Counter) -> dict[str, int]:
    return {str(key): int(value) for key, value in counter.items()}


def summarize_topic(topic: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": topic["id"],
        "label": topic["label"],
        "module_id": topic["module_id"],
        "lesson_id": topic["lesson_id"],
        "module": topic["module"],
        "topic": topic["topic"],
        "page": topic["page"],
        "score": topic_score(topic),
        "problemCounts": serializable_counter(topic["problem_counts"]),
        "statusCounts": serializable_counter(topic["status_counts"]),
        "methodCounts": serializable_counter(topic["methods"]),
        "knowledgeCounts": serializable_counter(topic["knowledge"]),
        "wrongReasons": serializable_counter(topic["wrong_reasons"]),
        "wrongCount": len(topic["wrong_items"]),
        "aiNoteCount": len(topic["ai_notes"]),
        "samples": topic["samples"],
    }


def render_readme(summary: dict[str, Any]) -> str:
    return f"""# LLM 知识库

这是在现有题库、错题库和 AI 笔记之上新增的持久 wiki 层。它借鉴 Karpathy 的 LLM-Wiki 思路：原始资料保持可追溯，LLM 负责把材料持续编译成更容易检索、复习和迁移的知识页。

## 入口

- [Wiki 首页](wiki/00_Index.md)
- [系统概览](wiki/01_Overview.md)
- [今日学习闭环](wiki/02_Learning_Loop.md)
- [资料源注册表](wiki/03_Source_Registry.md)
- [健康检查](wiki/04_Health_Check.md)
- [待编译队列](wiki/05_Compile_Queue.md)
- [操作规约](SCHEMA.md)

## 当前快照

- 题库题目：{summary["problemTotal"]}
- 错题：{summary["wrongTotal"]}
- AI 标准笔记：{summary["aiNoteTotal"]}
- 主题页：{summary["topicTotal"]}
- 方法页：{summary["methodTotal"]}
- 检查项：{summary["issueTotal"]}

## 维护

```powershell
.\\tools\\maintain_study_systems.ps1
```

或只重建这一层：

```powershell
python .\\tools\\llm_wiki_maintain.py refresh
```
"""


def render_schema() -> str:
    return """# LLM 知识库操作规约

## 核心原则

1. 原始资料不直接改写：题库、PDF、错题原文和 AI 对话归档是 source-of-truth。
2. Wiki 是编译层：主题页、方法页、学习闭环和健康检查可以反复生成。
3. 每个结论都要能追回来源：优先链接到错题、标准笔记、题目页或控制台数据。
4. LLM 的价值不是堆摘要，而是维护结构：分类、命名、链接、待办、薄弱点和迁移路线。

## 目录角色

| 目录 | 角色 | 写入策略 |
| --- | --- | --- |
| `Obsidian题库` | 二轮题库 source-of-truth | 只通过原维护脚本和导入脚本更新 |
| `高考数学五年经典` | 五年经典题库 source-of-truth | 只通过原维护脚本和解答导入脚本更新 |
| `个人错题库` | 个人错题和复习状态 source-of-truth | 新错题按模板进入，复习后更新状态字段 |
| `Obsidian题库/08_AI笔记管理/02_标准笔记` | 标准方法卡和知识卡 | 由 AI 对话/错题复盘整理后写入 |
| `LLM知识库/wiki` | LLM 编译出的持久 wiki | 可由 `llm_wiki_maintain.py` 重建 |

## LLM 工作流

1. 先读 `LLM知识库/wiki/00_Index.md`，再进入相关主题页或方法页。
2. 回答题目或复习问题时，至少链接一个源文件：错题、题目或标准笔记。
3. 发现重复错因时，优先补一张标准笔记，再让维护脚本重新编译。
4. 发现分类不确定时，把置信度写低，并在健康检查中暴露给人工确认。
5. 新材料先进入导入入口，不把聊天记录直接混进标准笔记区。

## 推荐字段

错题页应至少维护：`wrong_id`、`source_problem_id`、`lesson_id`、`module`、`topic`、`priority`、`status`、`mastery`、`wrong_reason`、`knowledge_points`、`methods`、`anti_mistake_tip`、`last_review`、`next_review`。

标准笔记应至少维护：`note_id`、`note_kind`、`status`、`title`、`lesson_id`、`module`、`topic`、`classification_confidence`、`related_problem_ids`、`knowledge_points`、`methods`、`quality_flags`。

## 复习闭环定义

错题重做 -> 标准笔记复盘 -> 二轮同类题 -> 五年经典迁移题 -> 更新错题状态。
"""


def render_index(topics: list[dict[str, Any]], methods: dict[str, dict[str, Any]], summary: dict[str, Any]) -> str:
    topic_rows = [
        [
            rel_link(WIKI_ROOT / "00_Index.md", topic["page"], topic["label"]),
            topic["wrongCount"],
            topic["aiNoteCount"],
            sum(topic["problemCounts"].values()),
            topic["score"],
        ]
        for topic in topics[:30]
    ]
    method_rows = [
        [
            rel_link(WIKI_ROOT / "00_Index.md", node["page"], name),
            node["count"],
            len(node["topics"]),
        ]
        for name, node in sorted(methods.items(), key=lambda item: (-int(item[1]["count"]), item[0]))[:30]
    ]
    return f"""# LLM Wiki Index

## 快速入口

- [系统概览](01_Overview.md)
- [今日学习闭环](02_Learning_Loop.md)
- [资料源注册表](03_Source_Registry.md)
- [健康检查](04_Health_Check.md)
- [待编译队列](05_Compile_Queue.md)
- [运行日志](log.md)

## 当前规模

| 项目 | 数量 |
| --- | ---: |
| 题库题目 | {summary["problemTotal"]} |
| 错题 | {summary["wrongTotal"]} |
| AI 标准笔记 | {summary["aiNoteTotal"]} |
| 主题页 | {summary["topicTotal"]} |
| 方法页 | {summary["methodTotal"]} |
| 健康检查项 | {summary["issueTotal"]} |

## 优先主题

{markdown_table(["主题", "错题", "AI笔记", "题量", "优先分"], topic_rows)}
## 方法索引

{markdown_table(["方法", "信号数", "关联主题"], method_rows)}
"""


def render_overview(banks: list[dict[str, Any]], wrong_notes: list[dict[str, Any]], ai_notes: list[dict[str, Any]], topics: list[dict[str, Any]], issues: list[dict[str, str]]) -> str:
    source_rows = []
    for bank in banks:
        progress = bank.get("progress_data") or {}
        source_rows.append(
            [
                bank["label"],
                len(bank["problems"]),
                f"{progress.get('handled', progress.get('done', 0))} / {progress.get('total', len(bank['problems']))}",
                rel_link(WIKI_ROOT / "01_Overview.md", bank["manifest"], "manifest"),
            ]
        )
    weak_rows = [
        [
            rel_link(WIKI_ROOT / "01_Overview.md", topic["page"], topic["label"]),
            topic["wrongCount"],
            "、".join(list(topic["wrongReasons"].keys())[:3]),
            "、".join(list(topic["methodCounts"].keys())[:4]),
        ]
        for topic in topics
        if topic["wrongCount"]
    ][:12]
    issue_rows = [[item["level"], item["area"], item["item"], item["message"]] for item in issues[:20]]
    return f"""# 系统概览

本页是 LLM 编译层的总览。原始题库和错题状态仍以各自目录为准，这里负责把它们合成可检索的知识地图。

## 资料源

{markdown_table(["来源", "题/笔记数", "进度", "数据入口"], source_rows + [["个人错题库", len(wrong_notes), "复习状态见错题页", rel_link(WIKI_ROOT / "01_Overview.md", WRONG_ROOT / "00_控制台" / "wrong_bank_data.json", "wrong_bank_data")], ["AI 标准笔记", len(ai_notes), "ready/review 见索引", rel_link(WIKI_ROOT / "01_Overview.md", AI_ROOT / "notes_index.json", "notes_index")]])}
## 薄弱主题

{markdown_table(["主题", "错题数", "高频错因", "方法信号"], weak_rows)}
## 健康检查摘要

{markdown_table(["级别", "区域", "对象", "说明"], issue_rows)}
"""


def render_learning_loop(path: list[dict[str, Any]]) -> str:
    rows = []
    for item in path:
        ai_note = item.get("ai_note") or {}
        two_round = item.get("two_round") or {}
        classic = item.get("classic") or {}
        rows.append(
            [
                item.get("order", ""),
                rel_link(WIKI_ROOT / "02_Learning_Loop.md", item.get("file"), item.get("title")),
                f"{item.get('priority', '')} / {item.get('status', '')} / 掌握度{item.get('mastery', '')}",
                item.get("review_reason", ""),
                item.get("anti_mistake_tip", ""),
                rel_link(WIKI_ROOT / "02_Learning_Loop.md", ai_note.get("file"), ai_note.get("title"), item.get("ai_note_action", "建议补笔记")),
                rel_link(WIKI_ROOT / "02_Learning_Loop.md", two_round.get("note_path"), two_round.get("problem_id")),
                rel_link(WIKI_ROOT / "02_Learning_Loop.md", classic.get("note_path"), classic.get("problem_id")),
            ]
        )
    return f"""# 今日学习闭环

执行顺序固定为：原错题重做 -> 标准笔记复盘 -> 二轮同类题 -> 五年经典迁移题 -> 更新错题状态。

{markdown_table(["顺序", "错题", "优先状态", "为什么今天做", "防错口令", "AI笔记", "二轮题", "五年题"], rows)}
"""


def render_source_registry(banks: list[dict[str, Any]]) -> str:
    rows = []
    for bank in banks:
        rows.append([bank["label"], bank["root"], "题库 source-of-truth", "只通过对应维护脚本更新"])
    rows.extend(
        [
            ["个人错题库", WRONG_ROOT.relative_to(ROOT).as_posix(), "错题和复习状态 source-of-truth", "按错题模板和复习记录更新"],
            ["AI 标准笔记", AI_NOTE_DIR.relative_to(ROOT).as_posix(), "方法卡/知识卡 source-of-truth", "由 AI 对话或错题复盘整理后写入"],
            ["LLM Wiki", WIKI_ROOT.relative_to(ROOT).as_posix(), "编译层", "可重复生成"],
        ]
    )
    return f"""# 资料源注册表

{markdown_table(["来源", "路径", "角色", "写入策略"], rows)}
## 使用约束

- 不把原始聊天、PDF 或截图直接写入 wiki 正文作为唯一证据。
- Wiki 页可以总结，但必须保留到源题、错题或标准笔记的链接。
- 需要人工判断的分类，使用低置信度并进入健康检查。
"""


def render_health_check(issues: list[dict[str, str]]) -> str:
    counts = Counter(item["level"] for item in issues)
    rows = [[item["level"], item["area"], item["item"], item["message"]] for item in issues]
    return f"""# 健康检查

## 摘要

- P1：{counts["P1"]}
- P2：{counts["P2"]}
- P3：{counts["P3"]}

## 问题清单

{markdown_table(["级别", "区域", "对象", "说明"], rows)}
"""


def render_compile_queue(topics: list[dict[str, Any]], issues: list[dict[str, str]]) -> str:
    queue_rows = []
    for topic in topics:
        if topic["wrongCount"] and not topic["aiNoteCount"]:
            queue_rows.append([rel_link(WIKI_ROOT / "05_Compile_Queue.md", topic["page"], topic["label"]), "补标准笔记", topic["wrongCount"], "把错因、防错口令、迁移题整理成方法卡"])
        elif topic["wrongCount"] and topic["aiNoteCount"]:
            queue_rows.append([rel_link(WIKI_ROOT / "05_Compile_Queue.md", topic["page"], topic["label"]), "复习验证", topic["wrongCount"], "按闭环完成迁移题并更新 mastery"])
    issue_rows = [[item["level"], item["area"], item["item"], item["message"]] for item in issues if item["level"] in {"P1", "P2"}]
    return f"""# 待编译队列

## 知识编译

{markdown_table(["主题", "动作", "错题数", "完成标准"], queue_rows)}
## 结构修复

{markdown_table(["级别", "区域", "对象", "说明"], issue_rows)}
"""


def render_topic_page(topic: dict[str, Any]) -> str:
    page = ROOT / topic["page"]
    problem_rows = [
        [
            item.get("bank", ""),
            rel_link(page, item.get("file"), item.get("problem_id")),
            item.get("section", ""),
            item.get("status", ""),
        ]
        for item in topic["samples"]
    ]
    wrong_rows = [
        [
            rel_link(page, item.get("file"), item.get("title")),
            item.get("priority", ""),
            item.get("status", ""),
            item.get("mastery", ""),
            item.get("anti_mistake_tip", ""),
        ]
        for item in topic["wrong_items"]
    ]
    note_rows = [
        [
            rel_link(page, item.get("file"), item.get("title")),
            item.get("kind", ""),
            item.get("status", ""),
            item.get("confidence", ""),
        ]
        for item in topic["ai_notes"]
    ]
    return f"""---
type: "llm_topic"
generated_by: "llm_wiki_maintain"
topic_id: "{topic["id"]}"
---
# {topic["label"]}

## 快照

- 二轮题量：{topic["problemCounts"].get("question_bank", 0)}
- 五年经典题量：{topic["problemCounts"].get("classic_bank", 0)}
- 错题数：{topic["wrongCount"]}
- AI 标准笔记：{topic["aiNoteCount"]}
- 方法信号：{"、".join(topic["methodCounts"].keys()) or "暂无"}

## 高频错因

{markdown_table(["错因", "次数"], [[k, v] for k, v in topic["wrongReasons"].items()])}
## 知识点

{markdown_table(["知识点", "次数"], [[k, v] for k, v in topic["knowledgeCounts"].items()])}
## 个人错题

{markdown_table(["错题", "优先级", "状态", "掌握度", "防错口令"], wrong_rows)}
## 标准笔记

{markdown_table(["笔记", "类型", "状态", "置信度"], note_rows)}
## 题库样本

{markdown_table(["题库", "题号", "来源", "状态"], problem_rows)}
## 下一步

- 有错题无标准笔记：先补方法卡。
- 有标准笔记仍错：按“错题 -> 笔记 -> 二轮 -> 五年经典”的闭环验证迁移。
- 只有题库没有错题：暂时作为检索背景，不进入今日优先队列。
"""


def render_method_page(method: str, node: dict[str, Any]) -> str:
    page = ROOT / node["page"]
    topic_rows = [
        [rel_link(page, item["page"], item["label"]), item["score"]]
        for item in node["topics"]
    ]
    sample_rows = [
        [
            item.get("bank", ""),
            rel_link(page, item.get("file"), item.get("problem_id")),
            item.get("section", ""),
            item.get("status", ""),
        ]
        for item in node["samples"]
    ]
    return f"""---
type: "llm_method"
generated_by: "llm_wiki_maintain"
method: "{method}"
---
# {method}

## 快照

- 信号数：{node["count"]}
- 关联主题：{len(node["topics"])}
- 关联错题主题数：{node["wrong_count"]}
- 关联 AI 笔记主题数：{node["ai_note_count"]}

## 关联主题

{markdown_table(["主题", "优先分"], topic_rows)}
## 题库样本

{markdown_table(["题库", "题号", "来源", "状态"], sample_rows)}
"""


def append_log(summary: dict[str, Any]) -> None:
    stamp = dt.datetime.now().isoformat(timespec="seconds")
    entry = f"""## {stamp}

- 题库题目：{summary["problemTotal"]}
- 错题：{summary["wrongTotal"]}
- AI 标准笔记：{summary["aiNoteTotal"]}
- 主题页：{summary["topicTotal"]}
- 方法页：{summary["methodTotal"]}
- 检查项：{summary["issueTotal"]}
"""
    if LOG_MD.exists():
        existing = LOG_MD.read_text(encoding="utf-8", errors="replace").rstrip()
        write_text(LOG_MD, existing + "\n\n" + entry)
    else:
        write_text(LOG_MD, "# LLM Wiki 运行日志\n\n" + entry)


def build_search_corpus(topics: list[dict[str, Any]], methods: dict[str, dict[str, Any]], wrong_notes: list[dict[str, Any]], ai_notes: list[dict[str, Any]], banks: list[dict[str, Any]]) -> list[dict[str, str]]:
    corpus: list[dict[str, str]] = []
    for topic in topics:
        corpus.append({"type": "topic", "title": topic["label"], "file": topic["page"], "text": normalize(json.dumps(topic, ensure_ascii=False))[:3000]})
    for method, node in methods.items():
        corpus.append({"type": "method", "title": method, "file": node["page"], "text": normalize(json.dumps(node, ensure_ascii=False))[:3000]})
    for note in wrong_notes:
        corpus.append({"type": "wrong", "title": str(note.get("_title") or note.get("wrong_id")), "file": str(note.get("_file") or ""), "text": str(note.get("_search") or "")[:3000]})
    for note in ai_notes:
        corpus.append({"type": "ai_note", "title": str(note.get("_title") or note.get("note_id")), "file": str(note.get("_file") or ""), "text": str(note.get("_search") or "")[:3000]})
    for bank in banks:
        for problem in bank["problems"]:
            corpus.append({"type": bank["id"], "title": str(problem.get("problem_id") or ""), "file": str(problem.get("_file") or ""), "text": str(problem.get("_search") or "")[:1600]})
    return corpus


def write_pages(banks: list[dict[str, Any]], wrong_notes: list[dict[str, Any]], ai_notes: list[dict[str, Any]], topics_raw: dict[str, dict[str, Any]], methods: dict[str, dict[str, Any]], issues: list[dict[str, str]], learning_path: list[dict[str, Any]], summary: dict[str, Any]) -> list[dict[str, str]]:
    topics = sorted([summarize_topic(topic) for topic in topics_raw.values()], key=lambda item: (-int(item["score"]), item["label"]))
    write_text(KB_ROOT / "README.md", render_readme(summary))
    write_text(KB_ROOT / "SCHEMA.md", render_schema())
    write_text(WIKI_ROOT / "00_Index.md", render_index(topics, methods, summary))
    write_text(WIKI_ROOT / "01_Overview.md", render_overview(banks, wrong_notes, ai_notes, topics, issues))
    write_text(WIKI_ROOT / "02_Learning_Loop.md", render_learning_loop(learning_path))
    write_text(WIKI_ROOT / "03_Source_Registry.md", render_source_registry(banks))
    write_text(WIKI_ROOT / "04_Health_Check.md", render_health_check(issues))
    write_text(WIKI_ROOT / "05_Compile_Queue.md", render_compile_queue(topics, issues))
    for bank in banks:
        progress = bank.get("progress_data") or {}
        rows = []
        for lesson in progress.get("lessons", [])[:160]:
            rows.append([lesson.get("id", ""), lesson.get("title", ""), lesson.get("total", 0), lesson.get("handled", lesson.get("done", 0)), lesson.get("review", 0)])
        write_text(
            SOURCE_DIR / f"{slug(bank['label'])}.md",
            f"""# {bank["label"]}

## 数据入口

- Manifest：{rel_link(SOURCE_DIR / f"{slug(bank['label'])}.md", bank["manifest"], "problems.json")}
- Progress：{rel_link(SOURCE_DIR / f"{slug(bank['label'])}.md", bank["progress"], "progress.json")}

## 讲次进度

{markdown_table(["讲次", "标题", "题量", "已处理", "待核对"], rows)}
""",
        )
    for topic in topics:
        source = topics_raw[topic["id"]]
        source["problemCounts"] = topic["problemCounts"]
        source["statusCounts"] = topic["statusCounts"]
        source["methodCounts"] = topic["methodCounts"]
        source["knowledgeCounts"] = topic["knowledgeCounts"]
        source["wrongReasons"] = topic["wrongReasons"]
        source["wrongCount"] = topic["wrongCount"]
        source["aiNoteCount"] = topic["aiNoteCount"]
        write_text(ROOT / topic["page"], render_topic_page(source))
    for method, node in methods.items():
        write_text(ROOT / node["page"], render_method_page(method, node))
    append_log(summary)
    return topics


def refresh() -> int:
    banks = [
        load_bank("question_bank", "二轮题库", QUESTION_ROOT),
        load_bank("classic_bank", "五年经典", CLASSIC_ROOT),
    ]
    wrong_notes = load_wrong_notes()
    ai_notes = load_ai_notes()
    topics_raw = build_topics(banks, wrong_notes, ai_notes)
    methods = build_methods(topics_raw)
    issues = build_lint(banks, wrong_notes, ai_notes, topics_raw)
    learning_path = content_learning_path()
    problem_total = sum(len(bank["problems"]) for bank in banks)
    summary = {
        "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
        "problemTotal": problem_total,
        "wrongTotal": len(wrong_notes),
        "aiNoteTotal": len(ai_notes),
        "topicTotal": len(topics_raw),
        "methodTotal": len(methods),
        "issueTotal": len(issues),
    }
    topics = write_pages(banks, wrong_notes, ai_notes, topics_raw, methods, issues, learning_path, summary)
    corpus = build_search_corpus(topics, methods, wrong_notes, ai_notes, banks)
    write_text(
        DATA_JSON,
        json.dumps(
            {
                "schemaVersion": 1,
                "generatedAt": summary["generatedAt"],
                "summary": summary,
                "sources": [
                    {"id": bank["id"], "label": bank["label"], "root": bank["root"], "problemCount": len(bank["problems"])}
                    for bank in banks
                ]
                + [
                    {"id": "wrong_bank", "label": "个人错题库", "root": WRONG_ROOT.relative_to(ROOT).as_posix(), "problemCount": len(wrong_notes)},
                    {"id": "ai_notes", "label": "AI标准笔记", "root": AI_NOTE_DIR.relative_to(ROOT).as_posix(), "problemCount": len(ai_notes)},
                ],
                "topics": topics,
                "methods": methods,
                "issues": issues,
                "learningPath": learning_path,
                "searchCorpus": corpus,
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    print(f"LLM Wiki 已刷新：{KB_ROOT / 'README.md'}")
    return 0


def search(query: str, limit: int) -> int:
    data = load_json(DATA_JSON)
    if not data:
        print("找不到 wiki_index.json，请先运行 refresh。")
        return 1
    q = normalize(query)
    tokens = [normalize(token) for token in re.split(r"\s+", query) if normalize(token)]
    scored = []
    for item in data.get("searchCorpus", []):
        text = str(item.get("text") or "")
        title = normalize(str(item.get("title") or ""))
        score = 0
        if q and q in text:
            score += 100
        if q and q in title:
            score += 80
        for token in tokens:
            if token in text:
                score += 12
            if token in title:
                score += 18
        if score:
            scored.append((score, item))
    scored.sort(key=lambda pair: (-pair[0], str(pair[1].get("type")), str(pair[1].get("title"))))
    rows = [[score, item.get("type", ""), item.get("title", ""), item.get("file", "")] for score, item in scored[:limit]]
    print(markdown_table(["分数", "类型", "标题", "文件"], rows))
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and search the local LLM wiki layer.")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("refresh", help="rebuild the LLM wiki")
    search_parser = sub.add_parser("search", help="search the compiled wiki index")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=12)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command in {None, "refresh"}:
        return refresh()
    if args.command == "search":
        return search(args.query, args.limit)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
