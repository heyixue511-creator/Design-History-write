# -*- coding: utf-8 -*-
"""更新 CH02 矩阵 CSV 中 2.4 节统计（本批次新增 B0353）。"""
import csv
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\06_核心命题—证据矩阵\CH02_核心命题—来源矩阵.csv")
rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
for row in rows:
    if row["section_id"] != "2.4":
        continue
    ids = [x for x in row["source_ids"].split(";") if x]
    indep = [x for x in row["independent_source_ids"].split(";") if x]
    if "B0353" not in ids:
        ids.append("B0353")
    if "B0353" not in indep:
        indep.append("B0353")
    row["source_ids"] = ";".join(ids)
    row["independent_source_ids"] = ";".join(indep)
    row["mapping_rows"] = str(len(ids))
    row["accepted_rows"] = str(len(indep))
    row["independent_support_rows"] = str(len(indep))
    row["grade_C"] = str(int(row["grade_C"]) + 1)
    row["audit_judgment"] = "全库最密集节：34条记录覆盖零售制度、消费革命前史、时尚媒介、物质文化与企业链；多来源以不同章节报告重复支撑同一机制，写作时必须按证据簇去重而非按条目引用；供给侧证据强，欲望塑造与家庭使用结果弱（本批次B0353'必然性的趣味'/'文化善意'提供品味机制理论背景）。"
with p.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print("2.4 updated:", [r["mapping_rows"] for r in rows if r["section_id"] == "2.4"])
