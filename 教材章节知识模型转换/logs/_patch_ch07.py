import re, io

p = r"D:\Design-history-知识库\教材章节知识模型转换\logs\_tmp_verify_ch05.py"
t = io.open(p, encoding="utf-8").read()
t = t.replace("BATCH-005-CH04-BAUHAUS", "BATCH-007-CH06-EASTASIA")
t = re.sub(r'ids = \[[^\]]*\]', 'ids = ["B0500", "B0485", "B0493", "B0505", "B0079", "B0469", "B0472", "B0495", "B0514", "B0219", "B0143", "B0465"]', t)
io.open(r"D:\Design-history-知识库\教材章节知识模型转换\logs\_tmp_verify_ch07.py", "w", encoding="utf-8").write(t)
print("patched")
