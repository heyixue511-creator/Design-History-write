import io

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-007-CH06-EASTASIA\review_data\B0485_review.json"
t = io.open(p, encoding="utf-8").read()
lines = t.splitlines()
ln = lines[38]
# print each char with codepoint around the quotes
for i, ch in enumerate(ln):
    if ch in '"“”「」' or ord(ch) < 32:
        print(i, repr(ch), hex(ord(ch)))
print("LEN", len(ln))
print(ln[:80])
