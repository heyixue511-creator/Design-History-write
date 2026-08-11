import io, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0465_review.json"
t = io.open(p, encoding="utf-8").read()
t2 = t.replace('["13", "C"', '["13.7", "C"')
io.open(p, "w", encoding="utf-8").write(t2)
json.loads(t2)
print("FIXED + VALID" if t2 != t else "NO CHANGE")
