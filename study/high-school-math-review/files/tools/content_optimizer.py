# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WRONG_ROOT = ROOT / "个人错题库"
WRONG_DIR = WRONG_ROOT / "01_错题"
WRONG_CONTROL = WRONG_ROOT / "00_控制台"
QUESTION_ROOT = ROOT / "Obsidian题库"
CLASSIC_ROOT = ROOT / "高考数学五年经典"

QUESTION_MANIFEST = QUESTION_ROOT / "04_原始资料" / "problems.json"
CLASSIC_MANIFEST = CLASSIC_ROOT / "04_原始资料" / "problems.json"

ROOT_OVERVIEW = ROOT / "内容优化总览.md"
ROOT_JSON = ROOT / "内容优化总览.json"
WRONG_ADVICE = WRONG_CONTROL / "内容复习建议.md"
SIMILAR_NOTE = WRONG_CONTROL / "相似题推荐.md"
RELATED_AI_NOTES = WRONG_CONTROL / "错题关联笔记.md"
LEARNING_PATH = WRONG_CONTROL / "今日学习路线.md"
QUESTION_CONTENT_MAP = QUESTION_ROOT / "00_控制台" / "内容地图.md"
CLASSIC_CONTENT_MAP = CLASSIC_ROOT / "00_控制台" / "内容地图.md"
AI_NOTE_ROOT = QUESTION_ROOT / "08_AI笔记管理"
AI_NOTE_DIR = AI_NOTE_ROOT / "02_标准笔记"


METHOD_PATTERNS = {
    "基本不等式": ["基本不等式", "均值不等式", "最小值", "最大值"],
    "代入消元": ["代入消元", "消元"],
    "换元": ["换元", "令 "],
    "对称结构": ["对称结构", "对称", "(a+1)(b+1)", "a+b", "ab"],
    "特征方程": ["特征方程", "特征根", "a_{n+2}", "递推式"],
    "递推验证": ["递推", "前几项", "通项", "等比数列"],
    "选项排除": ["多选", "选项", "判断"],
    "构造函数": ["构造函数", "构造"],
    "分类讨论": ["分类讨论", "讨论"],
    "数形结合": ["数形结合", "图像"],
    "导数单调性": ["导数", "单调", "极值"],
    "圆锥曲线定义": ["椭圆", "双曲线", "抛物线", "焦点", "准线"],
    "空间向量": ["空间向量", "法向量", "二面角"],
}

MODULE_ALIASES = {
    "基本不等式": ["不等式", "基本不等式"],
    "数列": ["数列"],
    "函数": ["函数"],
    "导数选填": ["导数"],
    "导数大题": ["导数"],
    "三角函数": ["三角函数", "解三角形"],
    "解三角形": ["三角函数", "解三角形"],
    "向量": ["向量", "平面向量"],
    "立体几何": ["立体几何", "空间向量"],
    "直线和圆": ["直线与圆", "直线和圆"],
    "圆锥曲线(难点)": ["圆锥曲线"],
    "圆锥曲线(小题)": ["圆锥曲线"],
    "概率统计": ["概率", "统计"],
    "排列组合": ["排列组合", "二项式"],
}


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


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
    lines = match.group(1).splitlines()
    data: dict[str, Any] = {}
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
    return data, text[match.end():]


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


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


def md_link(base_file: Path, target: str | Path, label: str) -> str:
    path = Path(target)
    if not path.is_absolute():
        path = ROOT / path
    try:
        rel = os.path.relpath(path, start=base_file.parent).replace("\\", "/")
        return f"[{label}]({rel})"
    except ValueError:
        return label


