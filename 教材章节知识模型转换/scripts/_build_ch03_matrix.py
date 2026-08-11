#!/usr/bin/env python3
"""Build CH02 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch03_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"2.1": "1851年万国工业博览会", "2.2": "博物馆、学校与国家治理", "2.3": "拉斯金、莫里斯与劳动伦理",
          "2.4": "百货商店与现代消费者", "2.5": "从唯美主义到新艺术", "2.6": "世界博览会与殖民分类",
          "2.7": "跨境迁移与地方现代性"}
BASELINE = {
    "2.1": "商品、机器、帝国与公众观看如何汇聚为“设计问题”。",
    "2.2": "亨利·科尔体系及设计教育的制度化：博物馆、学校与国家政策如何把审美变成治理。",
    "2.3": "反工业批判、社会主义理想与高价手工商品之间的张力：劳动伦理不能脱离市场现实。",
    "2.4": "陈列、橱窗、目录、广告和信用如何组织欲望：供给、定价与观看条件不等于购买动机和家庭使用。",
    "2.5": "整体环境、室内、家具、平面与生活方式：唯美主义与新艺术是跨媒介实践而非单一风格。",
    "2.6": "异域物如何被展示、命名和等级化：分类秩序是组织者话语，不是来源社会的自我分类。",
    "2.7": "以棉布、染织、陶瓷、装饰纹样和日本主义为例，把单向“影响”改写为贸易网络中的选择、误读、翻译和再生产。",
}
JUDGMENT = {
    "2.1": "六项A级来源覆盖组织（B0049）、对象与观看（B0052、B0175）、专史（B0204）、博览会计较史（B0339）与通史（B0101），B级补充改革语境与美国观察，C级提示殖民地征集网络与水晶宫前史；结构完整，但观众接受、殖民对象来源、评审效应和全部数字仍无P0。",
    "2.2": "A级覆盖英（B0049、B0175、B0427）、美（B0031）、欧陆与东亚制度（B0168、B0450、B0332、P0040）及通史（B0101）；机构意图证据充分，教学成效、工业采用、财政与课程等P0不足，殖民侧学校档案尤其薄弱。",
    "2.3": "A级十项构成最强节：行动者原典（B0383、B0318）、政治思想史（B0133）、企业史（B0070、B0348、B0091）、谱系（B0168）、通史（B0101）与跨区域（B0450）；张力命题证据充分，但工资、价格、产量与工人经验等P0缺口明显；共享行动者原文只计一份P0。",
    "2.4": "全库最密集节：33条记录覆盖零售制度、消费革命前史、时尚媒介、物质文化与企业链；多来源以不同章节报告重复支撑同一机制，写作时必须按证据簇去重而非按条目引用；供给侧证据强，欲望塑造与家庭使用结果弱。",
    "2.5": "A级覆盖唯美主义（B0035）、新艺术综合（B0338）、跨区域工艺美术（B0450）、企业史与行动者文本；整体环境叙事可用，但图版、对象、委托与使用材料未达V3，“唯美主义→新艺术”前史与“形式相似=传播”须作目的论与接触链审计。",
    "2.6": "A级机制链完整：殖民分类（B0082、B0427、B0463、B0303）、帝国资源与观看（B0175、B0204）、博物学分类（B0332）、棉帝国（B0169）与博览会计较史（B0339）；三条X明确排除B0035、B0049、B0450承担殖民分类核心；组织者话语证据充分，被展示者记录稀缺，观众接受不可推出。",
    "2.7": "全库映射最多节：A级形成“生产—贸易—选择—改造—消费”完整链（棉布、日本主义、东非消费、工艺美术转译、博览会模式东传、墨西哥挪用）；风险是同一条对象（sarasa、katagami、印度棉布）在多来源重复出现，写作时只计一份P0；“影响”类命题须逐链核验接触、委托、制作与再生产证据。",
}
P0_GAP = {
    "2.1": "1851年官方目录与分类表、评审报告、门票与观众统计、参观者日记与媒体评论、展品来源清单、殖民地征集函件、水晶宫结构与场地档案。",
    "2.2": "科学与艺术部政策文件、学校章程与课程表、考试与奖学金记录、博物馆购藏账册（如南肯辛顿First Report）、教师工资与就业、巡回展览目录、殖民侧学校档案。",
    "2.3": "莫里斯公司账簿与价格表、工人工资与工时记录、Kelmscott Press排印档案、Ruskin讲演原刊、协会章程与展览目录、同期报纸评论、消费者订单与家庭清单。",
    "2.4": "商店账册与橱窗／陈列照片、目录原件与定价、信用与赊购记录、广告排期与费用、消费者信件与家庭账簿、时尚期刊发行数据、商品来源与进口单。",
    "2.5": "室内实景照片与图版、家具与织物实物档案、委托与订单记录、期刊连载与评论原文、商店目录、博览会展品目录、日本器物购藏记录。",
    "2.6": "博览会官方目录与分类表、场地规划图、人类展示合同与薪酬记录、被展示者自述与书信、殖民地征集令与运输清单、人种学摄影原件、报刊评论、门票与观众统计。",
    "2.7": "贸易账册与海关记录、东印度公司信函与订单、织造／染整工序档案、图案手册与样品册、博览会购藏凭证、商人通信（Coppendale等）、地方再生产实物（和更纱、batik、kanga）、消费者记录与使用痕迹。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第三章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-004首批14个来源（先锋派专史与行动者文本）；与第二章共享博览会档案对象，同一对象只计一份P0。\n")

for sid in ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]:
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
print("WROTE CH02 matrix csv+md")

