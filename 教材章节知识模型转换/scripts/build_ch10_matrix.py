#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 10 sections -> structure JSON + matrix."""
import csv, json
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

sections = defaultdict(list)
for batch_dir in sorted((ROOT / "11_语义复核批次").glob("BATCH-*")):
    for m in sorted((batch_dir / "mappings").glob("*.csv")):
        with m.open(encoding="utf-8-sig", newline="") as h:
            for row in csv.DictReader(h):
                if row["section_id"].startswith("10."):
                    sections[row["section_id"]].append(row)

struct = {}
for sid in sorted(sections, key=lambda s: (int(s.split(".")[0]), int(s.split(".")[1]))):
    rows = sections[sid]
    grades = defaultdict(int)
    for r in rows:
        grades[r["grade"]] += 1
    items = []
    for r in sorted(rows, key=lambda x: (x["grade"], x["source_id"])):
        src = r["source_id"]
        items.append({"source_id": src, "title": assets.get(src, {}).get("folder_name", src),
                      "grade": r["grade"], "verification": r["verification"], "role": r["role"],
                      "accepted_claim": r["accepted_claim"], "evidence_boundary": r["evidence_boundary"],
                      "status": r["status"]})
    struct[sid] = {"grades": dict(grades), "count": len(rows), "items": items}

(ROOT / "logs" / "_ch10_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"10.1": "制度重组与术语延续", "10.2": "计划生产中的设计劳动", "10.3": "轻工业与日用品",
          "10.4": "大型公共活动与公共建筑", "10.5": "宣传视觉与出版系统",
          "10.6": "工艺美术与民族形式", "10.7": "短缺、政治变动与专业适应"}
BASELINE = {
    "10.1": "院校、行业部门、研究所及'工艺美术'范畴。",
    "10.2": "任务来源、设计室、样品、审批、定型与批量生产。",
    "10.3": "纺织、陶瓷、家具、搪瓷、钟表和包装。",
    "10.4": "全运会及其场馆、展览空间、公共建筑、导视系统与公共服务设施。",
    "10.5": "招贴、连环画、报刊、字体和公共空间。",
    "10.6": "传统技艺、出口创汇、地方组织和文化表述。",
    "10.7": "耐用、代用材料、修理和再利用，以及专业知识的中断、转化和隐性延续。",
}
JUDGMENT = {
    "10.1": "B0511（1998年'艺术设计'替代'工艺美术'B级）与B0476（设计功能本位）、B0488（外来学科移植）、B0479、B0512、B0468构成术语演进谱系；制度档案（1998学科目录原始文件、院校沿革档案）仍缺，'工艺美术'范畴的官方界定未闭合。",
    "10.2": "B0483（原始工业化宏观背景）仅C级；计划生产中设计劳动（任务来源、设计室、样品、审批、定型）的档案侧全缺——全章最薄节。",
    "10.3": "B0499（产品图案B级）承担日用品图案侧；工业设计侧仅B0468（C级教材参照）；轻工业产品档案（搪瓷、钟表、包装）未入。",
    "10.4": "B0516（室内设计三阶段B级）与B0499（建筑图案C级）、B0488（C级）承担；全运会场馆、导视系统等公共活动的专门研究未入批。",
    "10.5": "B0471（毛泽东时代文字设计B级）与B0499（文宣/票证B级）、B0501（国际主义对照C级）构成核心；前期批次已复核的B0266（宣传画）与B0219（漫画）跨章补强；招贴、连环画专史仍缺。",
    "10.6": "B0499（民间图案B级）与B0511（民族文化立场C级）、B0479（物用观C级）承担；出口创汇与地方组织的档案侧（工艺美术出口档案）未入——10.6为本章第二薄节。",
    "10.7": "B0483（工业化顺序C级）、B0516（背景决定论C级）、B0512（1990年代末专业适应C级）承担；短缺经济中的修理、代用材料与专业知识中断的专门研究未入批。",
}
P0_GAP = {
    "10.1": "1998年学科目录原始文件、院校沿革档案（中央工艺美术学院等）、行业部门（轻工业部）文件、'工艺美术'范畴的官方界定文件。",
    "10.2": "设计室档案（任务来源、样品、审批、定型记录）、轻工业部设计院所档案、批量生产与劳动记录。",
    "10.3": "轻工业产品档案（搪瓷、钟表、陶瓷、包装）、产品目录与样品、企业设计记录。",
    "10.4": "全运会场馆设计档案、展览空间与导视系统设计文件、十大建筑委托与建设档案。",
    "10.5": "招贴与连环画出版档案、报刊字体规范文件、文字改革文件（直排改横排）、公共空间视觉档案。",
    "10.6": "工艺美术出口档案（广交会、出口创汇记录）、地方工艺美术组织文件、传统技艺传承记录。",
    "10.7": "短缺经济中的代用材料档案、修理与再利用记录、专业知识中断与延续的口述史。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-012含12个来源（中国艺术设计通史、图案图录、文字设计、工艺美术理论、工业设计教材、平面设计史、经济史、室内设计史、设计理论）；与第六/八章共享中国设计对象时只计一份P0。\n")

