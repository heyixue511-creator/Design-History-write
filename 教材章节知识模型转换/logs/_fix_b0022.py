import io, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-006-CH05-COMMERCIAL\review_data\B0022_review.json"
t = io.open(p, encoding="utf-8").read()
t2 = t.replace('["9.x"', '["9.3"')
io.open(p, "w", encoding="utf-8").write(t2)
json.loads(t2)
print("FIXED + VALID" if t2 != t else "NO CHANGE")
