#!/usr/bin/env python3
"""Aggregate all reviewed mappings for chapter 11 sections -> structure JSON + matrix."""
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
                if row["section_id"].startswith("11."):
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

(ROOT / "logs" / "_ch11_structure.json").write_text(json.dumps(struct, ensure_ascii=False, indent=1), encoding="utf-8")

TITLES = {"11.1": "现代主义危机的社会条件", "11.2": "波普与日常商品", "11.3": "意大利激进设计与反设计",
          "11.4": "建筑的复杂、矛盾与符号", "11.5": "孟菲斯及对象的叙事化",
          "11.6": "朋克、自出版与亚文化图形", "11.7": "后现代的全球传播与边界"}
BASELINE = {
    "11.1": "城市更新、消费社会、青年反叛与媒体扩张。",
    "11.2": "高低文化边界、复制和消费图像。",
    "11.3": "对家庭、商品和专业制度的戏仿。",
    "11.4": "从纯粹功能转向历史、地域和大众传播。",
    "11.5": "色彩、表面、游戏和市场。",
    "11.6": "低技术生产、青年身份与商业吸收；不把某一视觉符号直接等同于统一的政治立场。",
    "11.7": "不同地区如何选择性使用后现代语言。",
}
JUDGMENT = {
    "11.1": "B0372（商业乡土正名B）、B0373（Main Street正名B）、B0071（单一价内容B）、B0368（共谋性批判C）构成社会条件论述；B0176（三大议题C）补框架；城市更新/青年反叛的专门档案（Pruitt-Igoe档案类）仍缺。",
    "11.2": "B0368（挪用B）、B0178（是而且哲学B）、B0075（波普词条C）、B0176（新浪潮B）、B0306（教材C）承担；波普原典（Hamilton等）未入批——高低文化边界命题以理论侧为主。",
    "11.3": "B0238（意大利激进路线A）为核心；B0346（Sparke意大利史，前期已复核）跨章补强；Archizoom/Superstudio档案未入。",
    "11.4": "全章最强节：B0071（现代建筑之死A、多价建筑A）、B0373（复杂矛盾宣言A、既-又A）、B0372（鸭子/装饰棚A）、B0238（双重编码A）构成A级四核；建筑档案（Pruitt-Igoe、AT&T）仍缺。",
    "11.5": "B0238（孟菲斯A）为核心；B0075（词条C）补图录侧；孟菲斯市场/收藏档案未入。",
    "11.6": "B0368（朋克解构A、设计师作者A）与B0178（混合图像B）构成核心；B0176（作者论争B）、B0009（反文化C）、B0364（谱系C）补；朋克自出版刊物（Sniffin' Glue等）未入批——'不把视觉符号等同于政治立场'的总纲约束须在写作中执行。",
    "11.7": "B0306（信息时代B）、B0238（复兴论B）、B0009（日本平面C）、B0197（日本前史C）、B0368（媒介传播B）承担；全球南方后现代设计专史未入批。",
}
P0_GAP = {
    "11.1": "城市更新档案（Pruitt-Igoe、圣路易斯）、青年反叛刊物、消费社会统计、媒体扩张数据。",
    "11.2": "波普艺术原典（Hamilton《Just What Is It...》）、波普设计作品档案、复制与消费图像档案。",
    "11.3": "Archizoom/Superstudio档案、Studio Alchimia档案、意大利反设计出版物原件。",
    "11.4": "Pruitt-Igoe档案、AT&T大楼委托档案、Venturi住宅档案、后现代建筑竞赛文件。",
    "11.5": "孟菲斯设计档案（Sottsass事务所）、米兰首展（1981）记录、孟菲斯市场与收藏记录。",
    "11.6": "朋克自出版刊物（Sniffin' Glue等）、Cranbrook教学档案、The Face/Emigre杂志档案。",
    "11.7": "全球南方后现代设计专史、后现代语言的区域转译档案（日本/拉美/东欧）。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第十一章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-013含12个来源（后现代建筑理论、平面后现代专书、设计理论文选、平面史教材、日本平面、图录）；与导论/六/七章共享对象时只计一份P0。\n")

for sid in ["11.1", "11.2", "11.3", "11.4", "11.5", "11.6", "11.7"]:
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
with (OUT / "CH11_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH11_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH11 matrix:", {k: v["count"] for k, v in struct.items()})