def load_manifest(path: Path, bank_name: str, root: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    for problem in data.get("problems", []):
        problem["_bank"] = bank_name
        problem["_root"] = str(root)
        problem["_text"] = searchable_text(problem)
    return data


def searchable_text(problem: dict[str, Any]) -> str:
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
    return normalize(" ".join(str(item) for item in fields))


def normalize(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\\[a-zA-Z]+", "", value)
    value = re.sub(r"[{}\[\]()\s，。；：、,.!?:;`'\"<>|]", "", value)
    return value


def load_wrong_notes() -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
    if not WRONG_DIR.exists():
        return notes
    for path in sorted(WRONG_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if fm.get("type") != "wrong_problem":
            continue
        title_match = re.search(r"^#\s+(.+)$", body, re.M)
        fm["_title"] = title_match.group(1).strip() if title_match else path.stem
        fm["_file"] = path.relative_to(ROOT).as_posix()
        fm["_path"] = str(path)
        fm["_body"] = body
        fm["_search"] = normalize(" ".join([body, str(fm.get("anti_mistake_tip", "")), str(fm.get("lesson_title", ""))]))
        notes.append(fm)
    return notes


def keyword_candidates(note: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for field in ["knowledge_points", "methods", "wrong_reason"]:
        values.extend(as_list(note.get(field)))
    values.extend([str(note.get("module") or ""), str(note.get("topic") or ""), str(note.get("lesson_title") or "")])
    body = str(note.get("_body") or "")
    for pattern in ["最小值", "最大值", "等比数列", "等差数列", "递推", "特征方程", "特征根", "换元", "消元", "对称结构", "多选题"]:
        if pattern in body:
            values.append(pattern)
    cleaned: list[str] = []
    seen: set[str] = set()
    for value in values:
        value = str(value).strip()
        if not value or value in seen:
            continue
        seen.add(value)
        cleaned.append(value)
    return cleaned


def source_note_path(problem: dict[str, Any]) -> Path:
    return Path(str(problem.get("_root"))) / str(problem.get("note_path", ""))


def source_problem_text(note: dict[str, Any]) -> str:
    original = str(note.get("original_file") or "").strip()
    if not original:
        return ""
    path = ROOT / original
    if not path.exists():
        return ""
    return normalize(path.read_text(encoding="utf-8", errors="replace"))


def note_priority_key(note: dict[str, Any]) -> tuple[str, int, int, str, str]:
    status = str(note.get("status") or "")
    return (
        str(note.get("priority") or "P2"),
        0 if status == "仍错" else 1,
        as_int(note.get("mastery"), 9),
        str(note.get("next_review") or "9999-12-31"),
        str(note.get("_title") or ""),
    )


def load_ai_notes() -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
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
        fm["_path"] = str(path)
        fm["_body"] = body
        fields = [
            fm.get("_title", ""),
            fm.get("module", ""),
            fm.get("topic", ""),
            fm.get("lesson_id", ""),
            " ".join(as_list(fm.get("knowledge_points"))),
            " ".join(as_list(fm.get("methods"))),
            " ".join(as_list(fm.get("related_problem_ids"))),
            body,
        ]
        fm["_search"] = normalize(" ".join(str(item) for item in fields))
        notes.append(fm)
    return notes


def score_ai_note(wrong: dict[str, Any], ai_note: dict[str, Any]) -> int:
    score = 0
    if str(wrong.get("source_problem_id") or "") in as_list(ai_note.get("related_problem_ids")):
        score += 90
    if str(wrong.get("lesson_id") or "") and str(wrong.get("lesson_id") or "") == str(ai_note.get("lesson_id") or ""):
        score += 70
    if str(wrong.get("module_id") or "") and str(wrong.get("module_id") or "") == str(ai_note.get("module_id") or ""):
        score += 45
    if str(wrong.get("topic") or "") and str(wrong.get("topic") or "") == str(ai_note.get("topic") or ""):
        score += 30
    if str(wrong.get("module") or "") and str(wrong.get("module") or "") == str(ai_note.get("module") or ""):
        score += 25

    search = str(ai_note.get("_search") or "")
    for keyword in keyword_candidates(wrong):
        norm = normalize(keyword)
        if norm and norm in search:
            score += 12

    if str(ai_note.get("status") or "") == "ready":
        score += 4
    if str(ai_note.get("classification_confidence") or "") == "high":
        score += 3
    return score


def recommend_ai_notes(wrong: dict[str, Any], ai_notes: list[dict[str, Any]], limit: int = 4) -> list[dict[str, Any]]:
    scored: list[tuple[int, dict[str, Any]]] = []
    for ai_note in ai_notes:
        score = score_ai_note(wrong, ai_note)
        if score >= 20:
            scored.append((score, ai_note))
    scored.sort(key=lambda item: (-item[0], str(item[1].get("module_id") or ""), str(item[1].get("lesson_id") or ""), str(item[1].get("_title") or "")))
    result = []
    for score, ai_note in scored[:limit]:
        result.append(
            {
                "score": score,
                "title": ai_note.get("_title", ""),
                "file": ai_note.get("_file", ""),
                "note_id": ai_note.get("note_id", ""),
                "note_kind": ai_note.get("note_kind", ""),
                "module": ai_note.get("module", ""),
                "lesson_id": ai_note.get("lesson_id", ""),
                "topic": ai_note.get("topic", ""),
                "status": ai_note.get("status", ""),
                "confidence": ai_note.get("classification_confidence", ""),
                "reason": explain_ai_note_match(wrong, ai_note),
            }
        )
    return result


def explain_ai_note_match(wrong: dict[str, Any], ai_note: dict[str, Any]) -> str:
    reasons = []
    if str(wrong.get("source_problem_id") or "") in as_list(ai_note.get("related_problem_ids")):
        reasons.append("关联原题")
    if str(wrong.get("lesson_id") or "") and str(wrong.get("lesson_id") or "") == str(ai_note.get("lesson_id") or ""):
        reasons.append("同讲次")
    elif str(wrong.get("module") or "") and str(wrong.get("module") or "") == str(ai_note.get("module") or ""):
        reasons.append("同专题")
    shared = [kw for kw in keyword_candidates(wrong) if normalize(kw) and normalize(kw) in str(ai_note.get("_search") or "")]
    if shared:
        reasons.append("命中：" + "、".join(shared[:3]))
    return "；".join(reasons) or "内容相近"


def score_problem(note: dict[str, Any], problem: dict[str, Any], original_text: str) -> int:
    score = 0
    bank = str(problem.get("_bank") or "")
    if problem.get("_bank") == "二轮题库" and str(problem.get("problem_id")) == str(note.get("source_problem_id")):
        return -1

    note_module = str(note.get("module") or "")
    aliases = MODULE_ALIASES.get(note_module, [note_module] if note_module else [])
    alias_hit = any(alias and alias in str(problem.get("module") or "") for alias in aliases)
    title_alias_hit = any(alias and alias in str(problem.get("lesson_title") or "") for alias in aliases)
    if bank == "二轮题库" and str(problem.get("lesson_id") or "") == str(note.get("lesson_id") or ""):
        score += 85
    if bank == "二轮题库" and str(problem.get("module_id") or "") == str(note.get("module_id") or ""):
        score += 35
    if str(problem.get("topic") or "") == str(note.get("topic") or ""):
        score += 30
    if alias_hit:
        score += 45 if bank != "二轮题库" else 30
    if title_alias_hit:
        score += 15

    problem_text = str(problem.get("_text") or "")
    for keyword in keyword_candidates(note):
        if normalize(keyword) and normalize(keyword) in problem_text:
            score += 12

    if original_text:
        for signal in ["最小值", "最大值", "等比数列", "递推", "a_{n+2}", "x+2y", "2xy", "多选"]:
            norm = normalize(signal)
            if norm in original_text and norm in problem_text:
                score += 8

    content = str(problem.get("content") or "")
    if "多选" in str(note.get("_body") or "") and "多选" in content:
        score += 6
    if str(problem.get("status") or "") in {"todo", "review"}:
        score += 3
    return score


def recommend_for_note(note: dict[str, Any], banks: list[dict[str, Any]], limit_per_bank: int = 5) -> list[dict[str, Any]]:
    original_text = source_problem_text(note)
    recommendations: list[dict[str, Any]] = []
    for bank in banks:
        scored = []
        for problem in bank.get("problems", []):
            score = score_problem(note, problem, original_text)
            if score > 0:
                scored.append((score, problem))
        scored.sort(key=lambda item: (-item[0], str(item[1].get("module_id") or ""), str(item[1].get("lesson_id") or ""), int(item[1].get("source_order") or 0)))
        for score, problem in scored[:limit_per_bank]:
            recommendations.append(
                {
                    "score": score,
                    "bank": problem.get("_bank", ""),
                    "problem_id": problem.get("problem_id", ""),
                    "lesson_id": problem.get("lesson_id", ""),
                    "lesson_title": problem.get("lesson_title", ""),
                    "module": problem.get("module", ""),
                    "topic": problem.get("topic", ""),
                    "section": problem.get("section", ""),
                    "status": problem.get("status", ""),
                    "note_path": source_note_path(problem).relative_to(ROOT).as_posix(),
                    "reason": explain_match(note, problem),
                }
            )
    return recommendations


def first_bank_recommendation(recommendations: list[dict[str, Any]], bank_name: str) -> dict[str, Any]:
    return next((item for item in recommendations if item.get("bank") == bank_name), {})


def suggested_ai_note_title(note: dict[str, Any]) -> str:
    methods = "、".join(keyword_candidates(note)[:3])
    suffix = f"：{methods}" if methods else ""
    return f"建议整理《{note.get('module', '待分类')} / {note.get('topic', '待分类')}{suffix}》"


def review_reason(note: dict[str, Any]) -> str:
    today = dt.date.today()
    due = parse_date(note.get("next_review"))
    status = str(note.get("status") or "")
    mastery = as_int(note.get("mastery"), 9)
    if status == "仍错":
        return "仍错优先"
    if due and due < today:
        return f"逾期 {(today - due).days} 天"
    if due and due == today:
        return "今日到期"
    if mastery <= 2:
        return "掌握度偏低"
    if status == "待复习":
        return "待复习"
    return "需要巩固"


def suggested_timebox(note: dict[str, Any]) -> str:
    priority = str(note.get("priority") or "P2")
    status = str(note.get("status") or "")
    mastery = as_int(note.get("mastery"), 3)
    if priority == "P1" or status == "仍错" or mastery <= 2:
        return "25-35 分钟"
    if priority == "P3" and mastery >= 4:
        return "10-15 分钟"
    return "15-25 分钟"


def build_learning_path(
    notes: list[dict[str, Any]],
    recommendations: dict[str, list[dict[str, Any]]],
    related_notes: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    today = dt.date.today()
    active_notes = []
    for note in notes:
        due = parse_date(note.get("next_review"))
        status = str(note.get("status") or "")
        if status in {"待复习", "仍错"} or (due and due <= today) or as_int(note.get("mastery"), 9) <= 2:
            active_notes.append(note)
    active_notes.sort(key=note_priority_key)

    path = []
    for index, note in enumerate(active_notes, start=1):
        wrong_id = str(note.get("wrong_id") or "")
        recs = recommendations.get(wrong_id, [])
        ai_recs = related_notes.get(wrong_id, [])
        two_round = first_bank_recommendation(recs, "二轮题库")
        classic = first_bank_recommendation(recs, "五年经典")
        ai_note = ai_recs[0] if ai_recs else {}
        path.append(
            {
                "order": index,
                "wrong_id": wrong_id,
                "title": note.get("_title", ""),
                "file": note.get("_file", ""),
                "priority": note.get("priority", ""),
                "status": note.get("status", ""),
                "mastery": note.get("mastery", ""),
                "module": note.get("module", ""),
                "topic": note.get("topic", ""),
                "wrong_reason": as_list(note.get("wrong_reason")),
                "anti_mistake_tip": note.get("anti_mistake_tip", ""),
                "review_reason": review_reason(note),
                "timebox": suggested_timebox(note),
                "ai_note": ai_note,
                "ai_note_action": "读对应标准笔记" if ai_note else suggested_ai_note_title(note),
                "two_round": two_round,
                "classic": classic,
                "action": "原错题重做 -> 方法/笔记复盘 -> 二轮同类题 -> 五年经典迁移题",
            }
        )
    return path


def explain_match(note: dict[str, Any], problem: dict[str, Any]) -> str:
    reasons = []
    if str(problem.get("lesson_id") or "") == str(note.get("lesson_id") or ""):
        reasons.append("同讲次")
    elif str(problem.get("module") or "") == str(note.get("module") or ""):
        reasons.append("同专题")
    elif any(alias and alias in str(problem.get("module") or "") for alias in MODULE_ALIASES.get(str(note.get("module") or ""), [])):
        reasons.append("相邻专题")
    shared = [kw for kw in keyword_candidates(note) if normalize(kw) and normalize(kw) in str(problem.get("_text") or "")]
    if shared:
        reasons.append("命中：" + "、".join(shared[:3]))
    return "；".join(reasons) or "内容相近"


def count_methods(problems: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for problem in problems:
        text = str(problem.get("_text") or "")
        for method, patterns in METHOD_PATTERNS.items():
            if any(normalize(pattern) in text for pattern in patterns):
                counts[method] += 1
    return counts


def bank_content_summary(bank: dict[str, Any]) -> dict[str, Any]:
    problems = bank.get("problems", [])
    module_counts = Counter(str(problem.get("module") or "未分类") for problem in problems)
    lesson_counts = Counter(f"{problem.get('lesson_id')} {problem.get('lesson_title') or problem.get('topic')}" for problem in problems)
    section_counts = Counter(str(problem.get("section") or "未标注") for problem in problems)
    kind_counts = Counter(str(problem.get("kind") or "未标注") for problem in problems)
    return {
        "total": len(problems),
        "modules": module_counts,
        "lessons": lesson_counts,
        "sections": section_counts,
        "kinds": kind_counts,
        "methods": count_methods(problems),
    }


def wrong_content_summary(notes: list[dict[str, Any]]) -> dict[str, Any]:
    today = dt.date.today()
    reason_counts: Counter[str] = Counter()
    knowledge_counts: Counter[str] = Counter()
    method_counts: Counter[str] = Counter()
    topic_counts: Counter[str] = Counter()
    due_count = 0
    for note in notes:
        reason_counts.update(as_list(note.get("wrong_reason")) or ["待补充"])
        knowledge_counts.update(as_list(note.get("knowledge_points")) or ["待补充"])
        method_counts.update(as_list(note.get("methods")) or ["待补充"])
        topic_counts.update([f"{note.get('module')} / {note.get('topic')}"])
        due = parse_date(note.get("next_review"))
        if str(note.get("status") or "") in {"待复习", "仍错"} or (due and due <= today):
            due_count += 1
    return {
        "total": len(notes),
        "due": due_count,
        "reasons": reason_counts,
        "knowledge": knowledge_counts,
        "methods": method_counts,
        "topics": topic_counts,
    }


def render_bank_map(bank_name: str, summary: dict[str, Any], wrong_summary: dict[str, Any]) -> str:
    focus_rows = []
    module_counts = summary["modules"]
    for topic, count in wrong_summary["topics"].most_common():
        module = str(topic).split(" / ", 1)[0]
        aliases = MODULE_ALIASES.get(module, [module])
        matched = sum(value for name, value in module_counts.items() if any(alias and alias in name for alias in aliases))
        focus_rows.append([topic, count, matched])
    return f"""# 内容地图

本页由 `tools/content_optimizer.py` 生成，按真实题目内容统计。

## 概览

- 题目总数：{summary["total"]}

## 与当前错题的连接

这里按错题里的薄弱主题，反查本题库里可迁移的题量。第三列不是推荐顺序，只是告诉你这个薄弱点在本题库里有多少可练空间。

{markdown_table(["错题主题", "错题数", f"{bank_name}相关题量"], focus_rows)}

## 专题题量

{markdown_table(["专题", "题量"], [[k, v] for k, v in summary["modules"].most_common()])}
## 高频题组

{markdown_table(["题组", "题量"], [[k, v] for k, v in summary["lessons"].most_common(20)])}
## 来源/题型分布

{markdown_table(["来源", "题量"], [[k, v] for k, v in summary["sections"].most_common(20)])}
## 方法信号

这些不是严格标签，而是从题干和题组标题中抓出来的内容信号，用来帮助复习选题。

{markdown_table(["方法信号", "相关题数"], [[k, v] for k, v in summary["methods"].most_common()])}
"""


def render_wrong_advice(
    notes: list[dict[str, Any]],
    wrong_summary: dict[str, Any],
    recommendations: dict[str, list[dict[str, Any]]],
    related_notes: dict[str, list[dict[str, Any]]],
) -> str:
    rows = []
    for note in sorted(notes, key=note_priority_key):
        recs = recommendations.get(str(note.get("wrong_id") or ""), [])
        ai = (related_notes.get(str(note.get("wrong_id") or ""), []) or [{}])[0]
        two_round = first_bank_recommendation(recs, "二轮题库")
        classic = first_bank_recommendation(recs, "五年经典")
        rows.append(
            [
                md_link(WRONG_ADVICE, note["_file"], note.get("_title", "")),
                note.get("priority", ""),
                note.get("status", ""),
                note.get("mastery", ""),
                "、".join(as_list(note.get("wrong_reason"))),
                note.get("anti_mistake_tip", ""),
                md_link(WRONG_ADVICE, ai.get("file", ""), str(ai.get("title", ""))) if ai else suggested_ai_note_title(note),
                md_link(WRONG_ADVICE, two_round.get("note_path", ""), f"{two_round.get('problem_id', '')}") if two_round else "暂无",
                md_link(WRONG_ADVICE, classic.get("note_path", ""), f"{classic.get('problem_id', '')}") if classic else "暂无",
            ]
        )

    weak_rows = []
    for topic, count in wrong_summary["topics"].most_common():
        weak_rows.append([topic, count])

    return f"""# 内容复习建议

本页由 `tools/content_optimizer.py` 生成。它不是按文件夹冷统计，而是读取错题的错因、知识点、方法和题库题干后给出的复习入口。

## 先处理什么

- 今日队列：{wrong_summary["due"]}
- 错题总数：{wrong_summary["total"]}
- 当前最集中的错因：{wrong_summary["reasons"].most_common(1)[0][0] if wrong_summary["reasons"] else "暂无"}
- 当前最集中的知识点：{wrong_summary["knowledge"].most_common(1)[0][0] if wrong_summary["knowledge"] else "暂无"}

## 薄弱主题

{markdown_table(["主题", "错题数"], weak_rows)}
## 错因画像

{markdown_table(["错因", "次数"], [[k, v] for k, v in wrong_summary["reasons"].most_common()])}
## 方法画像

{markdown_table(["方法", "次数"], [[k, v] for k, v in wrong_summary["methods"].most_common()])}
## 今日复习动作

{markdown_table(["错题", "优先级", "状态", "掌握度", "错因", "防错口令", "对应AI笔记", "二轮同类题", "五年迁移题"], rows)}
## 使用建议

- 每道错题先重做原题，再读或补“对应AI笔记”，然后做“相似题推荐”里的二轮同类题，最后做五年经典迁移题。
- `仍错` 和 `mastery <= 2` 的题，不要只看答案，先把防错口令写到草稿纸第一行。
- 如果同一个错因连续出现，把它整理成 AI 标准笔记，而不是继续只加题。
"""


def render_similar_note(notes: list[dict[str, Any]], recommendations: dict[str, list[dict[str, Any]]]) -> str:
    sections = []
    for note in sorted(notes, key=note_priority_key):
        recs = recommendations.get(str(note.get("wrong_id") or ""), [])
        rows = [
            [
                rec["bank"],
                md_link(SIMILAR_NOTE, rec["note_path"], str(rec["problem_id"])),
                rec["lesson_title"],
                rec["section"],
                rec["status"],
                rec["score"],
                rec["reason"],
            ]
            for rec in recs
        ]
        sections.append(
            f"""## {note.get('_title')}

- 原错因：{"、".join(as_list(note.get("wrong_reason")))}
- 知识点：{"、".join(as_list(note.get("knowledge_points")))}
- 防错口令：{note.get("anti_mistake_tip", "")}

{markdown_table(["题库", "题号", "题组", "来源", "状态", "匹配分", "推荐理由"], rows)}
"""
        )
    return "# 相似题推荐\n\n本页由 `tools/content_optimizer.py` 根据错题内容和两套题库题干自动生成。\n\n" + "\n".join(sections)


def render_related_ai_notes(notes: list[dict[str, Any]], related_notes: dict[str, list[dict[str, Any]]], ai_note_count: int) -> str:
    sections = []
    for note in sorted(notes, key=note_priority_key):
        recs = related_notes.get(str(note.get("wrong_id") or ""), [])
        rows = [
            [
                md_link(RELATED_AI_NOTES, rec["file"], rec["title"]),
                rec["note_kind"],
                rec["module"],
                rec["lesson_id"],
                rec["topic"],
                rec["status"],
                rec["score"],
                rec["reason"],
            ]
            for rec in recs
        ]
        fallback_line = f"- 暂无匹配时的整理方向：{suggested_ai_note_title(note)}" if not recs else ""
        sections.append(
            f"""## {note.get('_title')}

- 错因：{"、".join(as_list(note.get("wrong_reason")))}
- 知识点：{"、".join(as_list(note.get("knowledge_points")))}
- 防错口令：{note.get("anti_mistake_tip", "")}
{fallback_line}

{markdown_table(["AI笔记", "类型", "专题", "讲次", "知识点", "状态", "匹配分", "理由"], rows)}
"""
        )
    return f"""# 错题关联笔记

本页由 `tools/content_optimizer.py` 生成，把错题和 AI 标准笔记连接起来。

## 概览

- 当前标准笔记数：{ai_note_count}
- 当前错题数：{len(notes)}

如果某道错题下面暂无匹配笔记，就优先把它的“错因定位、关键结论、防错口令”整理成一张 AI 标准笔记。

""" + "\n".join(sections)


def render_learning_path(path: list[dict[str, Any]]) -> str:
    rows = []
    task_rows = []
    for item in path:
        ai_note = item.get("ai_note") or {}
        two_round = item.get("two_round") or {}
        classic = item.get("classic") or {}
        task_rows.append(
            [
                item["order"],
                md_link(LEARNING_PATH, item["file"], item["title"]),
                item.get("review_reason", ""),
                item.get("timebox", ""),
                "先独立重做，再看笔记和迁移题",
            ]
        )
        rows.append(
            [
                item["order"],
                md_link(LEARNING_PATH, item["file"], item["title"]),
                f"{item.get('priority', '')} / {item.get('status', '')} / 掌握度{item.get('mastery', '')}",
                item.get("review_reason", ""),
                "、".join(item.get("wrong_reason") or []),
                item.get("anti_mistake_tip", ""),
                md_link(LEARNING_PATH, ai_note.get("file", ""), ai_note.get("title", "")) if ai_note else item.get("ai_note_action", ""),
                md_link(LEARNING_PATH, two_round.get("note_path", ""), f"{two_round.get('problem_id', '')}") if two_round else "暂无",
                md_link(LEARNING_PATH, classic.get("note_path", ""), f"{classic.get('problem_id', '')}") if classic else "暂无",
            ]
        )
    return f"""# 今日学习路线

本页由 `tools/content_optimizer.py` 生成，用错题牵引题库和笔记。

## 闭环顺序

1. 重做原错题，只看题目和自己的防错口令。
2. 读对应 AI 笔记；如果暂无，就把这道错题整理成一张方法卡。
3. 做一道二轮同类题，确认方法能迁移。
4. 做一道五年经典迁移题，确认在陌生题面下也能识别。

## 今日执行卡

{markdown_table(["顺序", "错题", "为什么今天做", "建议用时", "动作"], task_rows)}
## 今日路线

{markdown_table(["顺序", "错题", "优先状态", "为什么今天做", "错因", "防错口令", "AI笔记/整理方向", "二轮同类题", "五年迁移题"], rows)}
"""


def render_root_overview(
    wrong_summary: dict[str, Any],
    question_summary: dict[str, Any],
    classic_summary: dict[str, Any],
    ai_note_count: int,
    learning_path: list[dict[str, Any]],
) -> str:
    path_rows = []
    for item in learning_path[:8]:
        ai_note = item.get("ai_note") or {}
        two_round = item.get("two_round") or {}
        classic = item.get("classic") or {}
        path_rows.append(
            [
                item["order"],
                md_link(ROOT_OVERVIEW, item["file"], item["title"]),
                item.get("priority", ""),
                item.get("status", ""),
                md_link(ROOT_OVERVIEW, ai_note.get("file", ""), ai_note.get("title", "")) if ai_note else "建议补笔记",
                md_link(ROOT_OVERVIEW, two_round.get("note_path", ""), two_round.get("problem_id", "")) if two_round else "暂无",
                md_link(ROOT_OVERVIEW, classic.get("note_path", ""), classic.get("problem_id", "")) if classic else "暂无",
            ]
        )
    return f"""# 内容优化总览

本页由 `tools/content_optimizer.py` 生成，聚合真实内容层面的复习建议。

## 快速入口

- {md_link(ROOT_OVERVIEW, LEARNING_PATH, "今日学习路线")}
- {md_link(ROOT_OVERVIEW, WRONG_ADVICE, "错题内容复习建议")}
- {md_link(ROOT_OVERVIEW, SIMILAR_NOTE, "错题相似题推荐")}
- {md_link(ROOT_OVERVIEW, RELATED_AI_NOTES, "错题关联笔记")}
- {md_link(ROOT_OVERVIEW, QUESTION_CONTENT_MAP, "二轮题库内容地图")}
- {md_link(ROOT_OVERVIEW, CLASSIC_CONTENT_MAP, "五年经典内容地图")}

## 当前内容焦点

| 项目 | 数量 |
| --- | ---: |
| 错题总数 | {wrong_summary["total"]} |
| 今日队列 | {wrong_summary["due"]} |
| 二轮题库题量 | {question_summary["total"]} |
| 五年经典题量 | {classic_summary["total"]} |
| AI 标准笔记 | {ai_note_count} |

## 今日学习闭环

{markdown_table(["顺序", "错题", "优先级", "状态", "AI笔记", "二轮题", "五年题"], path_rows)}

## 错题高频信号

{markdown_table(["类型", "高频项", "次数"], [["错因", k, v] for k, v in wrong_summary["reasons"].most_common(5)] + [["知识点", k, v] for k, v in wrong_summary["knowledge"].most_common(5)] + [["方法", k, v] for k, v in wrong_summary["methods"].most_common(5)])}
## 题库方法信号

{markdown_table(["题库", "方法信号", "相关题数"], [["二轮题库", k, v] for k, v in question_summary["methods"].most_common(8)] + [["五年经典", k, v] for k, v in classic_summary["methods"].most_common(8)])}
"""


def main() -> int:
    question_bank = load_manifest(QUESTION_MANIFEST, "二轮题库", QUESTION_ROOT)
    classic_bank = load_manifest(CLASSIC_MANIFEST, "五年经典", CLASSIC_ROOT)
    banks = [question_bank, classic_bank]
    notes = load_wrong_notes()
    ai_notes = load_ai_notes()

    recommendations = {str(note.get("wrong_id") or ""): recommend_for_note(note, banks) for note in notes}
    related_notes = {str(note.get("wrong_id") or ""): recommend_ai_notes(note, ai_notes) for note in notes}
    wrong_summary = wrong_content_summary(notes)
    question_summary = bank_content_summary(question_bank)
    classic_summary = bank_content_summary(classic_bank)
    learning_path = build_learning_path(notes, recommendations, related_notes)

    write_text(WRONG_ADVICE, render_wrong_advice(notes, wrong_summary, recommendations, related_notes))
    write_text(SIMILAR_NOTE, render_similar_note(notes, recommendations))
    write_text(RELATED_AI_NOTES, render_related_ai_notes(notes, related_notes, len(ai_notes)))
    write_text(LEARNING_PATH, render_learning_path(learning_path))
    write_text(QUESTION_CONTENT_MAP, render_bank_map("二轮题库", question_summary, wrong_summary))
    write_text(CLASSIC_CONTENT_MAP, render_bank_map("五年经典", classic_summary, wrong_summary))
    write_text(ROOT_OVERVIEW, render_root_overview(wrong_summary, question_summary, classic_summary, len(ai_notes), learning_path))
    write_text(
        ROOT_JSON,
        json.dumps(
            {
                "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
                "wrong": {
                    "total": wrong_summary["total"],
                    "due": wrong_summary["due"],
                    "reasons": dict(wrong_summary["reasons"]),
                    "knowledge": dict(wrong_summary["knowledge"]),
                    "methods": dict(wrong_summary["methods"]),
                    "topics": dict(wrong_summary["topics"]),
                },
                "recommendations": recommendations,
                "relatedNotes": related_notes,
                "learningPath": learning_path,
                "aiNotes": {
                    "total": len(ai_notes),
                    "statusCounts": dict(Counter(str(note.get("status") or "review") for note in ai_notes)),
                    "moduleCounts": dict(Counter(str(note.get("module") or "待分类") for note in ai_notes)),
                },
                "questionBank": {
                    "total": question_summary["total"],
                    "modules": dict(question_summary["modules"]),
                    "methods": dict(question_summary["methods"]),
                },
                "classicBank": {
                    "total": classic_summary["total"],
                    "modules": dict(classic_summary["modules"]),
                    "methods": dict(classic_summary["methods"]),
                },
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    print(f"内容优化已刷新：{ROOT_OVERVIEW}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
