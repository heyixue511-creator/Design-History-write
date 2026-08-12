import csv
from pathlib import Path
ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
B = ROOT / '11_语义复核批次' / 'BATCH-031-REMAINING2'
STD = ['source_id', 'section_id', 'grade', 'verification', 'role', 'accepted_claim', 'evidence_boundary', 'original_followup', 'status']

def status_for(grade):
    if grade == 'A':
        return 'ACCEPTED_AS_CORE_SOURCE'
    return 'ACCEPTED_AS_SUPPORTING_SOURCE'

for mp in sorted((B / 'mappings').glob('*_章节映射.csv')):
    with mp.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        out.append({
            'source_id': r['source_id'],
            'section_id': r['section_id'],
            'grade': r['grade'],
            'verification': r.get('verification', 'V2'),
            'role': r['role'],
            'accepted_claim': r['key_claims'],
            'evidence_boundary': r['evidence_location'],
            'original_followup': r['notes'],
            'status': status_for(r['grade']),
        })
    with mp.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=STD)
        w.writeheader()
        w.writerows(out)
    print('converted:', mp.name, len(out))
