# -*- coding: utf-8 -*-
"""Dump BATCH-032 列数异常文件的行（按列切分）。"""
import csv
from pathlib import Path

B = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-032-REMAINING\mappings')
for f in sorted(B.glob('*.csv')):
    with f.open(encoding='utf-8-sig') as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = list(reader)
    bad = [r for r in rows if len(r) != len(header)]
    if not bad:
        continue
    print(f'== {f.name} (ncol={len(header)}) ==')
    for r in bad:
        print(f'  n={len(r)} cols:')
        for i, c in enumerate(r):
            print(f'    [{i}] {c[:60]}')
