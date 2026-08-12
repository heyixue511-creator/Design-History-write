#!/usr/bin/env python3
"""统计各批次映射条数分布。"""
import csv
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
total = 0
for m in sorted((ROOT / "11_语义复核批次").glob("BATCH-*")):
    n = 0
    for mm in sorted((m / "mappings").glob("*.csv")):
        n += sum(1 for _ in csv.DictReader(mm.open(encoding="utf-8-sig")))
    total += n
    print(f"{m.name}: {n}")
print("total mappings:", total)
