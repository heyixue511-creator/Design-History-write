# -*- coding: utf-8 -*-
"""dump 多列映射行（列数与每列前 40 字符）。"""
import csv
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
BATCH = ROOT / '11_语义复核批次'

targets = [
    ('BATCH-001-CH01-CH02', 'B0001'), ('BATCH-001-CH01-CH02', 'B0132'), ('BATCH-001-CH01-CH02', 'B0204'),
    ('BATCH-013-CH11-POSTMODERN', 'B0178'), ('BATCH-014-CH12-ETHICS', 'B0151'),
    ('BATCH-014-CH12-ETHICS', 'B0230'), ('BATCH-022-CH16-PLATFORM', 'B0227'),
    ('BATCH-026-CH11-CH13-MATERIAL', 'B0208'), ('BATCH-026-CH11-CH13-MATERIAL', 'B0331'),
    ('BATCH-027-METHOD-VISUAL', 'B0233'),
]
for batch, sid in targets:
    d = BATCH / batch / 'mappings'
    f = list(d.glob(f'{sid}_*.csv'))
    if not f:
        print(f'{batch}/{sid}: 文件缺失')
        continue
    with f[0].open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    print(f'== {batch}/{f[0].name} (ncol={len(rows[0])}) ==')
    for i, row in enumerate(rows[1:], start=2):
        if len(row) != len(rows[0]):
            print(f'  行{i} n={len(row)}: ' + ' | '.join(c[:22] for c in row))
