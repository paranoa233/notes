# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any


VAULT = Path(__file__).resolve().parents[1]
STUDY_ROOT = VAULT.parent
MANIFEST = VAULT / "04_原始资料" / "problems.json"
WRONG_DIR = STUDY_ROOT / "个人错题库" / "01_错题"

SYSTEM_ROOT = VAULT / "08_AI笔记管理"
INBOX = SYSTEM_ROOT / "01_待整理"
CONVERSATION_INBOX = INBOX / "00_AI对话导入入口"
NOTE_INBOX = INBOX / "01_普通笔记草稿"
PROBLEM_REVIEW_INBOX = INBOX / "02_题解复盘"
OUTPUT_ROOT = SYSTEM_ROOT / "02_标准笔记"
ARCHIVE_ROOT = SYSTEM_ROOT / "03_原始归档"
RUN_ROOT = SYSTEM_ROOT / "04_运行记录"
TEMPLATE_DIR = SYSTEM_ROOT / "90_模板"
INDEX_NOTE = SYSTEM_ROOT / "标准笔记索引.md"
HEALTH_NOTE = SYSTEM_ROOT / "系统体检.md"
INDEX_JSON = SYSTEM_ROOT / "notes_index.json"
PIPELINE_NOTE = SYSTEM_ROOT / "AI学习流水线.md"
INTAKE_NOTE = SYSTEM_ROOT / "对话导入清单.md"
CONVERSION_NOTE = SYSTEM_ROOT / "AI笔记转化看板.md"

OPENAI_API_URL = os.environ.get("DEEPSEEK_OPENAI_API_URL", "https://api.deepseek.com/v1/chat/completions")
ANTHROPIC_API_URL = os.environ.get("DEEPSEEK_API_URL", "https://api.deepseek.com/anthropic/v1/messages")
API_STYLE = os.environ.get("DEEPSEEK_API_STYLE", "openai").strip().lower()
DEFAULT_MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-pro")
THINKING_MODE = os.environ.get("DEEPSEEK_THINKING", "enabled").strip().lower()
REASONING_EFFORT = os.environ.get("DEEPSEEK_REASONING_EFFORT", "max").strip().lower()

REQUIRED_HEADERS = [
    "## 原始问题",
    "## 一句话结论",
    "## 知识归属",
    "## 核心内容",
    "## 方法流程",
    "## 例题关联",
    "## 易错点",
    "## 下次复习",
    "## 待核对",
]

VALID_STATUS = {"ready", "review"}
VALID_CONFIDENCE = {"high", "medium", "low"}
SOURCE_SUFFIXES = {".md", ".markdown", ".txt"}


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def rel(path: Path) -> str:
    return path.resolve().relative_to(VAULT.resolve()).as_posix()


def yaml_quote(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def yaml_list(values: Any) -> str:
    if values is None or values == "":
        values = []
    if isinstance(values, str):
        values = [values] if values.strip() else []
    if not isinstance(values, list):
        values = [str(values)]
    items = [str(item).strip() for item in values if str(item).strip()]
    if not items:
        return "[]"
    return "\n" + "\n".join(f"  - {yaml_quote(item)}" for item in items)


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
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


def safe_name(value: str, default: str = "未命名") -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value.strip())
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value[:80] or default


