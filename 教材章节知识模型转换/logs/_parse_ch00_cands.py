# -*- coding: utf-8 -*-
"""解析 CH00 机器候选,标注已复核来源。"""
import csv
import re
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
cand = (ROOT / "04_文献—章节映射" / "CH00_导论　设计史的对象、证据、时间与叙事_机器候选.md").read_text(encoding="utf-8")

reviewed = set()
for p in (ROOT / "11_语义复核批次").glob("BATCH-*/mappings/*.csv"):
    with p.open(encoding="utf-8-sig", newline="") as h:
        for row in csv.DictReader(h):
            reviewed.add(row["source_id"])

sections = re.split(r"^## ", cand, flags=re.M)
for sec in sections[1:]:
    title = sec.splitlines()[0]
    print(f"=== {title}")
    for m in re.finditer(r"^\| (\d+) \| (B\d{4}|P\d{4}) \| (\w+) \| ([\d.]+) \| (.+?) \|$", sec, flags=re.M):
        rank, sid, ctype, score, name = m.groups()
        if int(rank) <= 8:
            mark = "已复核" if sid in reviewed else "未复核"
            print(f"  {rank:>2} {sid} [{mark}] {score} {name.strip()}")