for sid in ["10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "10.7"]:
    if sid not in struct:
        md_lines.append(f"## {sid} {TITLES[sid]}\n**结构统计**：0条映射。\n")
        continue
    v = struct[sid]
    g = v["grades"]
    accepted = v["count"] - g.get("X", 0)
    rows = sorted(v["items"], key=lambda x: x["source_id"])
    src_ids = ";".join(x["source_id"] for x in rows)
    indep_ids = ";".join(x["source_id"] for x in rows if x["grade"] != "X")
    csv_rows.append({
        "section_id": sid, "section_title": TITLES[sid], "baseline_claim": BASELINE[sid],
        "mapping_rows": v["count"], "accepted_rows": accepted, "independent_support_rows": accepted,
        "grade_A": g.get("A", 0), "grade_B": g.get("B", 0), "grade_C": g.get("C", 0),
        "grade_D": g.get("D", 0), "grade_X": g.get("X", 0), "verification": "V2 only",
        "source_ids": src_ids, "independent_source_ids": indep_ids,
        "audit_judgment": JUDGMENT[sid], "p0_gap": P0_GAP[sid], "gap_priority": "P0", "writing_gate": "RESEARCH_ROUTING_ONLY"})
    md_lines.append(f"## {sid} {TITLES[sid]}\n")
    md_lines.append(f"**总纲命题**：{BASELINE[sid]}\n")
    md_lines.append(f"**结构统计**：{v['count']}条映射；A {g.get('A',0)}、B {g.get('B',0)}、C {g.get('C',0)}、D {g.get('D',0)}、X {g.get('X',0)}；排除X及重复支持后，{accepted}条可独立承担不同命题角色的来源记录。\n")
    md_lines.append(f"**独立判断**：{JUDGMENT[sid]}\n")
    md_lines.append("| 来源 | 题名 | 等级 | 角色 | 状态 |\n|---|---|---|---|---|")
    for x in rows:
        md_lines.append(f"| {x['source_id']} | {x['title']} | {x['grade']}／V2 | {x['role']} | {x['status']} |")
    md_lines.append(f"\n**P0缺口**：{P0_GAP[sid]}。\n")
    md_lines.append("**准入门**：`RESEARCH_ROUTING_ONLY`。在至少完成核心命题的原文页码、关键P0及对象／图版核验前，不升级为可定稿正文。\n")

fields = ["section_id", "section_title", "baseline_claim", "mapping_rows", "accepted_rows", "independent_support_rows",
          "grade_A", "grade_B", "grade_C", "grade_D", "grade_X", "verification", "source_ids",
          "independent_source_ids", "audit_judgment", "p0_gap", "gap_priority", "writing_gate"]
with (OUT / "CH10_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH10_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH10 matrix:", {k: v["count"] for k, v in struct.items()})
