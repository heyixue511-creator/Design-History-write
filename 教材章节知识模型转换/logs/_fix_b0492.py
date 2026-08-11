import io, re, json

p = r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-005-CH04-BAUHAUS\review_data\B0492_review.json"
text = io.open(p, encoding="utf-8").read()

# fix: 《对"工艺美术"的诘难》 ASCII quotes -> curly quotes
fixed = text.replace('《对"工艺美术"的诘难》', "《对“工艺美术”的诘难》")

# scan remaining problematic inner ASCII quotes on json string lines
lines = fixed.splitlines()
issues = []
for i, ln in enumerate(lines):
    stripped = ln.strip()
    core = stripped[:-1] if stripped.endswith(",") else stripped
    if core.startswith('"') and core.endswith('"') and len(core) > 2:
        inner = core[1:-1]
        if '"' in inner:
            issues.append((i + 1, inner[:120]))
if issues:
    print("REMAINING ISSUES:")
    for n, s in issues:
        print(n, s)
else:
    json.loads(fixed)  # validate
    io.open(p, "w", encoding="utf-8").write(fixed)
    print("FIXED + VALID")
