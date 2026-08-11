import re, io

path = r"D:\Design-history-知识库\教材章节知识模型转换\04_文献—章节映射\CH07_第七章　重建与“优良设计”：欧美、日本的战后制度_机器候选.md"
text = io.open(path, encoding="utf-8").read()
sections = re.split(r"^## (7\.\d) ", text, flags=re.M)
for i in range(1, len(sections), 2):
    sid, body = sections[i], sections[i + 1]
    rows = re.findall(r"\|\s*(\d+)\s*\|\s*(B\d{4}|P\d{4})\s*\|\s*(\w+)\s*\|\s*([\d.]+)\s*\|\s*([^|]+)\s*\|", body)
    print(f"== {sid} (total {len(rows)})")
    for rank, sid2, typ, score, folder in rows[8:22]:
        print(f"{rank} {sid2} {score} {folder.strip()}")
