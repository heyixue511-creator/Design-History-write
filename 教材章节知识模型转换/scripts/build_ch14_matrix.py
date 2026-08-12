#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 14 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("14."):
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

(ROOT / "logs" / "_ch14_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"14.1": "从计算工具到软件媒介", "14.2": "图形用户界面与交互范式", "14.3": "HCI与设计方法的汇合",
          "14.4": "网络、网页与移动交互", "14.5": "服务设计与组织流程",
          "14.6": "设计系统与平台规模化", "14.7": "数据化商业模式及其边界"}
BASELINE = {
    "14.1": "批处理、个人计算、数字创作工具与“软件化”的设计对象。",
    "14.2": "桌面隐喻、直接操控、可见性及用户行动路径。",
    "14.3": "可用性、认知模型、参与式方法、用户研究和原型如何进入专业流程。",
    "14.4": "超文本、浏览器、开放标准、触屏、位置和持续连接。",
    "14.5": "触点、旅程、前台／后台，以及设计如何进入跨部门协作。",
    "14.6": "组件、接口、版本管理、组织协同和平台规则。",
    "14.7": "注意力、个性化、暗黑模式、内容生产与平台劳动。",
}
JUDGMENT = {
    "14.1": "B0274（元媒介A、文化软件史A）为核心——软件研究理论闭合；B0046（硬件史B）、B0054（软件设计史C）、B0122（数字理论B）补——个人计算与数字创作工具的档案（PARC、Macintosh）仍缺。",
    "14.2": "B0046（GUI历史A、交互原则A）为核心；B0096（设计法则B）、B0280（无品质材料B）、B0122（理论谱系B）、B0011（历史C）补——桌面隐喻与直接操控的原始档案（PARC内部文献）仍缺。",
    "14.3": "全章最强节：B0046（人+原型A）、B0087（情境调查B）、B0011（目标导向B）、B0096（四方法论B）、B0184（教科书B）、B0280（深思立场B）、B0054（软件宣言B）——HCI与设计方法汇合双源闭合；可用性测试档案仍缺。",
    "14.4": "B0122（编码未来B）承担网络前沿；网页/移动交互专史（浏览器、触屏）未入批——14.4为薄弱节。",
    "14.5": "B0294（五原则A、工具A）为服务设计核心；B0046（触点前史B）补——服务设计组织流程档案（跨部门协作案例）仍缺。",
    "14.6": "B0011（设计原则B）、B0122（范式转换C）承担；设计系统（组件库、版本管理、平台规则）专史未入批——14.6为最薄节。",
    "14.7": "B0385（压迫算法A、搜索偏见案例A）为核心——数据化商业模式批判闭合；B0096（设计伦理C）、B0184（FATE C）、P0061（价值共创C跨章）补——平台劳动与暗黑模式的量化档案仍缺。",
}
P0_GAP = {
    "14.1": "PARC内部文献（Alto/Star设计文件）、Macintosh人机交互指南、个人计算与数字创作工具档案。",
    "14.2": "桌面隐喻原始档案（Mott餐巾纸草图类）、GUI设计文件（Xerox、Apple）、可用性测试原始记录。",
    "14.3": "可用性测试档案、参与式设计项目记录（斯堪的纳维亚）、用户研究原始数据。",
    "14.4": "浏览器与开放标准档案（Mosaic、W3C）、触屏与移动交互设计文件、持续连接技术档案。",
    "14.5": "服务设计组织流程档案（跨部门协作案例）、触点与旅程工具原始文件、前台后台运作记录。",
    "14.6": "设计系统档案（组件库、版本管理）、平台规则文件（应用商店审核、API规范）、组织协同记录。",
    "14.7": "平台劳动数据（内容审核、零工）、暗黑模式设计档案、注意力经济统计、个性化算法文件。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十四章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-016含12个来源（软件研究、交互设计口述史、情境化设计、目标导向设计、服务设计、交互教科书、算法歧视）；与十三/十五章共享对象时只计一份P0。\n")

for sid in ["14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7"]:
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
with (OUT / "CH14_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH14_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH14 matrix:", {k: v["count"] for k, v in struct.items()})
