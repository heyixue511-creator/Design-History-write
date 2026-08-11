#!/usr/bin/env python3
"""Build CH00 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch00_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"0.1": "“设计”是对象、活动还是制度", "0.2": "现代性、现代化、现代主义与当代性", "0.3": "从英雄谱系到关系史",
          "0.4": "人工物如何成为史料", "0.5": "图像、档案、口述与数字痕迹", "0.6": "证据偏差与缺席者",
          "0.7": "全球设计史的三种模型", "0.8": "如何阅读本书"}
BASELINE = {
    "0.1": "区分日常造物、专业设计、设计话语与设计制度；说明历史概念不能直接套用到所有时代和地区。",
    "0.2": "建立四个概念的分析边界，解释时间分期为何既需要坐标又不能追求全球同步。",
    "0.3": "检讨“大师—名作—风格”的正典模式，引入生产—中介—消费、物质文化、社会史和全球关系史。",
    "0.4": "讨论材料、结构、磨损、维修、复制、陈列与使用痕迹；区分物的“被设计意图”与“实际社会生活”。",
    "0.5": "说明广告、目录、专利、企业档案、课程文件、访谈、软件版本和平台记录各自能证明什么、不能证明什么。",
    "0.6": "分析保存偏差、机构偏差、正典偏差、OCR讹误和数字平台的可视性偏差，追问工人、妇女、殖民地产者与普通使用者为何经常消失。",
    "0.7": "比较扩散、流动与转译、纠缠与不对称关系；强调地方并非被动接收端。",
    "0.8": "介绍每章的对象细读、制度机制、跨区域比较、争议档案、史料实验和章际问题链。",
}
JUDGMENT = {
    "0.1": "A级五项全部来自BATCH-009本批次：B0059（设计作为新自由艺术、四领域）、B0183（学科手册）、B0240（有态度的物/小写设计）、B0273（学科身份辩论）、B0440（学科—对象之辨）——概念节以学科元理论为A级核心；B级补B0242（设计文化三角）、B0108（Design Studies论证）与前期跨章来源；“设计”定义论（解决问题说/第三智慧系统等）须与B0411等教学定义并置标注命题身份。",
    "0.2": "A级十六项主要由前期各章核心文献承担（B0143时尚现代性、B0500观念史、B0485生活启蒙、B0338/B0259/B0084等），BATCH-009补B0337（现代主义概念历史化）为唯一本批次A级；现代性概念是全库跨引最密集的导论节，教材写作须区分“现代性体验/现代化进程/现代主义运动”三层并标注各来源命题身份。",
    "0.3": "A级二十九项全为前期各章核心文献（全球史B0005/B0169/B0209、工艺美术B0070/B0133/B0168、印刷资本B0079、中国设计史B0450/B0500等）——关系史转向已被全库实践；BATCH-009的十条B级提供方法论侧（反专论/关系束B0440、语境化转向B0273、权力地理学B0059、Dilnot四种传统B0108、批判指南B0214、物质文化转向B0240）。",
    "0.4": "A级二十项由前期来源承担（实物与档案类B0086、B0154、B0169、B0182、B0469、B0505等）；BATCH-009补B0240（物作为物理表达/积极中介）、B0183（生存偏差/实物一手经验）、B0059（产品语义学/可供性）为B级理论侧；X排除B0097；“物的社会生命”（Appadurai）为共享理论资源只计一份P0。",
    "0.5": "全库最强导论节（80条）：A级三十三项覆盖史料类型各维度（广告B0376、图像批判B0214、档案B0182/B0199、口述B0162、实物B0086等）；B级理论清单（B0440史料类型、B0183指南、B0273一次/二次辩证）支撑方法论框架；X排除B0478（译本审计职能）。",
    "0.6": "全库最密节（137条、A级51项）：前期各章贡献档案侧A级（B0388体裁批判、B0084、B0101、B0219、B0463等），BATCH-009的十一个来源提供学科层偏差批判（B级：正典建构B0440、Buckley缺席B0108、折射校正B0376、自我解构时间线B0214、史料非对称性B0313、好设计二分法B0240）；“缺席者”命题以Buckley女性主义批判与B0313史料非对称性为理论锚点。",
    "0.7": "A级九项由前期来源承担（B0005/B0086/B0154/B0169/B0181/B0259/B0334/B0338/B0450）；BATCH-009补B0313（纠缠与不对称案例）、B0059（中心—边缘/亚洲案例）、B0273（全球化学科呼吁）为B级；X排除B0170（与B0005同书别名）；扩散/流动/纠缠三模型须以第二章已复核的全球史来源为档案侧。",
    "0.8": "教材自指节：仅3条C级（无A级），外部来源（B0235/B0149/B0411等）作参考；本节以总纲自身与各章写作包为准，无需外部证据准入。",
}
P0_GAP = {
    "0.1": "学科制度档案（Design History Society 1977成立文件、Design Issues创刊文件）、“design”词义演变的词典史文献。",
    "0.2": "现代性分期关键文本原典（Habermas、Berman、Latour等）与各国现代性档案；本批次文献多为二手理论。",
    "0.3": "关系史转向关键原始文本（Giedion《机械化支配一切》、Pevsner《现代设计先驱》版次对照）、Fry权力地理学所引档案（Geelong福特工厂）。",
    "0.4": "具体实物档案（Heal's家具目录1939、梳妆台案例实物、专利局记录）、生存偏差的收藏史数据。",
    "0.5": "JWT等广告机构档案、铁路时刻表原件、Isotype档案（Neurath）、Mass Observation档案、平台数据保存机制。",
    "0.6": "被排除者的一手档案（女工、殖民地生产者、普通使用者记录）、OCR原始文本对照、博物馆购藏记录。",
    "0.7": "全球南方设计史专门文献与跨区域传播的档案证据（第二章已复核B0169/B0209为档案侧）、区域接受史案例。",
    "0.8": "无需外部P0；以总纲与各章写作包为准。",
}

csv_rows, md_lines = [], []
md_lines.append("# 导论核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。导论记录来自全库跨章积累（432条，121个来源）与BATCH-009首批12个专门来源（概念、史料方法论、史学批判）；同一对象（Good Design、斯堪的纳维亚设计等）与各章只计一份P0。\n")

for sid in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8"]:
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
with (OUT / "CH00_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as h:
    w = csv.DictWriter(h, fieldnames=fields)
    w.writeheader()
    w.writerows(csv_rows)
(OUT / "CH00_核心命题—来源矩阵.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
print("WROTE CH00 matrix csv+md")
