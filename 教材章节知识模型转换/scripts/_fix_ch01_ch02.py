# -*- coding: utf-8 -*-
"""按聚合索引重算 CH01/CH02 矩阵 CSV 的缺失节（source_ids 与计数），保留人工字段。"""
import csv
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
MATRIX = ROOT / '06_核心命题—证据矩阵'
AGG = ROOT / '04_文献—章节映射' / '已复核_来源到章节.csv'

agg = list(csv.DictReader(AGG.open(encoding='utf-8-sig')))
by_section = {}
for r in agg:
    by_section.setdefault(r['section_id'], []).append(r)

# 需要修复的 (文件名, 节列表)
targets = {
    'CH01_核心命题—来源矩阵.csv': ['1.2', '1.3', '1.4', '1.5', '1.6', '1.7'],
    'CH02_核心命题—来源矩阵.csv': ['2.3', '2.4', '2.5', '2.6'],
}

for fname, sids in targets.items():
    p = MATRIX / fname
    rows = list(csv.DictReader(p.open(encoding='utf-8-sig')))
    for r in rows:
        if r['section_id'] not in sids:
            continue
        agg_rows = by_section.get(r['section_id'], [])
        grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'X': 0}
        srcs_ordered = []
        for gr in ('A', 'B', 'C', 'D', 'X'):
            for ar in agg_rows:
                if ar['grade'] == gr:
                    grade_count[gr] += 1
                    srcs_ordered.append(ar['source_id'])
        total = len(agg_rows)
        # 合并现有 source_ids（保留现有顺序，追加缺失）
        existing = [s for s in r.get('source_ids', '').split(';') if s]
        merged = list(existing)
        for s in srcs_ordered:
            if s not in merged:
                merged.append(s)
        # independent_source_ids：现有 + 缺失的（grade!=X）
        ind_existing = [s for s in r.get('independent_source_ids', '').split(';') if s]
        ind_merged = list(ind_existing)
        for ar in agg_rows:
            if ar['grade'] != 'X' and ar['source_id'] not in ind_merged:
                ind_merged.append(ar['source_id'])
        r['source_ids'] = ';'.join(merged)
        r['independent_source_ids'] = ';'.join(ind_merged)
        r['mapping_rows'] = str(total)
        r['accepted_rows'] = str(total - grade_count['X'])
        r['independent_support_rows'] = str(total - grade_count['X'])
        r['grade_A'] = str(grade_count['A'])
        r['grade_B'] = str(grade_count['B'])
        r['grade_C'] = str(grade_count['C'])
        r['grade_D'] = str(grade_count['D'])
        r['grade_X'] = str(grade_count['X'])
        print(f"{fname} [{r['section_id']}]: rows={total} A{grade_count['A']} B{grade_count['B']} C{grade_count['C']} D{grade_count['D']} X{grade_count['X']} 追加来源={len(merged)-len(existing)}")
    with p.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
print('CH01/CH02 CSV updated')
