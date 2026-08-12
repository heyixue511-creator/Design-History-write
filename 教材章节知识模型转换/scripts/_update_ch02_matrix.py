# -*- coding: utf-8 -*-
"""更新 CH02 矩阵 CSV 中 2.3/2.6/2.7 三节的统计（本批次新增 P0047/P0030/B0028/B0089）。"""
import csv
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\06_核心命题—证据矩阵\CH02_核心命题—来源矩阵.csv")
rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))

updates = {
    "2.3": {
        "add": ["P0047"],
        "grades": (10, 6, 3, 0, 0),
        "judgment": "A级十项构成最强节：行动者原典（B0383、B0318）、政治思想史（B0133）、企业史（B0070、B0348、B0091）、谱系（B0168）、通史（B0101）与跨区域（B0450）；张力命题证据充分（本批次P0047补充'手工社会主义vs精英消费主义'二歧框架的B级社会学综述）；但工资、价格、产量与工人经验等P0缺口明显；共享行动者原文只计一份P0。",
    },
    "2.6": {
        "add": ["P0030"],
        "grades": (11, 15, 10, 0, 3),
        "judgment": "A级机制链完整：殖民分类（B0082、B0427、B0463、B0303）、帝国资源与观看（B0175、B0204）、博物学分类（B0332）、棉帝国（B0169）与博览会计较史（B0339）；三条X明确排除B0035、B0049、B0450承担殖民分类核心；组织者话语证据充分，被展示者记录稀缺，观众接受不可推出（本批次P0030异托邦'补偿'概念仅作理论参照）。",
    },
    "2.7": {
        "add": ["B0028", "B0089"],
        "grades": (21, 23, 7, 0, 2),
        "judgment": "全库映射最多节：A级形成'生产—贸易—选择—改造—消费'完整链（棉布、日本主义、东非消费、工艺美术转译、博览会模式东传、墨西哥挪用）；风险是同一条对象（sarasa、katagami、印度棉布）在多来源重复出现，写作时只计一份P0；'影响'类命题须逐链核验接触、委托、制作与再生产证据（本批次B0028商品普世圈提供跨文化流通理论框架、B0089提供晚明先例）。",
    },
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
    row["audit_judgment"] = u["judgment"]

with p.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print("updated:", {sid: len([x for x in r["source_ids"].split(';') if x]) for sid, r in [(x["section_id"], x) for x in rows] if sid in updates})
