# -*- coding: utf-8 -*-
"""更新 CH02 矩阵 CSV 中 2.7 节统计（BATCH-031 新增 B0354）。"""
import csv
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\06_核心命题—证据矩阵\CH02_核心命题—来源矩阵.csv")
rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
for row in rows:
    if row["section_id"] != "2.7":
        continue
    ids = [x for x in row["source_ids"].split(";") if x]
    indep = [x for x in row["independent_source_ids"].split(";") if x]
    if "B0354" not in ids:
        ids.append("B0354")
    if "B0354" not in indep:
        indep.append("B0354")
    row["source_ids"] = ";".join(ids)
    row["independent_source_ids"] = ";".join(indep)
    row["mapping_rows"] = str(len(ids))
    row["accepted_rows"] = str(len(indep))
    row["independent_support_rows"] = str(len(indep))
    row["grade_C"] = str(int(row["grade_C"]) + 1)
with p.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print("2.7 updated:", [r["mapping_rows"] for r in rows if r["section_id"] == "2.7"])
