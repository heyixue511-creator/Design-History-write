import io

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-005-CH04-BAUHAUS\review_data\B0492_review.json"
text = io.open(p, encoding="utf-8").read()
lines = text.splitlines()
for i, ln in enumerate(lines):
    stripped = ln.strip()
    if stripped.startswith('"') and stripped.endswith('"') and len(stripped) > 2:
        inner = stripped[1:-1]
        if '"' in inner:
            print("PROBLEM line", i + 1, ":", inner[:120])
