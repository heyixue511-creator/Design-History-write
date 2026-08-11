import csv, hashlib, io

rows = list(csv.DictReader(open(r"D:\Design-history-知识库\教材章节知识模型转换\03_来源清单与来源卡\来源资产总表.csv", encoding="utf-8-sig")))
keys = ["B0073", "B0436", "B0206", "B0205", "B0066", "B0409", "B0410", "B0145", "B0186",
        "B0022", "B0345", "B0400", "B0401", "B0433", "B0515", "B0162"]
lines = []
for r in rows:
    if r["source_id"] in keys:
        p = r["clean_source_path"]
        try:
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
        except Exception:
            h = "ERR"
        lines.append(f"{r['source_id']} | {h} | {r['folder_name']}")
io.open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch05_ids.txt", "w", encoding="utf-8").write("\n".join(lines))
