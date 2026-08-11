# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
rev = ROOT / "11_语义复核批次" / "BATCH-009-CH00-INTRO" / "review_data"
rows = []
for p in sorted(rev.glob("*_review.json")):
    j = json.loads(p.read_text(encoding="utf-8"))
    for m in j["maps"]:
        rows.append((m[0], m[1], j["source_id"]))

from collections import defaultdict
sec = defaultdict(list)
grades = defaultdict(int)
for s, g, sid in rows:
    sec[s].append((g, sid))
    grades[g] += 1

out = []
for s in sorted(sec, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    a = sum(1 for g, _ in sec[s] if g == "A")
    b = sum(1 for g, _ in sec[s] if g == "B")
    c = sum(1 for g, _ in sec[s] if g == "C")
    d = sum(1 for g, _ in sec[s] if g == "D")
    srcs = sorted(set(sid for _, sid in sec[s]))
    out.append(f"{s:<5} total={len(sec[s]):<3} A={a} B={b} C={c} D={d} srcs={','.join(srcs)}")
print("\n".join(out))
print("GRADES:", dict(grades), "TOTAL:", len(rows))
