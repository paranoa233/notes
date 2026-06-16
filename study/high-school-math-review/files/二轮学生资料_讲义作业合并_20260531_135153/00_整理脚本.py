from __future__ import annotations

import csv
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "二轮配套资料"

OUTPUT_STEM = "二轮学生资料_讲义作业合并"

CHAPTER_TITLES: Dict[int, str] = {
    1: "基本不等式",
    2: "函数",
    3: "新定义",
    4: "导数选填",
    5: "导数大题",
    6: "三角函数",
    7: "解三角形",
    8: "向量",
    9: "立体几何",
    10: "数列",
    11: "复数",
    12: "直线和圆",
    13: "圆锥曲线（难点）",
    14: "圆锥曲线（小题）",
    15: "概率统计",
    16: "排列组合",
    99: "补充资料",
}

KIND_ORDER = {
    "讲义": 1,
    "作业": 2,
    "作业解析": 3,
    "解析": 4,
    "专项训练": 5,
    "选题": 6,
}

PREFIX_RE = re.compile(r"^\s*(?P<chapter>\d+)-(?P<lesson>\d+)\s*(?P<title>.*?)(?:-(?P<suffix>作业解析|作业|解析|讲义))?\.pdf$", re.I)


@dataclass(frozen=True)
class Material:
    source_path: Path
    rel_path: Path
    chapter: int
    lesson: int
    item_order: int
    lesson_code: str
    module_title: str
    title: str
    kind: str
    kind_order: int
    pages: int

    @property
    def sort_key(self) -> Tuple[int, int, int, int, str]:
        return (self.chapter, self.lesson, self.item_order, self.kind_order, self.source_path.name)

    @property
    def group_key(self) -> Tuple[int, int, int]:
        return (self.chapter, self.lesson, 0)


