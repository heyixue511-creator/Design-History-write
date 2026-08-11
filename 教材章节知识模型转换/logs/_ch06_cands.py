import re, io

path = r"D:\Design-history-知识库\教材章节知识模型转换\04_文献—章节映射\CH06_第六章　东亚转译与中国现代设计的形成（1895—1949）_机器候选.md"
text = io.open(path, encoding="utf-8").read()
sections = re.split(r"^## (6\.\d) ", text, flags=re.M)
lines = []
for i in range(1, len(sections), 2):
    sid, body = sections[i], sections[i + 1]
    rows = re.findall(r"\|\s*(\d+)\s*\|\s*(B\d{4}|P\d{4})\s*\|\s*(\w+)\s*\|\s*([\d.]+)\s*\|\s*([^|]+)\s*\|", body)
    top = rows[:8]
    lines.append(f"== {sid}")
    for rank, sid2, typ, score, folder in top:
        lines.append(f"{rank} {sid2} {score} {folder.strip()}")
io.open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch06_cands.txt", "w", encoding="utf-8").write("\n".join(lines))
