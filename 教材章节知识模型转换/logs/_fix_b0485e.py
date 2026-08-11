import io, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0485_review.json"
t = io.open(p, encoding="utf-8").read()
lines = t.splitlines()
lines[38] = '    "clean第210-299行：附录「中国现代设计35年事记（1978年以来）」",'
t2 = "\n".join(lines)
try:
    json.loads(t2)
    io.open(p, "w", encoding="utf-8").write(t2)
    print("FIXED + VALID")
except json.JSONDecodeError as e:
    print("STILL ERR:", e)
