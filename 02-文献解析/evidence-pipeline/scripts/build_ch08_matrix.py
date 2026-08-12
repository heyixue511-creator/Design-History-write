#!/usr/bin/env python3
"""Build CH08 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch08_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"8.1": "冷战展览与生活方式竞争", "8.2": "东欧社会主义日常生活", "8.3": "苏联及社会主义现代主义",
          "8.4": "去殖民化后的公共建设", "8.5": "印度及南亚现代性", "8.6": "拉丁美洲与非洲的现代化项目",
          "8.7": "国际援助与专家网络"}
BASELINE = {
    "8.1": "家庭空间、家电和消费被转化为意识形态证据。",
    "8.2": "计划生产、标准住宅、短缺经济与使用者改造。",
    "8.3": "公共系统、技术崇拜与制度约束。",
    "8.4": "以基础设施、交通、公共建筑、展览与公共服务设施为对象，追踪委托、融资、建设、使用和维护。",
    "8.5": "国家机构、工艺政策、国际合作和地方知识。",
    "8.6": "发展主义、民族文化和不平等结构。",
    "8.7": "标准、课程、展览和技术合作中的权力关系。",
}
JUDGMENT = {
    "8.1": "B0099（先锋宫、意识形态张力）与P0062（Art into Life!展）承担核心，B0100（社会主义消费许诺）与B0166（现代性穿鞋而来）补消费侧；8.1仍缺美国侧档案（美苏厨房辩论类P0未入），'生活方式竞争'的双边结构未闭合。",
    "8.2": "全章最强节：B0099三项A级（公共隐私、私人公共性、私有化公民身份）为核心，P0062（Khrushchev Modern住房）与B0100（华沙家居）补苏联/波兰侧；'使用者改造'以短缺经济下的DIY与灰色经济为B级证据。",
    "8.3": "B0366（乌托邦实验与幻想国家）、B0292（苏联设计实验前史、极权国家设计）与B0099（塞瓦斯托波尔、纪念碑政治）构成B级核心，B0266（儒家列宁主义）补中国侧；社会主义现代主义的档案侧（苏联建筑档案）仍缺。",
    "8.4": "B0281（基础设施遗产）与B0166（印尼国家形象生产）承担B/C级；去殖民化公共建设的档案侧（委托、融资、建设记录）全缺，区域专史薄。",
    "8.5": "B0281（双重托管批判）仅C级；印度及南亚现代性的专史未入批，为本章最薄节。",
    "8.6": "B0038（文明化物品、发展物品）为拉美侧核心（A级一项）；非洲侧无专史入批，'拉丁美洲与非洲'的并列结构未闭合。",
    "8.7": "B0281（殖民发展政策、计划—执行差距）承担B级；专家网络（标准、课程、展览与技术合作）的专门研究未入批。",
}
P0_GAP = {
    "8.1": "美苏厨房辩论档案（1959莫斯科/1969）、国际博览会冷战展馆档案、东欧消费广告档案、家庭照片与使用者访谈。",
    "8.2": "公共公寓住户访谈原件（Gerasimova类）、dacha合作社档案、计划住宅标准文件（苏联/东德/波兰）、短缺经济家庭记录。",
    "8.3": "苏联建筑档案（塞瓦斯托波尔规划竞赛、先锋宫RGALI）、全苏技术美学研究所（VNIITE）档案、社会主义现代主义建筑照片。",
    "8.4": "去殖民化国家的基础设施委托与融资档案（援建项目合同）、公共建筑档案、展览与公共服务设施记录。",
    "8.5": "印度国家设计机构档案（NID/IIM）、工艺政策文件、南亚现代性专史文献。",
    "8.6": "拉美发展主义设计档案（进口替代产品目录）、非洲现代化项目档案（援建合同、产品）、区域设计史专史。",
    "8.7": "国际援助专家网络档案（UN/双边援助项目）、标准与课程传播文件、技术合作项目记录。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第八章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-010含12个来源（社会主义空间、东欧日常、苏联乌托邦、殖民发展、拉美物质文化、印尼外观、宣传机制）；与导论/五/七章共享对象时只计一份P0。\n")

for sid in ["8.1", "8.2", "8.3", "8.4", "8.5", "8.6", "8.7"]:
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
with (OUT / "CH08_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH08_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH08 matrix csv+md")
