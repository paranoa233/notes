# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "Obsidian题库"
AI_MANAGER = VAULT / "tools" / "ai_note_manager.py"
MAINTAIN = ROOT / "tools" / "maintain_study_systems.py"
AI_ROOT = VAULT / "08_AI笔记管理"
INBOX = AI_ROOT / "01_待整理"

DESTINATIONS = {
    "conversation": INBOX / "00_AI对话导入入口",
    "note": INBOX / "01_普通笔记草稿",
    "review": INBOX / "02_题解复盘",
}
SOURCE_SUFFIXES = {".md", ".markdown", ".txt"}


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def safe_name(value: str) -> str:
    cleaned = "".join("_" if char in '<>:"/\\|?*' else char for char in value)
    cleaned = " ".join(cleaned.strip().split())
    return cleaned.strip(" .") or "未命名"


def resolve_source(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def collect_files(sources: list[str]) -> list[Path]:
    files: list[Path] = []
    for source in sources:
        path = resolve_source(source)
        if not path.exists():
            raise FileNotFoundError(f"来源不存在：{path}")
        if path.is_file():
            if path.suffix.lower() in SOURCE_SUFFIXES and not path.name.lower().startswith("readme"):
                files.append(path)
            continue
        for child in sorted(path.rglob("*")):
            if child.is_file() and child.suffix.lower() in SOURCE_SUFFIXES and not child.name.lower().startswith("readme"):
                files.append(child)
    seen: set[Path] = set()
    unique: list[Path] = []
    for file in files:
        resolved = file.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def short_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]


def copy_into_batch(files: list[Path], kind: str) -> tuple[Path, list[dict[str, Any]]]:
    destination = DESTINATIONS[kind]
    batch_dir = destination / f"batch-{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    batch_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for index, source in enumerate(files, start=1):
        file_name = safe_name(source.name)
        target = batch_dir / file_name
        if target.exists():
            target = batch_dir / f"{target.stem}-{short_hash(source)}{target.suffix}"
        shutil.copy2(source, target)
        records.append(
            {
                "index": index,
                "source": str(source),
                "imported": str(target),
                "sourceHash": short_hash(source),
                "size": source.stat().st_size,
            }
        )
    write_text(
        batch_dir / "batch_manifest.json",
        json.dumps(
            {
                "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
                "kind": kind,
                "files": records,
            },
            ensure_ascii=False,
            indent=2,
        ),
    )
    return batch_dir, records


def rel_to_vault(path: Path) -> str:
    return path.resolve().relative_to(VAULT.resolve()).as_posix()


def run_python(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return subprocess.run(
        [sys.executable, *args],
        cwd=str(cwd),
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )


def direct_api_available() -> bool:
    return bool(os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import local md/txt material and process it through the AI note pipeline.")
    parser.add_argument("sources", nargs="+", help="md/txt file or folder paths, absolute or relative to the study root")
    parser.add_argument("--kind", choices=sorted(DESTINATIONS), default="conversation", help="where to import the material")
    parser.add_argument("--mode", choices=["auto", "run", "prompts", "import-only"], default="auto")
    parser.add_argument("--force", action="store_true", help="reprocess sources even if their hash was seen before")
    parser.add_argument("--limit", type=int, default=0, help="pass through to ai_note_manager")
    parser.add_argument("--skip-maintain", action="store_true", help="do not refresh the root dashboards after direct run")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    files = collect_files(args.sources)
    if not files:
        print("没有找到可处理的 md/txt 文件。")
        return 0

    batch_dir, records = copy_into_batch(files, args.kind)
    source_arg = rel_to_vault(batch_dir)
    mode = args.mode
    if mode == "auto":
        mode = "run" if direct_api_available() else "prompts"

    print(f"已导入 {len(records)} 个文件：{batch_dir}")

    if mode == "import-only":
        proc = run_python([str(AI_MANAGER), "intake", "--source", source_arg], VAULT)
        print(proc.stdout.strip() or proc.stderr.strip())
        return proc.returncode

    manager_args = [str(AI_MANAGER), mode, "--source", source_arg]
    if args.limit:
        manager_args.extend(["--limit", str(args.limit)])
    if args.force:
        manager_args.append("--force")

    proc = run_python(manager_args, VAULT)
    if proc.stdout.strip():
        print(proc.stdout.strip())
    if proc.stderr.strip():
        print(proc.stderr.strip(), file=sys.stderr)
    if proc.returncode != 0:
        print(f"AI 材料处理失败，批次已保留：{batch_dir}", file=sys.stderr)
        return proc.returncode

    if mode == "run" and not args.skip_maintain:
        refresh = run_python([str(MAINTAIN)], ROOT)
        if refresh.stdout.strip():
            print(refresh.stdout.strip())
        if refresh.stderr.strip():
            print(refresh.stderr.strip(), file=sys.stderr)
        if refresh.returncode != 0:
            return refresh.returncode
    elif mode == "prompts":
        intake = run_python([str(AI_MANAGER), "intake", "--source", source_arg], VAULT)
        if intake.stdout.strip():
            print(intake.stdout.strip())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
