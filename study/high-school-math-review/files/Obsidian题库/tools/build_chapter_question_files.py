# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / "04_原始资料" / "problems.json"
OUT_DIR = VAULT / "06_章节题目合集"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def slug(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]', "-", value.strip())
    value = re.sub(r"\s+", "", value)
    return value[:80]


def clean_problem_text(content: str) -> str:
    lines = content.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    kept: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("【总结】") or stripped in {"总结", "【总结】"}:
            break
        if stripped.startswith("动机:") or stripped.startswith("动机："):
            break
        if stripped.startswith("基本方法:") or stripped.startswith("基本方法："):
            break
        if stripped.startswith("代数技巧"):
            break
        kept.append(line)

    while kept and not kept[0].strip():
        kept.pop(0)
    while kept and not kept[-1].strip():
        kept.pop()

    if kept:
        kept[0] = re.sub(r"^\s*\d{1,3}[\.．、]\s*", "", kept[0]).strip()

    text = "\n".join(kept).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"!\[\[05_附件/images/([^\]|]+)(?:\|[^\]]+)?\]\]", r"![](../05_附件/images/\1)", text)
    return text


def pdf_source_line(problem: dict, lesson: dict) -> str:
    return ""


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lessons = data["lessons"]
    problems = data["problems"]

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    modules: dict[str, list[dict]] = defaultdict(list)
    for problem in problems:
        modules[str(problem["module_id"])].append(problem)

    lesson_lookup = {lesson["lesson_id"]: lesson for lesson in lessons}
    module_names = {}
    for lesson in lessons:
        module_names[str(lesson["module_id"])] = lesson["module"]

    index_lines = ["# 章节题目合集", "", "只保留题号和题目正文，已去掉总结、动机、基本方法、代数技巧等内容。", ""]

    for module_id in sorted(modules, key=lambda x: int(x)):
        module_name = module_names.get(module_id, "")
        filename = f"{int(module_id):02d}_{slug(module_name)}.md"
        rel_path = OUT_DIR / filename
        index_lines.append(f"- [[06_章节题目合集/{filename}|第{module_id}章 {module_name}]]")

        rows = sorted(
            modules[module_id],
            key=lambda p: (
                int(str(p["lesson_id"]).split("-")[0]),
                int(str(p["lesson_id"]).split("-")[1]),
                int(p["source_order"]),
            ),
        )

        output = [f"# 第{module_id}章 {module_name}", ""]
        current_lesson = None
        for problem in rows:
            lesson_id = problem["lesson_id"]
            if lesson_id != current_lesson:
                lesson = lesson_lookup[lesson_id]
                output.extend([f"## {lesson_id} {lesson['topic']}", ""])
                current_lesson = lesson_id

            text = clean_problem_text(problem["content"])
            if not text:
                continue
            source_line = pdf_source_line(problem, lesson_lookup[lesson_id])
            if source_line:
                output.extend([f"### {problem['problem_id']}", "", source_line, "", text, ""])
            else:
                output.extend([f"### {problem['problem_id']}", "", text, ""])

        write_text(rel_path, "\n".join(output).rstrip() + "\n")

    write_text(OUT_DIR / "README.md", "\n".join(index_lines).rstrip() + "\n")
    print(f"已生成 {len(modules)} 个章节题目文件：{OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
