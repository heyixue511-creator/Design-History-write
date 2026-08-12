#!/usr/bin/env python3
"""Build CH03 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch03_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"3.1": "战争、都市与机械感知", "3.2": "未来主义", "3.3": "达达与蒙太奇",
          "3.4": "俄国构成主义与生产主义", "3.5": "风格派与普遍秩序",
          "3.6": "新摄影、新字体与展览设计", "3.7": "跨国先锋网络"}
BASELINE = {
    "3.1": "速度、碎片化和大众动员构成新视觉经验。",
    "3.2": "宣言、排印、运动形式与战争政治。",
    "3.3": "拼贴如何破坏艺术自主性并批判媒体现实。",
    "3.4": "从绘画实验转向生产、宣传和日常用品。",
    "3.5": "抽象形式如何进入家具、住宅、出版和社会理想。",
    "3.6": "观看技术和公共传播的重组。",
    "3.7": "刊物、展览、迁徙与翻译如何形成非中心化传播。",
}
JUDGMENT = {
    "3.1": "A级七项覆盖未来主义宣言（B0027）、达达（B0121）、一战海报（B0199四条）、第一机器时代理论（B0363）；B级补蒙太奇、俄国与意大利案例；结构完整，但大众感知的经验证据（观众、读者、使用者记录）仍薄弱，机械感知多为纲领与图像学推断。",
    "3.2": "A级六项以行动者宣言（B0027三条）、排版史（B0187）、意大利通史（B0346）与理论史（B0363）构成核心；B级补俄国政治化路线、达达对照；未来主义与法西斯关联须以B0346史家判断＋B0027后记并置呈现。",
    "3.3": "A级覆盖达达六城（B0121）、蒙太奇专史（B0007）、排版谱系（B0187）与阿尔普自述（B0276）；X排除B0346（无达达内容）、D记录B0222（证据不足）；蒙太奇发明权与达达内部政治分歧须按“行动者自述vs档案”分层。",
    "3.4": "全章最密集节（31条）：A级17条以行动者文集（B0222）、塔特林（B0228）、构成主义专史（B0277）、乌托邦斗争（B0291）、罗德琴科摄影（B0013）与蒙太奇（B0007）形成“档案—人物—制度—媒介”完整链；X排除B0346；多数作品已毁或未量产，图像重建与“社会建构本质”论须标注作者框架。",
    "3.5": "已从全章最薄节升级为完整节（20条）：A级八项以B0048（形成期专史：期刊非团体论、1922断裂、宣言签署分歧）与B0342（通史：四画家共生、元素主义之争、复制即生产）为核心补证，B0187（风格派排版）与B0363（机器美学理论）继续承担；X排除B0346（无风格派内容）、D记录B0222（无收录文本）；红蓝椅断代（约1923而非1918）修正流行成说；与B0276共享条目P0只计一份。",
    "3.6": "33条且来源跨批次（B0338、B0035、B0052、B0339、B0348来自第二章；B0081新增Isotype）：A级覆盖新摄影（B0013、B0291）、新字体（B0187、B0269）、达达期刊与展览（B0121）、快照宣言（B0222）、Isotype视觉语言（B0081）；B级补蒙太奇、光动力学、展览案例；clean版缺图版，一切视觉判断须回原书。",
    "3.7": "A级五项以网络机制为主（B0121六城、B0276三语出版、B0291协商框架、B0363跨国谱系、B0228塔之传播）；B级补行动者网络自述；六城模型与“协商”框架须标注作者建构属性，中心化残余（罗马尼亚、日本缺席）须注明。",
}
P0_GAP = {
    "3.1": "一战海报档案（PRC/USFA/CPI）、先锋刊物原件（Lacerba、Der Sturm）、观众与读者记录、展览目录、未来主义宣言原刊（《费加罗报》1909）。",
    "3.2": "宣言意文原文与初版刊物、Sant'Elia建筑图纸、自由词语原版版面、Boccioni作品图版、未来主义—法西斯关联的政权档案。",
    "3.3": "达达刊物原件（Dada、391、Der Ventilator、Merz）、蒙太奇作品原件与图版、卡巴莱/展览记录、日记与书信（Ball、Huelsenbeck）、照片档案与颜料技术分析。",
    "3.4": "INkhUK会议记录（TsGALI fond 681）、VKhUTEMAS教学文件、塔特林档案与普宁小册子、OBMOKhU展览记录、1922柏林展目录、Lef/Novyi Lef原件、白海运河摄影底片。",
    "3.5": "De Stijl期刊原件、杜斯堡/蒙德里安通信、里特维尔德家具与施罗德宅图纸、风格派展览目录、Die Kunstismen原版图版。",
    "3.6": "新摄影原版图版与底片（Rodchenko、Moholy-Nagy）、排版实物（期刊整页、海报、广告）、FiFo展目录、Typographische Mitteilungen特刊、展览现场照片。",
    "3.7": "先锋期刊跨国发行记录、人物通信与旅行记录、展览目录与邮政网络、Veshch/G三语期刊原件、杜塞尔多夫大会记录。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第三章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-004首批14个来源（先锋派专史与行动者文本）；与第二章共享博览会档案对象，同一对象只计一份P0。\n")

for sid in ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"]:
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
with (OUT / "CH03_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH03_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH03 matrix csv+md")
