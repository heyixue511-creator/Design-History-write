#!/usr/bin/env python3
"""列出未复核资产中与 CH16/CH10 相关的下一批候选。"""
import csv
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
assets = {r["source_id"]: r for r in csv.DictReader((ROOT / "03_来源清单与来源卡" / "来源资产总表.csv").open(encoding="utf-8-sig"))}
reviewed = set()
for m in sorted((ROOT / "11_语义复核批次").glob("BATCH-*")):
    for mm in sorted((m / "mappings").glob("*.csv")):
        for r in csv.DictReader(mm.open(encoding="utf-8-sig")):
            reviewed.add(r["source_id"])

print("已复核:", len(reviewed), "未复核:", len(assets) - len(reviewed))
pat = r"China|沈榆|Digital|数字|Bubble|Interaction|Thoughtful|Information|Hybrid|Lever|Data|Dataset|Cloud|Label|Content|Platform|Baidu|Tencent|Alibaba|微信|小米|华为|AI|Artificial|Machine|Learning|Generative|Robot|Smart|Connected|Internet of|智能|算法|数据|平台|人工智能"
unreviewed = [a for sid, a in assets.items() if sid not in reviewed and __import__("re").search(pat, a["folder_name"])]
for a in sorted(unreviewed, key=lambda x: x["source_id"])[:24]:
    print(f"{a['source_id']} | {a['corpus']} | {a['folder_name'][:58]}")
