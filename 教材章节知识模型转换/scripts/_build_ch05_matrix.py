#!/usr/bin/env python3
"""Build CH04 core-claim-source matrix (CSV+MD) from reviewed mappings."""
import csv, json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
OUT = ROOT / "06_核心命题—证据矩阵"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
STRUCT = json.load(open(ROOT / "logs" / "_ch05_structure.json", encoding="utf-8"))
assets = {r["source_id"]: r for r in csv.DictReader(ASSETS.open(encoding="utf-8-sig"))}

TITLES = {"4.1": "改革联盟与企业系统", "4.2": "魏玛包豪斯与基础课程", "4.3": "1923年的制度转向",
          "4.4": "德绍体系与工坊劳动", "4.5": "社会功能与学校政治", "4.6": "从学校实验到可复制制度",
          "4.7": "迁徙、正典与区域转译"}
BASELINE = {
    "4.1": "制造联盟的标准之争，以及AEG如何协调建筑、产品与传播。",
    "4.2": "共同体理想、身体训练、材料实验和教育权力。",
    "4.3": "“艺术与技术”、实验住宅、原型与生产条件。",
    "4.4": "建筑、媒介、学校形象、性别分流与学生作者权。",
    "4.5": "迈耶、密斯、校内冲突及1933年关闭。",
    "4.6": "基础课程、工坊、原型、展览、出版和企业合作如何被选择性保存，哪些实验没有进入量产或通行课程。",
    "4.7": "人员、课程、出版和中国及其他地区教育中的选择性重组；区分直接接触、制度转译与后来的正典建构。",
}
JUDGMENT = {
    "4.1": "A级十三项覆盖Werkbund组织政治史（B0064）、AEG企业识别（B0060）、Loos前史批判（B0008）、维也纳工坊企业型工坊（B0247）与通史框架（B0168、B0450、B0363）；1914类型之争、1933 Gleichschaltung与AEG多行动者生产均有P0级档案；Behrens中心主义与“工业文化”命题须标注作者框架。",
    "4.2": "全章最强节（27条、A级14项）：档案集（B0182）、校史（B0282、B0158）、教学史（B0454）、行动者自述（B0216）与观念史（B0464）五层互补；双师制、Vorkurs与教学法转型证据链完整；教学成效不可由制度文献自动推定是本节统一边界。",
    "4.3": "A级八项覆盖1923转向的档案层（B0182）、校史层（B0282、B0158）与观念层（B0464“自我动员说”考证）；口号、展览、Haus am Horn与Itten离职事件可证；Forgács对1923展览缘起的反证论证须与档案直接证据分层。",
    "4.4": "A级十一项覆盖德绍章程与课程重组（B0182、B0282、B0158）与维也纳工坊比较前史（B0247）；工坊产品、授权合同与Bauhaus Ltd为制度事实；产品市场成效与教学成效不可推定；性别分流（纺织工坊女性化）有记录但缺深入分析。",
    "4.5": "A级十项覆盖学校政治全链条：魏玛议会斗争、Meyer社会功能主义、Mies去政治化、1932-33关闭（B0464、B0282、B0158、B0182）；Meyer解职因果各说并存不得断言单一解释。",
    "4.6": "A级八项聚焦制度选择性保存：教学法（B0454选择性保存机制）、Isotype方法-制度耦合（B0081）、课程制度（B0182 9学期制）、授权与文凭（B0282）；B16级构成制度要素补充网；“可复制”成效须以自限声明与接受史证据为界。",
    "4.7": "全章最密集节（46条）：中国接受史（B0492、B0517）、Isotype全球迁移（B0081）、包豪斯流散（B0158、B0182）、风格派转译（B0342）、Loos正典化（B0008）构成五条证据链；直接接触、制度转译与正典建构三级边界须严格区分；“影响”类命题以接触证据为限。",
}
P0_GAP = {
    "4.1": "Werkbund章程与年会记录、1914科隆争论文件、AEG董事会任命文件与玻璃底片档案、Osthaus/Behrens书信、Gleichschaltung执委会记录、维也纳工坊财务档案与商标注册。",
    "4.2": "包豪斯档案馆（Bauhaus-Archiv）教学文件、Vorkurs学生作业与注册统计、Itten/Klee/Schlemmer书信日记、1920年董事会决议、德绍章程与课程表原件。",
    "4.3": "1923年展览目录与政府贷款文件、Haus am Horn图纸与审计、Itten离职信、口号原始印刷物、同期报刊评论。",
    "4.4": "德绍校舍建筑图纸与照片、工坊产品目录与授权合同（Polytex、Rasch、耶拿玻璃）、Bauhaus Ltd注册文件、维也纳工坊车间照片与产品档案。",
    "4.5": "图林根/德绍议会记录、Meyer纲领全文与解职调查文件（Hesse/Grote）、Mies 1930.9.9决议、1932年关闭投票记录、纳粹搜查与解散档案。",
    "4.6": "乌尔姆HfG课程档案、北美三线（哈佛/黑山/芝加哥）教学档案、Isotype Collection（T/N文件、Guideline notes、Picture dictionary）、雷丁/维也纳/海牙机构档案。",
    "4.7": "梁思成致梅贻琦信原件与清华课程改革档案、圣约翰—同济教学档案、三大构成教材版本与传入路径档案、Isotype流亡档案与西非项目文件、De Stijl期刊与杜斯堡书信。",
}

csv_rows, md_lines = [], []
md_lines.append("# 第五章核心命题—来源矩阵（V2滚动版）\n")
md_lines.append("> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。本章BATCH-006含12个来源（Art Deco、美国消费体系、销售工程、流线型、职业形成、人体测量、室内设计、海报史）；与第二章共享博览会/消费对象，同一对象只计一份P0。\n")

for sid in ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"]:
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
print("WROTE CH04 matrix csv+md")