def source_hash(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def strip_code_fence(text: str) -> str:
    text = text.strip()
    match = re.fullmatch(r"```(?:markdown|md)?\s*(.*?)\s*```", text, re.S | re.I)
    return match.group(1).strip() if match else text


def ensure_structure() -> None:
    for path in [INBOX, CONVERSATION_INBOX, NOTE_INBOX, PROBLEM_REVIEW_INBOX, OUTPUT_ROOT, ARCHIVE_ROOT, RUN_ROOT, TEMPLATE_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def read_manifest() -> dict[str, Any]:
    if not MANIFEST.exists():
        return {"lessons": [], "problems": []}
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def build_lesson_context(data: dict[str, Any]) -> str:
    lessons = data.get("lessons", [])
    lines = []
    for lesson in lessons:
        lines.append(
            "- {lesson_id} | module_id={module_id} | module={module} | topic={topic} | title={title}".format(
                lesson_id=lesson.get("lesson_id", ""),
                module_id=lesson.get("module_id", ""),
                module=lesson.get("module", ""),
                topic=lesson.get("topic", ""),
                title=lesson.get("display_title", ""),
            )
        )
    return "\n".join(lines)


def find_related_problem_context(text: str, data: dict[str, Any], limit: int = 12) -> str:
    problems = {str(item.get("problem_id")): item for item in data.get("problems", [])}
    ids = []
    for match in re.finditer(r"\b\d{1,2}-\d{1,2}-\d{1,3}\b", text):
        problem_id = match.group(0)
        if problem_id in problems and problem_id not in ids:
            ids.append(problem_id)
    rows = []
    for problem_id in ids[:limit]:
        problem = problems[problem_id]
        content = re.sub(r"\s+", " ", str(problem.get("content", "")).strip())[:220]
        rows.append(
            "- {pid} | {lesson} | {kind} | {content}".format(
                pid=problem_id,
                lesson=problem.get("lesson_title", ""),
                kind=problem.get("kind", ""),
                content=content,
            )
        )
    return "\n".join(rows) if rows else "未在原文中识别到明确题号。"


def path_is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def infer_source_kind(source_path: Path, text: str) -> str:
    lower_name = source_path.name.lower()
    sample = text[:2000].lower()
    if path_is_relative_to(source_path, CONVERSATION_INBOX):
        return "AI对话"
    if path_is_relative_to(source_path, PROBLEM_REVIEW_INBOX):
        return "题解复盘"
    if any(token in lower_name for token in ["gemini", "chat", "对话", "conversation"]):
        return "AI对话"
    if any(token in sample for token in ["gemini", "user:", "assistant:", "用户：", "助手：", "model:"]):
        return "AI对话"
    if any(token in lower_name for token in ["错题", "复盘", "题解", "problem"]):
        return "题解复盘"
    return "普通笔记"


def suggested_source_type(source_kind: str) -> str:
    if source_kind == "AI对话":
        return "conversation"
    if source_kind == "题解复盘":
        return "problem_review"
    return "note"


def build_prompt(source_path: Path, text: str, data: dict[str, Any]) -> str:
    fm, body = parse_frontmatter(text)
    body = body.strip() or text.strip()
    lesson_context = build_lesson_context(data)
    related_context = find_related_problem_context(text, data)
    source_rel = rel(source_path)
    source_kind = infer_source_kind(source_path, text)
    source_type = suggested_source_type(source_kind)
    fm_json = json.dumps(fm, ensure_ascii=False, indent=2)
    today = dt.date.today().isoformat()
    required = "\n".join(REQUIRED_HEADERS)
    return f"""你是高中数学 Obsidian 笔记整理助手，正在把用户的一节学习材料整理成统一格式的标准笔记。

当前来源类型：{source_kind}
推荐 source_type：{source_type}

目标：
- 从原文中提炼真正可复习、可检索、可迁移的知识。
- 尽量匹配现有 Obsidian 题库的 module、lesson、topic。
- 保留用户自己的表达、疑问和错因，但要整理得更清楚。
- 不要编造题目来源、题号、图片细节或用户没有写出的结论。
- 如果内容不足以确定分类或结论，把 status 写成 review，并在“待核对”中列清楚。
- 如果来源是 AI 对话，把它视为“学习过程记录”，不要照搬对话；要提炼用户真正卡住的点、AI 给出的有效提示、最终可复习结论、仍需核对的内容。
- 如果对话里有多个问题，优先整理成一份本节主笔记；把值得拆成错题或方法卡的内容列入“待核对”。
- AI 对话中的结论不默认全对；涉及关键答案、证明、题号、图片信息时，能核对就核对，不能核对就写入“待核对”。

输出格式必须严格遵守：
1. 第一行必须是 `NOTE_META_JSON: {{...}}`，后面接一行合法 JSON，不要换行。
2. JSON 字段必须包含：
   title, source_type, note_kind, status, module_id, module, lesson_id, topic,
   classification_confidence, knowledge_points, methods, related_problem_ids, quality_flags
3. status 只能是 ready 或 review。
4. classification_confidence 只能是 high、medium、low。
5. source_type 可用 conversation、note、mixed、problem_review；本材料优先使用 `{source_type}`。
6. note_kind 可用 知识整理、方法卡片、错因复盘、题解复盘、对话总结、待分类。
7. JSON 后正文不要写一级标题，必须按下面标题顺序输出，标题一个都不能少：
{required}
8. 公式使用 Obsidian 可识别 LaTeX：行内 `\\( ... \\)`，独立公式 `\\[ ... \\]`。
9. “例题关联”里如果能关联题库题号，写成 `[[01_题目/...|题号]]` 的形式；如果不知道路径，只写题号并说明待核对。
10. “下次复习”要给出可执行动作：重做哪道题、先看哪句提醒、做哪类迁移题。
11. 今天日期是 {today}，不要把今天日期写成知识内容。

现有题库分类清单：
{lesson_context}

原文中已识别的题号线索：
{related_context}

来源文件：
{source_rel}

来源 frontmatter：
{fm_json}

原始 md 内容：
<<<SOURCE_MD
{body}
SOURCE_MD
"""


def api_key(prefer_deepseek: bool = True) -> str:
    names = ("DEEPSEEK_API_KEY", "ANTHROPIC_AUTH_TOKEN") if prefer_deepseek else ("ANTHROPIC_AUTH_TOKEN", "DEEPSEEK_API_KEY")
    key = next((os.environ.get(name) for name in names if os.environ.get(name)), "")
    if not key:
        raise RuntimeError(
            "没有找到 ANTHROPIC_AUTH_TOKEN 或 DEEPSEEK_API_KEY。"
            "如果你的 DeepSeek v4 Pro 只接在 Claude Code 里，请先用 prompts 命令生成提示词。"
        )
    return key


def call_deepseek_openai(prompt: str, model: str, max_tokens: int, timeout: int, temperature: float) -> str:
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "thinking": {"type": THINKING_MODE},
        "messages": [
            {"role": "system", "content": "你只输出符合要求的中文 Obsidian Markdown 标准笔记，不输出闲聊或解释。"},
            {"role": "user", "content": prompt},
        ],
    }
    if THINKING_MODE == "enabled":
        body["reasoning_effort"] = REASONING_EFFORT
    else:
        body["temperature"] = temperature
    data = json.dumps(body, ensure_ascii=True).encode("utf-8")
    req = urllib.request.Request(OPENAI_API_URL, data=data, method="POST")
    req.add_header("content-type", "application/json; charset=utf-8")
    req.add_header("authorization", "Bearer " + api_key(prefer_deepseek=True))
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    parts = []
    for choice in payload.get("choices", []):
        message = choice.get("message") or {}
        if message.get("content"):
            parts.append(message["content"])
    return "\n\n".join(part for part in parts if part).strip()


def call_deepseek_anthropic(prompt: str, model: str, max_tokens: int, timeout: int, temperature: float) -> str:
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "thinking": {"type": THINKING_MODE},
        "system": "你只输出符合要求的中文 Obsidian Markdown 标准笔记，不输出闲聊或解释。",
        "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
    }
    if THINKING_MODE == "enabled":
        body["output_config"] = {"effort": REASONING_EFFORT}
    else:
        body["temperature"] = temperature
    data = json.dumps(body, ensure_ascii=True).encode("utf-8")
    req = urllib.request.Request(ANTHROPIC_API_URL, data=data, method="POST")
    req.add_header("content-type", "application/json; charset=utf-8")
    req.add_header("anthropic-version", "2023-06-01")
    req.add_header("x-api-key", api_key(prefer_deepseek=False))
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    parts = []
    for block in payload.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n\n".join(part for part in parts if part).strip()


