# -*- coding: utf-8 -*-
import json
from pathlib import Path

s = json.loads(Path(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_ch07_structure.json").read_text(encoding="utf-8"))
for sid in ["7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7"]:
    v = s[sid]
    print(f"=== {sid} 共{v['count']}条 {v['grades']}")
    for x in v["items"]:
        if x["grade"] in ("A", "X"):
            print(f"  {x['grade']} {x['source_id']} | {x['role']} | {x['status']}")
