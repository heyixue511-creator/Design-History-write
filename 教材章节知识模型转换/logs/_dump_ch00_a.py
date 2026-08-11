# -*- coding: utf-8 -*-
import json
from pathlib import Path

s = json.loads(Path(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch00_structure.json").read_text(encoding="utf-8"))
for sid in sorted(s, key=lambda x: float(x)):
    v = s[sid]
    a = sorted(set(x["source_id"] for x in v["items"] if x["grade"] == "A"))
    x = sorted(set(x["source_id"] for x in v["items"] if x["grade"] == "X"))
    print(f"{sid}: total={v['count']} {v['grades']} A级={a} X级={x}")
