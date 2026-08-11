#!/usr/bin/env python3
"""Write the nine remaining human-reviewed records for BATCH-001-CH01-CH02.

The data below records a one-off semantic review.  Report-derived discoveries are
used only for routing and criticism; accepted claims are bounded by the source's
own argument and by clean-text spot checks.  All sources remain V2.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-001-CH01-CH02"
CARD_DIR = BATCH / "source_cards"
MAP_DIR = BATCH / "mappings"
ASSET_CSV = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


SOURCES = {
    "B0005": {
        "title": "Global Design History",
        "author": "Glenn Adamson、Giorgio Riello、Sarah Teasley 编；各章作者分别负责章内论证",
        "version": "Routledge, 2011；带页标记的转换文本",
        "material_type": "全球设计史方法论论文集",
        "scope": "14个跨时期、跨区域案例及逐章回应；不是全球设计通史",
        "duplicate_group": "VGRP001",
        "summary": "本书把全球设计史界定为一种研究方法，而不是一个可由全球名物填满的题目。其核心做法是以连接、比较和对象为路径，追踪地方物如何卷入超地方的材料、贸易、制度与意义过程。景德镇瓷器、印度棉布、日本茶道和南非国际展览等章节说明，地方生产者并非被动接收者；跨境流动会经过订货、工艺适配、语言命名、消费验证与展示制度而改变。",
        "strengths": [
            "主文与回应成对设置，使案例的概括、反例和方法边界同时可见。",
            "把对象细读同贸易、生产、展览和知识分类连接，适合导论及1.7、2.7。",
            "明确反对把设计史的全球化等同于扩大欧美正典的地理清单。",
        ],
        "limits": [
            "论文集不是一套无冲突的统一理论；引用时必须署具体章作者。",
            "欧洲和北美学术网络仍居中心，拉丁美洲、东欧、中亚等区域薄弱。",
            "部分章节重文化交换、轻结构性不平等；不能把连接自动写成互惠。",
            "景德镇、印度棉布和茶道案例不能互相替代，亦不能证明受众效果。",
        ],
        "spot_checks": [
            "导论第547行、PDF页3：全球设计史是方法而非题目。",
            "导论第674—676行、PDF页20：物总在地方，但可折叠超地方过程。",
            "Anne Gerritsen章第1774—1779行、PDF页46：更换蓝绘图样可不改变其余生产链。",
            "Prasannan Parthasarathi回应第2500—2505行、PDF页63：应说在英格兰／印度的设计，而非本质化民族设计。",
            "Christine Guth章第2580—2584行、PDF页65：进口替代可表现为以异质之物替代。",
        ],
        "mappings": [
            ("0.3", "A", "relational_global_design_history", "全球设计史应从英雄与名物清单转向对象、连接、比较和多地点关系", "这是编者的方法论主张，不代表论文集各章已消除欧美中心偏差", "回各章原文与所引区域研究，核定具体作者和页码", "ACCEPTED_WITH_LIMITS"),
            ("0.4", "B", "object_as_local_methodological_tool", "地方对象可作为追踪跨地域材料、技术和意义过程的方法工具", "物不是自足文本；制造地、流通地、使用地和收藏地须分开", "补对象检验、博物馆记录、贸易与使用材料", "ACCEPTED_AS_METHOD"),
            ("0.6", "B", "source_asymmetry_and_canonical_bias", "全球设计史须公开区域材料保存与可见性的不对称", "报告网络发现只构成审计线索，不能当成原书统计事实", "补各区域档案史与缺席主体材料", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("0.7", "A", "connections_comparisons_objects", "连接、比较和对象可构成全球设计史的互补路径，地方不是被动终点", "不能把跨境接触自动写成对等交流或直接影响", "逐案例补接触、委托、制作、流通与使用链", "ACCEPTED_WITH_LIMITS"),
            ("1.4", "B", "materials_and_distributed_production", "瓷器、棉布等商品的形式变化嵌入材料、工序、订货与长距离贸易系统", "各产业技术条件不同，不能用一个案例概括所有材料系统", "补配方、窑业／染织工艺、订单和实物分析", "ACCEPTED_AS_SUPPORT"),
            ("1.6", "C", "design_term_and_professional_identity_context", "design的地域命名与专业身份应被历史化而非预设为普遍类别", "本书不是完整的design词源史或职业制度史", "补词典、期刊、职位、学校和行业组织P0材料", "CONTEXT_ONLY"),
            ("1.7", "A", "local_production_global_connections", "地方生产可通过工艺适配、订货翻译和市场选择生成混合而非复制的结果", "景德镇与印度棉布案例不能证明所有地区采取同一路径", "补亚洲、非洲、美洲的生产者档案与对象序列", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4", "B", "trade_fashion_and_consumption", "贸易订货、时尚和消费验证会反向塑造商品图样与品类", "目录、订单和评论不能独立证明普通消费者的实际理解", "补账本、诉讼、穿用痕迹、消费者书信与零售档案", "ACCEPTED_AS_SUPPORT"),
            ("2.6", "B", "exhibition_identity_and_classification", "国际和帝国展览可通过选择、排除与陈列生产身份类别", "Dipti Bhagat个案限于南非1851—1936语境；Lockyer已质疑仅用表演性解释", "补官方目录、组织档案、地方媒体和观众材料", "ACCEPTED_WITH_COUNTERARGUMENT"),
            ("2.7", "A", "translation_and_local_modernities", "棉布、瓷器与茶器的跨境迁移包含选择、误读、替代和再生产", "不得把物的相似性升级为单向影响或和谐交流", "逐对象建立订单—制作—运输—销售—使用链", "ACCEPTED_WITH_LIMITS"),
        ],
    },
    "B0170": {
        "title": "Global Design History（另一转换资产）",
        "author": "Glenn Adamson、Giorgio Riello、Sarah Teasley 编",
        "version": "同为Routledge 2011版的连续文本／图像引用转换",
        "material_type": "同一编著的替代数字化转换",
        "scope": "与B0005为同一知识来源，不增加独立书目证据",
        "duplicate_group": "VGRP001",
        "summary": "此资产与B0005对应同一2011年编著，正文组织和图像引用方式不同。它可用于OCR互校和报告差异检查，但不得在章节参考文献数量、证据互证或权重统计中作为第二本书。",
        "strengths": ["连续文本便于检索，可辅助核对B0005的分页转换。"],
        "limits": ["没有独立知识增量；正式定位和页码以B0005及纸本为准。"],
        "spot_checks": ["题名页、编者、出版社和2011版信息与B0005一致；SHA-256不同说明转换资产不同而非著作不同。"],
        "mappings": [("0.7", "X", "version_alias_not_independent_evidence", "无独立证据增量；全球设计史方法由B0005规范记录承担", "不能作为第二项互证来源或增加参考文献数量", "需要逐字引文时回B0005页标文本和纸本", "EXCLUDED_DUPLICATE_VERSION")],
    },
    "B0040": {
        "title": "Empire of Cotton: A Global History",
        "author": "Sven Beckert",
        "version": "Alfred A. Knopf, 2014",
        "material_type": "全球商品史与资本主义史学术专著",
        "scope": "以棉花追踪约五百年的生产、劳动、国家、帝国和全球贸易；第一、二章主要使用16—19世纪材料",
        "duplicate_group": None,
        "summary": "Beckert以棉花为追踪对象，把原料、机器、工资劳动、奴隶制、土地剥夺、国家能力和贸易网络放进同一解释框架。其关键修正是：工业资本主义并非由机器或自由市场独自生成，而建立在更早的强制劳动、帝国扩张与武装贸易网络上。对教材第一章，它能补足材料供应链、区域不平等和劳动动员；对第二章，它主要提供棉布流通的政治经济条件，而不是纹样接受或百货商店内部史。",
        "strengths": [
            "以商品链连接田野、工厂、港口、金融与市场，恢复生产空间之间的依赖关系。",
            "大量企业、殖民和政府档案支撑跨尺度叙事。",
            "把奴隶制与土地剥夺置于工业化条件内部，而非附录性社会后果。",
        ],
        "limits": [
            "战争资本主义是作者的解释概念，需同技术、生态、人口和区域研究对话。",
            "宏观全球叙事仍以欧洲／北大西洋行动者为因果枢纽，中国及若干区域较薄。",
            "对纹样、设计职业、消费现场和对象形式的材料不足，不能代替设计史专门研究。",
            "知识涌现报告的‘暴力隐形化’等属于后续分析假设，不是原著明示命题。",
        ],
        "spot_checks": [
            "clean第66—72行：帝国扩张、奴隶劳动、机器和工资劳动被置于同一全球生产体系。",
            "clean第123—147行：作者界定战争资本主义及其与工业资本主义的关系。",
            "clean第89行及上下文：棉花在1000—1900年作为重要制造业的宏观判断，仍须核作者依据。",
        ],
        "mappings": [
            ("0.6", "B", "recover_coerced_and_displaced_labor", "设计史中的材料与商品叙事必须显现被奴役者、被剥夺者和工厂劳动者", "宏观叙事仍可能再生产北大西洋施动者中心", "补生产者主体材料、区域档案和环境史", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.1", "B", "multiple_preindustrial_cotton_worlds", "工业化前已存在多中心的棉纺知识、市场和生产体系", "本书概括跨度大，具体工序和地方知识须回区域研究", "补印度、中国、非洲和美洲染织技术与劳动材料", "ACCEPTED_AS_SUPPORT"),
            ("1.2", "A", "machines_states_and_scale", "机械化和工厂扩张依赖国家能力、原料控制、劳动力动员、资本与市场的组合", "不能因此否认机器性能和生产率变化的独立测量价值", "补技术测试、工厂账簿、专利和产量序列", "ACCEPTED_WITH_LIMITS"),
            ("1.3", "B", "labor_control_and_process_separation", "棉纺工业中的劳动组织和控制是工序重组的组成条件", "不足以单独证明图样、制模、规格和设计权力的具体分离", "补印花图样、订单、工厂组织与工人证言", "ACCEPTED_AS_SUPPORT"),
            ("1.4", "A", "cotton_material_supply_chain", "棉的形式与可得性受种植、纤维处理、运输、纺织和染整的全球供应链约束", "书中对生态代价与部分地方工艺处理不足", "补纤维对象、染料、土地和水资源材料", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.5", "B", "hidden_labor_and_merchant_state_network", "商品背后的匿名劳动、商人、国家和运输节点共同构成生产系统", "本书不能重建每件产品的设计责任或署名链", "补企业图样、职位、工资、承包与销售档案", "ACCEPTED_AS_SUPPORT"),
            ("1.7", "A", "uneven_regional_industrialization", "机械化、手工生产、去工业化与再工业化在不同地区非同步发生", "作者三阶段框架对中国社会主义工业化等路径解释有限", "补区域工业史和对称比较", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4", "B", "consumption_trade_and_production", "消费需求与贸易网络同原料和生产组织共同塑造棉商品扩张", "不是百货商店、橱窗、信用或普通消费者经验的专门史", "补零售档案、广告、账本和使用材料", "ACCEPTED_AS_PREHISTORY"),
            ("2.7", "B", "cotton_crossborder_political_economy", "棉布跨境迁移受国家保护、强制贸易、买方市场和区域生产能力共同塑造", "对纹样选择、误读和地方使用的直接证据相对不足", "与B0005、B0304及区域染织研究互证", "ACCEPTED_AS_STRUCTURAL_SUPPORT"),
        ],
    },
    "B0328": {
        "title": "Objects of Desire: Design and Society since 1750",
        "author": "Adrian Forty",
        "version": "Thames & Hudson英国版数字化文本；1986",
        "material_type": "设计社会史与设计政治经济学经典专著",
        "scope": "英国为主，1750年至20世纪后期；第一至三章直接关联设计分工与机械化",
        "duplicate_group": "VGRP002",
        "summary": "Forty把设计同时理解为物的外观和生产指令，并将其放回资本主义劳动分工、利润、市场与社会观念之中。他通过Wedgwood、印花布、服装和家具等案例反驳‘机器自动导致设计好坏’的技术决定论，主张当工匠失去对完整生产过程的控制时，图样和指令才成为独立活动。该书同时批评设计师中心史，但其意识形态解释常强于对实际消费者反应的证明。",
        "strengths": [
            "直接连接设计、劳动分工、企业决策、市场多样化和社会分类。",
            "使用企业书信、图样簿、议会报告、目录、行业期刊和实物案例。",
            "以破除机器决定论和设计师天才论构成第一章的重要史学支点。",
        ],
        "limits": [
            "英国中心且手稿成于1980年前后，后续劳动史、消费史和全球史需补充。",
            "目录与广告可证明企业如何分类消费者，不能直接证明消费者接受了这些意义。",
            "‘设计物化意识形态’是研究者解释，须同委托、生产、传播和使用证据分层。",
            "对工人和非欧美行动者的直接声音不均衡。",
        ],
        "spot_checks": [
            "clean第90行：批评设计史只连接眼睛而切断思想与利润。",
            "clean第460、501—503行：Wedgwood制模者、精确指令与劳动分工。",
            "clean第509—515行：Queensware形式变化不能归因于机械革命。",
            "clean第574—588、699—824行：机器无独立决定作用，应考察资本—劳动关系。",
            "clean第1278、1306行：产品差异化服务市场，但目录只呈现制造者的社会图景。",
        ],
        "mappings": [
            ("0.3", "A", "design_political_economy_method", "设计史须把形式同生产、利润、劳动和社会观念置于同一解释链", "Forty的结构主义和马克思主义解释不是唯一范式", "补消费者、工人、区域与对象反证", "ACCEPTED_WITH_LIMITS"),
            ("0.4", "B", "objects_as_materialized_social_claims", "人工物可用于分析生产者试图物化的社会分类和观念", "物的形式不能独自证明设计意图或受众效果", "补委托、广告、使用、维修和接受材料", "ACCEPTED_AS_METHOD"),
            ("0.6", "B", "designer_canon_and_missing_consumers", "设计师中心叙事会遮蔽企业、工人和市场中介，Forty自身也缺少充分消费者材料", "缺席不是某种具体经验的正面证据", "补工人、消费者、女性及非欧美材料", "ACCEPTED_AS_CRITIQUE"),
            ("1.2", "B", "anti_technological_determinism", "机器的形式后果取决于劳动、资本、市场和组织条件，而非机器单独作用", "不能反向写成技术性能不重要", "补具体机器性能、成本和工艺比较", "ACCEPTED_WITH_LIMITS"),
            ("1.3", "A", "design_as_production_instruction", "劳动分工使图样和生产指令成为协调分离工序的独立活动", "Wedgwood等案例不能代表所有行业的同一时间表", "补行业图样、模型、规格、工序和工资档案", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.4", "B", "wedgwood_material_and_organization", "陶瓷形式由材料、既有工艺、模型和工厂组织共同约束", "本书不是陶瓷材料科学或供应链专著", "补泥料、釉料、窑炉、样品和订单资料", "ACCEPTED_AS_SUPPORT"),
            ("1.5", "A", "anonymous_design_and_entrepreneurial_power", "制造品由制模者、工匠、企业主和销售体系协作形成，生产决策权不能归给单一设计师", "不能据此抹除具体设计者的可证责任", "逐企业核图样签名、委托、审批和生产记录", "ACCEPTED_WITH_LIMITS"),
            ("1.6", "A", "design_concept_and_professional_specialization", "design作为外观与生产指令的双重活动在劳动分工、版权、教育和改革话语中制度化", "英国术语与制度不能直接外推全球", "补词源、学校、行业组织和职业统计", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.1", "B", "great_exhibition_design_reform_context", "1851年博览会参与把机器、工艺和产品质量组织成公共设计争论", "该书不是博览会完整组织史，Cole意图和展品评价须回专门研究", "与B0204及官方报告互证", "ACCEPTED_AS_SUPPORT"),
            ("2.2", "B", "schools_committees_and_copyright", "议会委员会、设计学校、版权和展览共同促成设计的国家化治理", "引述多为二手组织，政策成效与工人经验不能由改革者话语推出", "回委员会报告、学校课程与行政档案", "ACCEPTED_AS_SUPPORT"),
            ("2.4", "B", "catalogues_variety_and_social_differentiation", "目录、品类差异和市场细分显示制造商如何想象消费者并组织选择", "不能证明实际购买者按同一性别阶级意义理解产品", "补销售、家庭账本、消费者书信和使用材料", "ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6", "C", "oriental_goods_in_reform_discourse", "英国改革话语把印度和所谓东方手工物置于机器产品的对照体系", "Forty并未提供殖民地参与者的完整立场，历史称谓须批判性转述", "补殖民展品档案、来源社群和地方媒体", "CONTEXT_ONLY"),
        ],
    },
    "B0157": {
        "title": "Objects of Desire（美国版转换资产）",
        "author": "Adrian Forty",
        "version": "Pantheon Books美国初版，1986；另有Thames & Hudson同年版",
        "material_type": "同一著作的替代版本／转换",
        "scope": "与B0328为同一知识作品；版本与数字化结构不同",
        "duplicate_group": "VGRP002",
        "summary": "此资产保留美国版书目信息，但clean文本长行与乱码较多。章节知识建模由更易定位的B0328英国版转换承担；若正式引文来自美国版，则必须按B0157纸本页码单独核定。",
        "strengths": ["可用于核对美国版题名页和版次差异。"],
        "limits": ["不能与B0328作为两项独立互证；转换质量不适合规范定位。"],
        "spot_checks": ["题名页显示Pantheon Books 1986美国初版，并注明同年英国原版；文本SHA与B0328不同。"],
        "mappings": [("1.3", "X", "version_alias_not_independent_evidence", "无独立证据增量；劳动分工与生产指令命题由B0328承担", "不得重复计为第二项核心文献", "若采用美国版逐字引文则回B0157纸本核页", "EXCLUDED_DUPLICATE_VERSION")],
    },
    "B0192": {
        "title": "From the American System to Mass Production, 1800–1932",
        "author": "David A. Hounshell",
        "version": "Johns Hopkins University Press, 1984",
        "material_type": "美国制造技术史与企业史学术专著",
        "scope": "美国军工、缝纫机、木工、收割机、自行车和汽车产业，约1800—1932",
        "duplicate_group": None,
        "summary": "Hounshell区分19世纪的‘美国制造体制’与20世纪大规模生产，借企业档案、政府调查和实物互换性测试，说明技术扩散并不迅速平滑。量规、夹具、专用机床、互换零件、工序协调、装配线与营销策略形成长期累积链；成功企业可能先靠营销而非先进制造领先。该书能具体化第一章的标准化、规格权力和匿名协作，但军工来源只作制度与技术文字分析。",
        "strengths": [
            "把技术史传说放回档案和实物测试，修正Whitney等英雄起源叙事。",
            "跨企业比较生产与营销，揭示技术采用的组织成本和滞后。",
            "附录以Singer缝纫机零件测试验证文献判断，适合0.4史料实验。",
        ],
        "limits": [
            "案例偏行业领导企业，对中小失败企业和工人经验覆盖较少。",
            "美国路径不能代表欧洲、亚洲或殖民地制造系统。",
            "1903年后的福特与GM材料超出第一编截止1914的部分须严格分期。",
            "制造协调不等于产品外观设计，图样与设计职位仍需另证。",
        ],
        "spot_checks": [
            "clean第522—530行：大规模生产与美国体制不同，互换性依赖军械部长期投入。",
            "clean第536—546行：Singer和McCormick技术扩散不平滑，营销可先于制造优势。",
            "clean第546行：Singer仍依赖手工修配，与‘大规模生产中没有修配工’判准对照。",
            "clean第433—435行：过剩后GM以年度车型和分层市场推动灵活大规模生产。",
        ],
        "mappings": [
            ("0.3", "B", "revisionist_anti_hero_technology_history", "制造技术史须用企业档案和实物检验修正发明家起源神话", "修正某位英雄不等于个人行动完全不重要", "补专利、企业与公共机构多方档案", "ACCEPTED_AS_METHOD"),
            ("0.4", "A", "artifact_test_of_interchangeability", "实物零件互换测试可检验企业宣传和文献中的标准化主张", "样本、年代和保存史限制必须公开", "核附录样本清单、测量方法和博物馆藏品", "ACCEPTED_WITH_REPRODUCTION_REQUIRED"),
            ("1.1", "B", "mobile_mechanics_and_distributed_knowledge", "机械师流动、公共军工厂与机床企业共同传递制造知识", "主要是美国金属和木工行业，不能等同所有前工业知识", "补学徒、工会、工场和区域材料", "ACCEPTED_AS_SUPPORT"),
            ("1.2", "A", "interchangeability_flow_and_scale", "互换零件、量规、机床、物流与连续装配共同改变生产尺度", "互换性不必然降低成本，规模也可能造成刚性和过剩", "补成本、产量、质量和工时序列", "ACCEPTED_WITH_LIMITS"),
            ("1.3", "A", "gauges_specs_and_process_control", "量规、夹具、精确规格和协调工序把判断权从装配修配转移到系统设计与监督", "本书较少直接讨论外观图样和设计师职位", "补产品图纸、工程变更、职位和审批记录", "ACCEPTED_AS_MECHANISM"),
            ("1.4", "B", "machine_tool_material_process_system", "金属与木材加工形式受机床、冲压、焊接、精度和材料流共同约束", "原料供应和环境维度不是本书重点", "补材料规范、采购、废料和测试记录", "ACCEPTED_AS_SUPPORT"),
            ("1.5", "A", "distributed_manufacturing_authorship", "公共机构、机械师、工程师、企业管理者和销售体系共同形成制造系统", "不能把技术系统无作者化，也不能忽略可证个人责任", "逐项目核设计、工程、审批、制作和营销责任", "ACCEPTED_WITH_LIMITS"),
            ("1.7", "A", "american_and_european_methods_uneven_diffusion", "所谓美国体制与欧洲方法长期并存，技术扩散受成本、组织和市场约束", "英美比较不等于全球区域比较", "补欧洲、亚洲和殖民地制造史", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.1", "C", "great_exhibition_technology_observation", "1851年博览会促使英国观察者讨论美国制造技术", "不是博览会公众观看、帝国展示或设计改革的完整证据", "回展览目录、评审报告和观察者记录", "CONTEXT_ONLY"),
            ("2.4", "B", "marketing_production_and_market_segmentation", "Singer等企业的广告、经销、服务和分期付款可先于生产技术优势塑造市场", "GM年度车型主要属1920年代，不能倒置到19世纪百货语境", "按时段补零售、广告、信用与销售数据", "ACCEPTED_WITH_PERIOD_LIMIT"),
        ],
    },
    "B0304": {
        "title": "Luxury and Pleasure in Eighteenth-Century Britain",
        "author": "Maxine Berg",
        "version": "Oxford University Press, 2005；2007平装版",
        "material_type": "消费史、经济史与物质文化研究专著",
        "scope": "18世纪英国为主，并连接亚洲商品生产与北美殖民市场",
        "duplicate_group": None,
        "summary": "Berg以‘产品革命’替代过宽的‘消费革命’，把设计、材料、制造、零售和购买重新连成一条链。她说明英国所谓新奢侈品并非单纯复制亚洲商品，而是通过材料替代、工艺组合、模仿、专利、展示与市场反馈形成新的品类；亚洲生产者本身具有大规模与差异化能力。该书为第一章的材料系统和混合生产、第二章的消费与跨境转译提供强支撑。",
        "strengths": [
            "把遗产清单、海关账册、广告、商业通信、专利和产品对象结合。",
            "避免把消费需求同具体产品和制造过程分离。",
            "强调亚洲生产能力和英国产品的模仿—再组合过程，纠正封闭民族创新叙事。",
        ],
        "limits": [
            "中间阶层和英格兰占主位，劳动者、殖民地消费者与被强制劳动者较弱。",
            "遗产清单受死亡、财产和记录制度偏差影响；广告不能直接证明购买。",
            "‘模仿即发明’须保留殖民权力、知识产权和原生产者署名问题。",
            "本书不是19世纪百货商店或1851年后展览制度专著。",
        ],
        "spot_checks": [
            "clean第93—112行：产品革命、新奢侈及其全球经济框架。",
            "clean第282—315行：模仿艺术与发明科学、亚洲生产能力和新奢侈属性。",
            "clean第599—655行：亚洲生产者面向欧洲多层市场调整产品。",
            "clean第1084—1308行：选择性模仿、专利与从模仿到新产品的论证。",
            "clean第2649行起：遗产清单的时段和记录限制。",
        ],
        "mappings": [
            ("0.4", "B", "objects_inventories_and_trade_records", "对象、遗产清单、价格、广告和贸易记录可互校产品的社会生命", "拥有记录不等于使用方式，广告不等于实际接受", "补实物磨损、家庭叙事、销售和使用材料", "ACCEPTED_AS_METHOD"),
            ("0.6", "B", "inventory_class_and_colonial_silences", "遗产清单与商业档案偏向有产者和商人，会压低劳动者与殖民地消费者的可见性", "不能由缺席推断其没有消费或没有能动性", "补工资、贫困救济、考古、殖民地和主体材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1", "B", "regional_specialization_and_craft_knowledge", "陶瓷、玻璃和金属品依赖区域专业化、作坊技能与商业网络", "主要是英国新奢侈产业，不能概括所有前工业造物", "补作坊账簿、工具、学徒和地方研究", "ACCEPTED_AS_SUPPORT"),
            ("1.2", "B", "new_materials_mechanisms_and_scale", "材料替代、机械装饰和扩大生产共同形成可及的新商品", "规模与价格判断需按行业核量化资料", "补专利、成本、产量和材料测试", "ACCEPTED_AS_SUPPORT"),
            ("1.3", "B", "patterns_models_and_imitation", "模式簿、样品、专利和模仿实践把形式知识转化为可重复生产指令", "不足以说明每一行业图样权力与工人控制关系", "补企业图样、订单、审批和劳动档案", "ACCEPTED_AS_SUPPORT"),
            ("1.4", "A", "global_material_and_product_systems", "瓷器、印花布、玻璃和金属品的形式来自跨境材料、工艺和市场的组合", "对棉纺和生态供应链处理不及专门研究", "与B0040及材料技术史互证", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.5", "B", "collective_product_revolution", "发明者、制造商、商人、零售者、广告者和购买者共同推动产品变化", "这种角色清单不能替代具体产品的责任链", "逐产品核委托、制作、营销和使用记录", "ACCEPTED_AS_SUPPORT"),
            ("1.7", "A", "asian_production_and_british_recombination", "亚洲差异化生产与英国材料替代、模仿和再组合构成不对称而混合的工业化路径", "不能写成亚洲仅提供灵感、英国独自完成创新", "补亚洲生产者、贸易中介和殖民制度材料", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4", "A", "product_revolution_shopping_and_consumers", "具体商品、零售、广告和中间阶层购买共同构成18世纪消费—制造前史", "不是19世纪百货商店制度的直接证明，普通劳动者覆盖不足", "补19世纪商店档案、信用、橱窗和消费者材料", "ACCEPTED_AS_PREHISTORY"),
            ("2.6", "B", "empire_markets_and_national_branding", "殖民市场、贸易保护和国家品质话语参与塑造英国商品身份", "商品国家化不能掩盖亚洲知识、殖民强制和地方消费者选择", "补航海法、海关、殖民报刊和地方回应", "ACCEPTED_AS_STRUCTURAL_SUPPORT"),
            ("2.7", "A", "imitation_translation_and_new_products", "跨境模仿可通过材料替代、工艺重组和市场适配生成新产品类别", "‘模仿即发明’是分析命题，不等于无条件正当化挪用", "补来源对象、生产者、专利争议和地方使用", "ACCEPTED_WITH_ETHICAL_LIMIT"),
        ],
    },
    "B0332": {
        "title": "The Grammar of Ornament",
        "author": "Owen Jones及受邀章节作者／绘图、石印协作者",
        "version": "1856年首版内容的数字化clean文本",
        "material_type": "维多利亚设计改革一手理论、跨文化图版汇编与教学工具",
        "scope": "37条一般原则、20类装饰传统与100组彩色图版；1856英国知识生产语境",
        "duplicate_group": None,
        "summary": "《装饰的语法》以37条命题把装饰组织为形式、色彩、几何、适合性与教育原则，并以跨文化图版作为‘例句’。它是第二章研究设计教育、装饰知识分类和殖民观看的关键P0行动者文本：能证明Jones及其协作者如何建构一套普遍语法，不能证明被分类文化自身同意这些范畴，也不能把19世纪色彩比例或文明等级判断当作今日事实。",
        "strengths": [
            "可直接呈现设计改革者如何把原则、历史实例、印刷技术和教育对象结合。",
            "序言、37条命题、图版来源和协作者网络允许重建知识生产机制。",
            "第36—37条把历史原则、制造者、艺术家、公众教育连成制度性纲领。",
        ],
        "limits": [
            "‘野蛮人’、民族性和文明等级语言属于帝国时代分类，必须署名、限域并批判。",
            "图样从建筑、器物和仪式语境中抽离再平面化，不能视为透明的文化代表。",
            "色彩比例与自然法则是行动者理论，不能作为当代科学定律。",
            "协作者贡献意味着不得把全书知识与图版全部归为Jones个人原创。",
        ],
        "spot_checks": [
            "clean第71—150行：37条一般原则，包括适合性、几何、历史原则和公共艺术教育。",
            "clean第88行：repose与true beauty属于Jones的规范性美学。",
            "clean第142—150行：第35—37条讨论模仿、过去原则与艺术教育。",
            "clean第986、1056行：作者承认材料保存不全，并以构造／外加装饰评价传统。",
        ],
        "mappings": [
            ("0.4", "B", "visual_examples_abstracted_from_context", "图版可研究19世纪如何把器物和建筑细部转换为可比较的平面史料", "图版不是原对象的中性复制，语境、尺度、材料和用途被削弱", "回原对象、采集记录、图版制作与馆藏", "ACCEPTED_AS_METHOD_CASE"),
            ("0.5", "B", "publication_and_visual_evidence_chain", "序言、图版、来源标注、协作者与石印流程构成复合证据链", "clean文本不能替代彩色图版与首版实物核验", "回1856首版、V&A预备稿和出版档案", "ACCEPTED_WITH_IMAGE_GAP"),
            ("0.6", "B", "victorian_classification_bias", "该书可作为研究维多利亚设计知识如何等级化非欧洲传统的一手材料", "不能把Jones的类别和评价转述为被研究文化的自我认识", "补来源社群、殖民采集史和当代区域研究", "ACCEPTED_AS_CRITICAL_PRIMARY_SOURCE"),
            ("0.7", "B", "early_crosscultural_formal_comparison", "跨文化并置展示了早期全球装饰比较的知识技术", "形式相似不能证明接触、传播或共同起源", "补年代、接触、贸易和地方谱系证据", "ACCEPTED_WITH_CAUSAL_LIMIT"),
            ("1.6", "A", "industrial_and_decorative_arts_actor_concepts", "37条命题直接呈现装饰艺术、制造、原则与教育的行动者概念", "它是规范文本，不是19世纪实践已实现的统计描述", "同学校课程、制造记录和批评接受互证", "ACCEPTED_AS_ACTOR_VIEW"),
            ("2.1", "B", "post_exhibition_design_reform_text", "该书属于1851年博览会后设计改革与Sydenham Crystal Palace知识工程", "不能独立重建1851博览会现场、公众或全部展品", "与B0204、官方目录和Cole档案互证", "ACCEPTED_AS_POSTHISTORY"),
            ("2.2", "A", "design_education_and_general_principles", "原则、范例与彩色复制被组织成面向艺术家、制造者和公众的设计教育体系", "第37条是改革诉求，不能证明教育成效", "补School of Design课程、学生作业、行政和使用记录", "ACCEPTED_WITH_OUTCOME_GAP"),
            ("2.6", "A", "colonial_ornament_classification", "跨文化图版和章节命名可直接分析世界装饰如何被选择、命名、排序和等级化", "只证明英国知识制度的分类实践，不代表对象来源社会", "补征集、展览、翻译、当地生产者与回应材料", "ACCEPTED_AS_CRITICAL_PRIMARY_SOURCE"),
            ("2.7", "B", "principles_from_past_and_design_reuse", "第36条显示改革者主张提取过去原则而非复制结果，构成跨文化再生产的规范模型", "不能把这种模型等同互惠转译或正当占有", "补具体设计的来源、改造、署名和争议链", "ACCEPTED_WITH_ETHICAL_LIMIT"),
        ],
    },
    "P0040": {
        "title": "Originality and Jones' The Grammar of Ornament of 1856",
        "author": "John Kresten Jespersen",
        "version": "Journal of Design History, 2008；paged clean共205行",
        "material_type": "设计史期刊论文与经典文本接受史研究",
        "scope": "《装饰的语法》的成书、图版、理论、接受与原创性",
        "duplicate_group": None,
        "summary": "Jespersen利用Cole日记、RIBA草稿、出版史、图版资料和接受史文献重建《装饰的语法》的形成，并把其原创性区分为理论、图版来源和处理方式。他强调37条命题、field与repose的可操作性，也指出各篇历史论文带有以自然科学保证权威的‘无误性修辞’。该文可校正对Jones一书的简单赞美，但作者本人长期参与Jones研究，其场理论与影响判断仍需独立复核。",
        "strengths": [
            "把出版物、档案、图版制作、理论文本与接受史放在同一证据链。",
            "明确约40%图版材料首次刊行及多人绘制、石印、出版协作。",
            "区分ornament、decoration、field和motif，便于分析图版如何组织观看。",
        ],
        "limits": [
            "作者与研究对象及CD-ROM项目关系密切，对field theory的反方意见不足。",
            "对实践者影响的若干判断偏列举和印象式，不能直接证明传播机制。",
            "Fig.3未复制，相关视觉论证不完整；Riegl部分未对勘德文原著。",
            "论文对殖民等级语言的批判不是主轴，仍须补后殖民与来源社群研究。",
        ],
        "spot_checks": [
            "clean第11行：37条命题、field、repose与文章总论。",
            "clean第33行：Jones的科学史观及‘无误性修辞’判断。",
            "clean第41行：图版制作、来源、约40%首次刊行与协作链。",
            "clean第93—99行：field theory、影响判断和repose解释。",
        ],
        "mappings": [
            ("0.5", "A", "archive_publication_plate_chain", "日记、草稿、图版、印刷与版次材料可重建设计知识出版链", "文章复述不能替代未直接核验的档案和首版图版", "回Cole日记、RIBA草稿、V&A预备图及首版", "ACCEPTED_WITH_PRIMARY_FOLLOWUP"),
            ("0.6", "B", "authority_and_infallibility_rhetoric", "所谓科学和自然原则也可构成知识权威修辞，应审查其排除与等级化效果", "这是Jespersen借用Wihl形成的解释，不是Jones自称", "补后殖民研究、来源社群与反向接受", "ACCEPTED_AS_INTERPRETATION"),
            ("0.7", "B", "global_coverage_and_context_loss", "《语法》的全球覆盖通过抽离语境、重绘和网格化形成", "覆盖广不等于去殖民或关系史；形式并置不证明传播", "补对象原境、采集与地方史", "ACCEPTED_WITH_LIMITS"),
            ("1.6", "A", "grammar_originality_and_design_theory", "37条命题构成19世纪装饰设计理论与原创性争论的核心文本", "论文支持的是理论和处理的原创性，不是所有图样由Jones原创", "分别核命题、图版来源、协作者和后期作品", "ACCEPTED_WITH_ATTRIBUTION_LIMIT"),
            ("2.1", "B", "crystal_palace_origin_context", "Cole圈、Crystal Palace与设计改革网络参与了该书的生成", "不能由成书史替代1851博览会完整历史", "补Cole档案、展览目录和同期批评", "ACCEPTED_AS_POSTHISTORY"),
            ("2.2", "A", "design_reform_publication_and_teaching", "《语法》把改革机构、教学原则、彩色复制和设计实践连接起来", "传播广与教育有效是不同命题，后者尚缺使用证据", "补学校借阅、课程、学生作业和事务所使用记录", "ACCEPTED_WITH_OUTCOME_GAP"),
            ("2.6", "B", "plate_selection_and_global_classification", "图版来源比例、重绘和编排可解释非欧洲装饰如何进入英国设计知识系统", "作者的‘视觉学术无可挑剔’属评价且未处理全部殖民语境", "补采集史、原对象与来源社群材料", "ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.7", "B", "precedent_to_new_design", "从旧例提取原则并生成新设计是Jones体系所宣称的转译机制", "不能由Templeton地毯个案证明普遍有效或文化上互惠", "补具体对象、图版、委托和接收史", "ACCEPTED_AS_SUPPORT"),
        ],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_assets() -> dict[str, dict[str, str]]:
    with ASSET_CSV.open(encoding="utf-8-sig", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def report_structure(asset: dict[str, str]) -> dict[str, int]:
    return {
        "report_file_count": int(asset["report_file_count"]),
        "report_characters": int(asset["report_characters"]),
        "review_basis": "overall_and_relevant_chapter_reports_plus_knowledge_discovery_audit",
    }


def write_card(source_id: str, data: dict, asset: dict[str, str]) -> None:
    clean_path = Path(asset["clean_source_path"])
    candidates = [
        {"section_id": row[0], "grade": row[1], "verification": "V2", "role": row[2]}
        for row in data["mappings"]
    ]
    card = {
        "source_id": source_id,
        "corpus": asset["corpus"],
        "folder_name": asset["folder_name"],
        "material_type": data["material_type"],
        "clean_source_path": str(clean_path),
        "clean_source_sha256": sha256(clean_path),
        "duplicate_group": data["duplicate_group"],
        "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
        "report_structure": report_structure(asset),
        "candidate_sections": candidates,
        "review_status": "semantic_review_complete",
        "evidence_level": "V2",
        "notes": data["limits"] + ["Clean原文仅作关键段落定位；未完成全篇、版次、图版、注释和所引P0材料核验。"],
        "original_spot_checks": data["spot_checks"],
    }
    (CARD_DIR / f"{source_id}_来源卡.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        f"# {source_id} 来源卡：{data['title']}",
        "",
        "## 一、来源身份与核验状态",
        "",
        "| 字段 | 内容 |",
        "|---|---|",
        f"| 来源ID | {source_id} |",
        f"| 作者／责任者 | {data['author']} |",
        f"| 版本 | {data['version']} |",
        f"| 材料类型 | {data['material_type']} |",
        f"| 研究范围 | {data['scope']} |",
        f"| 版本关系 | {data['duplicate_group'] or '无人工确认的版本组'} |",
        f"| clean原文 | `{clean_path}` |",
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |",
        f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
        "| 核验等级 | V2：分析资产已复核并局部回查clean原文；未达到全篇核验 |",
        "",
        "## 二、核心命题与教材价值",
        "",
        data["summary"],
        "",
        "## 三、论证强项",
        "",
    ]
    lines.extend(f"- {item}" for item in data["strengths"])
    lines.extend(["", "## 四、限度与不能外推", ""])
    lines.extend(f"- {item}" for item in data["limits"])
    lines.extend([
        "",
        "## 五、教材章节准入",
        "",
        "| 章／节 | 等级 | 角色 | 可接受命题 | 证据边界 | 状态 |",
        "|---|---|---|---|---|---|",
    ])
    for section, grade, role, claim, boundary, _follow, status in data["mappings"]:
        lines.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    lines.extend(["", "## 六、clean原文局部回查", ""])
    lines.extend(f"- {item}" for item in data["spot_checks"])
    lines.extend([
        "",
        "## 七、使用规则",
        "",
        "本卡中的A—D／X表示章节角色，V2表示当前核验深度。局部原文定位只用于确认报告没有明显误述，不授权逐字引用；正式教材须返回所用版次、页码、上下文以及关键P0材料。知识涌现报告提出的跨章结构只可作为研究假设，除非原著或独立材料另有证明。",
        "",
    ])
    (CARD_DIR / f"{source_id}_来源卡.md").write_text("\n".join(lines), encoding="utf-8")


def write_mapping(source_id: str, data: dict) -> None:
    fields = ["source_id", "section_id", "grade", "verification", "role", "accepted_claim", "evidence_boundary", "original_followup", "status"]
    with (MAP_DIR / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for section, grade, role, claim, boundary, followup, status in data["mappings"]:
            writer.writerow({
                "source_id": source_id,
                "section_id": section,
                "grade": grade,
                "verification": "V2",
                "role": role,
                "accepted_claim": claim,
                "evidence_boundary": boundary,
                "original_followup": followup,
                "status": status,
            })


def update_manifest() -> None:
    path = BATCH / "batch_manifest.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fields = list(rows[0])
    aliases = {"B0157", "B0170"}
    for row in rows:
        if row["source_id"] in SOURCES:
            row["semantic_review_status"] = "complete"
            row["mapping_status"] = "version_alias_suppressed" if row["source_id"] in aliases else "complete"
            row["original_verification_status"] = "version_identity_checked" if row["source_id"] in aliases else "partial_clean_text_spot_check"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_version_groups() -> None:
    path = ROOT / "01_语料清单" / "版本关系组_人工复核.csv"
    fields = ["version_group", "intellectual_work", "canonical_source_id", "alias_source_id", "relationship", "counting_rule", "verification_note"]
    rows = [
        {
            "version_group": "VGRP001",
            "intellectual_work": "Global Design History, edited by Adamson, Riello and Teasley, Routledge 2011",
            "canonical_source_id": "B0005",
            "alias_source_id": "B0170",
            "relationship": "同一版次同一著作的不同转换资产；B0005保留分页，B0170偏连续文本与图像引用",
            "counting_rule": "只计一个独立书目实体；B0170仅作OCR互校",
            "verification_note": "题名页、编者、出版社、年份一致；文件SHA不同",
        },
        {
            "version_group": "VGRP002",
            "intellectual_work": "Adrian Forty, Objects of Desire, 1986",
            "canonical_source_id": "B0328",
            "alias_source_id": "B0157",
            "relationship": "同一著作的Thames & Hudson英国版与Pantheon美国版／不同数字化转换",
            "counting_rule": "知识论证只计一个实体；逐字引文按实际版次单独核页",
            "verification_note": "题名与正文同一；版权页和版式不同；文件SHA不同",
        },
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_audit() -> None:
    lines = [
        "# BATCH-001-CH01-CH02 第一、二章核心来源阶段审计",
        "",
        "## 阶段结论",
        "",
        "批次12个资产均已完成人工语义复核与最终处置。其中B0170与B0157分别是B0005与B0328的版本别名，因此本批次对应10个独立知识来源，而不是12个。9项本阶段资产对应7个独立知识来源加2个版本别名。所有来源仍为V2：已读分析资产并局部回查clean原文，但尚未完成全书逐页、版次、图版、引注及P0材料核验。",
        "",
        "## 本阶段9项处置",
        "",
        "| 来源ID | 独立计数 | 核心准入 | 主要边界 |",
        "|---|---|---|---|",
        "| B0005 | 是 | 0.3、0.7、1.7、2.7为A | 论文集须按章作者引用；连接不等于互惠 |",
        "| B0170 | 否 | X，版本别名 | 与B0005同一2011编著，不作第二项互证 |",
        "| B0040 | 是 | 1.2、1.4、1.7为A | 政治经济强、形式与消费现场弱；涌现假设非原著命题 |",
        "| B0328 | 是 | 0.3、1.3、1.5、1.6为A | 英国中心；目录与形式不证明受众效果 |",
        "| B0157 | 否 | X，版本别名 | 与B0328同一著作；美国版引文须单独核页 |",
        "| B0192 | 是 | 0.4、1.2、1.3、1.5、1.7为A | 美国行业领导企业偏重；制造协调不等于外观设计 |",
        "| B0304 | 是 | 1.4、1.7、2.4、2.7为A | 中间阶层偏重；模仿—发明须保留殖民与署名问题 |",
        "| B0332 | 是 | 1.6、2.2、2.6为A | P0行动者文本；文明等级、自然法则不作今日事实 |",
        "| P0040 | 是 | 0.5、1.6、2.2为A | 作者立场接近对象；影响和field theory须独立复核 |",
        "",
        "## 关键方法判断",
        "",
        "1. P4分析报告和知识涌现文件只承担检索、结构比较、反例提示和缺口发现；其中的新命名不得转写为原著主张。",
        "2. 同一著作的版本资产可以互校OCR，但不能构成独立互证或增加章节参考文献数量。",
        "3. P0行动者文本能证明行动者当时如何主张、分类和规范，不能自动证明其主张真实、制度有效或被分类者认同。",
        "4. 目录、广告、图版和陈列可以证明生产者／机构的表达，不足以证明普通观看者和消费者的实际接受。",
        "5. 第一、二章下一轮应按节补齐P0：图样／模式簿、专利与版权、学校课程、委员会记录、企业生产档案、销售账簿、消费者材料及殖民地生产者材料。",
        "",
        "## 验证状态",
        "",
        "- 已验证：资产身份、报告结构、关键论点与限度、版本关系、clean SHA-256、关键段落存在。",
        "- 合理推断：上述来源在相应教材节的A／B／C角色；仍需在写作包中与其他来源组成证据簇。",
        "- 未验证：纸本页码全量一致性、图版颜色与细节、引注原始档案、所有数字与因果链、实际受众反应。",
        "",
    ]
    audit = "\n".join(lines)
    (ROOT / "10_证据缺口与审计" / "第一二章核心来源阶段审计.md").write_text(audit, encoding="utf-8")
    (BATCH / "audit.md").write_text(audit, encoding="utf-8")


def main() -> None:
    assets = load_assets()
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    MAP_DIR.mkdir(parents=True, exist_ok=True)
    for source_id, data in SOURCES.items():
        write_card(source_id, data, assets[source_id])
        write_mapping(source_id, data)
    update_manifest()
    write_version_groups()
    write_audit()
    print(json.dumps({"completed_sources": list(SOURCES), "cards": len(SOURCES), "mappings": sum(len(v["mappings"]) for v in SOURCES.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
