import io

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0485_review.json"
t = io.open(p, encoding="utf-8").read()
lines = t.splitlines()
ln = lines[38]
print("LINE39 repr:")
print(repr(ln[:120]))
# find control chars
for i, ch in enumerate(ln):
    if ord(ch) < 32 and ch not in "\n\r\t":
        print("CTRL at", i, "ord", ord(ch))
