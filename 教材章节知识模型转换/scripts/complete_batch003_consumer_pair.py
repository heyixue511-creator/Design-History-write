#!/usr/bin/env python3
"""Complete Liberty retail biography and the contested consumer-revolution classic."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0006": {
        "title": "Liberty's: A Biography of a Shop",
        "author": "Alison Adburgham",
        "version": "George Allen & Unwin, 1975",
        "type": "企业百年史、零售文化史、时尚与装饰艺术传播史",
        "scope": "Liberty从1875年创店至1975年；重点为1880—1914年的零售、织物、唯美主义、新艺术与跨国采购",
        "duplicate_group": "Liberty企业史料组：公司内刊、家族材料与后续Liberty研究可能重复；同一企业叙事和引文不得重复计证",
        "summary": "Adburgham把Liberty写成一家具有持续人格的商店，通过公司内刊、家族材料、馆藏记录、采访与报刊重建其从东方商品零售商到织物、服装、室内和金属工艺品牌的路径。它能具体说明橱窗、目录、展览、剧场、命名、代理、巴黎分店、生产整合与匿名设计政策如何共同组织消费和风格传播，也揭示进口材料、英国加工、品牌化和跨国复制的混合链。由于本书为百年纪念企业传记并得到公司与家族协助，其‘改变品味’主张、创始人轶事和员工福利叙述不能独立证明市场效果或劳动现实；‘东方’描述必须作为英国零售话语审读。",
        "strengths": [
            "连接店铺空间、橱窗、目录、剧场、展览、代理、合同和生产基地等多种零售机制。",
            "追踪进口坯料、英国染印、机器适配、默顿工坊与品牌命名的混合生产链。",
            "记录匿名设计政策、企业署名、仿冒诉讼与品牌控制，可审计作者制和知识产权。",
            "覆盖唯美主义、新艺术、服装、织物、银器与锡器，适合跨媒介商业现代性。",
            "保存员工回忆、公司内刊和家族经营资料，为进一步返回P0档案提供路线。",
        ],
        "limits": [
            "1975百年企业传记得到公司主席、家族和员工协助，存在企业自我叙事与纪念性偏向。",
            "无完整参考书目，若干轶事、首创、销量、影响和因果判断难以逐条追索。",
            "创始人和管理者主导叙事，工人、女性、殖民地生产者与消费者多经企业视角出现。",
            "‘东方’被作为商品来源、色彩秘密和品牌想象，容易抹去生产者、贸易强制与地方知识。",
            "橱窗、目录、奖项、记者评论和销售供给不能直接证明欲望、购买动机或使用效果。",
            "P4报告的创新周期、品牌悖论和隐形贡献等模型不得反写成原书实证结论。",
        ],
        "checks": [
            "clean第1—24行：1975年版、作者把商店拟作传记及其‘反映并推动品味’的中心主张。",
            "clean第99—116行：1862年展览、日本展区、Farmer & Rogers采购和Oriental Warehouse工作路径。",
            "clean第257—288行：Dresser对照、进口不足、英国机器适配、Wardle染色与Liberty Colours。",
            "clean第471—484行：Merton既有印花业、Littler合作、生产能力与Morris设厂先后。",
            "clean第783—811行：品牌标记、仿冒诉讼、1889博览会和巴黎分店的跨境扩张。",
            "clean第1048—1082行：Cymric／Tudric的推出、生产和参与者叙述。",
            "clean第1091—1104行：公司匿名设计政策及Archibald Knox等作者归属问题。",
        ],
        "maps": [
            ("0.3", "B", "retail_enterprise_media_production_and_style_method", "商店史可把零售空间、媒体、生产、品牌、跨境流通和风格运动连接起来", "企业人格化可能把结构与多行动者压缩为创始人意志", "补机构、工人、生产者、顾客与竞争者材料", "ACCEPTED_AS_ENTERPRISE_METHOD_CASE"),
            ("0.5", "B", "corporate_magazine_family_archive_interview_and_press", "公司内刊、家族材料、采访、馆藏和报刊可相互定位企业事件", "无完整书目且资料接近企业，当前只能作路由与有限转述", "返回公司档案、广告、目录、合同、账簿和报刊原件", "ACCEPTED_WITH_PROVENANCE_FOLLOWUP"),
            ("0.6", "A", "corporate_commemoration_founder_worker_gender_colonial_and_audience_bias", "纪念性企业叙事、创始人中心、工人／女性／殖民生产者缺口和受众效果断点须进入审计", "企业材料丰富不等于独立验证", "补独立商业史、劳动史、殖民贸易与消费者材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "import_dye_print_machine_block_and_brand_control", "进口坯料、英国染印、机器适配、木版工艺、品牌标记和诉讼共同组织构思—制作—控制", "企业品牌不能自动确定逐件设计者与生产者", "补样本、配方、图样、订单、工序、合同和诉讼卷宗", "ACCEPTED_AS_CORE_PRODUCTION_CASE"),
            ("1.4", "A", "silk_cotton_dye_water_print_and_metal_material_system", "丝、棉、染料、水质、木版、机器织造及金属合金说明材料供应如何限定产品", "‘东方秘密’和性能主张多为企业／作者叙述，未做物质核验", "补来源地生产、贸易、配方、样本检测和环境记录", "ACCEPTED_WITH_TECHNICAL_COLONIAL_FOLLOWUP"),
            ("1.5", "A", "anonymous_designers_suppliers_workers_and_corporate_authorship", "匿名设计政策、外部设计师、供应商、工坊与品牌共同制造企业作者制", "匿名并不表示无作者，后世归属也需对象级证据", "补设计簿、订单、工资、样品、印记和个人档案", "ACCEPTED_AS_CORE_AUTHORSHIP_CASE"),
            ("1.6", "B", "buyer_manager_designer_consultant_and_window_roles", "采购者、部门经理、外部设计师、设计顾问和橱窗设计等角色展示零售设计职业分化", "百年叙事跨期，不能把后期职位倒投到19世纪", "逐期补职位、合同、职责、薪酬和职业组织", "ACCEPTED_AS_ROLE_HISTORY"),
            ("2.3", "B", "morris_liberty_machine_craft_and_affordability_contrast", "Liberty与Morris在机器、手工、价格和大众可及性上的差异可构成工艺美术内部比较", "作者的二元对比可能简化两者混合生产和实际顾客结构", "与B0070、B0348、账簿、工艺和顾客材料互证", "ACCEPTED_WITH_COMPARATIVE_AUDIT"),
            ("2.4", "A", "shop_window_catalogue_display_brand_and_consumer_mediation", "店铺、橱窗、目录、剧场、展览、命名、奖项和代理共同构成现代消费者的中介条件", "供给、曝光和评论不能证明消费者被动接受或欲望被成功制造", "补销售、价格、信用、顾客记录、家庭清单与使用材料", "ACCEPTED_AS_CORE_RETAIL_SOURCE"),
            ("2.5", "A", "aestheticism_art_nouveau_fashion_interior_and_product_system", "织物、服装、家具、室内、珠宝和金属器把唯美主义与新艺术组织为商业化生活方式", "运动命名、品牌归属和设计者身份存在企业叙事与后见之明", "补对象、设计簿、委托、展览、评论、住宅与使用史", "ACCEPTED_AS_CORE_SOURCE_WITH_OBJECT_GAP"),
            ("2.6", "B", "oriental_warehouse_colonial_merchandising_and_classification", "Oriental Warehouse、商品命名和进口分类可显示英国零售如何消费性地组织亚洲物品", "不能用来代表日本、中国、印度等生产者自我分类或殖民经验", "补来源地工匠、贸易、采购、殖民制度和地方消费材料", "ACCEPTED_AS_BRITISH_RETAIL_DISCOURSE_ONLY"),
            ("2.7", "A", "asia_britain_paris_trade_translation_and_reproduction", "进口、英国改制、巴黎分店、代理、仿冒与地方生产构成选择—翻译—再生产链", "‘东方影响’不能由风格相似或企业宣传单向推出", "补贸易、人员、合同、样本、生产者和接收方材料", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("5.1", "B", "liberty_between_art_nouveau_and_art_deco_revival", "Liberty产品、巴黎时尚合作与后来的历史复兴可补装饰艺术商业谱系", "本书并非1925巴黎博览会或Art Deco核心研究", "补展览、对象、设计师、生产和同期评论", "ACCEPTED_AS_COMMERCIAL_CONTEXT"),
            ("5.5", "B", "retail_design_consultant_brand_and_anonymous_professionalization", "企业内部设计顾问、匿名设计和品牌控制可补商业设计职业化路径", "企业职位史不等于行业总体职业制度", "补合同、薪酬、组织、教育和行业比较", "ACCEPTED_AS_ENTERPRISE_ROLE_CASE"),
        ],
    },
    "B0305": {
        "title": "The Birth of a Consumer Society: The Commercialization of Eighteenth-Century England",
        "author": "Neil McKendrick、John Brewer、J. H. Plumb",
        "version": "Europa 1982初版；Indiana University Press 1985 Midland版",
        "type": "经典消费史、商业化史、经济—政治—社会史合著",
        "scope": "18世纪英格兰，核心为1760—1800年；消费革命、时尚商业化、Wedgwood、广告、信用、休闲与儿童市场",
        "duplicate_group": "消费革命学术史组：后续选集和消费史会重述本书命题；同一Wedgwood书信或广告原件不重复计证",
        "summary": "三位作者以‘商业化’统摄经济、政治与社会史，主张18世纪英格兰发生了与工业革命相匹配的消费革命。McKendrick尤其通过Wedgwood书信、广告、贸易卡、展厅、定价、贵族赞助和社会模仿说明企业如何主动扩张需求。本书能为第一章提供企业—市场—设计的强个案，也能为第二章2.4提供百货商店出现之前的零售、展示和消费机制前史。其1982年的‘世界第一个消费社会’、单向向上模仿、消费民主化和企业操纵叙事已成为争议对象；教材必须把这些标为作者命题，并补荷兰／欧洲、殖民商品、奴隶制、家庭劳动、消费者能动性和后续消费史。",
        "strengths": [
            "把需求侧、零售者、广告者和中小商人带回工业化解释。",
            "以Wedgwood—Bentley书信、广告、贸易卡、账目与实物建立企业营销个案。",
            "区分时尚、赞助、陈列、价格、信用、代理和媒体等不同商业机制。",
            "三位作者把经济、政治、休闲、儿童与现代性心态置于共同框架中。",
            "公开承认供给端生产、资本、劳动纪律和技术仍是企业成功条件。",
        ],
        "limits": [
            "‘世界第一个’与18世纪断裂论具有英格兰例外主义，荷兰、欧洲大陆和更早消费前史不足。",
            "社会模仿被窄化为下层向上层的仿效，弱化区分、拒绝、横向传播、身份和使用。",
            "‘商业操纵创造需求’常用强因果措辞，但消费者记录和反事实不足。",
            "消费民主化可能遮蔽贫困、债务、劳动延长、女性／儿童工时及不同阶层的损益。",
            "棉布、茶、糖、陶瓷等全球商品与殖民、奴隶制、强制贸易的关系处理不足。",
            "P4报告提出的正反馈环、阴影版本和十一项涌现发现是二次推理，不是原书明示。",
        ],
        "checks": [
            "clean第1—20行：题名、三位作者与版本前置页。",
            "clean第99—135行：消费革命宣言、奢侈／体面／必需品转换、商人主动作用与供给侧史学批评。",
            "clean第159—180行：18世纪分水岭、消费革命与工业革命的‘必要对应’命题。",
            "clean第271—299行：工资、家庭劳动、女性与儿童收入、长工时和遗产清单被用于消费扩展论证。",
            "clean第319—330行：作者说明为何消费扩张被经济史忽视，同时显露对悲观工业革命叙事的反论战立场。",
            "clean第787行：作者总结陈列、广告、时尚与社会模仿如何激发需求；属于强机制主张。",
            "clean第864—900行：Wedgwood借贵族、建筑师、展厅、陈列与地区网络组织时尚和销售。",
            "clean第990—1003行：作者把营销扩张与技术、资本、债务、劳动纪律和生产控制重新并置。",
        ],
        "maps": [
            ("0.2", "A", "consumer_revolution_historiographic_thesis", "‘消费革命’是改变设计史生产中心叙事的经典史学命题，也必须连同后续批评教授", "不能把1982年的‘第一’和断裂论当作无争议定论", "补Berg、de Vries、Brewer／Porter及跨区域研究", "ACCEPTED_AS_HISTORIOGRAPHIC_CORE"),
            ("0.3", "A", "demand_supply_commercialization_and_material_culture_method", "生产、需求、企业策略、政治制度、社会心态和物质证据可被置于共同解释框架", "三位作者对商业化的具体机制并未完全统一", "分作者、分章节、分机制使用并补反事实", "ACCEPTED_AS_METHOD_WITH_INTERNAL_DIFFERENCE"),
            ("0.5", "A", "letters_ads_trade_cards_inventories_objects_and_press", "企业书信、广告、贸易卡、遗产清单、实物与报刊可互校消费供给和商业意图", "商业意图与广告存在不能直接证明消费者心理和行为", "补销售、顾客、家庭账目、使用、拒绝与地方材料", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "england_first_emulation_causality_class_gender_and_colonial_bias", "英格兰例外主义、模仿窄化、强因果、阶级损益、性别与殖民缺口须进入审计", "后续批评和本书内部反例均需实证定位", "补比较消费史、殖民史、劳动史、性别史和消费者材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "wedgwood_design_production_marketing_and_control", "Wedgwood的设计、生产、展厅、样本、定价和销售控制说明构思与制作分离必须连到企业和市场", "营销史不能替代工厂内部逐件作者、工序和工人经验", "补设计簿、模具、工场、工资、工人和对象材料", "ACCEPTED_AS_CORE_ENTERPRISE_CASE"),
            ("1.4", "B", "ceramic_material_technology_and_product_differentiation", "creamware、jasper等材料技术与产品等级、价格和市场分层相互作用", "本书重点在商业化，不是陶瓷技术或材料供应链专史", "补配方、窑炉、原料、技术档案和对象检测", "ACCEPTED_WITH_TECHNICAL_FOLLOWUP"),
            ("1.5", "A", "entrepreneur_partner_artist_worker_retailer_and_consumer_network", "企业家、合伙人、艺术家、工人、零售者、赞助人和消费者共同形成商品网络", "行动者被企业档案不均衡照亮，普通工人和消费者声音较弱", "补对象级责任、工资、订单、顾客和家庭材料", "ACCEPTED_AS_ACTOR_NETWORK"),
            ("1.6", "A", "manufacturer_marketer_taste_legislator_and_retail_roles", "manufacturer、商人、品味立法者、广告者和零售者等角色显示工业艺术的职业功能分化", "不等于现代职业设计师已经形成", "补同期称谓、合同、行业组织与教育材料", "ACCEPTED_AS_ROLE_HISTORY"),
            ("1.7", "B", "english_consumer_revolution_as_contested_regional_path", "英格兰消费—生产互动可作为区域工业化路径之一", "不能外推为欧洲或全球唯一／最早道路", "补荷兰、法国、亚洲、殖民地和区域内部比较", "ACCEPTED_AS_CONTESTED_REGIONAL_CASE"),
            ("2.3", "C", "luxury_debate_and_moral_economy_context", "奢侈、体面、必要与消费伦理争论可作为Ruskin／Morris反消费批评的18世纪前史", "不直接研究工艺美术劳动伦理", "与B0383、B0133及19世纪改革文本对读", "CONTEXT_ONLY_AS_PREHISTORY"),
            ("2.4", "B", "shops_showrooms_display_ads_credit_and_consumer_prehistory", "展厅、陈列、广告、价格、信用和代理构成19世纪百货商店之前的消费中介机制", "时段主要为18世纪且无成熟百货制度，不能直接承担本节全部核心叙事", "补19世纪商店、百货档案、顾客、信用和使用史", "ACCEPTED_AS_MAJOR_PREHISTORY"),
            ("2.6", "C", "global_goods_without_colonial_power_analysis", "茶、棉布、陶瓷等可提示消费社会依赖跨境商品", "全书不能承担殖民分类、奴隶制或来源社会生产史", "补殖民贸易、奴隶制、原料、生产者与来源地档案", "CONTEXT_ONLY_WITH_COLONIAL_GAP"),
            ("2.7", "C", "calico_porcelain_trade_and_market_transfer_context", "棉布、瓷器、时尚版画和贸易网络可作为跨境物质流动入口", "英格兰消费端材料不能证明地方生产者能动性或完整迁移链", "补贸易、关税、样本、工艺、来源地和再生产", "CONTEXT_ONLY_WITH_TRANSFER_FOLLOWUP"),
            ("5.3", "C", "advertising_display_and_branding_prehistory", "广告、陈列、品牌与市场细分可作为20世纪大众传媒商业设计的长时段前史", "18世纪材料不能证明20世纪媒体制度和受众效果", "补20世纪企业、媒介、设计师、发行和受众材料", "CONTEXT_ONLY_AS_PREHISTORY"),
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
        "source_id": source_id, "corpus": asset["corpus"], "folder_name": asset["folder_name"],
        "material_type": data["type"], "clean_source_path": str(clean), "clean_source_sha256": file_hash(clean),
        "duplicate_group": data["duplicate_group"],
        "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
        "report_structure": {"review_basis": "overall_and_all_chapter_reports_plus_emergence_gap_audit"},
        "candidate_sections": [{"section_id": r[0], "grade": r[1], "verification": "V2", "role": r[2]} for r in data["maps"]],
        "review_status": "semantic_review_complete", "evidence_level": "V2",
        "notes": data["limits"] + ["clean原文仅局部定位；未完成全篇、版次、图版、数字和引注核验。"],
        "original_spot_checks": data["checks"],
    }
    card_dir, map_dir = BATCH / "source_cards", BATCH / "mappings"
    (card_dir / f"{source_id}_来源卡.json").write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = [f"# {source_id} 来源卡：{data['title']}", "", "## 一、来源身份与核验状态", "",
          "| 字段 | 内容 |", "|---|---|", f"| 来源ID | {source_id} |", f"| 作者／编者 | {data['author']} |",
          f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |", f"| 范围 | {data['scope']} |",
          f"| clean SHA-256 | `{card['clean_source_sha256']}` |", f"| 版本／史料关系 | {data['duplicate_group']} |",
          f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
          "| 核验 | V2：全部分析报告与知识涌现资产复核＋clean关键段落局部回查 |", "",
          "## 二、核心命题与教材价值", "", data["summary"], "", "## 三、论证强项", ""]
    md.extend(f"- {x}" for x in data["strengths"])
    md.extend(["", "## 四、限度与反例", ""]); md.extend(f"- {x}" for x in data["limits"])
    md.extend(["", "## 五、章节准入", "", "| 章／节 | 等级 | 角色 | 可接受命题 | 边界 | 状态 |", "|---|---|---|---|---|---|"])
    for section, grade, role, claim, boundary, _follow, status in data["maps"]:
        md.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    md.extend(["", "## 六、clean原文局部回查", ""]); md.extend(f"- {x}" for x in data["checks"])
    md.extend(["", "本卡不把P4分析报告或知识涌现命名升级为原著事实。正式引用须返回实际版次、页码、上下文、图版及关键P0材料。", ""])
    (card_dir / f"{source_id}_来源卡.md").write_text("\n".join(md), encoding="utf-8")
    fields = ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]
    with (map_dir / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader()
        for section, grade, role, claim, boundary, follow, status in data["maps"]:
            writer.writerow({"source_id": source_id, "section_id": section, "grade": grade, "verification": "V2", "role": role,
                             "accepted_claim": claim, "evidence_boundary": boundary, "original_followup": follow, "status": status})


def update_manifest():
    path = BATCH / "batch_manifest.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle)); fields = list(rows[0])
    for row in rows:
        if row["source_id"] in DATA:
            row["semantic_review_status"] = "complete"; row["mapping_status"] = "complete"
            row["original_verification_status"] = "partial_clean_text_spot_check"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(rows)


def main():
    assets = load_assets()
    for source_id, data in DATA.items(): write_source(source_id, data, assets[source_id])
    update_manifest()
    print(json.dumps({"completed": list(DATA), "mapping_rows": sum(len(x["maps"]) for x in DATA.values())}, ensure_ascii=False))


if __name__ == "__main__": main()
