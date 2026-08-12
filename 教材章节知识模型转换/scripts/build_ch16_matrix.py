#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 16 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("16."):
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

(ROOT / "logs" / "_ch16_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"16.1": "从规则系统到机器学习系统", "16.2": "数据集作为设计材料", "16.3": "推荐、搜索与可见性政治",
          "16.4": "生成式AI与作者制度", "16.5": "自动化界面与人的控制权", "16.6": "隐形劳动与行星基础设施",
          "16.7": "中国平台化生活与设计职业"}
BASELINE = {
    "16.1": "设计对象由确定流程转向概率行为。",
    "16.2": "分类、标注、代表性和历史偏差。",
    "16.3": "排序如何塑造知识、消费和公共文化。",
    "16.4": "共同创作、风格模仿、版权、真实性和专业劳动。",
    "16.5": "解释、纠错、退出、申诉与安全边界。",
    "16.6": "数据标注、内容审核、芯片、云计算、能源、碳、水、矿产、生物多样性、电子废弃物与代际责任。",
    "16.7": "移动支付、电商、短视频、即时配送、智能硬件和设计组织；小米、华为等品牌只在取得可核验材料后作为案例。",
}
JUDGMENT = {
    "16.1": "B0041（二维HCAI框架A）、B0413（理性主义批判A、本体论设计A）、B0423（设计科学纲领A）、B0128（技术理性批判A）、B0287（扩展定义A）构成五核——设计对象转向理论闭合；B0125（增强智能B）、B0128（行动中反思B）、B0423（有限理性B）、B0287（人工物政治B）补；跨章B0001、B0385、B0415等提供历史纵深。",
    "16.2": "B0191（不匹配/排斥循环B、算法排斥C）为本批唯一专源——数据集偏差专书（O'Neil、Benjamin《Race After Technology》等）未入批，为最薄弱节。",
    "16.3": "无本批映射——推荐/搜索可见性政治专源（B0385 Noble跨章已复核、Pasquale等）未入本批，为缺节。",
    "16.4": "P0046（AICAN艺术论证A、媒介论A、图灵测试B）为核心；B0119（批判性设计C）补——生成式AI作者制度双源闭合；版权/训练数据合法性未涉及（P0046作者自认限度）。",
    "16.5": "B0041（控制隐喻A、治理结构A）、B0125（共同基础A、自然交互A）、B0191（能力偏见B）、B0413（承诺对话C）构成四核——自动化界面理论闭合；解释/纠错/申诉的监管文献（GDPR条文等）未入。",
    "16.6": "B0287（可持续模型B）、B0423（社会规划C）为本批仅有两源——隐形劳动（数据标注/内容审核）与行星基础设施（芯片/云计算/能源）专源未入批，为最薄弱节。",
    "16.7": "B0119（非物质化设计B、平台经济C）为本批唯一专源——中国平台经济（移动支付/电商/短视频）专书未入批，小米/华为可核验材料未取得；跨章中国来源（B0327、B0500等）可补。",
}
P0_GAP = {
    "16.1": "AI系统版本与部署档案、机器学习基准数据集文档、算法系统设计文档。",
    "16.2": "数据集偏差专书（O'Neil《Weapons of Math Destruction》、Benjamin《Race After Technology》）、分类/标注规程档案、代表性偏差案例数据集。",
    "16.3": "推荐/搜索系统档案（B0385 Noble已复核跨章）、排序影响研究、平台可见性政策文档。",
    "16.4": "生成式AI训练数据与版权纠纷案卷、AICAN展览记录与图版、视觉图灵测试原始数据（P0046作者自认统计细节缺失）。",
    "16.5": "自动化决策的解释/纠错/申诉机制文档、GDPR第22条等监管条文、AI事故报告（AI Incident Database）。",
    "16.6": "数据标注与内容审核劳动档案、云计算/芯片供应链能源数据、电子废弃物与代际责任数据。",
    "16.7": "中国平台企业可核验材料（小米、华为产品与组织档案）、移动支付/电商/短视频平台数据、设计组织就业与职业结构数据。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十六章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-018含12个来源（人本AI、设计哲学、AI艺术、数字设计文化）；VGRP013/014/015的三组重复以X记录去重，只计一份P0。\n")

for sid in ["16.1", "16.2", "16.3", "16.4", "16.5", "16.6", "16.7"]:
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
with (OUT / "CH16_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH16_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH16 matrix:", {k: v["count"] for k, v in struct.items()})
