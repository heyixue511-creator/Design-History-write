#!/usr/bin/env python3
"""列出 BATCH-022 候选：16.7 中国平台 + 16.2 数据集/数字理论方向的未复核来源。"""
import csv
import re
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
assets = {r["source_id"]: r for r in csv.DictReader((ROOT / "03_来源清单与来源卡" / "来源资产总表.csv").open(encoding="utf-8-sig"))}
reviewed = set()
for m in sorted((ROOT / "11_语义复核批次").glob("BATCH-*")):
    for mm in sorted((m / "mappings").glob("*.csv")):
        for r in csv.DictReader(mm.open(encoding="utf-8-sig")):
            reviewed.add(r["source_id"])

print("已复核:", len(reviewed), "未复核:", len(assets) - len(reviewed))

pat_china = r"China|Chinese|中国|上海|北京|香港|台湾|靳埭强|杭间|沈榆|柳冠中|李砚祖|王受之|何人可|包豪斯|宣传|Poster|Comics|漫画|Lent"
pat_digital = r"Digital|Interaction|Mobile|Interface|Data|Dataset|HCI|Web|Online|App|Algorithm|AI|Artificial|Machine|Learning|Robot|Smart|Connected|Internet|信息|数据|算法|智能|网络|平台|Visualization|Graphic|Typography|Style|Inclusive|Accessib"

unreviewed = [a for sid, a in assets.items() if sid not in reviewed]
for label, pat in (("=== 中国/视觉文化方向 ===", pat_china), ("=== 数字/交互/数据方向 ===", pat_digital)):
    print(label)
    hits = [a for a in unreviewed if re.search(pat, a["folder_name"], re.I)]
    for a in sorted(hits, key=lambda x: x["source_id"]):
        print(f"  {a['source_id']} | {a['corpus']} | {a['folder_name'][:64]}")
print("=== 合计 ===")
all_hits = {a["source_id"] for a in unreviewed if re.search(pat_china, a["folder_name"], re.I) or re.search(pat_digital, a["folder_name"], re.I)}
print("候选总数:", len(all_hits))
