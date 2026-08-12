#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 15 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("15."):
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

(ROOT / "logs" / "_ch15_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"15.1": "从产品批评到批判性对象", "15.2": "设计虚构与推测设计", "15.3": "对推测设计的反批评",
          "15.4": "对抗性设计与公共争议", "15.5": "转型设计与系统时间尺度",
          "15.6": "去殖民设计与知识位置", "15.7": "多元世界与自主性"}
BASELINE = {
    "15.1": "对象如何制造陌生化和价值冲突。",
    "15.2": "情境、道具、原型和未来叙事。",
    "15.3": "特定欧美中产经验被普遍化、画廊语境与实际影响证据。",
    "15.4": "设计如何组织而非消除政治冲突。",
    "15.5": "多层系统、长期变迁和行动联盟。",
    "15.6": "谁有权命名问题、保存知识和代表共同体。",
    "15.7": "相互依存、地方世界建构及不可通约性。",
}
JUDGMENT = {
    "15.1": "B0024（批判设计定义A）、B0025（后最优对象A）、B0023（Design Noir A）、B0301（三分法A）构成四核——批判性对象理论闭合；B0017（设计人类学C）、B0065（产品意义C）补。",
    "15.2": "B0024（思辨宣言A、物理虚构A）为核心；B0023（Placebo项目B）、B0025（物质故事B）、B0301（推测类型B）、B0043（分类学B）、B0017（人类学侧C）补——推测设计理论闭合。",
    "15.3": "P0014（反批评A）为对Speculative Everything的系统批评核心；B0301（反艺术话语A、修辞性使用B）、B0043（合法性C）补——反批评双源闭合；画廊语境与实际影响证据仍缺。",
    "15.4": "对抗性设计（DiSalvo）专书未入批——本批B0065资产ID标注DiSalvo但内容为《设计的观念》中译（VGRP012），15.4为最薄弱节。",
    "15.5": "P0013（转型设计B）、P0005（本体论设计B）与B0032（Escobar跨章）承担；CMU转型设计团队系统文献（Irwin/Kossoff）未入——转型设计方法论待补。",
    "15.6": "B0140（去殖民五命题A、三元结构A）为核心；B0032（Escobar跨章B）、P0005（本体论政治B）补——去殖民设计双源闭合。",
    "15.7": "B0024（微观乌托邦B）、B0017（全球人类学C）与B0032（多元宇宙A跨章）承担；'不可通约性'的多元本体论专史未入。",
}
P0_GAP = {
    "15.1": "批判性对象档案（RCA项目、Placebo访谈原始记录）、设计作品图版与展览记录。",
    "15.2": "思辨设计项目档案（United Micro Kingdoms、Foragers）、虚构道具实物与展览记录、推测设计传播效果数据。",
    "15.3": "推测设计的实际影响证据（展览观众数据、政策采纳记录）、画廊语境档案、精英化批评的案例。",
    "15.4": "对抗性设计专书（DiSalvo《Adversarial Design》）、公共争议项目档案（设计组织政治冲突的案例）。",
    "15.5": "CMU转型设计团队系统文献、多层系统转型案例档案、行动联盟记录。",
    "15.6": "去殖民设计实践档案（OCAD集群招聘后续、原住民项目）、知识位置与代表权的社区记录。",
    "15.7": "多元世界设计实践档案（地方世界建构案例）、不可通约性的本体论冲突案例。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十五章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-017含12个来源（思辨设计宣言、批判设计理论、反批评、去殖民设计、转型设计、设计人类学）；与十二/十四章共享对象时只计一份P0。\n")

for sid in ["15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7"]:
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
with (OUT / "CH15_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH15_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH15 matrix:", {k: v["count"] for k, v in struct.items()})
