# -*- coding: utf-8 -*-
"""最终交付核验汇总：映射格式 / 矩阵-聚合一致 / 来源卡有效 / 聚合数字。"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
BATCH = ROOT / '11_语义复核批次'
AGG = ROOT / '04_文献—章节映射' / '已复核_来源到章节.csv'
MATRIX = ROOT / '06_核心命题—证据矩阵'

LEGAL_SID = re.compile(r'^(\d+\.\d+|C\.0)$')

# 1) 映射格式
fmt_errors = []
rows_all = []
for bdir in sorted(BATCH.glob('BATCH-*')):
    mdir = bdir / 'mappings'
    if not mdir.is_dir():
        continue
    for f in sorted(mdir.glob('*.csv')):
        with f.open(encoding='utf-8-sig', newline='') as fh:
            reader = csv.reader(fh)
            header = next(reader)
            if len(header) != 9:
                fmt_errors.append(f'{bdir.name}/{f.name}: 表头 {len(header)} 列')
            for row in reader:
                if len(row) != 9:
                    fmt_errors.append(f'{bdir.name}/{f.name}: 行 {len(row)} 列')
                    continue
                rows_all.append(row)
                if row[3] != 'V2':
                    fmt_errors.append(f'{bdir.name}/{f.name}: {row[0]} verification={row[3]}')
                if not LEGAL_SID.match(row[1]):
                    fmt_errors.append(f'{bdir.name}/{f.name}: {row[0]} 非法节 {row[1]}')
                if not row[8].strip():
                    fmt_errors.append(f'{bdir.name}/{f.name}: {row[0]} status 空')

# 2) 来源卡
card_errors = []
n_cards = 0
for bdir in sorted(BATCH.glob('BATCH-*')):
    cdir = bdir / 'source_cards'
    if not cdir.is_dir():
        continue
    for f in sorted(cdir.glob('*.json')):
        n_cards += 1
        try:
            d = json.loads(f.read_text(encoding='utf-8-sig'))
            if d.get('evidence_level') != 'V2':
                card_errors.append(f'{f.name}: level={d.get("evidence_level")}')
        except Exception as e:
            card_errors.append(f'{f.name}: {e}')

# 3) 矩阵-聚合一致
agg = list(csv.DictReader(AGG.open(encoding='utf-8-sig')))
by_section = {}
for r in agg:
    by_section.setdefault(r['section_id'], []).append(r['source_id'])
mismatch = []
for mf in sorted(MATRIX.glob('CH*_核心命题—来源矩阵.csv')):
    try:
        mrows = list(csv.DictReader(mf.open(encoding='utf-8-sig')))
    except Exception:
        mismatch.append(f'{mf.name}: 读取失败')
        continue
    for mr in mrows:
        sid = mr.get('section_id', '')
        if sid not in by_section:
            continue
        m_srcs = {s for s in mr.get('source_ids', '').split(';') if s}
        if m_srcs != set(by_section[sid]):
            mismatch.append(f'{mf.name} [{sid}]')

print(f'映射行总数: {len(rows_all)}')
print(f'格式错误: {fmt_errors if fmt_errors else "无"}')
print(f'来源卡: {n_cards} 张, 错误: {card_errors if card_errors else "无"}')
print(f'矩阵-聚合不一致节: {len(mismatch)} {mismatch[:5] if mismatch else ""}')
print(f'聚合索引: {len(agg)} 行 / {len({r["source_id"] for r in agg})} 来源')
