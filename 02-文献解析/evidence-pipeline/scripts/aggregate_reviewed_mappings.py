#!/usr/bin/env python3
"""Aggregate only human-reviewed mapping files into auditable indexes."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH_ROOT = ROOT / "11_语义复核批次"
OUTPUT = ROOT / "04_文献—章节映射"
LOGS = ROOT / "logs"
FIELDNAMES = [
    "source_id",
    "section_id",
    "grade",
    "verification",
    "role",
    "accepted_claim",
    "evidence_boundary",
    "original_followup",
    "status",
    "review_file",
]


def section_key(section_id: str) -> tuple[int, int, str]:
    match = re.fullmatch(r"(\d+)\.(\d+)", section_id)
    if match:
        return int(match.group(1)), int(match.group(2)), section_id
    return 999, 999, section_id


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows: list[dict] = []
    for path in sorted(BATCH_ROOT.glob("BATCH-*/mappings/*.csv"), key=lambda p: str(p).casefold()):
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                row["review_file"] = str(path)
                rows.append(row)

    source_rows = sorted(rows, key=lambda r: (r["source_id"], section_key(r["section_id"])))
    section_rows = sorted(rows, key=lambda r: (section_key(r["section_id"]), r["source_id"]))
    write_csv(OUTPUT / "已复核_来源到章节.csv", source_rows)
    write_csv(OUTPUT / "已复核_章节到来源.csv", section_rows)

    by_source: dict[str, list[dict]] = defaultdict(list)
    by_section: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_source[row["source_id"]].append(row)
        by_section[row["section_id"]].append(row)

    source_md = [
        "# 已复核：来源到章节索引",
        "",
        "> 本索引只汇入人工语义复核记录。它是滚动成果，不代表589项来源已全部完成。",
        "",
    ]
    for source_id in sorted(by_source):
        source_md.extend(
            [
                f"## {source_id}",
                "",
                "| 章／节 | 等级 | 核验 | 角色 | 状态 |",
                "|---|---|---|---|---|",
            ]
        )
        for row in sorted(by_source[source_id], key=lambda r: section_key(r["section_id"])):
            source_md.append(
                f"| {row['section_id']} | {row['grade']} | {row['verification']} | {row['role']} | {row['status']} |"
            )
        source_md.append("")
    (OUTPUT / "已复核_来源到章节.md").write_text("\n".join(source_md) + "\n", encoding="utf-8")

    section_md = [
        "# 已复核：章节到来源索引",
        "",
        "> 本索引只汇入人工语义复核记录；机器候选未被混入。A—D／X是章节角色，V0—V4是核验深度。",
        "",
    ]
    for section_id in sorted(by_section, key=section_key):
        section_md.extend(
            [
                f"## {section_id}",
                "",
                "| 来源ID | 等级 | 核验 | 可支持命题 | 边界 | 状态 |",
                "|---|---|---|---|---|---|",
            ]
        )
        for row in sorted(by_section[section_id], key=lambda r: r["source_id"]):
            claim = row["accepted_claim"].replace("|", "／")
            boundary = row["evidence_boundary"].replace("|", "／")
            section_md.append(
                f"| {row['source_id']} | {row['grade']} | {row['verification']} | {claim} | {boundary} | {row['status']} |"
            )
        section_md.append("")
    (OUTPUT / "已复核_章节到来源.md").write_text("\n".join(section_md) + "\n", encoding="utf-8")

    reviewed_sources = sorted(by_source)
    summary = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "reviewed_source_count": len(reviewed_sources),
        "total_source_count": 589,
        "reviewed_source_percent": round(len(reviewed_sources) / 589 * 100, 2),
        "mapping_row_count": len(rows),
        "reviewed_section_count": len(by_section),
        "grade_counts": dict(Counter(row["grade"] for row in rows)),
        "verification_counts": dict(Counter(row["verification"] for row in rows)),
        "status": "IN_PROGRESS",
        "warning": "Only human-reviewed batch mapping CSV files are aggregated; absence from this index does not mean irrelevance.",
    }
    (LOGS / "semantic-review-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    progress_lines = [
        "# 人工语义复核进度",
        "",
        f"- 生成时间：{summary['generated_at']}",
        f"- 已复核来源：{summary['reviewed_source_count']}／{summary['total_source_count']}（{summary['reviewed_source_percent']}%）",
        f"- 正式章／节处置记录：{summary['mapping_row_count']}",
        f"- 已触及教材节节点：{summary['reviewed_section_count']}／121",
        f"- 等级分布：{summary['grade_counts']}",
        f"- 核验分布：{summary['verification_counts']}",
        "",
        "## 状态边界",
        "",
        "本文件只统计人工复核批次中的映射CSV。机器候选未混入；某来源未出现表示尚未复核，不表示与教材无关。当前状态为`IN_PROGRESS`。",
        "",
        "## 已复核来源",
        "",
    ]
    progress_lines.extend(f"- {source_id}" for source_id in reviewed_sources)
    (LOGS / "人工语义复核进度.md").write_text("\n".join(progress_lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
