#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 12 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("12."):
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

(ROOT / "logs" / "_ch12_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"12.1": "从职业伦理到社会批判", "12.2": "帕帕奈克与真实世界", "12.3": "环境设计与生命周期",
          "12.4": "参与式设计的北欧传统", "12.5": "通用设计与残障社会模型",
          "12.6": "女性主义设计批评", "12.7": "社会创新、社区设计与正义"}
BASELINE = {
    "12.1": "设计服务市场的合法性危机。",
    "12.2": "社会需求、低成本技术及其家长主义争议。",
    "12.3": "能源、材料、污染、耐用、维修和废弃。",
    "12.4": "工作场所民主、共同设计和知识分配。",
    "12.5": "从'特殊使用者'转向制度性障碍。",
    "12.6": "家庭劳动、身体经验、照护与知识位置。",
    "12.7": "地方能力、共创、代表权、决策权、利益冲突及项目退出后的持续性。",
}
JUDGMENT = {
    "12.1": "B0434（帕帕奈克宣言A跨章）、B0406（好设计即好公民B）、B0418（设计哲学B）、B0032（本体论批判B）、B0230（技术先行批判B）构成职业伦理到社会批判的谱系；'合法性危机'的行业档案（设计职业协会争议）仍缺。",
    "12.2": "B0434（真实世界宣言A、五神话六方向A）为核心——帕帕奈克原典闭合；家长主义争议（'为需要设计'的决策权）以B0032/12.7为对照；低成本技术案例（罐头盒收音机）为行动者自述。",
    "12.3": "B0420（绿色律令A）与B0110（去未来化B）、B0230（设计正念B）、B0418（持存C）、B0434（Kleenex文化B）构成环境设计谱系；LCA/DFD的工程档案（产品生命周期数据）仍缺。",
    "12.4": "B0347（北欧传统B、persona基础设施B）承担；参与式设计原典（Ehn/Kyng）未入批——工作场所民主与知识分配的总纲命题待补。",
    "12.5": "全章最强节：B0138（新定义A、障碍社会建构A）＋B0460（手册B）、B0174（社会模型B、包容批评B）——通用设计双源闭合；残障制度档案（ADA、Olmstead判决）仍缺。",
    "12.6": "前期跨章积累（B0183/B0240/B0273/B0440四项女性主义）＋B0434（消费者权利C）、B0420（原住民智慧C）——女性主义设计批评专史仍未入批，为12.6短板。",
    "12.7": "B0151（散在/专家A、协作组织A）与B0032（自主性设计A、多元宇宙A）双A核心；B0230（感知回应B）、B0406（行动主义C）、B0347（社会政治C）补；代表权/利益冲突的社区案例档案仍缺。",
}
P0_GAP = {
    "12.1": "设计职业协会伦理争议档案、设计服务市场数据、行业自律文件。",
    "12.2": "Papanek低成本技术项目档案（罐头盒收音机）、'为需要设计'的受益者记录、家长主义争议文献。",
    "12.3": "产品生命周期数据（LCA）、能源与材料档案、污染与废弃记录、德国包装法等制度文件。",
    "12.4": "参与式设计原典（Ehn/Kyng UTOPIA）、斯堪的纳维亚工作场所民主档案、共同设计项目记录。",
    "12.5": "ADA/Olmstead判决等残障制度档案、通用设计评估数据、无障碍标准文件。",
    "12.6": "女性主义设计批评专史（Buckley之外）、家庭劳动与照护设计档案、女性设计职业数据。",
    "12.7": "社区设计项目档案（代表权、决策权、利益冲突）、项目退出后的持续性与失败记录、社会创新评估数据。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十二章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-014含12个来源（设计伦理原典、生态设计、通用设计、社会创新、参与式设计、设计哲学）；与导论/五/七/十一章共享对象时只计一份P0。\n")

for sid in ["12.1", "12.2", "12.3", "12.4", "12.5", "12.6", "12.7"]:
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
with (OUT / "CH12_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH12_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH12 matrix:", {k: v["count"] for k, v in struct.items()})
