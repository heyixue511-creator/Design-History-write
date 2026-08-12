#!/usr/bin/env python3
"""Generate candidate atomic evidence cards from A-grade reviewed mappings.

Output: 05_原子证据卡/_candidates/CH{xx}_候选卡.json (status=candidate).
Candidates are SPLIT MATERIAL ONLY: accepted cards must be manually split
into atomic claims and checked against clean text before status=accepted.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
INDEX = ROOT / "04_文献—章节映射" / "已复核_章节到来源.csv"
OUT = ROOT / "05_原子证据卡" / "_candidates"
OUT.mkdir(exist_ok=True)

CHAPTERS = {
    "0": "CH00", "1": "CH01", "2": "CH02", "3": "CH03", "4": "CH04",
    "5": "CH05", "6": "CH06", "7": "CH07", "8": "CH08", "9": "CH09",
    "10": "CH10", "11": "CH11", "12": "CH12", "13": "CH13", "14": "CH14",
    "15": "CH15", "16": "CH16", "99": "CH99",
}


def chapter_of(section_id: str) -> str:
    num = section_id.split(".")[0]
    return CHAPTERS.get(num, f"CH{num}")


def main() -> None:
    by_chapter: dict[str, list[dict]] = {}
    seq = 0
    with INDEX.open(encoding="utf-8-sig", newline="") as h:
        for row in csv.DictReader(h):
            if row["grade"] != "A":
                continue
            seq += 1
            ch = chapter_of(row["section_id"])
            card = {
                "evidence_id": f"EV-C{seq:04d}",
                "claim": row["accepted_claim"],
                "source_id": row["source_id"],
                "source_location": row["original_followup"],
                "source_class": "P0" if row["status"] == "ACCEPTED_AS_ACTOR_SOURCE" else "P1",
                "verification_level": row["verification"],
                "section_ids": [row["section_id"]],
                "textbook_function": row.get("role", ""),
                "supports": [row["accepted_claim"][:60]],
                "does_not_support": [row["evidence_boundary"]],
                "status": "candidate",
            }
            by_chapter.setdefault(ch, []).append(card)

    total = 0
    for ch, cards in sorted(by_chapter.items()):
        (OUT / f"{ch}_候选卡.json").write_text(
            json.dumps(cards, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(cards)
        print(f"{ch}: {len(cards)} candidates")
    print(f"TOTAL {total} candidates -> {OUT}")


if __name__ == "__main__":
    main()
