#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 9 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("9."):
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

(ROOT / "logs" / "_ch09_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"9.1": "丰裕社会与消费公民", "9.2": "厨房、家电与家庭劳动", "9.3": "性别化职业与物品",
          "9.4": "青年文化、亚文化使用与商业吸收", "9.5": "企业形象的系统化",
          "9.6": "瑞士平面与国际主义传播", "9.7": "信息设计、公共可读性与使用者能动性"}
BASELINE = {
    "9.1": "收入、零售、广告和耐用消费品。",
    "9.2": "效率承诺如何重新分配而非简单消除劳动。",
    "9.3": "谁设计、谁使用、谁被代表。",
    "9.4": "音乐、服装、杂志和短周期商品；区分参与者自我认同、媒体命名、改装／收藏与后来的商业吸收、学术解释。",
    "9.5": "标志、字体、包装、建筑和内部规范。",
    "9.6": "网格、客观性与组织权威。",
    "9.7": "Isotype、交通导视、跨语言沟通，以及选择、维修、拒绝和再利用。",
}
JUDGMENT = {
    "9.1": "B0431（Packard计划报废原典A级）与B0202（Baudrillard符号消费A级）构成批判双核，B0203（物体系）、B0315（再语境化）、B0367（商品文化前史）、B0001（百货商店）补理论侧；B0142（日常消费）提供实践理论修正；消费理论侧已闭合，消费制度档案（零售/信贷）仍缺。",
    "9.2": "B0142（厨房'拥有—做'动态A级）与B0431（质量劣化）、B0203（模型/系列）构成核心；'效率承诺重新分配而非消除劳动'的档案侧（家务时间数据）仍缺。",
    "9.3": "B0001（购物女性化）与B0120（设计语言性别讯息）承担B/C级；女性设计职业与使用者的专史未入批，为本章薄弱节。",
    "9.4": "B0367（消费主体）、B0120（时尚产业模型）、B0441（时尚再估值）、B0486（波普中文侧）承担C级；亚文化使用（改装/收藏/商业吸收）的专史未入批。",
    "9.5": "B0180（设计文化三角A级）与B0357（设计管理矩阵）构成核心；企业形象个案（Oliins、品牌系统）的档案侧仍缺。",
    "9.6": "瑞士平面与国际主义无专史入批——全章最薄节，网格/客观性/组织权威的专门研究为P0缺口。",
    "9.7": "B0142（实践导向设计A级）与B0315（消费者能动性）构成核心；Isotype、交通导视的档案侧（与B0081共享）未入本批。",
}
P0_GAP = {
    "9.1": "零售年报与信贷档案（Sears、Woolworth）、广告支出统计、消费者家庭账簿、耐用消费品产量数据。",
    "9.2": "家务时间调查原始数据（Vanek类）、家电产品目录与广告原件、厨房改造访谈档案（Shove类）。",
    "9.3": "女性设计职业档案（室内装饰、橱窗、广告）、性别化广告图像档案、使用者性别统计。",
    "9.4": "青年亚文化刊物原件（时尚杂志、乐迷杂志）、改装与收藏记录、商业吸收（广告采用）档案。",
    "9.5": "企业形象设计档案（Oliins、品牌手册）、标志与字体规范原件、企业内部设计规范文件。",
    "9.6": "瑞士平面设计专史（网格、国际主义）、瑞士设计学校档案（巴塞尔、苏黎世）、国际主义传播文件。",
    "9.7": "Isotype档案（与B0081共享）、交通导视系统设计文件、公共信息设计案例、维修与再利用档案。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第九章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-011含12个来源（消费批判、消费理论、实践理论、设计管理、百货商店史、中文通史）；与导论/二/五章共享对象时只计一份P0。\n")

for sid in ["9.1", "9.2", "9.3", "9.4", "9.5", "9.6", "9.7"]:
    if sid not in struct:
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
with (OUT / "CH09_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH09_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH09 matrix:", {k: v["count"] for k, v in struct.items()})
