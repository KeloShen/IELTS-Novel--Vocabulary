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


def extract_words(lines: List[str]) -> Dict[str, List[str]]:
    words_by_chapter: Dict[str, List[str]] = {name: [] for name in CHAPTER_NAMES}
    seen: Dict[str, set[str]] = {name: set() for name in CHAPTER_NAMES}
    chapter_idx = -1
    chapter_marks = 0

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line in {"---", "==="}:
            continue
        if line == "+++":
            chapter_idx += 1
            chapter_marks += 1
            continue
        if chapter_idx == -1:
            # Skip anything before the first chapter marker.
            continue
        if chapter_idx >= len(CHAPTER_NAMES):
            raise ValueError("More chapter markers found than CHAPTER_NAMES provided.")
        if "|" not in line:
            # Chapter titles or other notes.
            continue

        head = line.split("|", 1)[0].strip()
        if not head:
            continue
        for word in head.split("/"):
            cleaned = word.strip()
            if cleaned and cleaned not in seen[CHAPTER_NAMES[chapter_idx]]:
                words_by_chapter[CHAPTER_NAMES[chapter_idx]].append(cleaned)
                seen[CHAPTER_NAMES[chapter_idx]].add(cleaned)

    if chapter_marks != len(CHAPTER_NAMES):
        raise ValueError(
            f"Expected {len(CHAPTER_NAMES)} chapter markers, found {chapter_marks}."
        )
    return words_by_chapter


def write_output(words_by_chapter: Dict[str, List[str]], output_path: Path) -> None:
    parts: List[str] = []
    total = 0
    for name in CHAPTER_NAMES:
        words = words_by_chapter.get(name, [])
        total += len(words)
        parts.append(name)
        parts.extend(words)
        parts.append("")
    output_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {total} words into {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract words from vocabulary.txt and group them into chapters."
    )
    parser.add_argument(
        "-i",
        "--input",
        default="vocabulary.txt",
        type=Path,
        help="Input vocabulary text file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="extracted_words.txt",
        type=Path,
        help="Where to write the extracted word list.",
    )
    args = parser.parse_args()

    lines = args.input.read_text(encoding="utf-8").splitlines()
    words_by_chapter = extract_words(lines)
    write_output(words_by_chapter, args.output)


if __name__ == "__main__":
    main()
