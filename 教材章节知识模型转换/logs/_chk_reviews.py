import json
from pathlib import Path

REVIEW = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-005-CH04-BAUHAUS\review_data")
ids = ["B0064", "B0060", "B0182", "B0282", "B0158", "B0464", "B0216", "B0454",
       "B0081", "B0008", "B0517", "B0492", "B0247", "B0048", "B0342"]
for sid in ids:
    p = REVIEW / f"{sid}_review.json"
    try:
        json.loads(p.read_text(encoding="utf-8"))
        print(f"{sid}: OK")
    except Exception as e:
        print(f"{sid}: FAIL {e}")
        lines = p.read_text(encoding="utf-8").splitlines()
        print("  line39:", lines[38][:120] if len(lines) >= 39 else "N/A")
