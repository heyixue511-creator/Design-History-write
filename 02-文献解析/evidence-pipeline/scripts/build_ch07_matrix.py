#!/usr/bin/env python3
"""Build CH07 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch07_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"7.1": "战时技术与和平转用", "7.2": "英国重建与设计委员会", "7.3": "美国“Good Design”体系",
          "7.4": "乌尔姆设计学院", "7.5": "联邦德国企业设计", "7.6": "北欧设计的制度基础", "7.7": "日本战后设计重建"}
BASELINE = {
    "7.1": "战时技术与和平转用：材料、标准化、军工生产及其民用转化。",
    "7.2": "英国重建与设计委员会：展览、住宅、公共教育与出口政策。",
    "7.3": "美国“Good Design”体系：现代艺术博物馆、企业与中产消费。",
    "7.4": "乌尔姆设计学院：从包豪斯遗产转向方法、系统和科学化。",
    "7.5": "联邦德国企业设计：布劳恩、视觉统一和长期产品系统。",
    "7.6": "北欧设计的制度基础：福利国家、工艺传统、家庭生活与出口形象。",
    "7.7": "日本战后设计重建：工业政策、质量控制、企业设计与传统再解释。",
}
JUDGMENT = {
    "7.1": "A级三项全由B0316（Mindell技术史：雷达操作员作为技术人员、系统集成者的制度角色、战时雷达系统集成）承担，战时技术节以专史为核心；B级补人体工程学的战时起源（B0186航空医学、泰勒管理）与Dreyfuss行动者侧；“和平转用”须区分直接转用（材料/技术）与制度中介（标准、教育），不得将军事技术转用自动等同设计民主化。",
    "7.2": "A级四项全由B0235（Woodham通史：CoID建立、1946“英国能做到”展、1951英国节、英国好设计标签）承担；B级由B0234（词典）、B0401（Sparke）、B0503（王受之教材）补充；“英国能做到”展与英国节为关键P0对象，作者命题（英国重建的出口政策叙事）须标注。",
    "7.3": "A级三项：B0186（Dreyfuss行动者自著：好设计作为美国艺术形式、好设计评价框架）两项＋B0235（MoMA好设计展）一项；B级九项覆盖MoMA展、企业、中产消费网络；行动者侧（Dreyfuss）与机构侧（Woodham）互补；“好设计”概念的美日两线（7.7 G-Mark）同一对象只计一份P0。",
    "7.4": "A级两项全由B0235（乌尔姆课程与关闭、乌尔姆—布劳恩设计联系）承担；B级补B0401（Sparke）、B0234（词典）、B0415（《Design After Modernism》对科学化设计方法的批评侧）；B0411（雷曼教学著作）作乌尔姆遗产向中国传播的行动者侧；B0059（Buchanan/Margolin《The Idea of Design》）以设计学科方法论文献作C级旁证；“制度化完成”类判断为作者命题须标注。",
    "7.5": "全节6条（5B＋1C：B0108 Margolin《Design Discourse》以设计研究方法论文献作C级旁证），无A级——布劳恩专史未入批，保持B级准入；拉姆斯十原则、1957米兰三年展大奖等通用史实与B0101/B0102去重；后续补证批次（布劳恩/联邦德国设计专史）可提升准入。",
    "7.6": "全章结构最强节：A级三项＝B0076（Fiell图录：北欧作品视觉档案）与B0388（Fallan主编：咖啡桌书体裁批判、斯堪的纳维亚设计作为被发明的范畴）两项构成档案侧与批判侧正反对勘；B级补B0503/B0235；B0337（Greenhalgh《Modernism in Design》）以现代主义设计史学批评作C级旁证；“被发明的范畴”为史学批判命题须标注；Lunning Prize、Svenska Slöjdföreningen、Design in Scandinavia巡展等同一对象只计一份P0。",
    "7.7": "A级四项：B0253（Hiesinger图录：MITI政府政策、企业产品档案）两项＋B0235（G-Mark/MITI设计促进、日本企业内设计系统）两项——图录档案侧与通史侧互补；X排除B0316（无日本内容）；Loewy访日（1951）对象与B0186共享只计一份P0；“Japanese Modern第一个后现代风格”为Hiesinger命题须标注。",
}
P0_GAP = {
    "7.1": "雷达／火控系统档案（MIT辐射实验室、SCR-584）、军转民制度文件、Dreyfuss《为人的设计》版次与手稿。",
    "7.2": "CoID档案（1944成立文件、1956设计中心）、1946“英国能做到”展目录原件、1951英国节委员会记录、Utility计划文件。",
    "7.3": "MoMA Good Design展目录（1950—1955）、Kaufmann《What Is Modern Design?》（1950）、Dreyfuss《人体度量图表》（1960）数据来源。",
    "7.4": "乌尔姆课程表与人事档案（比尔／马尔多纳多任期、1968关闭决议）、乌尔姆—布劳恩合作协议、学生作业档案。",
    "7.5": "布劳恩企业档案（1954合作、1957米兰三年展获奖记录）、拉姆斯十原则原始文本、联邦德国设计委员会（Rat für Formgebung）文件。",
    "7.6": "Lunning Prize获奖档案（1951起）、Svenska Slöjdföreningen章程（1845）、Design in Scandinavia北美巡展（1954—1957）档案、Den Permanente（1931）文件。",
    "7.7": "G-Mark制度文件（1957启动、专利局→MITI→JIDPO沿革）、MITI政策文件（Design Year 1973、1993中期报告）、Loewy访日档案（1951）、Sony／GK等企业档案。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第七章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-008含12个来源（战时技术、英国重建、美国Good Design、乌尔姆、联邦德国、北欧、日本），另含B0168（北欧工艺美术谱系）与B0102（日本战后政策）两条前期批次跨章记录；与第五、六章共享的同一对象（Loewy访日、G-Mark、Good Design概念）只计一份P0。\n")

for sid in ["7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7"]:
    v = STRUCT[sid]
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
        folder = assets.get(x["source_id"], {}).get("folder_name", x["source_id"])
        md_lines.append(f"| {x['source_id']} | {folder} | {x['grade']}／V2 | {x['role']} | {x['status']} |")
    md_lines.append(f"\n**P0缺口**：{P0_GAP[sid]}。\n")
    md_lines.append("**准入门**：`RESEARCH_ROUTING_ONLY`。在至少完成核心命题的原文页码、关键P0及对象／图版核验前，不升级为可定稿正文。\n")

fields = ["section_id", "section_title", "baseline_claim", "mapping_rows", "accepted_rows", "independent_support_rows",
          "grade_A", "grade_B", "grade_C", "grade_D", "grade_X", "verification", "source_ids",
          "independent_source_ids", "audit_judgment", "p0_gap", "gap_priority", "writing_gate"]
with (OUT / "CH07_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH07_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH07 matrix csv+md")
