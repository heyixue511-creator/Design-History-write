# -*- coding: utf-8 -*-
"""复验 BATCH-032 映射文件：9 列、status 非空合法、verification=V2、accepted_claim 完整。"""
import csv
from pathlib import Path

B = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-032-REMAINING\mappings')
ok = True
for f in sorted(B.glob('*.csv')):
    with f.open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header = rows[0]
    assert len(header) == 9, f'{f.name} 表头列数 {len(header)}'
    for i, row in enumerate(rows[1:], start=2):
        if len(row) != 9:
            print(f'FAIL {f.name} 行{i}: {len(row)} 列')
            ok = False
            continue
        if row[3] != 'V2':
            print(f'FAIL {f.name} 行{i}: verification={row[3]}')
            ok = False
        if not row[8].strip():
            print(f'FAIL {f.name} 行{i}: status 空')
            ok = False
        if not row[5].strip():
            print(f'FAIL {f.name} 行{i}: accepted_claim 空')
            ok = False
    print(f'{f.name}: {len(rows)-1} 行 OK')
print('ALL PASS' if ok else 'HAS FAILURES')
