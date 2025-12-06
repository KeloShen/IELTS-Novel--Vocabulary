from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List


CHAPTER_NAMES = [
    "01_自然地理",
    "02_植物研究",
    "03_动物保护",
    "04_太空探索",
    "05_学校教育",
    "06_科技发明",
    "07_文化历史",
    "08_语言演化",
    "09_娱乐运动",
    "10_物品材料",
    "11_时尚潮流",
    "12_饮食健康",
    "13_建筑场所",
    "14_交通旅行",
    "15_国家政府",
    "16_社会经济",
    "17_法律法规",
    "18_沙场争锋",
    "19_社会角色",
    "20_行为动作",
    "21_身心健康",
    "22_时间日期",
]


def parse_extracted(lines: List[str]) -> Dict[str, List[str]]:
    data: Dict[str, List[str]] = {name: [] for name in CHAPTER_NAMES}
    current: str | None = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if line in CHAPTER_NAMES:
            current = line
            continue
        if current is None:
            # Skip anything before the first chapter.
            continue
        data[current].append(line)
    return data


def write_chapter_files(
    words_by_chapter: Dict[str, List[str]], out_dir: Path
) -> Dict[str, int]:
    out_dir.mkdir(parents=True, exist_ok=True)
    counts: Dict[str, int] = {}
    for chapter in CHAPTER_NAMES:
        words = words_by_chapter.get(chapter, [])
        (out_dir / f"{chapter}.txt").write_text(
            "\n".join(words) + ("\n" if words else ""), encoding="utf-8"
        )
        counts[chapter] = len(words)
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split extracted_words.txt into 22 chapter files."
    )
    parser.add_argument(
        "-i",
        "--input",
        default="extracted_words.txt",
        type=Path,
        help="Input file produced by extract_words.py.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=Path("chapters"),
        type=Path,
        help="Directory where chapter files will be written.",
    )
    args = parser.parse_args()

    lines = args.input.read_text(encoding="utf-8").splitlines()
    words_by_chapter = parse_extracted(lines)
    counts = write_chapter_files(words_by_chapter, args.output_dir)

    total = sum(counts.values())
    print(f"Wrote {total} words into {args.output_dir}/ (22 files).")


if __name__ == "__main__":
    main()