def safe_name(text: str) -> str:
    text = re.sub(r'[<>:"/\\|?*]', "_", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip(". ")


def detect_kind(name: str) -> str:
    if "作业解析" in name:
        return "作业解析"
    if "作业" in name:
        return "作业"
    if "解析" in name:
        return "解析"
    if "专项训练" in name or "练习" in name or "训练" in name:
        return "专项训练"
    if "选题" in name:
        return "选题"
    return "讲义"


def pdf_pages(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def normalize_title(title: str, suffix: Optional[str]) -> str:
    title = title.strip()
    if suffix and title.endswith("-"):
        title = title[:-1].strip()
    if title.endswith("讲义"):
        title = title[:-2].strip()
    return title or "未命名"


def parse_material(path: Path) -> Optional[Material]:
    name = path.name
    rel = path.relative_to(SOURCE_DIR)

    if path.suffix.lower() != ".pdf":
        return None
    if "板书" in name:
        return None
    if name == "计算基本法【完结】.pdf":
        return None

    kind = detect_kind(name)
    if kind == "讲义" and "讲义" not in name and not name.endswith("切线.pdf"):
        return None

    parent_parts = set(rel.parts[:-1])

    if "直播回放板书合集" in parent_parts:
        if kind not in {"作业", "选题"}:
            return None
        order = 1 if "20250125" in name else 2
        title = name[:-4] if name.lower().endswith(".pdf") else name
        return Material(
            source_path=path,
            rel_path=rel,
            chapter=99,
            lesson=order,
            item_order=0,
            lesson_code=f"99-{order}",
            module_title=CHAPTER_TITLES[99],
            title=title,
            kind=kind,
            kind_order=KIND_ORDER[kind],
            pages=pdf_pages(path),
        )

    if "新定义章节电子讲义" in parent_parts:
        if "新定义专项训练" in name:
            return Material(
                source_path=path,
                rel_path=rel,
                chapter=3,
                lesson=99,
                item_order=0,
                lesson_code="3-补充",
                module_title=CHAPTER_TITLES[3],
                title="新定义专项训练",
                kind=kind,
                kind_order=KIND_ORDER[kind],
                pages=pdf_pages(path),
            )
        if "新定义" in name and kind in {"讲义", "作业解析", "解析", "作业"}:
            item_order = 1
            if "（下）" in name:
                item_order = 2
            title = "新定义"
            return Material(
                source_path=path,
                rel_path=rel,
                chapter=3,
                lesson=1,
                item_order=item_order,
                lesson_code="3-1",
                module_title=CHAPTER_TITLES[3],
                title=title,
                kind=kind,
                kind_order=KIND_ORDER[kind],
                pages=pdf_pages(path),
            )
        return None

    match = PREFIX_RE.match(name)
    if not match:
        return None

    chapter = int(match.group("chapter"))
    lesson = int(match.group("lesson"))
    suffix = match.group("suffix")
    raw_title = normalize_title(match.group("title"), suffix)

    if kind not in KIND_ORDER:
        return None

    module_title = CHAPTER_TITLES.get(chapter)
    if module_title is None:
        module_title = raw_title.split("：", 1)[0] if "：" in raw_title else raw_title

    return Material(
        source_path=path,
        rel_path=rel,
        chapter=chapter,
        lesson=lesson,
        item_order=0,
        lesson_code=f"{chapter}-{lesson}",
        module_title=module_title,
        title=raw_title,
        kind=kind,
        kind_order=KIND_ORDER[kind],
        pages=pdf_pages(path),
    )


def collect_materials() -> List[Material]:
    materials: List[Material] = []
    for path in SOURCE_DIR.rglob("*.pdf"):
        item = parse_material(path)
        if item is not None:
            materials.append(item)
    return sorted(materials, key=lambda item: item.sort_key)


def group_materials(materials: Iterable[Material]) -> Dict[Tuple[int, int, int], List[Material]]:
    groups: Dict[Tuple[int, int, int], List[Material]] = {}
    for item in materials:
        groups.setdefault(item.group_key, []).append(item)
    return {key: sorted(value, key=lambda item: item.sort_key) for key, value in groups.items()}


def preferred_lesson_title(items: Sequence[Material]) -> str:
    lectures = [item.title for item in items if item.kind == "讲义"]
    if lectures:
        return lectures[0]
    return sorted((item.title for item in items), key=len)[0]


def lesson_file_name(items: Sequence[Material]) -> str:
    first = items[0]
    title = preferred_lesson_title(items)
    return safe_name(f"{first.lesson_code}_{title}_讲义作业解析.pdf")


def module_file_name(chapter: int, title: str) -> str:
    return safe_name(f"{chapter:02d}_{title}_讲义作业解析分册.pdf")


def ordered_groups(materials: Sequence[Material]) -> List[Tuple[Tuple[int, int, int], List[Material]]]:
    grouped = group_materials(materials)
    return sorted(grouped.items(), key=lambda pair: pair[0])


def add_material_pages(writer: PdfWriter, item: Material) -> Tuple[int, int]:
    start = len(writer.pages) + 1
    reader = PdfReader(str(item.source_path))
    for page in reader.pages:
        writer.add_page(page)
    end = len(writer.pages)
    return start, end


def write_pdf_for_items(
    items: Sequence[Material],
    output_path: Path,
    with_group_bookmarks: bool = True,
) -> List[Dict[str, object]]:
    writer = PdfWriter()
    rows: List[Dict[str, object]] = []
    module_bookmarks: Dict[int, object] = {}
    lesson_bookmarks: Dict[Tuple[int, int, int], object] = {}

    for item in items:
        group = item.group_key
        group_items = [candidate for candidate in items if candidate.group_key == group]
        lesson_title = preferred_lesson_title(group_items)

        if with_group_bookmarks and item.chapter not in module_bookmarks:
            module_bookmarks[item.chapter] = writer.add_outline_item(
                f"{item.chapter:02d} {item.module_title}",
                len(writer.pages),
            )

        if with_group_bookmarks and group not in lesson_bookmarks:
            parent = module_bookmarks.get(item.chapter)
            lesson_bookmarks[group] = writer.add_outline_item(
                f"{item.lesson_code} {lesson_title}",
                len(writer.pages),
                parent=parent,
            )

        start, end = add_material_pages(writer, item)

        parent = lesson_bookmarks.get(group) if with_group_bookmarks else None
        writer.add_outline_item(
            f"{item.kind}：{item.source_path.name[:-4]}",
            start - 1,
            parent=parent,
        )

        rows.append(
            {
                "material": item,
                "start": start,
                "end": end,
                "lesson_title": lesson_title,
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as fh:
        writer.write(fh)
    return rows


def write_markdown_index(rows: Sequence[Dict[str, object]], output_path: Path, title: str) -> None:
    lines: List[str] = [
        f"# {title}",
        "",
        f"生成时间：{datetime.now():%Y-%m-%d %H:%M:%S}",
        "",
        "合并口径：讲义、作业、解析/作业解析、专项训练/选题；未合并板书、直播板书和其它资料。",
        "",
        "页码为总合集中的 PDF 页码，从 1 开始。",
        "",
    ]

    current_chapter: Optional[int] = None
    for row in rows:
        item: Material = row["material"]  # type: ignore[assignment]
        if item.chapter != current_chapter:
            current_chapter = item.chapter
            lines.extend([f"## {item.chapter:02d} {item.module_title}", "", "| 课时 | 知识点 | 类型 | 页码 | 原文件 |", "|---|---|---|---:|---|"])
        lines.append(
            f"| {item.lesson_code} | {row['lesson_title']} | {item.kind} | {row['start']}-{row['end']} | {item.rel_path.as_posix()} |"
        )
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_csv_index(rows: Sequence[Dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "模块编号",
                "模块",
                "课时",
                "知识点",
                "资料类型",
                "原文件",
                "来源相对路径",
                "页数",
                "总合集起始页",
                "总合集结束页",
            ]
        )
        for row in rows:
            item: Material = row["material"]  # type: ignore[assignment]
            writer.writerow(
                [
                    item.chapter,
                    item.module_title,
                    item.lesson_code,
                    row["lesson_title"],
                    item.kind,
                    item.source_path.name,
                    str(item.rel_path),
                    item.pages,
                    row["start"],
                    row["end"],
                ]
            )


def write_check_report(materials: Sequence[Material], rows: Sequence[Dict[str, object]], output_path: Path) -> None:
    grouped = group_materials(materials)
    missing_lines: List[str] = []
    for _, items in ordered_groups(materials):
        kinds = {item.kind for item in items}
        first = items[0]
        title = preferred_lesson_title(items)
        missing = []
        if "讲义" not in kinds:
            missing.append("讲义")
        if "作业" not in kinds:
            missing.append("作业")
        if not ({"解析", "作业解析"} & kinds):
            missing.append("解析/作业解析")
        if missing:
            missing_lines.append(f"- {first.lesson_code} {title}：缺 {', '.join(missing)}")

    total_input_pages = sum(item.pages for item in materials)
    total_output_pages = rows[-1]["end"] if rows else 0
    lines = [
        "二轮学生资料整理检查",
        "",
        f"纳入资料数：{len(materials)}",
        f"纳入课时/专题数：{len(grouped)}",
        f"纳入页数合计：{total_input_pages}",
        f"总合集页数：{total_output_pages}",
        f"页数校验：{'通过' if total_input_pages == total_output_pages else '未通过'}",
        "",
        "未纳入口径：板书、直播板书、计算基本法【完结】.pdf、内容简介 docx。",
        "",
        "缺项提示（按“讲义+作业+解析/作业解析”理想组合检查，原资料不存在的不补造）：",
    ]
    lines.extend(missing_lines or ["- 无"])
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_output_readme(output_dir: Path) -> None:
    text = """二轮学生资料_讲义作业合并

整理口径：
- 纳入：讲义、作业、解析、作业解析、专项训练、选题。
- 排除：板书、直播板书、计算基本法【完结】.pdf、内容简介 docx。

目录说明：
- 2025阿不二轮学生资料_讲义作业解析_总合集.pdf：完整总合集，PDF 侧边栏带模块、课时、资料类型书签。
- 01_按知识点分册：按大知识模块生成的分册 PDF。
- 02_按课时合并：每个课时一个小册，内部顺序为讲义、作业、解析/作业解析、专项训练/选题。
- 00_总合集页码索引.md / .csv：每份原始资料在总合集里的页码范围。
- 00_缺项检查.txt：哪些课时原始资料中没有作业或解析。
"""
    (output_dir / "00_整理说明.txt").write_text(text, encoding="utf-8")


def copy_script(output_dir: Path) -> None:
    target = output_dir / "00_整理脚本.py"
    shutil.copy2(Path(__file__), target)


def main() -> None:
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"找不到资料目录：{SOURCE_DIR}")

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = ROOT / f"{OUTPUT_STEM}_{stamp}"
    lesson_dir = output_dir / "02_按课时合并"
    module_dir = output_dir / "01_按知识点分册"

    materials = collect_materials()
    if not materials:
        raise RuntimeError("没有找到可合并的学生资料。")

    # 先生成课时小册，方便按单个知识点打印。
    for _, items in ordered_groups(materials):
        first = items[0]
        folder = lesson_dir / safe_name(f"{first.chapter:02d}_{first.module_title}")
        write_pdf_for_items(items, folder / lesson_file_name(items), with_group_bookmarks=False)

    # 再生成模块分册。
    by_chapter: Dict[int, List[Material]] = {}
    for item in materials:
        by_chapter.setdefault(item.chapter, []).append(item)
    for chapter, items in sorted(by_chapter.items()):
        title = CHAPTER_TITLES.get(chapter, items[0].module_title)
        write_pdf_for_items(sorted(items, key=lambda item: item.sort_key), module_dir / module_file_name(chapter, title))

    full_pdf = output_dir / "2025阿不二轮学生资料_讲义作业解析_总合集.pdf"
    rows = write_pdf_for_items(materials, full_pdf)

    write_markdown_index(rows, output_dir / "00_总合集页码索引.md", "2025阿不二轮学生资料总合集页码索引")
    write_csv_index(rows, output_dir / "00_总合集页码索引.csv")
    write_check_report(materials, rows, output_dir / "00_缺项检查.txt")
    write_output_readme(output_dir)
    copy_script(output_dir)

    print(f"OUTPUT_DIR={output_dir}")
    print(f"MATERIALS={len(materials)}")
    print(f"GROUPS={len(group_materials(materials))}")
    print(f"PAGES={sum(item.pages for item in materials)}")
    print(f"FULL_PDF={full_pdf}")


if __name__ == "__main__":
    main()
