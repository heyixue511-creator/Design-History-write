#!/usr/bin/env python3
"""Complete fashion-cultural history and Victorian material-culture sources."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0080": {
        "title": "The Culture of Fashion: A New History of Fashionable Dress",
        "author": "Christopher Breward",
        "version": "Manchester University Press；1994编目、1995重印",
        "type": "时尚文化史、设计史与物质文化方法论",
        "scope": "以英格兰为主，从14世纪中期至20世纪末；重点为消费、现代性、性别、阶级、媒体与亚文化",
        "duplicate_group": "时尚文化史组：与消费史、亚文化研究及选集共享部分理论和案例；同一引文、图像或案例不重复计证",
        "summary": "Breward试图在服装形式编年、设计史和新文化史之间建立一种开放的时尚文化史，反对把服装看作社会结构的被动镜像，也反对精英风格单向向下传播的涓滴模型。第4—5章可校正‘消费革命—百货商店—大众消费’的线性进步叙事，并把印度棉布、裁缝、成衣、媒体、性别和阶级差异接入第二章。第6—7章为大众媒体、生活方式、朋克与街头风格提供后续路径，但书中亚文化多经媒体、零售和研究者解释出现，不能把某套服饰直接等同于统一政治立场。其英格兰中心、生产工序薄弱和1990年代当代观察限制了全球与近期解释。",
        "strengths": [
            "把服装形式、生产、消费、身体、身份、媒体和社会差异置于同一历史框架。",
            "系统批判涓滴理论、单因果和消费革命的无缝进步叙事。",
            "混合实物、图像、广告、杂志、文学、账目、通信与专利等多类材料。",
            "指出设计史的现代主义与男性化偏向，为时尚和女性劳动进入设计史提供学科批评。",
            "区分亚文化自我塑造、零售供给、媒体标签、商业吸收与研究者解释的潜在层次。",
        ],
        "limits": [
            "地理重心为英格兰，欧洲大陆与非西方地区主要作为影响或商品来源出现。",
            "服装构造、纺织技术、工场组织、裁缝与缝纫工劳动的系统性不足。",
            "图像与服装形态丰富，但本地OCR乱码、图注错位和图片可用性限制视觉核验。",
            "第七章依赖1990年代新闻与行业话语，距离当代事件过近且已明显过时。",
            "服装能参与形成差异，但不能由表象直接推断穿着者身份、意图、性取向或政治立场。",
            "P4报告的弧线、网络与综合命题不得当作原著独立实证发现。",
        ],
        "checks": [
            "clean第1—13行：版本、题名、1994编目与1995重印信息及七章结构。",
            "clean第50—79行：对裙摆史的辩证评价、设计史性别偏向、多学科框架与核心命题。",
            "clean第1329—1345行：对工业革命／消费革命宏大解释的警惕。",
            "clean第1435—1478行：印度棉布、商业与消费前史，以及反对仓库—百货—购物中心无缝进化。",
            "clean第1510—1545行：反涓滴证据与贫困群体消费形成自身身份的解释。",
            "clean第1938—1992行：百货商店、阶级市场、裁缝系统、成衣与劳动条件。",
            "clean第2274—2295行：后现代、街头风格、第三世界文化等被商业拼贴后政治意义可能流失的判断。",
            "clean第2488—2505行：朋克零售、亚文化与1980年代市场化生活方式之间的区分。",
        ],
        "maps": [
            ("0.2", "A", "fashion_historiography_and_anti_linear_periodization", "时尚史从形式编年转向文化史，并批判涓滴、革命断裂与单线现代化", "作者仍使用‘现代时尚诞生’等阶段命题且范围以英格兰为主", "补全球时尚史、生产史和区域比较", "ACCEPTED_AS_HISTORIOGRAPHIC_CORE"),
            ("0.3", "A", "form_production_consumption_identity_and_media_method", "服装形式须与生产、消费、身体、身份、媒体和多重意义共同解释", "开放解释不能免除对象、行动者和因果证据要求", "逐案例分开形式描述、行动者主张、制度机制和接受", "ACCEPTED_AS_METHOD"),
            ("0.5", "B", "objects_images_ads_magazines_literature_and_archives", "实物、图像、广告、杂志、文学、账目与通信可互校时尚话语和实践", "OCR及图像缺失限制引文与视觉核验，文学／广告不直接证明行为", "返回纸本、图版、档案、发行和消费者材料", "ACCEPTED_WITH_SOURCE_TYPE_BOUNDARIES"),
            ("0.6", "A", "england_visual_production_class_gender_identity_and_contemporary_bias", "英格兰中心、生产薄弱、图像偏差、阶级不对称、身份推断和当代新闻依赖须进入审计", "性别批评本身也不能替代劳动和对象证据", "补全球、工场、劳动、男性／女性／酷儿主体和较新研究", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.4", "B", "cotton_aniline_steel_support_and_clothing_materials", "棉布、苯胺染料、钢制裙撑和机织布说明材料技术如何介入服装形式", "不是材料技术或供应链专史，视觉描述待图像核验", "补原料、工艺、专利、样本、劳动与贸易", "ACCEPTED_WITH_TECHNICAL_FOLLOWUP"),
            ("1.5", "B", "tailors_seamstresses_retailers_media_and_wearers", "裁缝、缝纫工、零售者、媒体和穿着者共同参与时尚意义生产", "书中生产者覆盖不均，穿着图像不说明制作或意图", "补工资、工场、订单、口述、对象和使用材料", "ACCEPTED_AS_ACTOR_SUPPORT"),
            ("1.6", "A", "fashion_designer_and_gendered_design_history", "时尚在现代主义设计史中被女性化和边缘化，显示学科与职业分类的性别政治", "1990年代学科诊断需用后续教育、出版和职业数据更新", "补学科史、课程、协会、企业职位和近期研究", "ACCEPTED_AS_CONCEPT_AND_DISCIPLINE_HISTORY"),
            ("2.4", "A", "shops_department_stores_media_credit_and_active_consumers", "商店、百货、时尚媒体、成衣和消费者身份协商共同组织现代消费", "反涓滴不等于所有消费者自主，陈列和媒体也不能证明接受效果", "补销售、信用、家庭账目、顾客记录、使用和拒绝", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.5", "B", "aesthetic_dress_gender_body_and_lifestyle", "唯美服装、身体轮廓、室内消费与生活方式可补整体环境的穿着维度", "不是新艺术对象、室内和企业生产的完整专史", "与B0006、对象、设计者、制作和使用材料对读", "ACCEPTED_AS_FASHION_DIMENSION"),
            ("2.6", "B", "indian_cotton_oriental_taste_and_british_consumption", "印度棉布和东方趣味可显示英国时尚消费如何分类与再编码殖民商品", "英国消费端不能代表印度生产者、贸易强制或来源社会意义", "补殖民政策、贸易、工匠、染织知识和来源地使用", "ACCEPTED_AS_BRITISH_CONSUMPTION_DISCOURSE"),
            ("2.7", "A", "indian_textiles_trade_retail_and_identity_translation", "进口棉布、英国仿制、零售、穿着和身份建构提供跨境选择与再生产链", "不能把形式采用写成单向影响或完整技术转移", "补贸易、工艺、样本、生产者、穿着者与地方再生产", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("5.2", "B", "mass_fashion_advertising_ready_made_and_retail", "成衣、广告、杂志和分层零售可补大众消费体系的服装个案", "英国时尚史不能承担美国消费制度的核心叙事", "补美国企业、连锁、信用、媒体、劳动和消费者", "ACCEPTED_AS_COMPARATIVE_CASE"),
            ("5.6", "B", "gendered_body_clothing_home_and_efficiency", "服装、身体规范、家务与性别领域可校正效率史只写标准人体的倾向", "不是人体测量、厨房或科学管理专史", "补测量、家务劳动、残障、职业和家庭材料", "ACCEPTED_AS_GENDERED_BODY_CONTEXT"),
            ("11.1", "B", "consumer_society_youth_media_and_fashion", "大众消费、青年身份与媒体扩张为后现代设计危机提供时尚领域语境", "服装史不能单独解释城市更新、反设计或政治运动", "与建筑、媒体、运动和制度材料对读", "ACCEPTED_AS_SOCIAL_CONTEXT"),
            ("11.6", "A", "punk_retail_media_subculture_and_commercial_absorption", "朋克与街头风格须区分参与者实践、零售供给、媒体标签、设计师挪用和商业吸收", "服装符号不能直接等同于统一身份或政治立场，且材料多为二手／媒体", "补参与者自述、同期刊物、对象制作、销售、场景和反例", "ACCEPTED_AS_CORE_INTERPRETIVE_SOURCE_WITH_POSITION_CAUTION"),
            ("12.6", "A", "fashion_gender_body_labour_and_design_history_critique", "时尚史揭示设计正典、身体规范、女性劳动与公共／私人领域的性别建构", "性别表征不能替代实际劳动、制度和多样主体经验", "补女性／酷儿／男性劳动者、教育、企业、工资和使用材料", "ACCEPTED_AS_CORE_GENDER_CRITIQUE"),
            ("13.2", "C", "designer_lifestyle_media_and_brand_system_prehistory", "生活方式媒体和设计师品牌可为品牌体验系统提供20世纪末时尚个案", "1995年材料不能解释平台时代或中国品牌体系", "补企业档案、空间、服务、组织文化、用户与中国材料", "CONTEXT_ONLY"),
        ],
    },
    "B0052": {
        "title": "Victorian Things",
        "author": "Asa Briggs",
        "version": "B. T. Batsford 1988初版；University of Chicago Press 1989版",
        "type": "维多利亚物质文化史、技术—消费—展览综合史",
        "scope": "1837—1901年英国，以1851博览会、日常物、家庭、煤铁纸、邮政和新技术为专题",
        "duplicate_group": "维多利亚物史组：与展览史、技术史及消费史共享官方目录、评论和常见案例；相同P0材料不重复计证",
        "summary": "Briggs以‘物是文化的使节’为方法论起点，通过相互关联的专题把1851年展览、分类与收藏、视觉技术、日常用品、家庭、煤铁纸、邮票和新技术写成维多利亚物质文明史。它的价值不在提供一条整齐的设计风格线，而在把物质遗存同广告、文学、遗嘱、统计、技术文献和博物馆材料互校，并显示物的丰裕、贫困、分类权力、家庭道德和能源基础相互纠缠。由于选题选择性强、英国与中产阶级重心明显，性别、帝国、殖民生产者和工人经验不足；作为1988年综合史，具体数字、技术优先权和世界领先／落后判断须回P0和较新研究。",
        "strengths": [
            "以多种物和材料组织历史，避免只写名家与经典作品。",
            "把物质遗存与广告、文学、遗嘱、统计、技术文献和博物馆材料互证。",
            "以展览分类、收藏和博物馆说明知识秩序本身是历史对象。",
            "把煤、铁、纸与家庭、媒体、邮政和消费连接为物质基础设施。",
            "强调维多利亚风格多重、重叠和循环，抵制单线进步叙事。",
        ],
        "limits": [
            "专题选择具有作者个人性，不能代表维多利亚物的系统抽样。",
            "中产阶级家庭、收藏和文字材料较强，工人阶级与贫困者的物质生活较弱。",
            "性别维度分散，女性作为制造者、家务劳动者与消费者未系统展开。",
            "帝国和日本、印度、澳大利亚等联系分散且以英国视角为主。",
            "1988年综合史中的技术、统计和国别比较需以较新专史复核。",
            "P4报告的跨章‘技术动力学’、枢纽和综合模型不等于作者明示结论。",
        ],
        "checks": [
            "clean第1—20行：题名、作者、出版信息和物质文化定位。",
            "clean第66—150行：‘物作为使节’、人物—城市—事物三部曲、商品拜物与物质证据方法。",
            "clean第380—399行：Pitt-Rivers收集、进化分类与material culture概念。",
            "clean第475行附近：作者把帝国、阶级、性别和儿童物作为分类问题提出。",
            "clean第780—810行：1851年博览会分类争论、材料类别和大型展示。",
            "clean第1125—1155行：艺术制造、生产者／消费者与博览会审美争议。",
            "clean第3382—3425行：家庭道德文本、Beeton、Eastlake与现实家庭实践之间的距离。",
            "clean第4606—4629行：煤、铁、纸和carboniferous capitalism的物质—传播联系。",
            "clean第4770—4805行：Jevons的煤、能源、英国竞争和技术未来判断及作者的后见评论。",
        ],
        "maps": [
            ("0.2", "B", "multiple_victorian_periods_and_non_linear_style", "早中晚维多利亚内部存在重叠、竞争和循环的多重物质文化", "三段分期仍是组织工具，不能抹去区域、阶级和帝国差异", "补细分时段、地区和对象序列", "ACCEPTED_AS_PERIODIZATION_SUPPORT"),
            ("0.3", "A", "things_as_emissaries_multi_source_material_culture_method", "对象须同制作、使用、展示、分类、文字与制度证据共同解释", "物不是透明文化密码，‘使节’隐喻仍需中介和反例", "逐对象分开物证、文本、行动者和作者解释", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "objects_ads_literature_wills_statistics_technical_and_museum_sources", "实物、广告、文学、遗嘱、统计、技术文献与馆藏可互补各自沉默", "文学和广告不直接证明行为，统计与实物样本均有保存偏差", "返回版本、样本、档案、目录、图版和统计口径", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "selective_middle_class_gender_empire_worker_and_recency_bias", "专题选择、中产中心、性别／帝国分散、工人弱与研究年代须进入审计", "作者提出问题不等于已补足证据", "补劳动史、性别史、帝国史、区域史和较新技术史", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.2", "A", "coal_iron_steam_paper_transport_and_scale", "煤、铁、蒸汽与纸构成生产、交通、包装和信息扩张的相互依赖系统", "宏观综合不能替代单项技术、能源数量和环境后果核验", "补能源、产量、设备、企业、劳动和环境P0", "ACCEPTED_AS_CORE_MATERIAL_INFRASTRUCTURE"),
            ("1.4", "A", "coal_iron_steel_glass_paper_dye_and_rubber_systems", "基础材料、合成染料、橡胶、玻璃和纸的新组合拓展对象形式与流通", "技术首创和国别领先判断需现代专史与专利复核", "补专利、配方、样本、供应链、企业和环境记录", "ACCEPTED_AS_CORE_MATERIAL_SOURCE"),
            ("1.5", "B", "common_things_makers_users_and_anonymous_design", "火柴、针、笔、眼镜、邮票等平凡物显示匿名制造者、制度与用户共同塑造设计", "综合史常以发明者和制度代表普通劳动，工人声音仍弱", "补工厂、工资、专利、维护、使用和失败案例", "ACCEPTED_AS_COMMON_OBJECT_SUPPORT"),
            ("1.6", "B", "art_manufactures_common_things_and_design_categories", "art manufactures、common things等分类显示设计概念在艺术、制造和日用物之间竞争", "分类用语不能自动对应职业设计师制度", "补同期目录、学校、行业组织、职位和词典", "ACCEPTED_AS_CONCEPT_HISTORY_SUPPORT"),
            ("2.1", "A", "great_exhibition_objects_materials_classification_and_spectacle", "1851年展览通过材料、对象、分类、规模与观看组织物的公共世界", "综合史不能独立证明组织、观众接受、殖民来源或逐件制作", "与B0049、B0339、B0175及官方目录／对象互证", "ACCEPTED_AS_CORE_SYNTHETIC_SOURCE"),
            ("2.2", "B", "collection_museum_classification_and_knowledge_governance", "Pitt-Rivers收藏、博物馆与展览分类说明对象秩序如何生产知识与等级", "进化分类的描述不能成为教材自身的中性分类", "补机构档案、征集来源、来源社群和分类变更", "ACCEPTED_AS_CLASSIFICATION_SUPPORT"),
            ("2.4", "A", "plenitude_goods_ads_home_and_consumer_conditions", "商品范围、广告、家庭物、收藏与贫困并置可说明消费者所处的物质条件和社会差异", "物的增殖不等于普遍占有、购买动机或相同使用", "补价格、工资、信用、家庭清单、典当、维修和使用", "ACCEPTED_AS_CORE_MATERIAL_CULTURE_SOURCE"),
            ("2.5", "A", "hearth_home_household_taste_and_material_practice", "家庭道德、家务管理、品味指南、家具与实际住宅之间的落差构成整体环境的核心问题", "规范文本不能代表家庭实践，性别与劳动材料不均", "补室内清单、家务劳动、住宅、对象、女性与仆役材料", "ACCEPTED_AS_CORE_DOMESTIC_SOURCE"),
            ("2.6", "B", "exhibition_collection_empire_and_evolutionary_classification", "展览和收藏把帝国物品纳入英国的材料、用途和进化序列", "缺少来源社会主体且帝国分析分散，不能承担殖民经验", "补征集、贸易、殖民档案、被分类者与来源社群材料", "ACCEPTED_AS_BRITISH_CLASSIFICATION_CONTEXT"),
            ("2.7", "B", "japan_india_materials_trade_and_british_selection", "日本趣味、印度纺织与跨国材料可显示英国对外来物的选择和再编码", "零散英国叙事不能证明完整传播、地方能动性或双向交换", "补贸易、旅行、译介、工匠、对象与地方再生产", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("3.6", "B", "photography_print_paper_and_new_visual_regime", "摄影、印刷、纸张和图像传播改变对象被看见、记录与复制的条件", "不是先锋摄影、字体或版式的专史，图像需逐件核验", "补照片、出版、技术、设计者、发行和观众", "ACCEPTED_AS_VISUAL_MEDIA_PREHISTORY"),
            ("5.6", "B", "household_management_taste_gender_and_efficiency_prehistory", "家务管理、家庭道德和品味指南是20世纪家务效率制度的19世纪前史", "不含完整人体测量、科学管理或厨房设计链", "补时间研究、设备、家务劳动者、住宅和使用材料", "ACCEPTED_AS_DOMESTIC_PREHISTORY"),
            ("12.3", "C", "coal_energy_material_plenitude_and_environmental_prehistory", "煤炭能源、材料增殖和废弃可作为生命周期与环境设计的长时段前史", "本书不是生态设计、碳核算或环境正义研究", "补排放、污染、开采、劳动、生命周期和当代理论", "CONTEXT_ONLY_AS_ENVIRONMENTAL_PREHISTORY"),
        ],
    },
}


def load_assets():
    with ASSETS.open(encoding="utf-8-sig", newline="") as handle:
        return {r["source_id"]: r for r in csv.DictReader(handle)}


def digest(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_source(source_id, data, asset):
    clean = Path(asset["clean_source_path"])
    card = {"source_id": source_id, "corpus": asset["corpus"], "folder_name": asset["folder_name"],
            "material_type": data["type"], "clean_source_path": str(clean), "clean_source_sha256": digest(clean),
            "duplicate_group": data["duplicate_group"],
            "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
            "report_structure": {"review_basis": "overall_and_all_chapter_reports_plus_emergence_gap_audit"},
            "candidate_sections": [{"section_id": r[0], "grade": r[1], "verification": "V2", "role": r[2]} for r in data["maps"]],
            "review_status": "semantic_review_complete", "evidence_level": "V2",
            "notes": data["limits"] + ["clean原文仅局部定位；未完成全篇、版次、图版、数字和引注核验。"],
            "original_spot_checks": data["checks"]}
    card_dir, map_dir = BATCH / "source_cards", BATCH / "mappings"
    (card_dir / f"{source_id}_来源卡.json").write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = [f"# {source_id} 来源卡：{data['title']}", "", "## 一、来源身份与核验状态", "", "| 字段 | 内容 |", "|---|---|",
          f"| 来源ID | {source_id} |", f"| 作者／编者 | {data['author']} |", f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |",
          f"| 范围 | {data['scope']} |", f"| clean SHA-256 | `{card['clean_source_sha256']}` |", f"| 版本／史料关系 | {data['duplicate_group']} |",
          f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
          "| 核验 | V2：全部分析报告与知识涌现资产复核＋clean关键段落局部回查 |", "", "## 二、核心命题与教材价值", "",
          data["summary"], "", "## 三、论证强项", ""]
    md.extend(f"- {x}" for x in data["strengths"]); md.extend(["", "## 四、限度与反例", ""]); md.extend(f"- {x}" for x in data["limits"])
    md.extend(["", "## 五、章节准入", "", "| 章／节 | 等级 | 角色 | 可接受命题 | 边界 | 状态 |", "|---|---|---|---|---|---|"])
    for section, grade, role, claim, boundary, _follow, status in data["maps"]:
        md.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    md.extend(["", "## 六、clean原文局部回查", ""]); md.extend(f"- {x}" for x in data["checks"])
    md.extend(["", "本卡不把P4分析报告或知识涌现命名升级为原著事实。正式引用须返回实际版次、页码、上下文、图版及关键P0材料。", ""])
    (card_dir / f"{source_id}_来源卡.md").write_text("\n".join(md), encoding="utf-8")
    fields = ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]
    with (map_dir / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields); w.writeheader()
        for section, grade, role, claim, boundary, follow, status in data["maps"]:
            w.writerow({"source_id": source_id, "section_id": section, "grade": grade, "verification": "V2", "role": role,
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
        w = csv.DictWriter(handle, fieldnames=fields); w.writeheader(); w.writerows(rows)


def main():
    assets = load_assets()
    for source_id, data in DATA.items(): write_source(source_id, data, assets[source_id])
    update_manifest()
    print(json.dumps({"completed": list(DATA), "mapping_rows": sum(len(x["maps"]) for x in DATA.values())}, ensure_ascii=False))


if __name__ == "__main__": main()
