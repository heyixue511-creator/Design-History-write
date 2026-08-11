#!/usr/bin/env python3
"""Complete Kelmscott Press production history and Ruskin actor-text sources."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0348": {
        "title": "The Kelmscott Press: A History of William Morris's Typographical Adventure",
        "author": "William S. Peterson",
        "version": "Clarendon Press／Oxford University Press, 1991",
        "type": "档案型印刷史、书籍设计生产史、企业史与接受史",
        "scope": "Kelmscott Press 1891—1898年的建社、字体、材料、生产、经营、关社与英美欧接受",
        "duplicate_group": "Kelmscott共享史料组：与B0070、B0133及其他Morris研究共享书信和行动者文本；Peterson的档案重建可独立使用，共享原文不重复计证",
        "summary": "Peterson利用Cockerell日记、往来函、账簿、校样、试页、报刊与实物逐日重建Kelmscott Press。该书把‘理想书’拆解为字体、纸、墨、手压机、电铸、机械铸字、摄影转刻、编辑、校对、工会、定价、书商折扣与收藏市场，足以校正‘莫里斯独自手工制作美书’的神话。它还呈现社会主义理想、严格设计控制、劳动分工、昂贵收藏品和市场投机之间的矛盾。其遗产章节可追踪私人出版社与商业印刷的接受路径，但‘影响’仍须按直接接触、复制、机构采用和地方再生产分级。",
        "strengths": [
            "以多类档案和实物材料重建建社、生产、财务与关社，证据定位细密。",
            "把字体、纸张、机械、装饰、插图、编辑、校对和装帧拆成多行动者工序。",
            "记录工会化、工资线索、管理更替和档案保存条件，避免艺术家独创叙事。",
            "用账簿、价格、折扣、投机和盗版揭示理想书的市场条件。",
            "通过报刊、价格波动、仿制字体和出版社谱系处理接受史与争议史。",
        ],
        "limits": [
            "研究以莫里斯及英语世界为中心，法国、意大利与非英语接受较薄。",
            "Cockerell 1894年后档案异常丰富，可能造成前后期证据密度和管理者可见性不均。",
            "工资、工时和福利多来自管理者或同事证词，工人自述与女性日常劳动仍不足。",
            "作者关于‘书设计师角色再发明’和现代精印起点的判断属于史学解释，不是无争议事实。",
            "账目混合且未按19世纪会计惯例完全重算，盈利结论只能采用作者的保守措辞。",
            "P4报告关于隐藏枢纽、量化悖论与插画翻译理论的扩展不能反写成原著实证结论。",
        ],
        "checks": [
            "clean第27—32行：研究缘起、新材料与超越印刷史的研究范围。",
            "clean第877—896行：Art-Workers' Guild、Arts and Crafts Exhibition Society与Emery Walker讲座的建社链。",
            "clean第1001—1013行：Prince刻冲模、Reed铸字厂机器铸字及Golden／Troy／Chaucer字体尺度。",
            "clean第1166—1183行：作者反驳单一Kelmscott风格刻板印象，并区分商业印刷规则与不受价格约束的理想书。",
            "clean第1715—1753行：出版社的复杂组织、秘书更替与Cockerell档案造成的可重建性。",
            "clean第1924—1934行：印工工会化、工资与福利证词；具体工资仍不明。",
            "clean第2162—2179行：收藏市场矛盾、账目缺口、保守盈亏判断、大小书互补和书商折扣。",
            "clean第3335—3341行：全要素控制、书设计师角色解释及其与劳动分工／工人自由的矛盾。",
        ],
        "maps": [
            ("0.3", "A", "production_business_object_and_reception_method", "书籍设计史可把理念、工序、企业、劳动、市场与接受连成可核机制链", "单一名人—机构个案不能代表全部工艺美术生产", "与其他企业、普通印刷厂和劳动史比较", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "diary_letters_ledger_proofs_press_and_objects", "日记、通信、账簿、校样、试页、报刊和实物可互校行动者记忆与生产事实", "资料保存受Cockerell角色和藏所收集史影响", "回档案号、纸本页码、账簿结构、实物和图版", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "morris_cockerell_worker_gender_archive_and_anglophone_bias", "名人中心、档案保存者偏差、工人／女性缺口和英语世界重心须进入审计", "材料丰富不等于主体覆盖完整", "补工人、女性、外包者、顾客与非英语接受材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "type_design_reproduction_workflow_and_control", "字体设计、冲模、机器铸字、电铸、摄影转刻和版面规范说明构思—复制—控制的多阶段分工", "Morris全要素控制不等于亲手执行全部工序", "逐对象补制作者、图样、账单、工序与署名", "ACCEPTED_AS_CORE_PRODUCTION_SOURCE"),
            ("1.4", "A", "paper_ink_type_press_and_material_constraints", "手工纸、墨、字体尺度、手压机与复制技术共同限定书页形式、成本和产量", "材料选择的审美解释仍需实物和技术核验", "补纸张水印、墨色、尺寸、设备、印数和保存状态", "ACCEPTED_WITH_OBJECT_VERIFICATION"),
            ("1.5", "A", "book_as_collective_authorship_and_hidden_labour", "Morris、Walker、Prince、Batchelor、Burne-Jones、转刻者、印工、编辑和校对共同形成书籍作者网络", "档案可见度不等于贡献大小，女性与印工声音较弱", "补工人自述、工资、任务、署名和性别材料", "ACCEPTED_AS_CORE_AUTHORSHIP_SOURCE"),
            ("1.6", "A", "book_designer_printer_editor_manager_and_craft_roles", "书设计师、印刷者、编辑、秘书、刻工和企业管理等角色的区分可进入职业概念史", "‘发明书设计师’是作者解释，Moxon等前史已构成反例", "补同期称谓、职位、合同和更长印刷职业史", "ACCEPTED_WITH_PRIORITY_CLAIM_AUDIT"),
            ("2.3", "A", "ideal_book_socialism_division_of_labour_and_collectors", "理想书、社会主义、工人待遇、严格控制、昂贵商品和收藏市场共同构成劳动伦理的实践矛盾", "管理者证词和保守账目不能证明工人获得解放", "与Ruskin、B0070、B0133、工人及消费者材料对读", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.4", "A", "pricing_discount_speculation_piracy_and_collecting_market", "价格、版本、折扣、投机、盗版与跨洋复制说明设计价值如何被市场组织", "市场价格不能等同于审美接受或使用意义", "补顾客、阅读、流通、图书馆和二手市场记录", "ACCEPTED_AS_CORE_MARKET_CASE"),
            ("2.5", "A", "typography_ornament_illustration_and_unified_page", "字体、页边距、装饰、插图与文本的整体编排构成工艺美术的书籍环境", "著名Chaucer重页不是全部Kelmscott书的代表，当前未逐图核验", "补不同开本、普通页面、实物、图像和阅读使用", "ACCEPTED_WITH_VISUAL_FOLLOWUP"),
            ("2.7", "A", "printing_exhibitions_piracy_and_transatlantic_reproduction", "展览、代理、报刊、摄影复制、仿制字体与地方出版社形成可追踪的跨境再生产链", "复制、仿制与市场知名度不等于思想或社会理想被接受", "按人物、技术、企业、对象和评论分层核验", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("3.6", "B", "private_press_to_twentieth_century_typographic_debate", "Kelmscott经Doves、Vale、商业印刷与功能主义批评进入20世纪字体和版式论争", "不是新摄影、新字体或先锋排版的核心专史", "补相关设计者原文、对象、学校、企业和传播材料", "ACCEPTED_AS_PREHISTORY"),
            ("5.5", "B", "book_designer_and_commercial_print_professionalization", "全要素协调与商业印刷接受可作为平面／书籍设计职业化的具体前史", "私人出版社不能替代20世纪职业组织、教育和企业职位史", "补协会、课程、合同、职位、工资和商业印刷档案", "ACCEPTED_AS_PROFESSIONALIZATION_PREHISTORY"),
        ],
    },
    "B0383": {
        "title": "The Stones of Venice（本地文本仅第一、二卷）",
        "author": "John Ruskin",
        "version": "第一卷1851、第二卷1853；本地为纽约John Wiley数字化OCR合装本，未含第三卷",
        "type": "19世纪行动者原典、建筑批评、劳动伦理与文明史写作",
        "scope": "威尼斯建筑构造、装饰、拜占庭与哥特；本地9939行仅覆盖原著前两卷",
        "duplicate_group": "Ruskin行动者文本组：后续选集或Morris研究可能重印《哥特的本质》；相同段落只计一份P0文本证据",
        "summary": "Ruskin把现场测量、石工、图绘和文献考据同宗教—道德批评结合，以建筑构造、装饰和工人痕迹解释威尼斯兴衰。《哥特的本质》把不完美与工人的判断空间相连，批判把劳动者分割成机械片段，并要求消费者放弃以劳动退化换来的便利、便宜和精确。这是2.3最重要的行动者原典之一，也能为第一章劳动分工和第二章总体环境提供同期概念材料。但其风格—宗教—民族道德的直接对应、基督教优越论、文艺复兴衰败论和消费道德化不能作为经验证实的普遍规律；本地文件又缺第三卷，引用范围必须收紧。",
        "strengths": [
            "把现场测量、材料、构造、装饰、图绘和历史文献用于同一建筑判断。",
            "从劳动分工、工人判断空间和消费者责任建立美学—劳动伦理连接。",
            "以构件和细部说明形式不是抽象风格标签，而与制作、观看距离和结构相关。",
            "承认不确定性并与同时代批评者论辩，保留19世纪知识生产现场。",
            "作为行动者原典，可区分Ruskin自述与后世Morris／工艺美术史解释。",
        ],
        "limits": [
            "本地数字文本只含第一、二卷，不能称为三卷《威尼斯之石》全本。",
            "OCR损伤、希腊文、表格和图版缺失限制逐字引用、测量与视觉判断。",
            "宗教活力等于艺术活力、民族道德直接化石化为风格等属于规范性目的论。",
            "基督教优越、南北血统和非基督教文化判断带有19世纪宗教与种族化偏见。",
            "以工人自由解释粗糙／变化并不能证明中世纪工人的法律、工资或实际自主状态。",
            "对消费品的道德判断以作者规范立场为主，不能替代工人、消费者和企业行为证据。",
        ],
        "checks": [
            "clean第1—15行：第一卷前言及作者对亲自考察、测量和图绘方法的说明。",
            "clean第471—506行：建筑三类价值、行动／言说／外观与构造劳动的判断框架。",
            "clean第2238—2260行：装饰材料、自然对象与形式处理的论述入口。",
            "clean第6534—6575行：《哥特的本质》的章节位置与六种心智要素。",
            "clean第6658—6685行：工人判断空间、劳动分工是人的分割，以及生产便利与人的代价。",
            "clean第6686—6705行：作者把消费者选择、必要性、精确完成和劳动退化相连；这是规范论证而非行为统计。",
            "clean第6738—6768行：主人参与艰难劳动、不完美与工人表达、变化性之间的论证。",
            "clean第7313—7357行：形式与品质判断清单显示作者如何把精神论转为观察规则。",
        ],
        "maps": [
            ("0.3", "B", "material_observation_moral_criticism_actor_method", "现场、构造、装饰和历史文献如何被19世纪批评者组织为文明判断，可作史学案例", "规范性道德推演不能升级为现代经验方法", "与现代建筑史、劳动史、宗教史和物质分析对读", "ACCEPTED_AS_ACTOR_METHOD_CASE"),
            ("0.5", "A", "primary_actor_text_measurement_and_argument", "Ruskin原文可证明其本人如何表述建筑、劳动、工艺和消费责任", "本地只含两卷且OCR／图版不完整，当前仍为V2", "核定纸本版次、卷页、图版、上下文和第三卷范围", "ACCEPTED_AS_P0_ACTOR_TEXT_WITH_VERSION_LIMIT"),
            ("0.6", "A", "religious_teleology_racialized_geography_worker_and_ocr_bias", "宗教目的论、民族／地理本质化、工人证据缺口和数字本残损须进入审计", "指出偏见不等于否定其历史影响，也不等于接受其结论", "补同时代反对意见、劳动档案、地区研究与完整版本", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "division_of_labour_judgement_and_execution", "‘被分割的是人而非劳动’说明同期批评者如何理解构思、判断与重复执行的分离", "不能据此证明所有工厂或中世纪工场的真实劳动关系", "补工厂账目、工资、工时、技术、工人和行业材料", "ACCEPTED_AS_CORE_ACTOR_ARGUMENT"),
            ("1.4", "B", "stone_structure_ornament_material_and_distance", "石材、构造、荷载、装饰取材与观看距离显示材料系统如何约束形式判断", "图版缺失且测量未复核，不能直接采用具体视觉或数字结论", "补扫描图版、建筑实测、修复记录和现代技术史", "ACCEPTED_WITH_VISUAL_TECHNICAL_GAP"),
            ("1.5", "B", "anonymous_workman_and_architect_control", "工人的判断、变化与不完美被用来反对建筑师对制作的完全控制", "这是Ruskin的伦理解释，不是匿名工人的自述或作者权事实", "补工匠姓名、合同、工资、工场规制和制作痕迹", "ACCEPTED_AS_ACTOR_CRITIQUE"),
            ("1.6", "B", "architecture_decorative_art_workman_and_design_terms", "architecture、ornament、design、workman等同期用法可补设计概念的19世纪语境", "不能直接对应现代设计师职业分类", "补同期词典、学校、企业和行业称谓", "ACCEPTED_AS_CONCEPT_HISTORY_SUPPORT"),
            ("2.3", "A", "nature_of_gothic_labour_freedom_and_consumer_duty", "工人自由、不完美、劳动分工和消费者责任构成Ruskin劳动伦理的核心行动者文本", "哥特形式不证明工人实际自由，宗教优越论不进入教材事实陈述", "与Morris、企业史、劳动档案、批评者和对象材料对读", "ACCEPTED_AS_CORE_P0_ACTOR_SOURCE"),
            ("2.5", "B", "architecture_ornament_nature_and_total_environment", "构造、装饰、自然形式和建筑整体的关系构成工艺美术总体环境的重要思想前史", "不等于唯美主义、新艺术或具体室内的生产与使用史", "补对象、室内、委托、工场、图像和用户材料", "ACCEPTED_AS_INTELLECTUAL_PREHISTORY"),
            ("2.7", "X", "racialized_style_genealogy_without_transfer_chain", "不使用其希腊／阿拉伯／拜占庭／哥特‘血统’叙述证明跨境影响或地方现代性", "地理—宗教本质化且缺贸易、人员、翻译、制作与接收方证据", "改用跨区域建筑史、贸易、工匠迁移和地方档案", "EXCLUDE_AS_TRANSFER_CORE_SOURCE"),
            ("15.4", "C", "workman_judgement_as_distant_participation_genealogy", "工人判断空间可作为参与式设计与劳动民主讨论的远距离思想谱系", "19世纪规范论不能替代当代参与机制、权力与效果证据", "补当代理论、项目、参与者和效果评估", "CONTEXT_ONLY_AS_GENEALOGY"),
        ],
    },
}


def load_assets():
    with ASSETS.open(encoding="utf-8-sig", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def file_hash(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_source(source_id, data, asset):
    clean = Path(asset["clean_source_path"])
    card = {
        "source_id": source_id,
        "corpus": asset["corpus"],
        "folder_name": asset["folder_name"],
        "material_type": data["type"],
        "clean_source_path": str(clean),
        "clean_source_sha256": file_hash(clean),
        "duplicate_group": data["duplicate_group"],
        "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
        "report_structure": {"review_basis": "overall_and_all_chapter_reports_plus_emergence_gap_audit"},
        "candidate_sections": [
            {"section_id": row[0], "grade": row[1], "verification": "V2", "role": row[2]}
            for row in data["maps"]
        ],
        "review_status": "semantic_review_complete",
        "evidence_level": "V2",
        "notes": data["limits"] + ["clean原文仅局部定位；未完成全篇、版次、图版、数字和引注核验。"],
        "original_spot_checks": data["checks"],
    }
    card_dir = BATCH / "source_cards"
    map_dir = BATCH / "mappings"
    (card_dir / f"{source_id}_来源卡.json").write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        f"# {source_id} 来源卡：{data['title']}", "", "## 一、来源身份与核验状态", "",
        "| 字段 | 内容 |", "|---|---|", f"| 来源ID | {source_id} |", f"| 作者／编者 | {data['author']} |",
        f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |", f"| 范围 | {data['scope']} |",
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |", f"| 版本／史料关系 | {data['duplicate_group']} |",
        f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
        "| 核验 | V2：全部分析报告与知识涌现资产复核＋clean关键段落局部回查 |", "",
        "## 二、核心命题与教材价值", "", data["summary"], "", "## 三、论证强项", "",
    ]
    md.extend(f"- {item}" for item in data["strengths"])
    md.extend(["", "## 四、限度与反例", ""])
    md.extend(f"- {item}" for item in data["limits"])
    md.extend(["", "## 五、章节准入", "", "| 章／节 | 等级 | 角色 | 可接受命题 | 边界 | 状态 |", "|---|---|---|---|---|---|"])
    for section, grade, role, claim, boundary, _follow, status in data["maps"]:
        md.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    md.extend(["", "## 六、clean原文局部回查", ""])
    md.extend(f"- {item}" for item in data["checks"])
    md.extend(["", "本卡不把P4分析报告或知识涌现命名升级为原著事实。正式引用须返回实际版次、页码、上下文、图版及关键P0材料。", ""])
    (card_dir / f"{source_id}_来源卡.md").write_text("\n".join(md), encoding="utf-8")

    fields = ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]
    with (map_dir / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for section, grade, role, claim, boundary, follow, status in data["maps"]:
            writer.writerow({
                "source_id": source_id, "section_id": section, "grade": grade, "verification": "V2",
                "role": role, "accepted_claim": claim, "evidence_boundary": boundary,
                "original_followup": follow, "status": status,
            })


def update_manifest():
    path = BATCH / "batch_manifest.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fields = list(rows[0])
    for row in rows:
        if row["source_id"] in DATA:
            row["semantic_review_status"] = "complete"
            row["mapping_status"] = "complete"
            row["original_verification_status"] = "partial_clean_text_spot_check"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    assets = load_assets()
    for source_id, data in DATA.items():
        write_source(source_id, data, assets[source_id])
    update_manifest()
    print(json.dumps({"completed": list(DATA), "mapping_rows": sum(len(item["maps"]) for item in DATA.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
