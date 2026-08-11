#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 7 sections -> structure JSON for matrix authoring."""
import csv, json
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

sections = defaultdict(list)
for batch_dir in sorted((ROOT / "11_语义复核批次").glob("BATCH-*")):
    for m in sorted((batch_dir / "mappings").glob("*.csv")):
        with m.open(encoding="utf-8-sig", newline="") as h:
            for row in csv.DictReader(h):
                if row["section_id"].startswith("7."):
                    sections[row["section_id"]].append(row)

out = {}
for sid in sorted(sections, key=lambda s: (int(s.split(".")[0]), int(s.split(".")[1]))):
    rows = sections[sid]
    grades = defaultdict(int)
    for r in rows:
        grades[r["grade"]] += 1
    items = []
    for r in sorted(rows, key=lambda x: (x["grade"], x["source_id"], x["role"])):
        src = r["source_id"]
        title = assets.get(src, {}).get("folder_name", src)
        items.append({"source_id": src, "title": title, "grade": r["grade"],
                      "verification": r["verification"], "role": r["role"],
                      "accepted_claim": r["accepted_claim"], "evidence_boundary": r["evidence_boundary"],
                      "status": r["status"]})
    out[sid] = {"grades": dict(grades), "count": len(rows), "items": items}

(ROOT / "logs" / "_ch07_structure.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("WROTE", len(out), "sections:", {k: out[k]["count"] for k in out})
