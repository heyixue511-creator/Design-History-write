#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 13 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("13."):
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

(ROOT / "logs" / "_ch13_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"13.1": "后福特生产与供应链", "13.2": "品牌从标志到体验系统", "13.3": "跨国公司、区域流动与地方市场",
          "13.4": "设计教育、学科史与职业制度恢复", "13.5": "“中国制造”的形成",
          "13.6": "城市化与消费视觉", "13.7": "从制造到创造的政策话语"}
BASELINE = {
    "13.1": "外包、柔性生产、物流和全球分工。",
    "13.2": "产品、空间、广告、服务和组织文化。",
    "13.3": "标准化、适应性设计和文化翻译，以及香港、台湾与内地之间的教育、出版、公司和专业网络。",
    "13.4": "1978年后中国官方教育政策、专业与学科目录、院校建制、设计学院、行业组织和职业网络。",
    "13.5": "OEM、加工贸易、产业集群与隐形设计劳动。",
    "13.6": "广告、包装、企业形象、媒体、北京奥运会等大型公共活动及其场馆、导视和公共空间。",
    "13.7": "自主品牌、文化资源和作者身份；以海尔、联想、华为等企业的可核验产品与品牌档案为候选案例。",
}
JUDGMENT = {
    "13.1": "B0250（快时尚全球链B）、B0105（脚本化即兴B）、B0211（时尚产业劳动C）承担；OEM/加工贸易的产业档案（珠三角工厂记录）未入批——后福特生产的中国侧档案全缺。",
    "13.2": "B0329（企业识别A、三种身份结构A）为品牌理论核心；B0053（价值三路径B）、B0226（形象/身份C）、P0061（服务主导逻辑C）、B0015（苹果范式C）补——品牌体验系统的企业档案仍缺。",
    "13.3": "B0421（设计皆政治B、标准偏见B）承担文化翻译政治；香港/台湾与内地网络专史未入批——区域流动为薄弱节。",
    "13.4": "B0327（职业网络C）、B0105（职业治理C）承担；1978年后教育政策、学科目录、院校建制的官方档案（1998学科目录类）未入——设计教育恢复以政策档案为核心缺口。",
    "13.5": "B0327（非正式经济B）承担中国制造侧；OEM、加工贸易、产业集群专史未入批——隐形设计劳动为P0缺口。",
    "13.6": "B0327（三城叙事B）承担城市化消费视觉核心；B0211（时尚消费C）补；北京奥运会等大型公共活动档案（场馆、导视）未入。",
    "13.7": "B0327（中国性构建B）、B0105（设计政策B）、B0032/B0015（跨章）承担政策话语；海尔/联想/华为企业品牌档案未入批——'从制造到创造'的个案证据为P0缺口。",
}
P0_GAP = {
    "13.1": "OEM/加工贸易产业档案（珠三角工厂）、全球供应链合同与劳动记录、物流与外包数据。",
    "13.2": "企业品牌档案（海尔/联想/华为等候选案例）、品牌手册与体验系统设计文件、品牌价值评估数据。",
    "13.3": "香港/台湾与内地教育、出版、公司、专业网络档案、跨国公司本地化设计文件。",
    "13.4": "1978年后官方教育政策文件、专业与学科目录（1998类）、院校建制档案、设计学院与行业组织记录。",
    "13.5": "OEM订单与合同、加工贸易统计、产业集群档案（珠三角/长三角）、隐形设计劳动记录。",
    "13.6": "广告与包装档案、企业形象设计文件、北京奥运会场馆与导视设计档案、媒体视觉档案。",
    "13.7": "自主品牌档案（海尔/联想/华为产品与品牌记录）、'从制造到创造'政策文件、文化资源与作者身份讨论文献。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十三章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-015含12个来源（企业识别、设计管理、设计政策、中国当代设计、设计政治、时尚、服务逻辑、通论）；与导论/九/十/十一章共享对象时只计一份P0。\n")

for sid in ["13.1", "13.2", "13.3", "13.4", "13.5", "13.6", "13.7"]:
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
with (OUT / "CH13_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH13_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH13 matrix:", {k: v["count"] for k, v in struct.items()})
