import json
from pathlib import Path

REVIEW = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data")
ids = ["B0500", "B0485", "B0493", "B0505", "B0079", "B0469", "B0472", "B0495", "B0514", "B0219", "B0143", "B0465"]
for sid in ids:
    p = REVIEW / f"{sid}_review.json"
    try:
        json.loads(p.read_text(encoding="utf-8"))
        print(f"{sid}: OK")
    except Exception as e:
        print(f"{sid}: FAIL {e}")
        lines = p.read_text(encoding="utf-8").splitlines()
        if len(lines) >= 39:
            print("  line39:", repr(lines[38][:150]))
