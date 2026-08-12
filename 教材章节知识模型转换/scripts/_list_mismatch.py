# -*- coding: utf-8 -*-
"""列出矩阵-聚合不一致的全部节（详细版，不截断）。"""
import csv
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
MATRIX = ROOT / '06_核心命题—证据矩阵'
AGG = ROOT / '04_文献—章节映射' / '已复核_来源到章节.csv'

agg = list(csv.DictReader(AGG.open(encoding='utf-8-sig')))
by_section = {}
for r in agg:
    by_section.setdefault(r['section_id'], []).append(r['source_id'])

for mf in sorted(MATRIX.glob('CH*_核心命题—来源矩阵.csv')):
    mrows = list(csv.DictReader(mf.open(encoding='utf-8-sig')))
    for mr in mrows:
        sid = mr.get('section_id', '')
        if sid not in by_section:
            continue
        m_srcs = {s for s in mr.get('source_ids', '').split(';') if s}
        a_srcs = set(by_section[sid])
        if m_srcs != a_srcs:
            only_m = sorted(m_srcs - a_srcs)
            only_a = sorted(a_srcs - m_srcs)
            print(f'{mf.name} [{sid}]: 矩阵多 {only_m[:6]} / 矩阵缺 {only_a[:8]}')
