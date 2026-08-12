#!/usr/bin/env python3
"""Create lossless reading packets for a semantic-review batch."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.jsonl"


def safe_name(value: str) -> str:
    return re.sub(r"[<>:\"/\\|?*]", "_", value)


def load_assets() -> dict[str, dict]:
    assets: dict[str, dict] = {}
    with ASSETS.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            assets[item["source_id"]] = item
    return assets


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "utf-16"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch_id")
    parser.add_argument("source_ids", nargs="+")
    args = parser.parse_args()
    assets = load_assets()
    batch_root = ROOT / "11_语义复核批次" / args.batch_id
    packet_dir = batch_root / "packets"
    card_dir = batch_root / "source_cards"
    mapping_dir = batch_root / "mappings"
    for directory in (packet_dir, card_dir, mapping_dir):
        directory.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict] = []
    for source_id in args.source_ids:
        if source_id not in assets:
            raise SystemExit(f"Unknown source_id: {source_id}")
        source = assets[source_id]
        folder = Path(
            r"D:\Design-history-知识库\report-book"
            if source["corpus"] == "book"
            else r"D:\Design-history-知识库\report-paper"
        ) / source["folder_name"]
        lines = [
            f"# {source_id} {source['folder_name']}",
            "",
            f"- 语料类型：{source['corpus']}",
            f"- 材料类型初判：{source['material_type']}",
            f"- clean原文：{source['clean_source_path'] or '未匹配'}",
            f"- 重复组：{source['duplicate_group'] or '无精确哈希重复'}",
            f"- 分析文件数：{source['report_structure']['file_count']}",
            f"- 总字符数：{source['report_structure']['total_characters']}",
            "- 当前核验等级：V2候选；须完成本包语义复核后确认",
            "",
            "> 以下内容按原目录文件顺序无损汇集。文件标题是证据边界，不得把不同报告视为独立来源。",
            "",
        ]
        for record in source["files"]:
            path = folder / record["relative_path"]
            lines.extend(
                [
                    "---",
                    "",
                    f"## FILE `{record['relative_path']}`",
                    "",
                    f"- category: `{record['category']}`",
                    f"- sha256: `{record['sha256']}`",
                    f"- characters: {record['characters']}",
                    "",
                    read_text(path),
                    "",
                ]
            )
        packet_path = packet_dir / f"{source_id}_{safe_name(source['folder_name'])}.md"
        packet_path.write_text("\n".join(lines), encoding="utf-8")
        manifest_rows.append(
            {
                "batch_id": args.batch_id,
                "source_id": source_id,
                "corpus": source["corpus"],
                "folder_name": source["folder_name"],
                "packet_path": str(packet_path),
                "packet_characters": len("\n".join(lines)),
                "semantic_review_status": "pending",
                "mapping_status": "pending",
                "original_verification_status": "not_started",
            }
        )
    with (batch_root / "batch_manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest_rows[0]))
        writer.writeheader()
        writer.writerows(manifest_rows)
    print(json.dumps({"batch": args.batch_id, "sources": len(manifest_rows), "root": str(batch_root)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
