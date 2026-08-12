# -*- coding: utf-8 -*-
"""更新 BATCH-027-METHOD-VISUAL manifest 为 complete 状态。"""
import csv

p = r'D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-027-METHOD-VISUAL\batch_manifest.csv'
rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
for r in rows:
    r['semantic_review_status'] = 'complete'
    r['mapping_status'] = 'complete'
    r['original_verification_status'] = 'partial_clean_text_spot_check'
with open(p, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print('manifest updated:', len(rows), 'rows')
