#!/usr/bin/env python3
"""列出 BATCH-023 候选：薄弱章节方向的未复核来源（CH13 全球化/CH12 伦理/CH15 多元/CH16 数字/CH11 激进）。"""
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

unreviewed = [a for sid, a in assets.items() if sid not in reviewed]
print("已复核:", len(reviewed), "未复核:", len(unreviewed))

pats = {
    "CH13 全球化/制造/品牌": r"Global|Brand|Supply|Manufactur|OEM|Consumer|Corporat|Multinational|China|中国|海尔|联想|华为|产业|Made in",
    "CH12 伦理/生态/参与": r"Ethic|Ecology|Sustainable|Environment|Participat|Feminist|Social|Responsib|Green|Papanek|Packed|Inclusive|Accessib|Community",
    "CH15 批判/推测/多元": r"Critical|Speculat|Future|Design Fiction|Decolon|Plural|Radical|Anti|Utopia|Dystopia|Post-|Transform|Contest",
    "CH16 数字/算法/平台": r"Digital|Algorithm|AI|Artificial|Data|Machine|Internet|Platform|Web|Software|Code|Hacker|Cyber|Network|信息|数字|算法|平台|互联网",
    "CH11 激进/后现代": r"Radical|Postmodern|Memphis|Pop|Punk|Anti-design|Italian|Semiotic|Narrative|Deconstruct|Graphic",
    "CH14 交互/服务/系统": r"Interaction|Service|Interface|User|Usability|UX|HCI|System|Design System|Mobile|App",
}
for label, pat in pats.items():
    hits = sorted([a for a in unreviewed if re.search(pat, a["folder_name"], re.I)], key=lambda x: x["source_id"])
    print(f"\n=== {label}（{len(hits)}）===")
    for a in hits:
        print(f"  {a['source_id']} | {a['corpus']} | {a['folder_name'][:58]}")
