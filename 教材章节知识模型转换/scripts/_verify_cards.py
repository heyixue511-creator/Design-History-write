# -*- coding: utf-8 -*-
"""全库来源卡 JSON 有效性校验（utf-8-sig 容忍 BOM）。"""
import json
from pathlib import Path

ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
BATCH = ROOT / '11_语义复核批次'

fails = []
count = 0
for bdir in sorted(BATCH.glob('BATCH-*')):
    cdir = bdir / 'source_cards'
    if not cdir.is_dir():
        continue
    for f in sorted(cdir.glob('*.json')):
        count += 1
        try:
            d = json.loads(f.read_text(encoding='utf-8-sig'))
            if d.get('evidence_level') != 'V2':
                fails.append(f"{f.name}: evidence_level={d.get('evidence_level')}")
            if d.get('review_status') != 'semantic_review_complete':
                fails.append(f"{f.name}: review_status={d.get('review_status')}")
        except Exception as e:
            fails.append(f"{f.name}: {e}")
print(f'来源卡总数: {count}')
print(f'解析/字段失败: {fails if fails else "无（全部有效）"}')
