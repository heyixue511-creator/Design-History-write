#!/usr/bin/env python3
"""Build CH06 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch06_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"6.1": "概念前史", "6.2": "晚清工业、博览会与国货意识", "6.3": "印刷资本与视觉公共领域",
          "6.4": "上海都市消费文化", "6.5": "教育制度与东亚中介", "6.6": "民族形式与现代形式之争",
          "6.7": "战争环境中的宣传与生产"}
BASELINE = {
    "6.1": "概念前史：设计/图案/工艺美术的语词与观念谱系。",
    "6.2": "晚清工业、博览会与国货意识：近代转型与设计观念的经济思想起点。",
    "6.3": "印刷资本与视觉公共领域：石印/铅印、报刊、书衣与月份牌。",
    "6.4": "上海都市消费文化：摩登都市、商业美术与消费现代性。",
    "6.5": "教育制度与东亚中介：图案教育、日本/香港中介与设计教育谱系。",
    "6.6": "民族形式与现代形式之争：金石味、汉文正楷、三大构成与工艺美术之辨。",
    "6.7": "战争环境中的宣传与生产：漫画武器化、宣传画与延安样式。",
}
JUDGMENT = {
    "6.1": "A级两项以B0493（工艺美学学科奠基：造物的美学、六大基本特征）与B0495（设计道：1998学科目录正名史）为核心；B级补图案教育（B0500）与漫画前史（B0219）；X排除B0209（东非消费）、B0463（东方展示）；“工艺美学”“设计道”为作者建构框架须标注。",
    "6.2": "A级九项覆盖晚清工业（B0500洋务—实业救国谱系）、技术转移（B0079石印先行、机器本土制造）、器道之争（B0493）、国货品牌（B0500）；B级补经世致用传统（B0493）与西艺教育（B0505）；博览会作为设计观念输入节点可证；影响程度评估多为作者判断。",
    "6.3": "全章最强节（23条、A级11项）：B0079（印刷资本主义：石印先行、商务印书馆中枢、教科书三足鼎立）与B0505/B0469/B0472（书衣、月份牌、期刊分期、东方杂志刊名考据）构成核心；“谷登堡在上海”为修辞类比须标注；“文化决定技术”为作者命题。",
    "6.4": "A级五项以B0469（月份牌产业机制、申报广告业）、B0500（上海消费现代性个案）、B0505（摩登都市与书衣感官文化）为核心；B0143（时尚现代性理论）提供机制解释；上海消费数据与个案须与一手史料互证。",
    "6.5": "A级五项以B0465（香港教育谱系：1955-1981院校沿革、王无邪包豪斯传播链）与B0472（北京美术学校1918图案专业、图案法讲义）、B0492（圣约翰—同济转译）为核心；香港作为中西中介定位为作者框架；“三大构成”经香港/日本两渠道传入为教育史事实。",
    "6.6": "A级四项以B0469（汉字本位民族特质）、B0472（金石味与汉文正楷个案）、B0495（设计之道归于风格）、B0514（民族形式论争完整史实链：苏联口号输入→梁思成中国化→三类型→十四字方针）为核心；B级十一项覆盖工艺美术/设计之争（B0485）与装饰功罪（B0493）；“民族形式”政治化须区分建筑侧与工艺侧机制。",
    "6.7": "A级两项以B0219（漫画武器化、31幅传单内容分析）为核心；B级补宣传画图式（B0472）、延安样式、国共宣传对比；漫画图像可证供给与再现，不能证明接受效果；作者自认共产党/大陆视角偏差须标注。",
}
P0_GAP = {
    "6.1": "《考工记》等典籍版本、1998年学科目录原始文件、图案教育章程（三江师范学堂等）、工艺美术概念史文献。",
    "6.2": "洋务运动奏议原件（《制洋器议》《振百工说》）、博览会档案（1925巴黎/1929费城/1904路易斯安那）、国货运动档案、明精机器厂档案与海关贸易数据。",
    "6.3": "书业公所/商会档案（S313）、商务印书馆/中华书局企业档案、石印书实物与版次、月份牌原件（上海图书馆藏）、《申报》《东方杂志》历年原件与广告档案。",
    "6.4": "上海百货公司档案、月份牌画家工作室记录（杭穉英）、报刊广告统计、电影公司档案（联华/明星）、上海工厂名录（1914-1928）。",
    "6.5": "北京美术学校学则与图案法讲义原件、香港院校沿革档案（1955/1960/1967/1981）、王无邪课程材料、圣约翰—同济教学档案、三大构成教材版本与传入路径。",
    "6.6": "汉文正楷呈请档案（1935）、《东方杂志》四十年刊名原件、首都机场壁画档案、十四字方针文件、三大构成论战文章原件（《装饰》《中国美术报》）。",
    "6.7": "救亡漫画宣传队档案、31幅传单原件、延安美术设计档案（鲁迅艺术文学院）、宣传画图式案例、国共宣传对比材料（Kushner 2006转引源）。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第六章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-007含12个来源（观念史、晚清工业、印刷资本、上海消费、教育中介、民族形式、战争宣传）；与第四章共享中国接受史对象（B0517/B0492），同一对象只计一份P0。\n")

for sid in ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7"]:
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
with (OUT / "CH06_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH06_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH06 matrix csv+md")
