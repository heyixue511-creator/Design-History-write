import csv, io

rows = list(csv.DictReader(open(r"D:\Design-history-知识库\教材章节知识模型转换\03_来源清单与来源卡\来源资产总表.csv", encoding="utf-8-sig")))
keys = ["B0064", "B0060", "B0182", "B0282", "B0158", "B0464", "B0216", "B0454", "B0081", "B0008", "B0517", "B0492", "B0247"]
lines = []
for r in rows:
    if r["source_id"] in keys:
        lines.append(f"{r['source_id']} | {r['folder_name']}")
for r in rows:
    if "De Stijl" in r["folder_name"] or "Blotkamp" in r["folder_name"]:
        lines.append(f"### {r['source_id']} | {r['folder_name']}")
io.open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch04_ids.txt", "w", encoding="utf-8").write("\n".join(lines))
