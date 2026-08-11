import io, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0485_review.json"
t = io.open(p, encoding="utf-8").read()
try:
    json.loads(t)
    print("VALID")
except json.JSONDecodeError as e:
    print("ERR line", e.lineno, "col", e.colno, "pos", e.pos)
    lo = max(0, e.pos - 60)
    hi = min(len(t), e.pos + 60)
    print("CTX:", repr(t[lo:hi]))
