import json, io

t = json.load(io.open(r"D:\Design-history-知识库\教材章节知识模型转换\02_总纲知识结构化\章节树.json", encoding="utf-8"))
lines = []
for c in t["chapters"]:
    if c["chapter_id"] in ("CH04", "CH05"):
        lines.append(f"== {c['chapter_id']} {c['title']}")
        for s in c["sections"]:
            lines.append(f"{s['section_id']} | {s['title']} | {s['description']}")
io.open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch04_desc.txt", "w", encoding="utf-8").write("\n".join(lines))
