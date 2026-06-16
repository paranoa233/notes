# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / "04_原始资料" / "problems.json"
RUN_ROOT = VAULT / "tools" / "deepseek_solution_runs"
API_URL = "https://api.deepseek.com/anthropic/v1/messages"
DEFAULT_MODEL = "deepseek-v4-pro"

REQUIRED_HEADERS = [
    "## 题目勘误",
    "## 思路分析",
    "## 详细解答",
    "## 答案",
    "## 总结",
]

PRINT_LOCK = threading.Lock()
LOG_LOCK = threading.Lock()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    temp.replace(path)


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def load_problems() -> list[dict]:
    data = read_json(MANIFEST)
    return data["problems"]


def extract_problem_body(problem: dict) -> str:
    note = VAULT / problem["note_path"]
    if note.exists():
        text = note.read_text(encoding="utf-8", errors="replace")
        start = re.search(r"(?m)^## 题目\s*$", text)
        if start:
            body = text[start.end() :]
            end = re.search(r"(?m)^## 我的解答\s*$", body)
            if end:
                body = body[: end.start()]
            body = body.strip()
            if body:
                return body
    return str(problem.get("content", "")).strip()


def is_complete_solution(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if not all(header in text for header in REQUIRED_HEADERS):
        return False
    if re.search(r"(?m)^status:\s*[\"']?todo[\"']?\s*$", text):
        return False
    detail = text.split("## 详细解答", 1)[-1].strip()
    is_review = bool(re.search(r"(?m)^status:\s*[\"']?review[\"']?\s*$", text))
    min_detail = 40 if is_review else 180
    return len(detail) >= min_detail and "待补充" not in text[:1200]


def update_problem_status(problem_note: Path, status: str, solution_link: str) -> None:
    if not problem_note.exists():
        return
    text = problem_note.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        return

    now = dt.datetime.now().isoformat(timespec="seconds")
    fm_lines = text[4:end].splitlines()
    body = text[end + 5 :]
    wanted = {
        "status": yaml_quote(status),
        "solution": yaml_quote(solution_link),
        "updated": yaml_quote(now),
    }
    seen: set[str] = set()
    new_lines: list[str] = []
    for line in fm_lines:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in wanted and not line.startswith(" "):
            new_lines.append(f"{key}: {wanted[key]}")
            seen.add(key)
        else:
            new_lines.append(line)
    for key, value in wanted.items():
        if key not in seen:
            new_lines.append(f"{key}: {value}")

    body = re.sub(r"> 状态：`[^`]+`", f"> 状态：`{status}`", body, count=1)
    write_text(problem_note, "---\n" + "\n".join(new_lines) + "\n---\n" + body)


def strip_code_fence(text: str) -> str:
    text = text.strip()
    match = re.fullmatch(r"```(?:markdown|md)?\s*(.*?)\s*```", text, re.S | re.I)
    return match.group(1).strip() if match else text


def normalize_model_output(text: str) -> tuple[str, str]:
    text = strip_code_fence(text)
    status = "done"
    status_match = re.search(r"(?im)^\s*STATUS\s*[:：]\s*(done|review)\s*$", text)
    if status_match:
        status = status_match.group(1).lower()
        text = text[: status_match.start()] + text[status_match.end() :]

    first_header = None
    for header in REQUIRED_HEADERS:
        idx = text.find(header)
        if idx != -1:
            first_header = idx if first_header is None else min(first_header, idx)
    if first_header is not None:
        text = text[first_header:]
    return status, text.strip()


def validate_sections(text: str, status: str) -> bool:
    if not all(header in text for header in REQUIRED_HEADERS):
        return False
    detail = text.split("## 详细解答", 1)[-1].strip()
    min_detail = 40 if status == "review" else 180
    return len(detail) >= min_detail


def build_solution_note(problem: dict, problem_body: str, model_sections: str, status: str) -> str:
    now = dt.datetime.now().isoformat(timespec="seconds")
    problem_id = problem["problem_id"]
    problem_note = VAULT / problem["note_path"]
    solution_rel = rel(VAULT / problem["solution_note"])
    problem_rel = rel(problem_note)
    frontmatter = (
        "---\n"
        'type: "solution"\n'
        f"problem_id: {yaml_quote(problem_id)}\n"
        f"status: {yaml_quote(status)}\n"
        f"updated: {yaml_quote(now)}\n"
        "tags:\n"
        '  - "我的解答"\n'
        '  - "高考数学五年经典"\n'
        "---\n\n"
        f"# {problem_id} 我的解答\n\n"
        f"对应题目：[[{problem_rel}|{problem_id}]]\n\n"
        "## 完整题目\n\n"
        f"{problem_body.strip()}\n\n"
    )
    return frontmatter + model_sections.strip() + "\n"


def build_prompt(problem: dict, problem_body: str) -> str:
    meta = {
        "problem_id": problem.get("problem_id", ""),
        "lesson_title": problem.get("lesson_title", ""),
        "module": problem.get("module", ""),
        "topic": problem.get("topic", ""),
        "section": problem.get("section", ""),
        "kind": problem.get("kind", ""),
        "original_number": problem.get("original_number", ""),
    }
    return f"""你是严谨的高考数学解题老师。请为下面这一道题生成 Obsidian Markdown 解答。

必须遵守：
1. 只输出 Markdown 正文，不要解释你将如何做，不要包代码块。
2. 第一行必须是 `STATUS: done`；如果题目文字或图片信息缺失到无法确定题意，第一行写 `STATUS: review`。
3. 除第一行外，必须且只能按下面标题顺序输出：
## 题目勘误
## 思路分析
## 详细解答
## 答案
## 总结
4. 题目勘误中，如果没有明显 OCR 问题，写“无明显勘误。”；如果有，列出原文、建议更正、理由。
5. 解答要完整：选择题和填空题也要写推理过程；多选题要逐项判断；解答题要分步骤推导。
6. 公式使用 Markdown/Obsidian 可识别的 LaTeX：行内 `\\( ... \\)`，独立公式 `\\[ ... \\]`。
7. 如果题目依赖图片而文本无法完全读出，尽量依据文字解答，并在题目勘误说明“图片信息需人工核对”。
8. 不要编造题目没有给出的图片细节。

题目信息：
{json.dumps(meta, ensure_ascii=False, indent=2)}

完整题目：
{problem_body}
"""


def api_key() -> str:
    key = os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("缺少 ANTHROPIC_AUTH_TOKEN 或 DEEPSEEK_API_KEY")
    return key


def call_deepseek(prompt: str, model: str, max_tokens: int, timeout: int, temperature: float) -> str:
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "system": "你只负责输出高质量中文数学解答 Markdown。不要输出与题目无关的闲聊。",
        "messages": [{"role": "user", "content": prompt}],
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, method="POST")
    req.add_header("content-type", "application/json")
    req.add_header("anthropic-version", "2023-06-01")
    req.add_header("x-api-key", api_key())
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    parts = []
    for block in payload.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n\n".join(part for part in parts if part).strip()


