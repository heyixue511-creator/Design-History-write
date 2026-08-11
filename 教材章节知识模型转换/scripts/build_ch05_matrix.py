#!/usr/bin/env python3
"""Build CH05 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch05_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"5.1": "装饰艺术与1925年巴黎博览会", "5.2": "美国大众消费体系", "5.3": "经济危机与“销售工程”",
          "5.4": "流线型的媒介迁移", "5.5": "工业设计职业的形成", "5.6": "人体测量、家务与效率",
          "5.7": "商业设计的伦理争议"}
BASELINE = {
    "5.1": "奢侈工艺、现代材料与殖民装饰资源。",
    "5.2": "广告、连锁零售、分期付款和企业实验室。",
    "5.3": "设计如何被赋予刺激需求的经济功能。",
    "5.4": "从交通工具到家电、办公设备和包装。",
    "5.5": "咨询设计师、企业内部团队与作者品牌。",
    "5.6": "科学管理如何进入办公室、厨房和家庭身体。",
    "5.7": "计划性报废、表面造型与消费者能动性。",
}
JUDGMENT = {
    "5.1": "A级四项以B0073（V&A图录：1925博览会定义性事件、家族相似性、殖民资源语境）与B0022（室内维度）为核心，B0339提供博览会制度比较；C级八项（B0436图册）作普及补充；D记录B0410（新艺术拒斥背景）；“modern but not Modernist”为编者命题，“Art Deco”术语为后设建构。",
    "5.2": "A级三项以B0345（消费作为现代性发动机、美国消费体系）与B0409（de Grazia：福特主义分配回路、广告营销专业化）为核心；B级十项构成制度要素网（广告、连锁、百货）；B0080/B0145补充时尚与性别化消费；“美国化”与“消费者主权vs消费公民权”为比较框架命题。",
    "5.3": "A级七项以B0206（消费工程学理论考古、人为废弃、行为主义）与B0205/B0066（Calkins消费不足论、Fortune命名、销售吸引力标准）为核心；Sheldon & Arens《Consumer Engineering》(1932)为关键P0文本；销售工程是“当事人话语+Meikle批判分析”双层证据。",
    "5.4": "全章最密集节（24条）：A级十项覆盖流线型三层隐喻（B0205）、萧条心理补偿（B0206）、媒介迁移（B0022/B0145/B0073）、风格漂移（B0206）；B级十二项补好莱坞传播、失败案例与营销工具化；D记录B0436（无streamline术语仅直线对照）；流线型解释须标注史学建构属性。",
    "5.5": "A级十四项覆盖职业命名（B0066 Fortune 1934）、四巨头出身（B0206）、咨询设计职业生成（B0345）、室内装饰女性职业（B0022）、Dreyfuss P0自述（B0186）、职业组织沿革（B0066）；职业史命题与B0206去重后计P0；匿名从业者材料仍缺。",
    "5.6": "A级五项以B0186（Dreyfuss人体测量P0：Joe/Josephine百分位图、五感框架）与B0145（Vanek家务时间悖论、泰勒制入办公室）为核心；人体测量数据科学性不可独立引用；家务“省力解放”话语与数据并置构成悖论命题。",
    "5.7": "全章无A级（11条均为B/C）：伦理争议依赖B0206（消费工程操纵逻辑）、B0066（SID伦理准则、博物馆vs市场）、B0186（行动者伦理立场）、B0205（精英vs商业分裂）、B0345（Papanek谱系）；Papanek《Design for the Real World》与Vance Packard《Hidden Persuaders》批判原典未入，须补证后该节方可升为完整节。",
}
P0_GAP = {
    "5.1": "1925年巴黎博览会官方目录与评审记录、Ruhlmann工坊档案、V&A Object List对应实物、殖民展档案、百货公司展厅记录。",
    "5.2": "JWT等广告公司档案、连锁零售年报与信用记录（Woolworth、Dufayel abonnement）、ICC报告、广告支出统计、企业实验室档案。",
    "5.3": "Sheldon & Arens《Consumer Engineering》(1932)原文、Calkins 1930年会议演讲、Fortune 1934年原文、GM造型部档案与Sloan年款制度、专利与收费记录。",
    "5.4": "流线型交通工具档案（M-10,000、Zephyr、Airflow销量数据）、家电流线型产品目录、好莱坞布景档案、1933/1939世博会官方档案。",
    "5.5": "Fortune 1934年原文、SID/IDSA组织档案与会员标准、Carnegie Tech/ADI课程档案、设计师合同与收费记录、Dreyfuss事务所档案。",
    "5.6": "Dreyfuss人体测量原始样本与统计方法、Vanek调查原始数据、泰勒制办公室改造档案（Larkin Building）、家电产品目录与广告原件。",
    "5.7": "Papanek《Design for the Real World》(1971)原文、Vance Packard《Hidden Persuaders》(1957)、MoMA Good Design展览档案、计划性报废立法与批评文献。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第五章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-006含12个来源（Art Deco、美国消费体系、销售工程、流线型、职业形成、人体测量、室内设计、海报史）；与第二章共享博览会/消费对象，同一对象只计一份P0。\n")

for sid in ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7"]:
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
with (OUT / "CH05_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH05_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH05 matrix csv+md")
