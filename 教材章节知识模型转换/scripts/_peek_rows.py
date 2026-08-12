# -*- coding: utf-8 -*-
"""查看 BATCH-031 正常映射文件（B0433）与 BATCH-032 7 个 status 空文件（B0286）的行。"""
import csv
from pathlib import Path

B31 = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-031-REMAINING2\mappings\B0433_章节映射.csv')
B32 = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-032-REMAINING\mappings\B0286_章节映射.csv')

print('== B0433 (BATCH-031 正常) ==')
with B31.open(encoding='utf-8-sig') as fh:
    for row in csv.reader(fh):
        print(f'n={len(row)}: [0]{row[0]} [1]{row[1]} [2]{row[2]} [3]{row[3]} [4]{row[4]} [5]{row[5][:30]}... [6]{row[6][:30]} [7]{row[7][:30]} [8]{row[8]}')

print()
print('== B0286 (BATCH-032 status 空) ==')
with B32.open(encoding='utf-8-sig') as fh:
    for row in csv.reader(fh):
        print(f'n={len(row)}: [0]{row[0]} [1]{row[1]} [2]{row[2]} [3]{row[3]} [4]{row[4]} [5]{row[5][:30]}... [6]{row[6][:30]} [7]{row[7][:30]} [8]={row[8] if len(row)>8 else "MISSING"}')