def call_deepseek(prompt: str, model: str, max_tokens: int, timeout: int, temperature: float) -> str:
    if API_STYLE == "anthropic":
        return call_deepseek_anthropic(prompt, model, max_tokens, timeout, temperature)
    return call_deepseek_openai(prompt, model, max_tokens, timeout, temperature)


def parse_model_output(text: str) -> tuple[dict[str, Any], str]:
    text = strip_code_fence(text)
    match = re.search(r"(?m)^\s*NOTE_META_JSON\s*[:：]\s*(\{.*\})\s*$", text)
    if not match:
        raise RuntimeError("模型输出缺少 NOTE_META_JSON 第一行")
    meta = json.loads(match.group(1))
    body = (text[: match.start()] + text[match.end() :]).strip()

    first_header = None
    for header in REQUIRED_HEADERS:
        index = body.find(header)
        if index != -1:
            first_header = index if first_header is None else min(first_header, index)
    if first_header is not None:
        body = body[first_header:].strip()
    return meta, body


def validate_model_note(meta: dict[str, Any], body: str) -> list[str]:
    issues: list[str] = []
    for key in [
        "title",
        "source_type",
        "note_kind",
        "status",
        "module_id",
        "module",
        "lesson_id",
        "topic",
        "classification_confidence",
        "knowledge_points",
        "methods",
        "related_problem_ids",
        "quality_flags",
    ]:
        if key not in meta:
            issues.append(f"NOTE_META_JSON 缺少字段：{key}")

    status = str(meta.get("status", "")).strip()
    if status and status not in VALID_STATUS:
        issues.append(f"status 应为 ready/review：{status}")

    confidence = str(meta.get("classification_confidence", "")).strip()
    if confidence and confidence not in VALID_CONFIDENCE:
        issues.append(f"classification_confidence 应为 high/medium/low：{confidence}")

    last = -1
    for header in REQUIRED_HEADERS:
        index = body.find(header)
        if index == -1:
            issues.append(f"正文缺少小节：{header}")
        elif index < last:
            issues.append(f"正文小节顺序错误：{header}")
        else:
            last = index
    if len(body) < 300:
        issues.append("正文过短，可能没有完成整理")
    return issues


def infer_output_path(meta: dict[str, Any], source_path: Path, digest: str) -> Path:
    title = safe_name(str(meta.get("title") or source_path.stem), source_path.stem)
    module_id = safe_name(str(meta.get("module_id") or ""), "")
    module = safe_name(str(meta.get("module") or ""), "")
    lesson_id = safe_name(str(meta.get("lesson_id") or ""), "")
    topic = safe_name(str(meta.get("topic") or ""), "")

    if module_id and module:
        folder = OUTPUT_ROOT / f"{module_id}_{module}"
        if lesson_id:
            folder = folder / safe_name(f"{lesson_id}_{topic or '未命名'}")
    elif module:
        folder = OUTPUT_ROOT / safe_name(module)
    else:
        folder = OUTPUT_ROOT / "00_待分类"

    note_id = f"AI-{digest[:8]}"
    return folder / f"{note_id}_{title}.md"


