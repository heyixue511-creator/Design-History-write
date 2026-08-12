# -*- coding: utf-8 -*-
"""修复 BATCH-032 全部 12 个映射文件为标准 9 列（status 空补齐 / 列错位重组）。"""
import csv
from pathlib import Path

B = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-032-REMAINING\mappings')

def status_for(grade):
    if grade == 'A':
        return 'ACCEPTED_AS_CORE_SOURCE'
    if grade in ('D', 'X'):
        return 'EXCLUDED'
    return 'ACCEPTED_AS_SUPPORTING_SOURCE'

for f in sorted(B.glob('*.csv')):
    with f.open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header = rows[0]
    out = [header]
    info = []
    for row in rows[1:]:
        if not row or all(c == '' for c in row):
            continue
        if len(row) == 9:
            if row[8].strip() == '':
                row[8] = status_for(row[2])
                info.append(f'row {row[0]}@{row[1]} status补齐={row[8]}')
            out.append(row)
        elif len(row) == 11:
            # 模式：id,sid,grade,V2,role,claim,boundary,重复sid,节标题,followup,status
            assert row[7] == row[1], f'{f.name} 行11 校验失败: {row[7]} != {row[1]}'
            out.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[9], row[10]])
            info.append(f'row {row[0]}@{row[1]} 重组(11列): 丢弃[{row[7]},{row[8][:12]}...]')
        elif len(row) == 12:
            # 模式：id,sid,grade,V2,role,claim1,claim2,boundary,重复sid,节标题,followup,status
            assert row[8] == row[1], f'{f.name} 行12 校验失败: {row[8]} != {row[1]}'
            claim = row[5] + ',' + row[6]
            out.append([row[0], row[1], row[2], row[3], row[4], claim, row[7], row[10], row[11]])
            info.append(f'row {row[0]}@{row[1]} 重组(12列): claim合并, 丢弃[{row[8]},{row[9][:12]}...]')
        else:
            raise SystemExit(f'{f.name} 未知列数: {len(row)}')
    with f.open('w', encoding='utf-8-sig', newline='') as fh:
        csv.writer(fh).writerows(out)
    print(f'fixed {f.name}: {len(out)-1} 行')
    for i in info:
        print(f'  {i}')
