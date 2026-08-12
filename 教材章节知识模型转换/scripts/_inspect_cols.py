# -*- coding: utf-8 -*-
"""检查 BATCH-031/032 映射文件每行列数与表头列数。"""
import csv
from pathlib import Path

for batch in ['BATCH-031-REMAINING2', 'BATCH-032-REMAINING']:
    B = Path(r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次') / batch / 'mappings'
    print(f'== {batch} ==')
    for f in sorted(B.glob('*.csv')):
        with f.open(encoding='utf-8-sig') as fh:
            reader = csv.reader(fh)
            header = next(reader)
            ncol = len(header)
            bad = []
            for i, row in enumerate(reader, start=2):
                if len(row) != ncol:
                    bad.append((i, len(row)))
            # 每行第 9 列（status）抽样
            statuses = []
            with f.open(encoding='utf-8-sig') as fh:
                reader = csv.reader(fh)
                next(reader)
                for row in reader:
                    if len(row) >= 9:
                        statuses.append(row[8])
            empty_status = sum(1 for s in statuses if not s.strip())
            print(f'{f.name}: ncol={ncol} 行数={len(statuses)} 列数异常={bad if bad else "无"} status空={empty_status}')