def build_final_note(meta: dict[str, Any], body: str, source_path: Path, digest: str) -> str:
    today = dt.date.today().isoformat()
    title = str(meta.get("title") or source_path.stem).strip() or source_path.stem
    status = str(meta.get("status") or "review").strip()
    if status not in VALID_STATUS:
        status = "review"

    module_id = str(meta.get("module_id") or "").strip()
    lesson_id = str(meta.get("lesson_id") or "").strip()
    tags = ["AI整理笔记", "高中数学"]
    if module_id:
        tags.append(f"module/{module_id}")
    if lesson_id:
        tags.append(f"lesson/{lesson_id}")

    source_rel = rel(source_path)
    frontmatter = (
        "---\n"
        'type: "standard_note"\n'
        f"note_id: {yaml_quote(f'AI-{digest[:8]}')}\n"
        f"source_type: {yaml_quote(meta.get('source_type', 'mixed'))}\n"
        f"note_kind: {yaml_quote(meta.get('note_kind', '待分类'))}\n"
        f"status: {yaml_quote(status)}\n"
        f"title: {yaml_quote(title)}\n"
        f"module_id: {yaml_quote(module_id)}\n"
        f"module: {yaml_quote(meta.get('module', ''))}\n"
        f"lesson_id: {yaml_quote(lesson_id)}\n"
        f"topic: {yaml_quote(meta.get('topic', ''))}\n"
        f"classification_confidence: {yaml_quote(meta.get('classification_confidence', 'low'))}\n"
        f"source_hash: {yaml_quote(digest)}\n"
        f"source_files:{yaml_list([source_rel])}\n"
        f"related_problem_ids:{yaml_list(meta.get('related_problem_ids'))}\n"
        f"knowledge_points:{yaml_list(meta.get('knowledge_points'))}\n"
        f"methods:{yaml_list(meta.get('methods'))}\n"
        f"quality_flags:{yaml_list(meta.get('quality_flags'))}\n"
        f"created: {yaml_quote(today)}\n"
        f"updated: {yaml_quote(today)}\n"
        f"tags:{yaml_list(tags)}\n"
        "---\n\n"
    )
    meta_line = (
        f"> 来源：[[{source_rel}|{source_path.name}]]  \n"
        f"> 分类：{meta.get('module', '待分类')} / {lesson_id or '待分类'} {meta.get('topic', '')}  \n"
        f"> 状态：`{status}`，分类置信度：`{meta.get('classification_confidence', 'low')}`\n\n"
    )
    return frontmatter + f"# {title}\n\n" + meta_line + body.strip() + "\n"


def load_existing_hashes() -> dict[str, Path]:
    result: dict[str, Path] = {}
    if not OUTPUT_ROOT.exists():
        return result
    for path in OUTPUT_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_frontmatter(text)
        digest = str(fm.get("source_hash") or "").strip()
        if digest:
            result[digest] = path
    return result


