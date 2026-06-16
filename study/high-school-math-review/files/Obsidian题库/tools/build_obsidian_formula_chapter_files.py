# -*- coding: utf-8 -*-
from __future__ import annotations

import re
import shutil
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
SOURCE_DIR = VAULT / "06_章节题目合集"
OUT_DIR = VAULT / "07_章节题目合集_Obsidian公式版"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def convert_math_delimiters(text: str) -> str:
    parts = split_by_fenced_code(text)
    converted: list[str] = []
    for part, is_code in parts:
        if is_code:
            converted.append(part)
            continue
        part = convert_block_math(part)
        part = convert_inline_math(part)
        converted.append(part)
    return "".join(converted)


def split_by_fenced_code(text: str) -> list[tuple[str, bool]]:
    lines = text.splitlines(keepends=True)
    parts: list[tuple[str, bool]] = []
    buf: list[str] = []
    in_code = False
    for line in lines:
        if line.startswith("```"):
            if buf:
                parts.append(("".join(buf), in_code))
                buf = []
            buf.append(line)
            in_code = not in_code
            parts.append(("".join(buf), not in_code))
            buf = []
            continue
        buf.append(line)
    if buf:
        parts.append(("".join(buf), in_code))
    return parts


def convert_block_math(text: str) -> str:
    def repl(match: re.Match) -> str:
        body = match.group(1).strip()
        return "\n$$\n" + body + "\n$$\n"

    return re.sub(r"\\\[((?:.|\n)*?)\\\]", repl, text)


def convert_inline_math(text: str) -> str:
    def repl(match: re.Match) -> str:
        body = match.group(1).strip()
        body = body.replace("$", r"\$")
        return f"${body}$"

    return re.sub(r"\\\((.*?)\\\)", repl, text)


def main() -> int:
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(SOURCE_DIR)

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    total_inline = 0
    total_block = 0
    for source in sorted(SOURCE_DIR.glob("*.md")):
        text = source.read_text(encoding="utf-8", errors="replace")
        total_inline += len(re.findall(r"\\\(.*?\\\)", text))
        total_block += len(re.findall(r"\\\[((?:.|\n)*?)\\\]", text))
        output = convert_math_delimiters(text)
        if source.name == "README.md":
            output = output.replace("# 章节题目合集", "# 章节题目合集（Obsidian公式版）", 1)
            output = output.replace("[[06_章节题目合集/", "[[07_章节题目合集_Obsidian公式版/")
            output += "\n\n本文件夹专门给 Obsidian 使用：已把 `\\(...\\)` / `\\[...\\]` 转成 `$...$` / `$$...$$`，原始章节合集未改动。\n"
        write_text(OUT_DIR / source.name, output)

    print(f"已生成 Obsidian 公式版：{OUT_DIR}")
    print(f"转换行内公式：{total_inline}")
    print(f"转换块级公式：{total_block}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
