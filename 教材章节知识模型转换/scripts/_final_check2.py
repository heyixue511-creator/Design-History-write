# -*- coding: utf-8 -*-
"""交付终检 II：矩阵 MD/CSV 一致、manifest vs 映射文件数、聚合 claim 完整性、audit.md 存在性。"""
import csv
import re
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
BATCH = ROOT / '11_语义复核批次'
MATRIX = ROOT / '06_核心命题—证据矩阵'
AGG = ROOT / '04_文献—章节映射' / '已复核_来源到章节.csv'

print('== 1) 矩阵 MD vs CSV 统计段一致性 ==')
md_csv_mismatch = []
for mf in sorted(MATRIX.glob('CH*_核心命题—来源矩阵.csv')):
    md = mf.with_suffix('.md')
    if not md.exists():
        continue
    mrows = list(csv.DictReader(mf.open(encoding='utf-8-sig')))
    md_text = md.read_text(encoding='utf-8')
    for mr in mrows:
        sid = mr.get('section_id', '')
        rows_n = mr.get('mapping_rows', '')
        if not rows_n or sid.startswith('C.'):
            continue
        # MD 中该节的 **结构统计** 行（格式：**结构统计**：NN条映射；...）
        m = re.search(rf'^## {re.escape(sid)} .*?\n\n.*?\*\*结构统计\*\*：(\d+)条映射', md_text, re.M | re.S)
        if not m:
            md_csv_mismatch.append(f'{mf.name} [{sid}]: MD 无统计段')
            continue
        if m.group(1) != rows_n:
            md_csv_mismatch.append(f'{mf.name} [{sid}]: MD={m.group(1)} CSV={rows_n}')
print(f'MD/CSV 统计数字不一致: {md_csv_mismatch if md_csv_mismatch else "无（全部一致）"}')

print()
print('== 2) 各批次 manifest 行数 vs 映射文件数 ==')
mf_issues = []
for bdir in sorted(BATCH.glob('BATCH-*')):
    mf = bdir / 'batch_manifest.csv'
    mdir = bdir / 'mappings'
    if not mf.exists() or not mdir.is_dir():
        mf_issues.append(f'{bdir.name}: 缺 manifest 或 mappings')
        continue
    mrows = list(csv.DictReader(mf.open(encoding='utf-8-sig')))
    n_maps = len(list(mdir.glob('*.csv')))
    n_manifest = len(mrows)
    n_complete = sum(1 for r in mrows if r.get('semantic_review_status') == 'complete')
    if n_manifest != n_maps or n_complete != n_maps:
        mf_issues.append(f'{bdir.name}: manifest={n_manifest} complete={n_complete} maps={n_maps}')
print(f'manifest/映射不一致: {mf_issues if mf_issues else "无（32 批次全部一致）"}')

print()
print('== 3) 聚合索引 accepted_claim 完整性（修复的 8 个来源抽查） ==')
agg = list(csv.DictReader(AGG.open(encoding='utf-8-sig')))
claim_short = []
for r in agg:
    if r['source_id'] in ('B0178', 'B0151', 'B0230', 'B0227', 'B0208', 'B0331', 'B0233'):
        c = r.get('accepted_claim', '')
        if len(c) < 30:
            claim_short.append(f"{r['source_id']}@{r['section_id']}: claim={c[:40]}")
print(f'claim 过短: {claim_short if claim_short else "无（claim 完整）"}')

print()
print('== 4) audit.md 存在性 ==')
missing_audit = [b.name for b in sorted(BATCH.glob('BATCH-*')) if not (b / 'audit.md').exists()]
print(f'缺 audit.md 的批次: {missing_audit if missing_audit else "无（全部批次均有）"}')
