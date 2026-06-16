# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
INBOX = VAULT / "99_上传入口"
MANIFEST = VAULT / "04_原始资料" / "problems.json"
ATTACH_ROOT = VAULT / "05_附件" / "解答附件"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    data: dict[str, str] = {}
    if not match:
        return data, text
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data, text[match.end():]


def find_problem_id(path: Path, text: str | None = None) -> tuple[str | None, str]:
    name_match = re.search(r"(\d{1,2}-\d{1,2}-\d{1,3})", path.stem)
    if name_match:
        return name_match.group(1), "filename"
    if text:
        fm, _ = strip_frontmatter(text)
        for key in ("problem_id", "题号", "编号"):
            if key in fm:
                return fm[key], "frontmatter"
        body_match = re.search(r"(?:problem_id|题号|编号)\s*[:：]\s*(\d{1,2}-\d{1,2}-\d{1,3})", text)
        if body_match:
            return body_match.group(1), "body"
    return None, "missing"


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = strip_frontmatter(text)
    return fm, body, text


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_text(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def update_problem_status(problem_note: Path, status: str, solution_link: str) -> None:
    text = problem_note.read_text(encoding="utf-8", errors="replace")
    now = dt.datetime.now().isoformat(timespec="seconds")
    if not text.startswith("---\n"):
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        return
    fm = text[4:end].splitlines()
    body = text[end + 5 :]
    wanted = {
        "status": yaml_quote(status),
        "solution": yaml_quote(solution_link),
        "updated": yaml_quote(now),
    }
    seen: set[str] = set()
    new_lines: list[str] = []
    for line in fm:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in wanted and not line.startswith(" "):
            new_lines.append(f"{key}: {wanted[key]}")
            seen.add(key)
        else:
            new_lines.append(line)
    for key, value in wanted.items():
        if key not in seen:
            new_lines.append(f"{key}: {value}")
    write_text(problem_note, "---\n" + "\n".join(new_lines) + "\n---\n" + body)


def append_solution_note(solution_note: Path, problem_id: str, problem_note: Path, content: str, status: str) -> None:
    now = dt.datetime.now().isoformat(timespec="seconds")
    header = (
        "---\n"
        'type: "solution"\n'
        f"problem_id: {yaml_quote(problem_id)}\n"
        f"status: {yaml_quote(status)}\n"
        f"updated: {yaml_quote(now)}\n"
        'tags:\n'
        '  - "我的解答"\n'
        "---\n"
        f"# {problem_id} 我的解答\n\n"
        f"对应题目：[[{rel(problem_note)}|{problem_id}]]\n\n"
    )
    if solution_note.exists():
        existing = solution_note.read_text(encoding="utf-8", errors="replace").rstrip()
        write_text(solution_note, existing + f"\n\n## 上传 {now}\n\n" + content.strip() + "\n")
    else:
        solution_note.parent.mkdir(parents=True, exist_ok=True)
        write_text(solution_note, header + "## 上传 " + now + "\n\n" + content.strip() + "\n")


def import_one(path: Path, problems: dict) -> tuple[bool, str]:
    suffix = path.suffix.lower()
    text = None
    fm: dict[str, str] = {}
    body = ""
    if suffix in {".md", ".markdown", ".txt"}:
        fm, body, text = parse_frontmatter(path)
    problem_id, source = find_problem_id(path, text)
    if not problem_id:
        return False, f"未识别题号：{path.name}"
    if problem_id not in problems:
        return False, f"题号不存在：{problem_id} ({path.name})"

    problem = problems[problem_id]
    problem_note = VAULT / problem["note_path"]
    solution_dir = VAULT / problem["solution_dir"]
    solution_note = VAULT / problem["solution_note"]
    attach_dir = ATTACH_ROOT / problem_id
    attach_dir.mkdir(parents=True, exist_ok=True)
    solution_dir.mkdir(parents=True, exist_ok=True)

    status = fm.get("status", "submitted")
    if status not in {"todo", "submitted", "done", "review", "stuck"}:
        status = "submitted"

    if suffix in {".md", ".markdown", ".txt"}:
        archive_path = attach_dir / path.name
        if archive_path.exists():
            archive_path = attach_dir / f"{path.stem}-{dt.datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        shutil.move(str(path), archive_path)
        content = body.strip() or f"[[{rel(archive_path)}]]"
    else:
        target = attach_dir / path.name
        if target.exists():
            target = attach_dir / f"{path.stem}-{dt.datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        shutil.move(str(path), target)
        if suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}:
            content = f"![[{rel(target)}]]"
        else:
            content = f"[[{rel(target)}|{target.name}]]"

    append_solution_note(solution_note, problem_id, problem_note, content, status)
    solution_link = f"[[{rel(solution_note)}|我的解答]]"
    update_problem_status(problem_note, status, solution_link)
    return True, f"{problem_id} <- {path.name} ({source})"


def main() -> int:
    if not MANIFEST.exists():
        print("找不到 problems.json，请先生成题库。")
        return 1
    data = read_json(MANIFEST)
    problems = {item["problem_id"]: item for item in data["problems"]}
    files = [
        path
        for path in INBOX.rglob("*")
        if path.is_file()
        and not path.name.startswith("README")
        and path.suffix.lower() in {".md", ".markdown", ".txt", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".pdf", ".docx"}
    ]
    if not files:
        print("上传入口里暂时没有可导入的文件。")
        return 0

    ok = 0
    for path in files:
        success, message = import_one(path, problems)
        print(message)
        ok += int(success)

    refresh = VAULT / "tools" / "refresh_progress.py"
    if refresh.exists():
        subprocess.run([sys.executable, str(refresh)], check=False)

    print(f"完成：成功导入 {ok} 个文件，剩余 {len(files) - ok} 个需要检查。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
