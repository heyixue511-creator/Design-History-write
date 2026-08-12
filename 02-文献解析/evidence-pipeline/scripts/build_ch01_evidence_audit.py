#!/usr/bin/env python3
"""Build the rolling CH01 V2 evidence matrix and gap audit from reviewed mappings."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
INDEX = ROOT / "04_文献—章节映射" / "已复核_章节到来源.csv"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"
OUT_DIR = ROOT / "06_核心命题—证据矩阵"
AUDIT_DIR = ROOT / "10_证据缺口与审计"


SECTIONS = {
    "1.1": {
        "title": "前工业造物与分布式知识",
        "claim": "作坊、行会、家庭劳动、地方材料与默会知识共同构成前工业造物，不能还原为孤立工匠。",
        "judgment": "二手研究与行动者理论覆盖充分，已有行会修正主义、奥斯曼、西非、棉纺、瓷器、印刷和Guild个案；但跨地区P0与家庭／女性劳动仍不足。",
        "p0": "行会章程与诉讼、作坊账簿、学徒契约、家庭清单、工资／工时、工具与在制品、非欧洲地方档案。",
        "priority": "P0",
    },
    "1.2": {
        "title": "机器、能源与尺度变化",
        "claim": "机器、能源、交通、国家采购与标准化共同改变生产尺度，机器不是设计职业生成的充分原因。",
        "judgment": "通史、技术史与全球比较已能否定单线机器决定论；美国体系部分存在B0225／B0084重印，且设备性能、产量与劳动后果尚未回原档。",
        "p0": "设备图与规格、能耗／产量数据、厂房布局、国家合同、运输账册、维修记录、工资工时、民用扩散档案。",
        "priority": "P0",
    },
    "1.3": {
        "title": "劳动分工与图样权力",
        "claim": "图样、模具、规格、专利、监督与组织制度逐步分配构思和执行权，而非瞬时产生唯一设计师。",
        "judgment": "来源数量最多且包含企业制度、印刷工序和专利线索；核心缺口不是理论数量，而是具体对象的图样—工序—岗位—修改—责任链。",
        "p0": "签名图与无名图、模具／样板、规格书、专利及诉讼、工序签记、会议决议、职位工资、返工与质量记录。",
        "priority": "P0",
    },
    "1.4": {
        "title": "材料系统与新形式",
        "claim": "棉、陶瓷、金属、玻璃等材料的来源、加工、工艺转换与供应链共同限定形式。",
        "judgment": "棉与瓷材料链明显增强，另有全球史和通史支撑；现阶段仍偏文本综合，材料检测、环境代价和具体对象复原不足。",
        "p0": "材料检测、配方、窑炉／机器记录、样品册、采购与贸易账、废料污染、对象测绘、修复和实验复原。",
        "priority": "P0",
    },
    "1.5": {
        "title": "工厂中的匿名设计",
        "claim": "工人、工匠、制图员、工程师、企业主、商人和销售者共同参与设计，但责任与署名并不均等。",
        "judgment": "Heskett、Ashbee、印刷、棉纺、西非和企业史已提供分布式作者框架；普通工人、妇女、家庭成员和失败项目的可追踪署名仍薄弱。",
        "p0": "雇员名册、岗位说明、工资簿、工序签名、图样版本、内部通信、目录署名、工会材料、女性与家属自述。",
        "priority": "P0",
    },
    "1.6": {
        "title": "“工业艺术”“装饰艺术”与“设计”",
        "claim": "设计相关术语、教育、职位与组织身份在竞争中形成，不能将现代职业定义倒投到早期。",
        "judgment": "已有莫里斯、Crane等行动者文本以及通史、企业史和设计史方法来源；缺少系统同期词频、职位、课程和行业组织的时间序列。",
        "p0": "同期词典、报刊语料、职位广告、人口／职业统计、课程表、学校章程、协会章程、企业组织图、法律分类。",
        "priority": "P0",
    },
    "1.7": {
        "title": "区域差异与混合生产",
        "claim": "工业化是手工、家庭、作坊、外包与工厂在不同地区的非同步重组，英国不是普遍模板。",
        "judgment": "奥斯曼、西非、印度棉纺、全球分流和欧洲比较已形成反英国中心组；中国、南亚内部、拉丁美洲、东欧与更多非洲区域仍不足，且种族／气候与国家本质模型已排除。",
        "p0": "区域生产统计、税关与贸易账、企业／作坊档案、家庭劳动、地方术语、技术迁移、政策执行、工资价格与使用材料。",
        "priority": "P0",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    mappings = [row for row in read_csv(INDEX) if row["section_id"] in SECTIONS]
    assets = {row["source_id"]: row for row in read_csv(ASSETS)}
    by_section: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mappings:
        by_section[row["section_id"]].append(row)

    fields = [
        "section_id", "section_title", "baseline_claim", "mapping_rows", "accepted_rows",
        "independent_support_rows", "grade_A", "grade_B", "grade_C", "grade_D", "grade_X",
        "verification", "source_ids", "independent_source_ids", "audit_judgment",
        "p0_gap", "gap_priority", "writing_gate",
    ]
    matrix_rows: list[dict[str, str | int]] = []
    detail_lines = [
        "# 第一章核心命题—来源矩阵（V2滚动版）", "",
        "> 生成依据仅为人工复核映射。A—D／X表示章节角色，不表示来源质量；所有条目仍为V2，不能逐字引用。", "",
    ]
    for sid, meta in SECTIONS.items():
        rows = sorted(by_section[sid], key=lambda r: r["source_id"])
        grades = Counter(row["grade"] for row in rows)
        accepted = [row for row in rows if row["grade"] != "X"]
        independent = [
            row for row in accepted
            if "DUPLICATE" not in row["status"] and row["role"] != "version_alias_not_independent_evidence"
        ]
        source_ids = [row["source_id"] for row in rows]
        independent_ids = [row["source_id"] for row in independent]
        matrix_rows.append({
            "section_id": sid,
            "section_title": meta["title"],
            "baseline_claim": meta["claim"],
            "mapping_rows": len(rows),
            "accepted_rows": len(accepted),
            "independent_support_rows": len(independent),
            "grade_A": grades["A"], "grade_B": grades["B"], "grade_C": grades["C"],
            "grade_D": grades["D"], "grade_X": grades["X"],
            "verification": "V2 only",
            "source_ids": ";".join(source_ids),
            "independent_source_ids": ";".join(independent_ids),
            "audit_judgment": meta["judgment"],
            "p0_gap": meta["p0"],
            "gap_priority": meta["priority"],
            "writing_gate": "RESEARCH_ROUTING_ONLY",
        })

        detail_lines.extend([
            f"## {sid} {meta['title']}", "",
            f"**总纲命题**：{meta['claim']}", "",
            f"**结构统计**：{len(rows)}条映射；A {grades['A']}、B {grades['B']}、C {grades['C']}、D {grades['D']}、X {grades['X']}；排除X及重复支持后，{len(independent)}条可独立承担不同命题角色的来源记录。", "",
            f"**独立判断**：{meta['judgment']}", "",
            "| 来源 | 题名 | 等级 | 角色 | 状态 |", "|---|---|---|---|---|",
        ])
        for row in rows:
            title = assets.get(row["source_id"], {}).get("folder_name", "未在资产表定位").replace("|", "／")
            detail_lines.append(f"| {row['source_id']} | {title} | {row['grade']}／{row['verification']} | {row['role']} | {row['status']} |")
        detail_lines.extend(["", f"**P0缺口**：{meta['p0']}", "", "**准入门**：`RESEARCH_ROUTING_ONLY`。在至少完成核心命题的原文页码、关键P0及对象／图版核验前，不升级为可定稿正文。", ""])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUT_DIR / "CH01_核心命题—来源矩阵.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(matrix_rows)
    (OUT_DIR / "CH01_核心命题—来源矩阵.md").write_text("\n".join(detail_lines) + "\n", encoding="utf-8")

    all_ids = sorted({row["source_id"] for row in mappings})
    x_rows = [row for row in mappings if row["grade"] == "X"]
    audit = [
        "# 第一章证据结构汇总审计（V2）", "",
        "## 审计结论", "",
        f"第一章七节已有{len(mappings)}条人工处置记录，涉及{len(all_ids)}个资产ID。B0157与B0328属于同一著作的不同版本资产，所以按整书折算为25个独立书目实体；B0084阅读材料8与B0225美国体系章节局部重印，相关命题只计一次。数量显示检索结构已成形，但所有来源均为V2，不能据此判断正文证据已经闭合。", "",
        "当前最明显的问题不是‘文献太少’，而是四种证据不平衡：二手综合多于P0；理论与通史多于对象级生产链；欧美与少数区域个案多于真正均衡的全球比较；行动者主张多于工人、女性、殖民生产者和使用者材料。第一章因此可以进入定向原文核验和P0补证，尚不能进入无保留定稿。", "",
        "## 七节密度与准入", "",
        "| 节 | 映射 | 排除X／重复后支持记录 | A/B/C/D/X | 当前判断 | 首要缺口 |", "|---|---:|---:|---|---|---|",
    ]
    for row in matrix_rows:
        dist = f"{row['grade_A']}/{row['grade_B']}/{row['grade_C']}/{row['grade_D']}/{row['grade_X']}"
        audit.append(f"| {row['section_id']} {row['section_title']} | {row['mapping_rows']} | {row['independent_support_rows']} | {dist} | {row['audit_judgment']} | {row['p0_gap']} |")
    audit.extend([
        "", "## 已排除模型", "",
        "以下X记录不是缺失值，而是经过复核后明确不准入的模型或重复证据：", "",
    ])
    for row in x_rows:
        audit.append(f"- {row['source_id']} → {row['section_id']}：`{row['role']}`，状态`{row['status']}`。边界：{row['evidence_boundary']}")
    audit.extend([
        "", "## 下一轮核验顺序", "",
        "1. 先处理1.3与1.5的对象级图样、岗位、工序和责任链；这是当前来源最多但P0最薄的环节。",
        "2. 再处理1.2与1.4的设备、材料、产量、采购、环境和实物复原，防止把通史机制写成对象事实。",
        "3. 随后处理1.6的同期术语、课程、职位与协会制度，避免回顾性定义倒投。",
        "4. 1.1与1.7同步补女性／家庭劳动及中国、南亚、拉丁美洲、东欧与更多非洲区域原档。",
        "", "## 验证状态", "",
        "- 已验证：映射CSV结构、等级分布、来源ID、重复／版本关系和所有V2状态。",
        "- 合理推断：第一章的研究路由已足以安排定向补证；该判断基于来源功能覆盖，不等于史实已核定。",
        "- 未验证：逐字引文、完整页码、全部图版、关键数字、引注所指P0和跨版本逐章差异。",
        "- 决策：第一章扩展批次关闭；保持`RESEARCH_ROUTING_ONLY`，转入第二章扩展批次，同时保留上述P0回填队列。", "",
    ])
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    (AUDIT_DIR / "第一章证据结构汇总审计-v1.md").write_text("\n".join(audit), encoding="utf-8")
    print({"chapter1_mapping_rows": len(mappings), "asset_ids": len(all_ids), "x_rows": len(x_rows)})


if __name__ == "__main__":
    main()