def append_log(path: Path, record: dict) -> None:
    with LOG_LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def solve_one(problem: dict, args: argparse.Namespace, log_path: Path) -> dict:
    problem_id = problem["problem_id"]
    solution_note = VAULT / problem["solution_note"]
    problem_note = VAULT / problem["note_path"]
    solution_link = f"[[{rel(solution_note)}|我的解答]]"

    if not args.force and is_complete_solution(solution_note):
        update_problem_status(problem_note, "done", solution_link)
        return {"problem_id": problem_id, "result": "skip"}

    problem_body = extract_problem_body(problem)
    prompt = build_prompt(problem, problem_body)
    last_error = ""
    raw_text = ""
    for attempt in range(1, args.retries + 1):
        try:
            raw_text = call_deepseek(
                prompt=prompt,
                model=args.model,
                max_tokens=args.max_tokens,
                timeout=args.timeout,
                temperature=args.temperature,
            )
            status, sections = normalize_model_output(raw_text)
            if not validate_sections(sections, status):
                raise RuntimeError("模型输出缺少必要标题或详细解答过短")
            note_text = build_solution_note(problem, problem_body, sections, status)
            write_text(solution_note, note_text)
            update_problem_status(problem_note, status, solution_link)
            result = {"problem_id": problem_id, "result": status, "attempt": attempt}
            append_log(log_path, result)
            return result
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            last_error = f"HTTP {e.code}: {body[:500]}"
        except Exception as e:  # noqa: BLE001 - batch runner must keep going
            last_error = f"{type(e).__name__}: {e}"

        if attempt < args.retries:
            time.sleep(min(90, 2**attempt + random.random() * 3))

    review_sections = (
        "## 题目勘误\n\n"
        "模型批处理未能生成可靠解答，需人工核对。"
        f"\n\n- 失败原因：{last_error}\n\n"
        "## 思路分析\n\n"
        "本题暂未完成自动解析。\n\n"
        "## 详细解答\n\n"
        "本题自动生成失败，说明模型多次返回的内容未通过结构校验，或 API 请求在重试后仍未成功。"
        "建议优先核对原题 OCR、图片与题干是否完整，再重新运行本题或人工补解。\n\n"
        "## 答案\n\n"
        "待人工确认。\n\n"
        "## 总结\n\n"
        "自动解答失败，需复核题目文字、图片或模型输出。\n"
    )
    write_text(solution_note, build_solution_note(problem, problem_body, review_sections, "review"))
    update_problem_status(problem_note, "review", solution_link)
    record = {"problem_id": problem_id, "result": "review", "error": last_error, "raw": raw_text[:1000]}
    append_log(log_path, record)
    return record


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Solve 高考数学五年经典 problems with DeepSeek.")
    parser.add_argument("--start", type=int, default=1, help="1-based start index")
    parser.add_argument("--end", type=int, default=0, help="1-based end index, inclusive; 0 means all")
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--batch-size", type=int, default=400)
    parser.add_argument("--model", default=os.environ.get("DEEPSEEK_MODEL", DEFAULT_MODEL))
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--ids", default="", help="Comma/space separated problem ids to process")
    parser.add_argument("--ids-file", default="", help="UTF-8 text file with one problem id per line")
    parser.add_argument("--only-incomplete", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    problems = load_problems()
    id_filter: list[str] = []
    if args.ids:
        id_filter.extend(part.strip() for part in re.split(r"[\s,;]+", args.ids) if part.strip())
    if args.ids_file:
        id_path = Path(args.ids_file)
        if not id_path.is_absolute():
            id_path = VAULT / id_path
        id_filter.extend(
            line.strip()
            for line in id_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )

    if id_filter:
        wanted = set(id_filter)
        selected = [problem for problem in problems if problem["problem_id"] in wanted]
        missing = [problem_id for problem_id in id_filter if problem_id not in {p["problem_id"] for p in selected}]
        if missing:
            print(f"题号不存在，已忽略：{', '.join(missing)}")
        end = args.end or len(problems)
    else:
        end = args.end or len(problems)
        selected = problems[args.start - 1 : end]

    if args.only_incomplete:
        selected = [
            problem
            for problem in selected
            if not is_complete_solution(VAULT / problem["solution_note"])
        ]

    if args.limit:
        selected = selected[: args.limit]
    if not selected:
        print("没有需要处理的题目。")
        return 0

    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    run_id = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_path = RUN_ROOT / f"run-{run_id}.jsonl"

    print(
        f"开始：{args.start}-{end}，共 {len(selected)} 题，workers={args.workers}，"
        f"batch_size={args.batch_size}，model={args.model}"
    )
    append_log(
        log_path,
        {
            "event": "start",
            "time": dt.datetime.now().isoformat(timespec="seconds"),
            "start": args.start,
            "end": end,
            "count": len(selected),
            "workers": args.workers,
            "model": args.model,
        },
    )

    totals = {"done": 0, "review": 0, "failed": 0, "skip": 0}
    started = time.time()
    completed = 0

    with cf.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(solve_one, problem, args, log_path): problem["problem_id"]
            for problem in selected
        }
        for future in cf.as_completed(futures):
            completed += 1
            problem_id = futures[future]
            try:
                result = future.result()
            except Exception as e:  # noqa: BLE001
                result = {"problem_id": problem_id, "result": "failed", "error": repr(e)}
                append_log(log_path, result)
            kind = result.get("result", "failed")
            if kind in totals:
                totals[kind] += 1
            else:
                totals["failed"] += 1

            if completed % 5 == 0 or kind in {"failed", "review"}:
                elapsed = max(1, int(time.time() - started))
                with PRINT_LOCK:
                    print(
                        f"[{completed}/{len(selected)}] {problem_id}: {kind}; "
                        f"done={totals['done']} review={totals['review']} "
                        f"failed={totals['failed']} skip={totals['skip']} elapsed={elapsed}s"
                    )

    append_log(
        log_path,
        {
            "event": "finish",
            "time": dt.datetime.now().isoformat(timespec="seconds"),
            "totals": totals,
        },
    )
    print(f"完成：{json.dumps(totals, ensure_ascii=False)}")
    return 0 if totals["failed"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
