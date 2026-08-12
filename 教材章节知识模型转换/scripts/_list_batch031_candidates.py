import csv
from pathlib import Path
ROOT = Path(r'D:\Design-history-知识库\教材章节知识模型转换')
assets = {r['source_id']: r for r in csv.DictReader((ROOT/'03_来源清单与来源卡'/'来源资产总表.csv').open(encoding='utf-8-sig'))}
reviewed = set()
for m in sorted((ROOT/'11_语义复核批次').glob('BATCH-*')):
    for mm in sorted((m/'mappings').glob('*.csv')):
        for r in csv.DictReader(mm.open(encoding='utf-8-sig')):
            reviewed.add(r['source_id'])
cand = [a for sid, a in assets.items() if sid not in reviewed]
print('未复核总数:', len(cand))
wanted = ['B0223','B0229','B0433','B0461','B0088','B0095','B0264','B0219','B0004','B0012','B0021','B0031','B0034','B0041','B0051','B0054','B0066','B0071','B0078','B0080','B0085','B0093','B0101','B0106','B0111','B0119','B0127','B0134','B0141','B0149','B0156','B0161','B0168','B0178','B0184','B0193','B0194','B0197','B0205','B0212','B0218','B0220','B0226','B0232','B0238','B0244','B0250','B0257','B0263','B0271','B0275','B0281','B0287','B0294','B0301','B0308','B0315','B0322','B0328','B0335','B0341','B0347','B0354','B0360','B0366','B0372','B0378','B0384','B0390','B0397','B0403','B0408','B0412','B0418','B0424','B0430','B0435','B0441','B0447','B0453','B0457','B0466','B0472','B0478','B0484','B0490','B0496','B0502','P0004','P0012','P0016','P0023','P0028','P0039','P0044','P0051','P0054']
found = [w for w in wanted if w in assets and w not in reviewed]
print('命中的候选:', len(found))
for w in found:
    print(w, '|', assets[w]['folder_name'][:70])
