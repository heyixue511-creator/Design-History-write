import json
from pathlib import Path

d = json.load(open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch04_structure.json", encoding="utf-8"))
lines = []
for sid, v in d.items():
    g = v["grades"]
    lines.append(f"{sid} {v['count']} A{g.get('A',0)} B{g.get('B',0)} C{g.get('C',0)} D{g.get('D',0)} X{g.get('X',0)}")
    srcs = {}
    for it in v["items"]:
        srcs.setdefault(it["source_id"], []).append(it["grade"])
    lines.append("  " + ", ".join(f"{s}:{'/'.join(gs)}" for s, gs in srcs.items()))
Path(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch04_stats.txt").write_text("\n".join(lines), encoding="utf-8")
