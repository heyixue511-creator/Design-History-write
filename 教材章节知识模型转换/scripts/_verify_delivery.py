# -*- coding: utf-8 -*-
"""交付终检：映射格式、来源卡 JSON、矩阵 vs 聚合索引逐节全量对比。"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
BATCH = ROOT / '11_语义复核批次'
AGG = ROOT / '04_文献—章节映射' / '已复核_来源到章节.csv'
MATRIX = ROOT / '06_核心命题—证据矩阵'

LEGAL_SID = re.compile(r'^(\d+\.\d+|C\.0)$')

# ---------- 1) 映射格式 ----------
fmt_errors = []
all_rows = []
for bdir in sorted(BATCH.glob('BATCH-*')):
    mdir = bdir / 'mappings'
    if not mdir.is_dir():
        continue
    for f in sorted(mdir.glob('*.csv')):
        rows = list(csv.DictReader(f.open(encoding='utf-8-sig')))
        for r in rows:
            all_rows.append(r)
            if not LEGAL_SID.match(r.get('section_id', '')):
                fmt_errors.append(f"非法 section_id: {r.get('source_id')}@{r.get('section_id')}")
            if r.get('verification') != 'V2':
                fmt_errors.append(f"verification 非 V2: {r.get('source_id')}@{r.get('section_id')}")
            if not r.get('role') or not r.get('accepted_claim'):
                fmt_errors.append(f"role/accepted_claim 空: {r.get('source_id')}@{r.get('section_id')}")
            if r.get('status') not in ('ACCEPTED_AS_CORE_SOURCE', 'ACCEPTED_AS_SUPPORTING_SOURCE',
                                       'CONTEXT_ONLY', 'EXCLUDED', 'ACCEPTED_WITH_COUNTERSOURCE_REQUIRED',
                                       'ACCEPTED_AS_REFORM_CONTEXT', 'CONTEXT_ONLY_AS_PREHISTORY',
                                       'ACCEPTED_AS_THEORY_SUPPORT', 'ACCEPTED_AS_EARLY_GENEALOGY',
                                       'CONTEXT_ONLY_AS_GENDER_DIMENSION', 'ACCEPTED_AS_CERAMIC_TRADE_CHAIN',
                                       'ACCEPTED_AS_MARKET_MEDIATION', 'ACCEPTED_AS_SUPPORT'):
                fmt_errors.append(f"status 非常规: {r.get('source_id')} {r.get('status')}")

# ---------- 2) 来源卡 JSON ----------
card_errors = []
card_ids = set()
for bdir in sorted(BATCH.glob('BATCH-*')):
    cdir = bdir / 'source_cards'
    if not cdir.is_dir():
        continue
    for f in sorted(cdir.glob('*.json')):
        try:
            d = json.loads(f.read_text(encoding='utf-8'))
            card_ids.add(d.get('source_id', ''))
            if d.get('evidence_level') != 'V2':
                card_errors.append(f"{d.get('source_id')}: evidence_level={d.get('evidence_level')}")
            if d.get('review_status') != 'semantic_review_complete':
                card_errors.append(f"{d.get('source_id')}: review_status={d.get('review_status')}")
        except Exception as e:
            card_errors.append(f"{f.name}: JSON 解析失败 {e}")

map_ids = {r['source_id'] for r in all_rows}
print(f'映射行: {len(all_rows)} / 来源: {len(map_ids)} / 来源卡: {len(card_ids)}')
print(f'格式错误: {fmt_errors if fmt_errors else "无"}')
print(f'来源卡错误: {card_errors if card_errors else "无"}')
print(f'有映射无卡: {sorted(map_ids - card_ids) if map_ids - card_ids else "无"}')
print(f'有卡无映射: {sorted(card_ids - map_ids) if card_ids - map_ids else "无"}')

# ---------- 3) 矩阵 vs 聚合索引逐节对比 ----------
agg = list(csv.DictReader(AGG.open(encoding='utf-8-sig')))
by_section = {}
for r in agg:
    sid = r['section_id']
    by_section.setdefault(sid, []).append(r['source_id'])

mismatch = []
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
            mismatch.append(f"{mf.name} [{sid}]: 矩阵独有 {only_m[:5]} / 聚合独有 {only_a[:5]}")

print(f'矩阵-聚合逐节对比: {len([m for m in mismatch if not m])} 节一致')
print(f'不一致节数: {len(mismatch)}')
for m in mismatch[:20]:
    print('  MISMATCH:', m)
