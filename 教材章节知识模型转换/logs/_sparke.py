import csv

rows = list(csv.DictReader(open(r"D:\Design-history-知识库\教材章节知识模型转换\03_来源清单与来源卡\来源资产总表.csv", encoding="utf-8-sig")))
for r in rows:
    if r["source_id"] in ("B0398", "B0400", "B0401"):
        print(r["source_id"], "|", r["folder_name"][:90])
