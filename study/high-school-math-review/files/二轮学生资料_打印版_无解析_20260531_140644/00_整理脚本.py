from __future__ import annotations

import csv
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from pypdf import PdfReader

from organize_abuer_2025_student_materials import (
    CHAPTER_TITLES,
    Material,
    collect_materials,
    group_materials,
    ordered_groups,
    preferred_lesson_title,
    safe_name,
    write_pdf_for_items,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_STEM = "二轮学生资料_打印版_无解析"
MAX_PRINT_PAGES = 200


@dataclass(frozen=True)
class VolumeDef:
    code: str
    title: str
    chapters: Tuple[int, ...]


VOLUME_DEFS: Tuple[VolumeDef, ...] = (
    VolumeDef("01", "基本不等式与函数", (1, 2)),
    VolumeDef("02", "新定义", (3,)),
    VolumeDef("03", "导数选填", (4,)),
    VolumeDef("04", "导数大题", (5,)),
    VolumeDef("05", "三角函数_解三角形_向量_复数", (6, 7, 8, 11)),
    VolumeDef("06", "数列与立体几何", (9, 10)),
    VolumeDef("07", "解析几何_直线圆与圆锥曲线_补充", (12, 13, 14, 99)),
    VolumeDef("08", "概率统计与排列组合", (15, 16)),
)


def collect_print_materials() -> List[Material]:
    materials = [
        item
        for item in collect_materials()
        if item.kind not in {"解析", "作业解析"}
    ]
    return sorted(materials, key=lambda item: item.sort_key)


def split_items_by_page_limit(items: Sequence[Material]) -> List[List[Material]]:
    chunks: List[List[Material]] = []
    current: List[Material] = []
    current_pages = 0

    for _, group_items in ordered_groups(items):
        group_pages = sum(item.pages for item in group_items)
        if current and current_pages + group_pages > MAX_PRINT_PAGES:
            chunks.append(current)
            current = []
            current_pages = 0
        current.extend(group_items)
        current_pages += group_pages

    if current:
        chunks.append(current)
    return chunks


def material_page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def lesson_print_file_name(items: Sequence[Material]) -> str:
    first = items[0]
    title = preferred_lesson_title(items)
    return safe_name(f"{first.lesson_code}_{title}_讲义作业.pdf")


def write_catalog_markdown(rows: Sequence[Dict[str, object]], output_path: Path) -> None:
    lines = [
        "# 2025阿不二轮学生资料打印版目录",
        "",
        f"生成时间：{datetime.now():%Y-%m-%d %H:%M:%S}",
        "",
        "合并口径：讲义、作业、专项训练、选题。",
        "",
        "已排除：作业解析、普通解析、板书、直播板书、计算基本法【完结】.pdf、内容简介 docx。",
        "",
        "页码为所在分册 PDF 内的页码，从 1 开始。",
        "",
        "## 分册概览",
        "",
        "| 分册 | 页数 | 文件 |",
        "|---|---:|---|",
    ]

    seen = set()
    for row in rows:
        key = row["volume_file"]
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"| {row['volume_title']} | {row['volume_pages']} | {key} |")

    current_volume = None
    for row in rows:
        if row["volume_title"] != current_volume:
            current_volume = row["volume_title"]
            lines.extend(
                [
                    "",
                    f"## {current_volume}",
                    "",
                    "| 课时 | 知识点 | 类型 | 页码 | 原文件 |",
                    "|---|---|---|---:|---|",
                ]
            )
        item: Material = row["material"]  # type: ignore[assignment]
        lines.append(
            f"| {item.lesson_code} | {row['lesson_title']} | {item.kind} | {row['start']}-{row['end']} | {item.rel_path.as_posix()} |"
        )

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_catalog_csv(rows: Sequence[Dict[str, object]], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "分册编号",
                "分册",
                "分册文件",
                "分册页数",
                "模块",
                "课时",
                "知识点",
                "资料类型",
                "分册起始页",
                "分册结束页",
                "原文件",
                "来源相对路径",
            ]
        )
        for row in rows:
            item: Material = row["material"]  # type: ignore[assignment]
            writer.writerow(
                [
                    row["volume_code"],
                    row["volume_title"],
                    row["volume_file"],
                    row["volume_pages"],
                    item.module_title,
                    item.lesson_code,
                    row["lesson_title"],
                    item.kind,
                    row["start"],
                    row["end"],
                    item.source_path.name,
                    str(item.rel_path),
                ]
            )


