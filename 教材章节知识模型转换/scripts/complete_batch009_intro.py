#!/usr/bin/env python3
"""Complete BATCH-009-CH00-INTRO: 12 sources."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-009-CH00-INTRO"
REVIEW = BATCH / "review_data"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
SOURCE_IDS = ["B0242", "B0059", "B0337", "B0313", "B0273", "B0240", "B0108", "B0214", "B0376", "B0115", "B0183", "B0440"]


def load_assets():
    with ASSETS.open(encoding="utf-8-sig", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_review(source_id: str) -> dict:
    path = REVIEW / f"{source_id}_review.json"
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    assert data["source_id"] == source_id, f"review id mismatch: {data['source_id']}"
    for row in data["maps"]:
        assert len(row) == 7, f"{source_id}: map row length {len(row)}"
        section, grade = row[0], row[1]
        assert grade in "ABCDX", f"{source_id}:{section} bad grade {grade}"
        assert section.count(".") == 1 and section.split(".")[0].isdigit() and section.split(".")[1].isdigit(), \
            f"{source_id}: bad section id {section}"
    return data


def write_source(source_id: str, data: dict, asset: dict) -> None:
    clean = Path(asset["clean_source_path"])
    card = {
        "source_id": source_id,
        "corpus": asset["corpus"],
        "folder_name": asset["folder_name"],
        "material_type": data["type"],
        "clean_source_path": str(clean),
        "clean_source_sha256": digest(clean),
        "duplicate_group": data["duplicate_group"],
        "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
        "report_structure": {"review_basis": "overall_and_all_chapter_reports_plus_emergence_gap_audit"},
        "candidate_sections": [{"section_id": row[0], "grade": row[1], "verification": "V2", "role": row[2]} for row in data["maps"]],
        "review_status": "semantic_review_complete",
        "evidence_level": "V2",
        "notes": data["limits"] + ["clean原文仅局部定位；未完成全篇、版次、图版、数字和引注核验。"],
        "original_spot_checks": data["checks"],
    }
    card_dir, map_dir = BATCH / "source_cards", BATCH / "mappings"
    (card_dir / f"{source_id}_来源卡.json").write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        f"# {source_id} 来源卡：{data['title']}", "", "## 一、来源身份与核验状态", "",
        "| 字段 | 内容 |", "|---|---|", f"| 来源ID | {source_id} |", f"| 作者／编者 | {data['author']} |",
        f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |", f"| 范围 | {data['scope']} |",
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |", f"| 版本／史料关系 | {data['duplicate_group']} |",
        f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
        "| 核验 | V2：全部分析报告与知识涌现资产复核＋clean关键段落局部回查 |", "",
        "## 二、核心命题与教材价值", "", data["summary"], "", "## 三、论证强项", "",
    ]
    md.extend(f"- {item}" for item in data["strengths"])
    md.extend(["", "## 四、限度与反例", ""])
    md.extend(f"- {item}" for item in data["limits"])
    md.extend(["", "## 五、章节准入", "", "| 章／节 | 等级 | 角色 | 可接受命题 | 边界 | 状态 |", "|---|---|---|---|---|---|"])
    for section, grade, role, claim, boundary, _follow, status in data["maps"]:
        md.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    md.extend(["", "## 六、clean原文局部回查", ""])
    md.extend(f"- {item}" for item in data["checks"])
    md.extend(["", "本卡不把P4分析报告或知识涌现命名升级为原著事实。正式引用须返回实际版次、页码、上下文、图版及关键P0材料。", ""])
    (card_dir / f"{source_id}_来源卡.md").write_text("\n".join(md), encoding="utf-8")


def write_mapping(source_id: str, data: dict) -> None:
    fields = ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]
    map_dir = BATCH / "mappings"
    with (map_dir / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for section, grade, role, claim, boundary, follow, status in data["maps"]:
            writer.writerow({"source_id": source_id, "section_id": section, "grade": grade, "verification": "V2", "role": role,
                             "accepted_claim": claim, "evidence_boundary": boundary, "original_followup": follow, "status": status})


def update_manifest() -> None:
    path = BATCH / "batch_manifest.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fields = list(rows[0])
    for row in rows:
        if row["source_id"] in SOURCE_IDS:
            row["semantic_review_status"] = "complete"
            row["mapping_status"] = "complete"
            row["original_verification_status"] = "partial_clean_text_spot_check"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    assets = load_assets()
    for source_id in SOURCE_IDS:
        data = load_review(source_id)
        write_source(source_id, data, assets[source_id])
        write_mapping(source_id, data)
    update_manifest()
    print(json.dumps({"completed": SOURCE_IDS,
                      "mapping_rows": sum(len(load_review(s)["maps"]) for s in SOURCE_IDS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
