#!/usr/bin/env python3
"""Temporary verification for BATCH-005-CH04-BAUHAUS."""
import csv, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-005-CH04-BAUHAUS"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"

ids = ["B0064", "B0060", "B0182", "B0282", "B0158", "B0464", "B0216", "B0454",
       "B0081", "B0008", "B0517", "B0492", "B0247", "B0048", "B0342"]
errors, warns = [], []
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

for sid in ids:
    card = json.loads((BATCH / "source_cards" / f"{sid}_来源卡.json").read_text(encoding="utf-8"))
    clean = Path(assets[sid]["clean_source_path"])
    actual = hashlib.sha256(clean.read_bytes()).hexdigest().upper()
    if actual != card["clean_source_sha256"]:
        errors.append(f"{sid}: SHA256 mismatch")
    else:
        print(f"{sid}: SHA-256 OK ({actual[:16]}...)")

    for f in ["source_id", "corpus", "folder_name", "material_type", "clean_source_path",
              "clean_source_sha256", "duplicate_group", "files", "report_structure",
              "candidate_sections", "review_status", "evidence_level", "notes", "original_spot_checks"]:
        if f not in card:
            errors.append(f"{sid}: card missing field {f}")
    if card["evidence_level"] != "V2" or card["review_status"] != "semantic_review_complete":
        errors.append(f"{sid}: bad status fields")

    map_rows = list(csv.DictReader((BATCH / "mappings" / f"{sid}_章节映射.csv").open(encoding="utf-8-sig")))
    if len(map_rows) != len(card["candidate_sections"]):
        errors.append(f"{sid}: mapping rows {len(map_rows)} != candidates {len(card['candidate_sections'])}")
    seen = set()
    for row in map_rows:
        if row["grade"] not in "ABCDX":
            errors.append(f"{sid}:{row['section_id']} invalid grade {row['grade']}")
        if row["verification"] != "V2":
            errors.append(f"{sid}:{row['section_id']} invalid verification")
        if not re.fullmatch(r"\d+\.\d+", row["section_id"]):
            errors.append(f"{sid}:{row['section_id']} bad section id")
        key = (row["section_id"], row["role"])
        if key in seen:
            errors.append(f"{sid}: duplicate section+role {key}")
        seen.add(key)
        for f in ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]:
            if not row.get(f, "").strip():
                errors.append(f"{sid}:{row['section_id']} empty field {f}")
    md = BATCH / "source_cards" / f"{sid}_来源卡.md"
    if not md.exists() or md.stat().st_size < 2000:
        errors.append(f"{sid}: source card md missing/small")

    for p in [BATCH / "source_cards" / f"{sid}_来源卡.json", BATCH / "source_cards" / f"{sid}_来源卡.md",
              BATCH / "mappings" / f"{sid}_章节映射.csv"]:
        text = p.read_text(encoding="utf-8")
        for bad in ["\ufffd", "锟斤拷", "Ã©", "â€"]:
            if bad in text:
                errors.append(f"{sid}: mojibake {bad!r} in {p.name}")
    print(f"{sid}: fields/levels/mojibake checked ({len(map_rows)} mapping rows)")

    text = clean.read_text(encoding="utf-8", errors="replace")
    nlines = text.count("\n") + 1
    nums = [int(x) for x in re.findall(r"clean[第L](\d+)", " ".join(card["original_spot_checks"]))]
    nums += [int(x) for x in re.findall(r"L(\d{3,4})", " ".join(card["original_spot_checks"]))]
    if nums:
        mx = max(nums)
        if mx > nlines:
            warns.append(f"{sid}: check refs line {mx} > clean file lines {nlines}")
        print(f"{sid}: clean lines={nlines}, max check ref={mx}")

rows = list(csv.DictReader((BATCH / "batch_manifest.csv").open(encoding="utf-8-sig")))
for row in rows:
    if row["source_id"] in ids and row["semantic_review_status"] != "complete":
        errors.append(f"{row['source_id']}: manifest not updated")

print("----")
print("ERRORS:", len(errors))
for e in errors: print(" E:", e)
print("WARNINGS:", len(warns))
for w in warns: print(" W:", w)
sys.exit(1 if errors else 0)
