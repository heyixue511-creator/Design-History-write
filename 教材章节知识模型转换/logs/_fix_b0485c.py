import io, json, re

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0485_review.json"
t = io.open(p, encoding="utf-8").read()
lines = t.splitlines()
# fix line 39 (index 38): inner ASCII quotes -> corner brackets
ln = lines[38]
fixed = re.sub(r'附录"([^"]+)"', lambda m: "附录「" + m.group(1) + "」", ln)
lines[38] = fixed
t2 = "\n".join(lines)
try:
    json.loads(t2)
    io.open(p, "w", encoding="utf-8").write(t2)
    print("FIXED + VALID")
except json.JSONDecodeError as e:
    print("STILL ERR:", e)
