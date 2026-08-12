# -*- coding: utf-8 -*-
"""修复 8 个多列映射文件：拼接 accepted_claim 拆列段、归位最后 3 列、删除空行。"""
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

def status_for(grade):
    if grade == 'A':
        return 'ACCEPTED_AS_CORE_SOURCE'
    if grade in ('D', 'X'):
        return 'EXCLUDED'
    return 'ACCEPTED_AS_SUPPORTING_SOURCE'

for batch, sid in targets:
    d = BATCH / batch / 'mappings'
    files = list(d.glob(f'{sid}_*.csv'))
    if not files:
        print(f'{batch}/{sid}: 文件缺失')
        continue
    p = files[0]
    with p.open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header = rows[0]
    out = [header]
    fixed = 0
    for row in rows[1:]:
        if not row or all(c == '' for c in row):
            continue  # 删除空行
        if len(row) == 9:
            out.append(row)
        elif len(row) > 9:
            claim = ','.join(row[5:len(row)-3])
            boundary = row[len(row)-3]
            followup = row[len(row)-2]
            status = row[len(row)-1]
            if not status.startswith('ACCEPTED') and not status.startswith('EXCLUDE') and not status.startswith('CONTEXT'):
                status = status_for(row[2])
            out.append([row[0], row[1], row[2], row[3], row[4], claim, boundary, followup, status])
            fixed += 1
        else:
            print(f'{batch}/{sid}: 行列数异常 {len(row)}')
    with p.open('w', encoding='utf-8-sig', newline='') as fh:
        csv.writer(fh).writerows(out)
    print(f'{batch}/{p.name}: 修复 {fixed} 行, 总行 {len(out)-1}')