def resolve_source(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = VAULT / path
    return path.resolve()


def collect_sources(source: str | None, limit: int = 0) -> list[Path]:
    if source:
        root = resolve_source(source)
        if root.is_file():
            files = [root]
        else:
            files = [path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES]
    else:
        files = [path for path in INBOX.rglob("*") if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES]
    files = [path for path in sorted(files) if not path.name.lower().startswith("readme")]
    return files[:limit] if limit else files


def source_status(path: Path, existing: dict[str, Path]) -> str:
    digest = source_hash(path)
    return f"已整理 -> [[{rel(existing[digest])}|标准笔记]]" if digest in existing else "待整理"


def render_intake_index(sources: list[Path], existing: dict[str, Path]) -> str:
    rows = []
    for path in sources:
        text = path.read_text(encoding="utf-8", errors="replace")
        kind = infer_source_kind(path, text)
        digest = source_hash(path)
        rows.append(
            [
                f"[[{rel(path)}|{path.name}]]",
                kind,
                round(path.stat().st_size / 1024, 1),
                digest[:8],
                source_status(path, existing),
                "生成提示词" if digest not in existing else "可归档原始对话",
            ]
        )
    return f"""# 对话导入清单

本页由 `tools/ai_note_manager.py intake` 生成，用来检查每节 AI 对话、草稿和题解复盘是否已经进入标准笔记系统。

## 使用方式

1. 每节课或每组题只放一个导出文件到 `01_待整理/00_AI对话导入入口`。
2. 文件名建议：`10-3_数列特征根_2026-05-31_AI对话.md`。
3. 运行 `python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口`。
4. 用生成的提示词让 DeepSeek v4 Pro 整理，写入 `02_标准笔记`。
5. 运行 `python tools/ai_note_manager.py index`，再运行总维护刷新错题和题库联动。

## 当前待整理材料

{markdown_table(["来源文件", "类型", "大小KB", "指纹", "状态", "下一步"], rows)}
"""


def command_intake(args: argparse.Namespace) -> int:
    ensure_structure()
    sources = collect_sources(args.source, args.limit)
    existing = load_existing_hashes()
    write_text(INTAKE_NOTE, render_intake_index(sources, existing))
    print(f"对话导入清单已刷新：{INTAKE_NOTE}")
    return 0


def render_prompt_file(source_path: Path, prompt: str) -> str:
    source_kind = infer_source_kind(source_path, source_path.read_text(encoding="utf-8", errors="replace"))
    return f"""# Claude Code / DeepSeek v4 Pro 整理提示词

把下面整段提示词交给你已经接好 DeepSeek v4 Pro 的 Claude Code。模型输出后，应保存为一份标准笔记；如果你希望完全自动保存，可以让 Claude Code 按 `NOTE_META_JSON` 和正文内容写入 `08_AI笔记管理/02_标准笔记`。

来源文件：`{rel(source_path)}`
来源类型：`{source_kind}`

建议：一节 AI 对话通常整理成一份本节主笔记；如果里面出现明确错题、方法套路或待核对结论，在“待核对”里列出拆分建议，后续再单独转错题或方法卡。

---

{prompt}
"""


def command_prompts(args: argparse.Namespace) -> int:
    ensure_structure()
    data = read_manifest()
    sources = collect_sources(args.source, args.limit)
    if not sources:
        print("01_待整理 里暂时没有可生成提示词的 md/txt 文件。")
        return 0
    existing = load_existing_hashes()
    skipped = []
    pending = []
    for source_path in sources:
        digest = source_hash(source_path)
        if not getattr(args, "force", False) and digest in existing:
            skipped.append({"source": rel(source_path), "existing_note": rel(existing[digest]), "source_hash": digest})
        else:
            pending.append((source_path, digest))
    if not pending:
        print(f"没有需要生成提示词的新增材料；已跳过 {len(skipped)} 个已整理文件。")
        return 0
    prompt_dir = RUN_ROOT / "prompts" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    prompt_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for source_path, digest in pending:
        text = source_path.read_text(encoding="utf-8", errors="replace")
        prompt = build_prompt(source_path, text, data)
        file_name = f"{safe_name(source_path.stem)}-{digest[:8]}.prompt.md"
        prompt_path = prompt_dir / file_name
        write_text(prompt_path, render_prompt_file(source_path, prompt))
        generated.append(
            {
                "source": rel(source_path),
                "prompt": rel(prompt_path),
                "source_hash": digest,
                "source_kind": infer_source_kind(source_path, text),
            }
        )
    write_text(
        prompt_dir / "README.md",
        f"""# 本次提示词

这些文件是给 Claude Code / DeepSeek v4 Pro 用的整理提示词。每个 prompt 对应一份原始 md/txt。

- 生成数量：{len(generated)}
- 跳过已整理：{len(skipped)}
- 批次清单：[[prompt_manifest.json]]
""",
    )
    write_text(
        prompt_dir / "prompt_manifest.json",
        json.dumps(
            {
                "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
                "generated": generated,
                "skipped": skipped,
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    print(f"已生成 {len(generated)} 份提示词：{prompt_dir}；跳过已整理 {len(skipped)} 个。")
    return 0


def process_one(source_path: Path, args: argparse.Namespace, data: dict[str, Any], existing: dict[str, Path]) -> tuple[str, str]:
    digest = source_hash(source_path)
    if not args.force and digest in existing:
        return "skip", f"{rel(source_path)} 已整理过 -> {rel(existing[digest])}"

    text = source_path.read_text(encoding="utf-8", errors="replace")
    prompt = build_prompt(source_path, text, data)
    raw = call_deepseek(
        prompt=prompt,
        model=args.model,
        max_tokens=args.max_tokens,
        timeout=args.timeout,
        temperature=args.temperature,
    )
    meta, body = parse_model_output(raw)
    issues = validate_model_note(meta, body)
    if issues:
        meta.setdefault("quality_flags", [])
        flags = as_list(meta["quality_flags"]) + issues
        meta["quality_flags"] = flags
        meta["status"] = "review"

    out_path = infer_output_path(meta, source_path, digest)
    note_text = build_final_note(meta, body, source_path, digest)
    if out_path.exists() and not args.force:
        out_path = out_path.with_name(f"{out_path.stem}-{dt.datetime.now().strftime('%H%M%S')}{out_path.suffix}")
    write_text(out_path, note_text)
    return "done" if not issues else "review", f"{rel(source_path)} -> {rel(out_path)}"


def command_run(args: argparse.Namespace) -> int:
    ensure_structure()
    data = read_manifest()
    sources = collect_sources(args.source, args.limit)
    if not sources:
        print("01_待整理 里暂时没有可整理的 md/txt 文件。")
        return 0
    existing = load_existing_hashes()
    run_log = RUN_ROOT / "api_runs" / f"run-{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.jsonl"
    totals = {"done": 0, "review": 0, "skip": 0, "failed": 0}
    for index, source_path in enumerate(sources, start=1):
        started = time.time()
        try:
            kind, message = process_one(source_path, args, data, existing)
            totals[kind] = totals.get(kind, 0) + 1
            record = {"source": rel(source_path), "result": kind, "message": message, "seconds": round(time.time() - started, 2)}
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            totals["failed"] += 1
            record = {"source": rel(source_path), "result": "failed", "error": f"HTTP {e.code}: {body[:500]}"}
        except Exception as e:  # noqa: BLE001
            totals["failed"] += 1
            record = {"source": rel(source_path), "result": "failed", "error": f"{type(e).__name__}: {e}"}
        with run_log.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"[{index}/{len(sources)}] {record.get('result')}: {record.get('message') or record.get('error')}")

    render_indexes()
    print(f"完成：{json.dumps(totals, ensure_ascii=False)}")
    return 0 if totals["failed"] == 0 else 2


def scan_standard_notes() -> tuple[list[dict[str, Any]], list[str]]:
    notes: list[dict[str, Any]] = []
    issues: list[str] = []
    if not OUTPUT_ROOT.exists():
        return notes, issues
    seen_ids: dict[str, str] = {}
    for path in sorted(OUTPUT_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if fm.get("type") != "standard_note":
            continue
        note_id = str(fm.get("note_id") or "").strip()
        file_rel = rel(path)
        fm["_file"] = file_rel
        fm["_path"] = path
        fm["_title"] = str(fm.get("title") or path.stem)
        notes.append(fm)
        if not note_id:
            issues.append(f"{file_rel} 缺少 note_id")
        elif note_id in seen_ids:
            issues.append(f"{file_rel} 与 {seen_ids[note_id]} 的 note_id 重复：{note_id}")
        else:
            seen_ids[note_id] = file_rel
        for field in ["status", "title", "module", "topic", "classification_confidence", "source_hash"]:
            if not str(fm.get(field) or "").strip():
                issues.append(f"{file_rel} 缺少字段：{field}")
        status = str(fm.get("status") or "")
        if status not in VALID_STATUS:
            issues.append(f"{file_rel} status 不推荐：{status}")
        confidence = str(fm.get("classification_confidence") or "")
        if confidence not in VALID_CONFIDENCE:
            issues.append(f"{file_rel} classification_confidence 不推荐：{confidence}")
        for header in REQUIRED_HEADERS:
            if header not in body:
                issues.append(f"{file_rel} 缺少正文小节：{header}")
    return notes, issues


def inbox_stats(existing: dict[str, Path] | None = None) -> dict[str, Any]:
    existing = existing if existing is not None else load_existing_hashes()
    files = collect_sources(None)
    kind_counts = Counter()
    pending = 0
    processed = 0
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        kind_counts[infer_source_kind(path, text)] += 1
        if source_hash(path) in existing:
            processed += 1
        else:
            pending += 1
    return {
        "total": len(files),
        "pending": pending,
        "processed": processed,
        "kindCounts": dict(kind_counts),
    }


def known_problem_ids(data: dict[str, Any]) -> set[str]:
    return {str(problem.get("problem_id") or "") for problem in data.get("problems", []) if str(problem.get("problem_id") or "").strip()}


def existing_wrong_source_problem_ids() -> set[str]:
    result: set[str] = set()
    if not WRONG_DIR.exists():
        return result
    for path in WRONG_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_frontmatter(text)
        if fm.get("type") != "wrong_problem":
            continue
        source_id = str(fm.get("source_problem_id") or "").strip()
        if source_id:
            result.add(source_id)
    return result


def note_body(note: dict[str, Any]) -> str:
    path = note.get("_path")
    if isinstance(path, Path) and path.exists():
        text = path.read_text(encoding="utf-8", errors="replace")
        _, body = parse_frontmatter(text)
        return body
    return ""


def conversion_analysis(notes: list[dict[str, Any]], data: dict[str, Any]) -> dict[str, Any]:
    problem_ids = known_problem_ids(data)
    wrong_source_ids = existing_wrong_source_problem_ids()
    needs_review: list[dict[str, Any]] = []
    missing_problem_links: list[dict[str, Any]] = []
    wrong_candidates: list[dict[str, Any]] = []
    method_candidates: list[dict[str, Any]] = []
    invalid_problem_links: list[dict[str, Any]] = []

    for note in notes:
        body = note_body(note)
        related = as_list(note.get("related_problem_ids"))
        methods = as_list(note.get("methods"))
        quality_flags = as_list(note.get("quality_flags"))
        status = str(note.get("status") or "")
        confidence = str(note.get("classification_confidence") or "")
        kind = str(note.get("note_kind") or "")
        title = str(note.get("_title") or "")
        file = str(note.get("_file") or "")

        if status == "review" or confidence in {"low", ""} or quality_flags:
            needs_review.append(
                {
                    "title": title,
                    "file": file,
                    "status": status,
                    "confidence": confidence,
                    "reason": "；".join(quality_flags) if quality_flags else "状态或分类置信度需要人工确认",
                }
            )

        if not related:
            missing_problem_links.append(
                {
                    "title": title,
                    "file": file,
                    "module": str(note.get("module") or ""),
                    "lesson_id": str(note.get("lesson_id") or ""),
                    "topic": str(note.get("topic") or ""),
                    "suggestion": "补 related_problem_ids；如果没有明确题号，就在例题关联写待核对",
                }
            )
        else:
            bad_ids = [item for item in related if item and item not in problem_ids]
            if bad_ids:
                invalid_problem_links.append(
                    {
                        "title": title,
                        "file": file,
                        "problem_ids": "、".join(bad_ids),
                        "suggestion": "题号不在二轮题库 manifest 中，确认是否来自五年经典或手动题",
                    }
                )

        wrong_signals = ["错因", "误选", "不会", "卡住", "做错", "漏选", "下次重做", "防错"]
        already_in_wrong_bank = bool(related) and all(item in wrong_source_ids for item in related if item)
        wrong_signal_hit = kind in {"错因复盘", "题解复盘"} or (kind != "方法卡片" and any(signal in body for signal in wrong_signals))
        if wrong_signal_hit and not already_in_wrong_bank:
            wrong_candidates.append(
                {
                    "title": title,
                    "file": file,
                    "kind": kind,
                    "related": "、".join(related) or "暂无",
                    "suggestion": "适合检查是否需要转入个人错题库",
                }
            )

        if methods and kind != "方法卡片":
            method_candidates.append(
                {
                    "title": title,
                    "file": file,
                    "kind": kind,
                    "methods": "、".join(methods[:5]),
                    "suggestion": "若方法可复用，拆成方法卡片并关联题号",
                }
            )

    return {
        "needsReview": needs_review,
        "missingProblemLinks": missing_problem_links,
        "invalidProblemLinks": invalid_problem_links,
        "wrongCandidates": wrong_candidates,
        "methodCandidates": method_candidates,
        "summary": {
            "needsReview": len(needs_review),
            "missingProblemLinks": len(missing_problem_links),
            "invalidProblemLinks": len(invalid_problem_links),
            "wrongCandidates": len(wrong_candidates),
            "methodCandidates": len(method_candidates),
        },
    }


def render_conversion_dashboard(analysis: dict[str, Any]) -> str:
    summary = analysis["summary"]
    review_rows = [
        [f"[[{item['file']}|{item['title']}]]", item["status"], item["confidence"], item["reason"]]
        for item in analysis["needsReview"]
    ]
    missing_rows = [
        [f"[[{item['file']}|{item['title']}]]", item["module"], item["lesson_id"], item["topic"], item["suggestion"]]
        for item in analysis["missingProblemLinks"]
    ]
    invalid_rows = [
        [f"[[{item['file']}|{item['title']}]]", item["problem_ids"], item["suggestion"]]
        for item in analysis["invalidProblemLinks"]
    ]
    wrong_rows = [
        [f"[[{item['file']}|{item['title']}]]", item["kind"], item["related"], item["suggestion"]]
        for item in analysis["wrongCandidates"]
    ]
    method_rows = [
        [f"[[{item['file']}|{item['title']}]]", item["kind"], item["methods"], item["suggestion"]]
        for item in analysis["methodCandidates"]
    ]
    return f"""# AI 笔记转化看板

本页由 `tools/ai_note_manager.py index` 生成，用来把标准笔记继续转化成可复习资产。

## 总览

| 项目 | 数量 |
| --- | ---: |
| 需要人工核对 | {summary["needsReview"]} |
| 缺少题号关联 | {summary["missingProblemLinks"]} |
| 题号可能无效 | {summary["invalidProblemLinks"]} |
| 候选错题 | {summary["wrongCandidates"]} |
| 候选方法卡 | {summary["methodCandidates"]} |

## 需要人工核对

{markdown_table(["笔记", "状态", "置信度", "原因"], review_rows)}
## 缺少题号关联

{markdown_table(["笔记", "专题", "讲次", "知识点", "建议"], missing_rows)}
## 题号可能无效

{markdown_table(["笔记", "题号", "建议"], invalid_rows)}
## 候选错题

这些笔记里出现了错因、卡点或题解复盘信号，适合检查是否要转入个人错题库。

{markdown_table(["笔记", "类型", "已关联题号", "建议"], wrong_rows)}
## 候选方法卡

这些笔记有方法标签，但还不是方法卡片。若方法可复用，可以拆成更短的方法卡。

{markdown_table(["笔记", "类型", "方法", "建议"], method_rows)}
"""


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


def render_indexes() -> None:
    ensure_structure()
    data = read_manifest()
    notes, issues = scan_standard_notes()
    existing_hashes = load_existing_hashes()
    sources = collect_sources(None)
    intake = inbox_stats(existing_hashes)
    conversion = conversion_analysis(notes, data)
    today = dt.date.today().isoformat()
    status_counts = Counter(str(note.get("status") or "review") for note in notes)
    kind_counts = Counter(str(note.get("note_kind") or "待分类") for note in notes)
    confidence_counts = Counter(str(note.get("classification_confidence") or "low") for note in notes)
    module_counts = Counter(str(note.get("module") or "待分类") for note in notes)
    rows = []
    for note in sorted(notes, key=lambda item: (str(item.get("module_id") or ""), str(item.get("lesson_id") or ""), str(item.get("_title") or ""))):
        rows.append(
            [
                f"[[{note['_file']}|{note['_title']}]]",
                note.get("note_kind", ""),
                note.get("module", ""),
                note.get("lesson_id", ""),
                note.get("topic", ""),
                note.get("status", ""),
                note.get("classification_confidence", ""),
            ]
        )
    status_rows = [[key, value] for key, value in status_counts.most_common()]
    kind_rows = [[key, value] for key, value in kind_counts.most_common()]
    module_rows = [[key, value] for key, value in module_counts.most_common()]
    index_text = f"""# 标准笔记索引

本页由 `tools/ai_note_manager.py index` 生成。

## 概览

- 更新日期：{today}
- 标准笔记数：{len(notes)}
- 需要检查的问题：{len(issues)}
- 待整理材料：{intake["pending"]} / {intake["total"]}
- 转化待处理：{sum(conversion["summary"].values())}
- 可直接读取的数据：[[08_AI笔记管理/notes_index.json|notes_index.json]]

## 快捷入口

- [[08_AI笔记管理/AI学习流水线|AI学习流水线]]
- [[08_AI笔记管理/对话导入清单|对话导入清单]]
- [[08_AI笔记管理/AI笔记转化看板|AI笔记转化看板]]
- [[08_AI笔记管理/01_待整理/README|待整理入口]]
- [[08_AI笔记管理/01_待整理/00_AI对话导入入口/README|AI对话导入入口]]
- [[08_AI笔记管理/02_标准笔记/README|标准笔记目录]]
- [[08_AI笔记管理/系统体检|系统体检]]
- [[08_AI笔记管理/90_模板/AI对话整理要求|AI对话整理要求]]
- [[08_AI笔记管理/90_模板/标准笔记模板|标准笔记模板]]
- [[08_AI笔记管理/90_模板/ClaudeCode_DeepSeek整理Prompt|Claude Code 整理说明]]

## 状态分布

{markdown_table(["状态", "数量"], status_rows)}
## 笔记类型

{markdown_table(["类型", "数量"], kind_rows)}
## 专题分布

{markdown_table(["专题", "数量"], module_rows)}
## 笔记列表

{markdown_table(["笔记", "类型", "专题", "讲次", "知识点", "状态", "置信度"], rows)}
"""
    write_text(INDEX_NOTE, index_text)
    write_text(INTAKE_NOTE, render_intake_index(sources, existing_hashes))
    write_text(CONVERSION_NOTE, render_conversion_dashboard(conversion))
    write_text(
        INDEX_JSON,
        json.dumps(
            {
                "generatedAt": today,
                "total": len(notes),
                "issueCount": len(issues),
                "statusCounts": dict(status_counts),
                "kindCounts": dict(kind_counts),
                "confidenceCounts": dict(confidence_counts),
                "moduleCounts": dict(module_counts),
                "inbox": intake,
                "conversion": conversion,
                "issues": issues,
                "notes": [
                    {
                        "title": str(note.get("_title") or ""),
                        "file": str(note.get("_file") or ""),
                        "note_id": str(note.get("note_id") or ""),
                        "note_kind": str(note.get("note_kind") or ""),
                        "status": str(note.get("status") or ""),
                        "module_id": str(note.get("module_id") or ""),
                        "module": str(note.get("module") or ""),
                        "lesson_id": str(note.get("lesson_id") or ""),
                        "topic": str(note.get("topic") or ""),
                        "classification_confidence": str(note.get("classification_confidence") or ""),
                    }
                    for note in notes
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    health_rows = [[issue] for issue in issues]
    write_text(
        HEALTH_NOTE,
        f"""# 系统体检

本页由 `tools/ai_note_manager.py index` 生成。

## 结果

- 检查日期：{today}
- 标准笔记数：{len(notes)}
- 问题数：{len(issues)}
- 待整理材料：{intake["pending"]} / {intake["total"]}
- 转化待处理：{sum(conversion["summary"].values())}

## 问题清单

{markdown_table(["说明"], health_rows)}
""",
    )


def command_index(args: argparse.Namespace) -> int:
    render_indexes()
    print("AI 笔记索引已刷新。")
    return 0


def command_init(args: argparse.Namespace) -> int:
    ensure_structure()
    render_indexes()
    print(f"AI 笔记管理目录已准备好：{SYSTEM_ROOT}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI note manager for Obsidian question bank.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="create folders and refresh index")
    sub.add_parser("index", help="refresh AI note index and health check")

    intake_parser = sub.add_parser("intake", help="refresh AI conversation/import intake list")
    intake_parser.add_argument("--source", default="", help="source file/folder relative to vault")
    intake_parser.add_argument("--limit", type=int, default=0)

    prompt_parser = sub.add_parser("prompts", help="generate Claude Code / DeepSeek prompts")
    prompt_parser.add_argument("--source", default="", help="source file/folder relative to vault")
    prompt_parser.add_argument("--limit", type=int, default=0)
    prompt_parser.add_argument("--force", action="store_true", help="generate prompts even for already processed sources")

    run_parser = sub.add_parser("run", help="call DeepSeek API directly and write standard notes")
    run_parser.add_argument("--source", default="", help="source file/folder relative to vault")
    run_parser.add_argument("--limit", type=int, default=0)
    run_parser.add_argument("--force", action="store_true")
    run_parser.add_argument("--model", default=DEFAULT_MODEL)
    run_parser.add_argument("--max-tokens", type=int, default=32768)
    run_parser.add_argument("--timeout", type=int, default=420)
    run_parser.add_argument("--temperature", type=float, default=0.2)

    args = parser.parse_args(argv)
    if not args.command:
        args.command = "init"
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.command == "init":
        return command_init(args)
    if args.command == "intake":
        return command_intake(args)
    if args.command == "prompts":
        return command_prompts(args)
    if args.command == "run":
        return command_run(args)
    if args.command == "index":
        return command_index(args)
    raise RuntimeError(f"未知命令：{args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
