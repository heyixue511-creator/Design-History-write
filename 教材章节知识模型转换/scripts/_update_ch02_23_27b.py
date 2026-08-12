# -*- coding: utf-8 -*-
"""更新 CH02 矩阵 CSV 中 2.3/2.7 节统计（本批次新增 B0330/B0148）。"""
import csv
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\06_核心命题—证据矩阵\CH02_核心命题—来源矩阵.csv")
rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))

updates = {
    "2.3": {"add": ["B0330"], "grades": (10, 7, 4, 0, 0)},
    "2.7": {"add": ["B0148"], "grades": (21, 24, 8, 0, 2)},
}
for row in rows:
    sid = row["section_id"]
    if sid not in updates:
        continue
    u = updates[sid]
    ids = [x for x in row["source_ids"].split(";") if x]
    indep = [x for x in row["independent_source_ids"].split(";") if x]
    for a in u["add"]:
        if a not in ids:
            ids.append(a)
        if a not in indep:
            indep.append(a)
    row["source_ids"] = ";".join(ids)
    row["independent_source_ids"] = ";".join(indep)
    row["mapping_rows"] = str(len(ids))
    row["accepted_rows"] = str(len(indep))
    row["independent_support_rows"] = str(len(indep))
    row["grade_A"], row["grade_B"], row["grade_C"], row["grade_D"], row["grade_X"] = (str(v) for v in u["grades"])

with p.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print("updated:", {sid: len([x for x in r["source_ids"].split(';') if x]) for sid, r in [(x["section_id"], x) for x in rows] if sid in updates})