def write_check_report(
    materials: Sequence[Material],
    volume_files: Sequence[Path],
    output_path: Path,
) -> None:
    grouped = group_materials(materials)
    missing_lines: List[str] = []
    for _, items in ordered_groups(materials):
        kinds = {item.kind for item in items}
        first = items[0]
        missing = []
        if "讲义" not in kinds:
            missing.append("讲义")
        if "作业" not in kinds and first.chapter not in {3, 99}:
            missing.append("作业")
        if missing:
            missing_lines.append(
                f"- {first.lesson_code} {preferred_lesson_title(items)}：缺 {', '.join(missing)}"
            )

    over_limit = []
    for path in volume_files:
        pages = material_page_count(path)
        if pages > MAX_PRINT_PAGES:
            over_limit.append(f"- {path.name}：{pages} 页")

    lines = [
        "二轮学生资料打印版检查",
        "",
        f"纳入资料数：{len(materials)}",
        f"纳入课时/专题数：{len(grouped)}",
        f"纳入页数合计：{sum(item.pages for item in materials)}",
        f"打印分册数：{len(volume_files)}",
        f"单册页数上限：{MAX_PRINT_PAGES}",
        f"页数检查：{'通过' if not over_limit else '有分册超过上限'}",
        "",
        "已排除：作业解析、普通解析、板书、直播板书、计算基本法【完结】.pdf、内容简介 docx。",
        "",
        "超过页数上限的分册：",
    ]
    lines.extend(over_limit or ["- 无"])
    lines.extend(["", "缺项提示（仅检查原资料中是否有讲义和作业；缺项不补造）："])
    lines.extend(missing_lines or ["- 无"])
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_readme(output_dir: Path) -> None:
    text = f"""二轮学生资料打印版_无解析

整理口径：
- 纳入：讲义、作业、专项训练、选题。
- 排除：作业解析、普通解析、板书、直播板书、计算基本法【{chr(23436)}结】.pdf、内容简介 docx。

目录说明：
- 01_打印分册：按知识体系切成适合打印装订的分册，每册尽量不超过 {MAX_PRINT_PAGES} 页。
- 02_按课时小册：备用，每个课时/专题单独合并。
- 00_分册目录.md / .csv：每份资料在对应分册里的页码范围。
- 00_检查.txt：页数上限与缺项检查。
"""
    (output_dir / "00_整理说明.txt").write_text(text, encoding="utf-8")


def copy_script(output_dir: Path) -> None:
    shutil.copy2(Path(__file__), output_dir / "00_整理脚本.py")


def main() -> None:
    materials = collect_print_materials()
    if not materials:
        raise RuntimeError("没有找到可合并的打印版资料。")

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = ROOT / f"{OUTPUT_STEM}_{stamp}"
    volume_dir = output_dir / "01_打印分册"
    lesson_dir = output_dir / "02_按课时小册"
    volume_dir.mkdir(parents=True, exist_ok=True)
    lesson_dir.mkdir(parents=True, exist_ok=True)

    rows: List[Dict[str, object]] = []
    volume_files: List[Path] = []

    by_chapter: Dict[int, List[Material]] = {}
    for item in materials:
        by_chapter.setdefault(item.chapter, []).append(item)

    volume_index = 1
    for volume_def in VOLUME_DEFS:
        volume_items: List[Material] = []
        for chapter in volume_def.chapters:
            volume_items.extend(by_chapter.get(chapter, []))
        volume_items = sorted(volume_items, key=lambda item: item.sort_key)
        if not volume_items:
            continue

        chunks = split_items_by_page_limit(volume_items)
        for part_index, chunk in enumerate(chunks, 1):
            suffix = f"_第{part_index}册" if len(chunks) > 1 else ""
            volume_code = f"{volume_index:02d}"
            volume_title = f"{volume_code}_{volume_def.title}{suffix}"
            volume_path = volume_dir / safe_name(f"{volume_title}.pdf")
            pdf_rows = write_pdf_for_items(chunk, volume_path)
            volume_pages = material_page_count(volume_path)
            volume_files.append(volume_path)

            for row in pdf_rows:
                row.update(
                    {
                        "volume_code": volume_code,
                        "volume_title": volume_title,
                        "volume_file": volume_path.name,
                        "volume_pages": volume_pages,
                    }
                )
                rows.append(row)
            volume_index += 1

    for _, items in ordered_groups(materials):
        first = items[0]
        folder = lesson_dir / safe_name(f"{first.chapter:02d}_{first.module_title}")
        write_pdf_for_items(items, folder / lesson_print_file_name(items), with_group_bookmarks=False)

    write_catalog_markdown(rows, output_dir / "00_分册目录.md")
    write_catalog_csv(rows, output_dir / "00_分册目录.csv")
    write_check_report(materials, volume_files, output_dir / "00_检查.txt")
    write_readme(output_dir)
    copy_script(output_dir)

    print(f"OUTPUT_DIR={output_dir}")
    print(f"MATERIALS={len(materials)}")
    print(f"GROUPS={len(group_materials(materials))}")
    print(f"PAGES={sum(item.pages for item in materials)}")
    print(f"VOLUMES={len(volume_files)}")
    for path in volume_files:
        print(f"{path.name}\t{material_page_count(path)}")


if __name__ == "__main__":
    main()
