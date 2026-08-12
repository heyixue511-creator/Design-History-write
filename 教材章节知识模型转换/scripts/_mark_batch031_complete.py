import csv
import json
from pathlib import Path
ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
B = ROOT / '11_语义复核批次' / 'BATCH-031-REMAINING2'

# 1) 校验 12 cards + 12 mappings 完整性
cards = sorted((B/'source_cards').glob('*_来源卡.json'))
maps = sorted((B/'mappings').glob('*_章节映射.csv'))
assert len(cards) == 12 and len(maps) == 12, (len(cards), len(maps))
for c in cards:
    d = json.loads(c.read_text(encoding='utf-8'))
    assert d['review_status'] == 'semantic_review_complete' and d['evidence_level'] == 'V2'
    for cs in d['candidate_sections']:
        assert cs['grade'] in ('A', 'B', 'C'), (c.name, cs)
# 2) 映射行数与等级统计
rows = []
for m in maps:
    rows += list(csv.DictReader(m.open(encoding='utf-8-sig')))
print('mapping rows:', len(rows))
from collections import Counter
g = Counter(r['grade'] for r in rows)
print('grades:', dict(g))
# 3) manifest 标记 complete
mp = B / 'batch_manifest.csv'
out = []
with mp.open(encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        r['semantic_review_status'] = 'complete'
        out.append(r)
with mp.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print('manifest complete:', len(out))
