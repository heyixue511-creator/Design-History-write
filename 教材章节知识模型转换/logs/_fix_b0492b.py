import io, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-005-CH04-BAUHAUS\review_data\B0492_review.json"
text = io.open(p, encoding="utf-8").read()
try:
    json.loads(text)
    print("VALID")
except json.JSONDecodeError as e:
    print("ERR at line", e.lineno, "col", e.colno, "char", e.pos)
    lo = max(0, e.pos - 80)
    hi = min(len(text), e.pos + 80)
    print("CONTEXT:", repr(text[lo:hi]))
