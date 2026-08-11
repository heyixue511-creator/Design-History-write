#!/usr/bin/env python3
"""Complete the exhibition, governance, labour, and empire group in BATCH-003."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0049": {
        "title": "The Great Exhibitor: The Life and Work of Henry Cole",
        "author": "Elizabeth Bonython、Anthony Burton",
        "version": "V&A Publications, 2003",
        "type": "档案型人物传记、设计改革制度史与博物馆史",
        "scope": "Henry Cole 1808—1882年的公共事业；重点为英国设计改革、1851年博览会与南肯辛顿体制",
        "duplicate_group": None,
        "summary": "Bonython与Burton以Cole日记、通信、政府蓝皮书、议会报告和同期报刊重建其从公共改革鼓动者到文化制度建构者的路径。该书最适合说明个人行动如何经由艺术家、制造商、王室庇护、学会、媒体和行政部门转化为展览、学校与博物馆制度；它也记录了博览会成功、盈余、任命、收藏、教育拨款与机构冲突之间的连续链条。作为人格中心传记，它不能单独承担帝国分类、工人接受、女性经验或教学成效的判断。",
        "strengths": [
            "Cole逐日日记、通信、政府文件和同期报刊形成可追溯的多类史料链。",
            "把Felix Summerly商业实验、艺术学会展览、1851年博览会和南肯辛顿制度连成连续行动链。",
            "呈现王室庇护、同行协作、舆论传播、预算与行政任命共同作用，而非只写个人天才。",
            "记录Department of Practical Art、设计学校、博物馆收藏、巡回借展和payment by results等制度细节。",
            "保留Cole与Redgrave、Robinson等人的协作和冲突，可用于分析行政权威、专业权威和集体作者制。",
        ],
        "limits": [
            "以Cole人格统摄制度叙事，容易把合作者、普通公务员、教师、工匠与公众转化为传主行动环境。",
            "依赖Cole事务性日记导致女性、私人生活和非精英主体结构性不足。",
            "帝国与殖民地几乎不构成分析主轴，不能因涉及1851年展览就承担殖民分类史。",
            "机构成立、展览参观或考试制度存在不能证明教育、产业和公众品味实际改善。",
            "作者对Cole持批判性同情，部分制度后果和权力批判较含蓄，须与劳动史、帝国史和博物馆批判史对读。",
            "报告中的中心性、三阶推动力等网络模型是P4二次分析，不得反写为原著的实证发现。",
        ],
        "checks": [
            "clean第8—15行：题名、封面说明及目录确认Part III为Art and Industry、Part IV为The Levers of Power。",
            "clean第2165—2169行：法国消费品竞争、设计教育和1837年设计学校的同期问题链。",
            "clean第3217—3222行：作者把博览会后的英国商品质量／价格与美观判断、Cole后续制度道路相连。",
            "clean第3284—3290行：Cole与Redgrave的角色划分及1852年Department of Practical Art设立和任命条件。",
            "clean第3334—3339行：地方委员会、按考试结果向教师付酬及节约公共开支的制度逻辑。",
            "clean第4277—4285行：作者区分Cole在elementary education payment by results中的幕后作用，并呈现教育史批评。",
        ],
        "maps": [
            ("0.3", "A", "institutional_biography_network_and_mediation", "人物行动须经合作网络、传播、庇护和行政装置转化为制度结果", "传记的Cole中心性不能替代多主体制度史", "补合作者、工匠、教师、公众与机构档案", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "diary_letters_blue_books_press_triangulation", "日记、通信、政府报告和报刊可互相约束改革者自述与制度事件", "日记的事务性和传主自我呈现造成系统性沉默", "正式写作逐条返回档案号、页码、作者与日期", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "personality_empire_gender_and_public_bias", "人格中心、帝国缺席、女性不足与公众接受断点必须成为证据审计项目", "识别缺口不等于已经补足缺失主体", "补帝国、性别、劳动、教育效果和观众材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.5", "B", "reformer_artist_manufacturer_patron_and_administrator_network", "Cole、Redgrave、Minton、艺术家、制造商、王室与部门共同形成制度行动者网络", "网络关系不能自动确定具体对象的设计与制作责任", "逐对象补图样、合同、工序、署名和机构记录", "ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.6", "B", "art_manufactures_mediator_and_public_administrator_roles", "Art Manufactures、文化中介、艺术行政和设计学校管理显示设计角色在19世纪中期的重组", "这些角色不等同于20世纪职业工业设计师", "补同期职位、章程、课程、工资和职业争论", "ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("2.1", "A", "great_exhibition_organization_design_reform_and_publicity", "1851年博览会把国家竞争、产品判断、组织网络与公众传播汇聚为设计改革事件", "人物传记不能独立证明参展对象来源、观众接受或全国性效果", "补皇家委员会、目录、评审、对象、媒体和观众材料", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.2", "A", "cole_school_museum_department_and_governance", "博览会资本经部门任命、学校、收藏、博物馆和考核机制转化为南肯辛顿治理体系", "设立和扩张不证明教学成效、产业采用或公共可达性", "补预算、课程、学生作业、考试、就业、地方学校和工业记录", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.4", "B", "guidebooks_press_exhibitions_and_public_pedagogy", "导览手册、儿童书、报刊宣传和展览构成Cole面向公众的品味中介网络", "传播供给不能证明消费欲望、购买或接受结果", "补发行、价格、读者、销售、家庭使用和观众记录", "ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6", "X", "cole_biography_without_colonial_analysis", "不把该传记用于证明博览会的殖民分类、殖民者经验或帝国效果", "书中帝国维度结构性不足，相关展览事实也以Cole为中心", "改用殖民展览、来源社群和被展示者材料", "EXCLUDE_AS_COLONIAL_CORE_SOURCE"),
        ],
    },
    "B0339": {
        "title": "Ephemeral Vistas: The Expositions Universelles, Great Exhibitions and World's Fairs, 1851—1939",
        "author": "Paul Greenhalgh",
        "version": "Manchester University Press, 1988",
        "type": "世界博览会比较史、帝国文化史与展示政治研究",
        "scope": "1851—1939年，以英国、法国、美国为主，专题讨论制度、帝国、人类展示、国家形象、建筑、性别与美术",
        "duplicate_group": None,
        "summary": "Greenhalgh把博览会写成由资金、组织、门票、城市基础设施、娱乐和意识形态共同构成的制度媒介，并以英国、法国、美国的比较说明不同政治经济结构如何改变展览内容。它是第二章2.1与2.6的核心解释文献，也可为1925年巴黎博览会和展览设计提供长时段背景。其批判贡献在于区分官方的和平、教育、贸易和进步修辞与实际展示结构；但对观众接受、殖民地人民能动性和非西方国家反向挪用缺乏系统材料，部分强因果措辞必须降格为作者解释。",
        "strengths": [
            "以官方目录、指南、财务记录、报刊、信札与回忆录支撑制度和展示分析。",
            "把资金来源、组织控制、门票、娱乐化、城市遗产与展示内容接入同一机制链。",
            "区分物产展示、人类展示、民族形象、性别和美术，使殖民分类的不同层面可审计。",
            "通过英法美结构比较避免把单一国家展览模式写成普遍规律。",
            "对女性参展进行目录统计，并公开不同国家和专业之间的差异。",
        ],
        "limits": [
            "1988年的三国框架压低德国、日本、奥斯曼、中国、殖民地自身和拉丁美洲等路径。",
            "主要分析展览发出何种信息，系统观众日记、民族志与行为材料不足，不能推出接受效果。",
            "被展示者的主体声音稀少；作者在若干段落明确只能推测其感受，教材不得补写内心。",
            "资金‘决定’内容、帝国衰落导致宣传增长等是研究者机制解释，须按具体事件补反例和中介。",
            "人类展示章节包含历史种族主义语言；教材只最小限度说明制度机制，不复制侮辱性描述。",
            "知识涌现报告的中心性、闭环和跨主题模型为P4重组，不得当作原书独立量化结论。",
        ],
        "checks": [
            "clean第28—46行：题名与作者信息确认研究范围为1851—1939年的国际博览会传统。",
            "clean第181—187行：法国制造商反对国际化及Cole、Albert把未实现方案转入1851年伦敦的叙述。",
            "clean第359—363行：四类资金、共同目标、皇家委员会、地方筹款及1851年财务数字。",
            "clean第365—371行：作者把反革命解释、门票阶级筛选与同期评论并置；后者不能代表全部工人经验。",
            "clean第583—587行：殖民物产组织、India／raw materials表述及glorify／domesticate双重展示目标。",
            "clean第957—961行：作者明确以speculate处理被展示者内心，显示接受与主体经验不可知边界。",
            "clean第1983—1987行：五届巴黎博览会女性作品比例、602名女性艺术家及总样本数字；OCR百分号须回页核定。",
        ],
        "maps": [
            ("0.3", "A", "institution_display_finance_and_ideology_framework", "展览应同时分析组织、资金、空间、对象、受众条件与意识形态解释", "该框架仍以主办国和展览发出端为中心", "补观众、劳动者、来源地与非西方组织者材料", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "catalogue_report_finance_press_and_absence_reading", "目录、官方报告、财务、报刊、建筑和统计可互证并通过缺席指认检验官方叙事", "官方文本中的类别不等于被展示者自我认同，统计OCR待核", "回原版页码、目录分类、数据表和相关档案", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "three_country_audience_agency_and_period_bias", "三国中心、观众接受断点、殖民主体能动性缺失和1914分期均需进入审计", "作者自陈或报告识别缺口不等于补足", "补区域研究、观众记录、来源社群与较新博览会史", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("2.1", "A", "great_exhibition_evolution_funding_ticket_and_public_viewing", "1851年展览由既有展览制度、国际竞争、资金组织、门票分层和展示分类共同形成", "不能写成单一发明，也不能由观看条件推出观众认同", "补皇家委员会、对象、评审、现场、观众和地方委员会档案", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.2", "B", "cole_royal_commission_and_exhibition_governance", "Cole、Albert、皇家委员会、地方委员会和私人筹款展示文化治理的组织层次", "该书不系统处理设计学校课程与教学效果", "与B0049、B0175及官方教育档案互证", "ACCEPTED_AS_INSTITUTIONAL_SUPPORT"),
            ("2.4", "B", "tickets_entertainment_and_mass_consumption_conditions", "门票、指南、娱乐设施和媒体合作共同组织大众进入博览会的消费条件", "票价和到场数字不能证明欲望、认同或具体使用", "补访客日记、消费记录、销售、媒体读者和阶级比较", "ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.5", "B", "exhibition_architecture_style_and_ideological_choice", "水晶宫原型、历史主义、现代主义与Art Deco可作为展览媒介中风格政治的长时段线索", "该书不承担家庭室内、新艺术对象的逐件形式和使用史", "补建筑图纸、对象、委托、设计者和现场观看材料", "ACCEPTED_AS_EXHIBITION_CONTEXT"),
            ("2.6", "A", "colonial_classification_human_display_and_visibility", "殖民物产的去语境化分类、人类展示和核心／边缘空间共同制造帝国知识秩序", "作者的批判解释不能替代被展示者声音、来源地档案与观众接受", "补殖民档案、招募合同、被展示者记录、来源社群和观众材料", "ACCEPTED_AS_CORE_SOURCE_WITH_ETHICAL_LIMITS"),
            ("2.7", "B", "exhibition_transfer_selection_and_reverse_appropriation_gap", "国际展览提供对象、风格与国家形象跨境选择和再生产的制度场域", "同场、可见或形式相似不等于影响；非西方反向挪用处理不足", "补贸易、人员、委托、制作、评论与地方主体材料", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("3.6", "B", "interwar_exhibition_architecture_and_visual_regime", "一战后博览会的建筑、国家馆和展示编排可说明展览设计如何承载政治竞争", "全书不是新摄影或新字体专史，视觉对象尚未逐图核验", "补展览平面、照片、平面材料、设计档案和观众路径", "ACCEPTED_AS_EXHIBITION_SUPPORT"),
            ("5.1", "A", "1925_paris_exposition_and_art_deco_production", "1925年巴黎博览会是装饰艺术命名、国家竞争、展馆和消费风格交汇的核心事件", "不能把博览会单独写成Art Deco的唯一来源或全球同步起点", "补1925官方目录、展馆、对象、设计者、生产与国际接受", "ACCEPTED_AS_CORE_CONTEXT"),
            ("5.7", "B", "style_nationalism_consumption_and_exclusion_ethics", "风格选择、国家宣传、大众消费与边缘排除之间的关系可构成商业设计伦理争议", "历史展览批判不能直接回答当代职业伦理", "与企业、职业组织、消费者和对象级材料对读", "ACCEPTED_AS_HISTORICAL_ETHICS_CONTEXT"),
            ("6.2", "C", "china_and_japan_at_world_fairs_as_external_view", "中国、日本等参展线索可用于发现晚清东亚博览会研究问题", "书中材料零散且主要从西方展览框架观察，不能承担中国国货意识史", "补清末官档、参展目录、报刊、商人、工匠和回国传播", "CONTEXT_ONLY_WITH_CHINA_P0_GAP"),
            ("8.1", "C", "interwar_national_pavilions_before_cold_war", "1937年前后的国家馆对峙可作为战后冷战展览竞争的前史", "止于1939年，不能证明冷战制度、观众或生活方式传播", "补战后政府、展览、媒体、对象和观众材料", "CONTEXT_ONLY_AS_PREHISTORY"),
            ("15.6", "C", "colonial_display_as_historiography_of_knowledge_position", "对分类、可见性与帝国展示的批判可作为去殖民设计史的史学前提", "1988年博览会史不是当代去殖民设计理论或实践证据", "补来源社群、返还、共同策展和去殖民设计研究", "CONTEXT_ONLY_AS_HISTORIOGRAPHY"),
        ],
    },
    "B0175": {
        "title": "Grand Designs: Labor, Empire, and the Museum in Victorian Culture",
        "author": "Lara Kriegel",
        "version": "Duke University Press, 2007",
        "type": "设计改革制度史、劳动文化史、帝国与博物馆研究",
        "scope": "1830年代至1870年代英国设计学校、版权、1851年博览会、装饰艺术博物馆和南肯辛顿体系",
        "duplicate_group": None,
        "summary": "Kriegel把设计改革从1851年向前追溯至1830年代的学校和议会调查，并通过课程、版权、展览文本、品味原则和博物馆地理说明改革从训练生产者转向教育消费者的争议过程。该书的核心修正是：劳动与贸易没有被商品奇观完全遮蔽，工匠、制造商和地方公众也不是被动接受国家规训，而会挪用改革话语争取版权、文化资本和博物馆可达性。它可承担第二章制度—劳动—消费—帝国的交叉解释，但对女性、非印度殖民地和对象形式仍不充分。",
        "strengths": [
            "把议会报告、设计注册、博物馆目录、商业账簿、地方报纸、工人信件、文学和图像组成复调证据链。",
            "以学校—版权—博览会—消费者教育—博物馆地理的历时链解释制度策略变化。",
            "把工匠、制造商、商人和消费者视为设计改革行动者，校正单向国家规训模型。",
            "通过印度工艺、棉布复制和帝国物品讨论劳动、贸易、原创与品味的跨境矛盾。",
            "对South Kensington与Bethnal Green的空间政治揭示可达性、阶级和地方行动如何改变制度配置。",
        ],
        "limits": [
            "全书以英国制度形成期为主，不能代表世界博览会、整个帝国或欧洲设计改革的全部路径。",
            "工人声音虽被恢复，仍多经公开演说、报刊和改革话语中介，日常劳动经验不完整。",
            "消费性别分析主要以男性气质修辞和不完整商业账簿展开，女性购买、制作和家庭劳动仍需补充。",
            "帝国劳动重点集中印度；非洲、加勒比、中国等地区多为缺口或英国表述对象。",
            "讽刺文学、漫画和期刊是话语行动证据，不能直接证明现实行为或普遍社会效果。",
            "知识涌现报告提出的五态文化资本、同构和递归模型为P4解释，须与原书论证分开。",
        ],
        "checks": [
            "clean第23—33行：作者、题名、Duke University Press与2007年版权信息。",
            "clean第221—227行：作者明确修正exhibitionary complex与imperial archive，主张劳动、贸易和市场行动者的中心作用。",
            "clean第299—305行：Haydon、议会调查、公开讲演及‘milk jug／heroic limb’的课程论证语境。",
            "clean第878—882行：Cole把consumer will与装饰艺术博物馆的消费教育联系起来，并说明开放、巡展和摄影传播。",
            "clean第1163—1169行：Bethnal Green藏品等级、王室开幕、工人可达性修辞与当地居民被排除的并置。",
        ],
        "maps": [
            ("0.3", "A", "social_cultural_institutional_and_market_history", "设计改革需把制度、劳动、市场、话语、空间和行动者能动性置于同一分析框架", "英国个案不能自动外推为全球设计制度规律", "与其他地区制度史、对象史和劳动史比较", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "archives_catalogues_ledgers_press_literature_and_worker_voice", "官方档案、目录、账簿、报刊、文学和工人材料须按证据功能对位使用", "虚构与讽刺证明话语参与，不直接证明行为；账簿样本不完整", "逐项标明作者、体裁、受众、日期、位置和沉默", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "british_institution_worker_gender_empire_and_object_bias", "英国制度中心、工人中介、性别不均、印度偏重和形式分析不足须进入审计", "偏差审计不能替代缺失的地区与主体材料", "补女性、家庭劳动、殖民地生产者、对象和地方研究", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "drawing_copyright_originality_replication_and_control", "课程、图样、机械复制、版权和设计注册共同重组构思、复制与控制关系", "版权论战中的原创／盗版是行动者修辞，不等于可直接判定每件产品归属", "补设计注册、样本、工序、企业和司法档案", "ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.5", "A", "artisan_manufacturer_trader_consumer_and_state_actors", "工匠、制造商、商人、消费者、教师和国家官员共同参与设计改革", "行动者进入公共论战不说明其权力相等或代表全部群体", "补工资、工场、成员、女性与地方行动者材料", "ACCEPTED_AS_ACTOR_NETWORK"),
            ("1.6", "A", "industrial_artist_design_reform_skill_and_taste_concepts", "industrial artist、design reform、property of skill与taste等同期用语显示设计概念和角色竞争", "这些术语不能直接翻译为成熟的现代设计师职业", "补同期词典、课程、职位、协会和企业用语", "ACCEPTED_AS_CONCEPT_HISTORY"),
            ("2.1", "A", "great_exhibition_labour_print_culture_and_global_goods", "1851年展览通过目录、周刊、图像与对象同时组织机械、手艺、劳动、帝国和公众观看", "展览文本中的劳动可见性不等于工人处境改善或观众接受", "补对象、制作、工人、发行、读者和观众材料", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.2", "A", "design_school_museum_consumer_pedagogy_and_spatial_governance", "设计学校、版权、博物馆、巡展和分馆构成从生产者训练到消费者教育的制度链", "政策与开放时间不能证明教学、品味或社会改良效果", "补课程、学生、预算、工业采用、访客与地方机构档案", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.3", "B", "labour_skill_and_market_before_arts_crafts", "技能产权、手艺理想、机器与工场争论构成拉斯金和莫里斯劳动批判的重要中期前史", "本书不是Ruskin／Morris思想或工艺美术企业的核心研究", "与B0383、B0318、B0070和B0133对读", "ACCEPTED_AS_PREHISTORY"),
            ("2.4", "A", "consumer_will_taste_pedagogy_market_and_public_dispute", "消费者意志、品味规则、负面样本、商业账簿和公共争论说明消费教育如何介入市场", "不等同于百货商店、广告和信用的完整机制，也不能证明消费者被成功塑造", "补商店、目录、广告、价格、信用、家庭清单和消费者材料", "ACCEPTED_AS_CORE_MECHANISM_WITH_RETAIL_GAP"),
            ("2.5", "C", "ornamental_art_museum_and_taste_principles", "装饰艺术博物馆、室内商品和品味规则可补充整体环境的制度前史", "不系统处理唯美主义、新艺术或具体室内的设计生产与使用", "补B0035、B0338、对象、室内和委托档案", "CONTEXT_ONLY"),
            ("2.6", "A", "imperial_goods_indian_labour_and_museum_classification", "帝国物品、印度劳动、展览目录和博物馆分类把审美标准与贸易、劳动和帝国权力联系起来", "英国改革者对印度／中国的评价不是来源社会事实，其他殖民地覆盖不足", "补来源地生产者、贸易、征集、对象、翻译和地方档案", "ACCEPTED_AS_CORE_SOURCE_WITH_COLONIAL_LIMITS"),
            ("2.7", "A", "calico_copying_india_britain_trade_and_reproduction", "棉布从印度产品到英国复制、机械量产、版权与再出口构成跨境选择和再生产链", "不能把复制链写成单向欧洲吸收，也不能由英国档案替代印度生产者经验", "补贸易、样本、印染工序、印度工匠、商人和消费地材料", "ACCEPTED_AS_CORE_TRANSFER_CASE"),
            ("5.5", "C", "early_design_school_administration_and_industrial_artist", "设计学校、工业艺术家和艺术行政可作为20世纪工业设计职业制度化的前史", "19世纪角色不能直接等同于20世纪工业设计职业", "补职业组织、企业职位、合同、教育和统计", "CONTEXT_ONLY_AS_PREHISTORY"),
            ("6.2", "C", "china_at_exhibition_as_british_classificatory_discourse", "关于中国产品和劳动的展览评论可用于审查英国如何分类晚清物品", "这是外部凝视且常带浪费劳动判断，不能承担中国国货、生产或接受史", "补晚清官档、商人、工匠、参展目录、报刊和回国传播", "CONTEXT_ONLY_WITH_CHINA_P0_GAP"),
            ("15.6", "C", "contested_museum_imperial_archive_and_labour_agency", "对展览复合体、帝国档案和劳动者能动性的修正可作为去殖民设计史的方法论资源", "本书不是当代去殖民设计实践、返还或共同治理研究", "补来源社群、博物馆治理、返还、共同策展和当代研究", "CONTEXT_ONLY_AS_HISTORIOGRAPHY"),
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
    (card_dir / f"{source_id}_来源卡.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        f"# {source_id} 来源卡：{data['title']}", "", "## 一、来源身份与核验状态", "",
        "| 字段 | 内容 |", "|---|---|", f"| 来源ID | {source_id} |", f"| 作者／编者 | {data['author']} |",
        f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |", f"| 范围 | {data['scope']} |",
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |",
        f"| 版本关系 | {data['duplicate_group'] or '未发现重复组'} |",
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
                "source_id": source_id,
                "section_id": section,
                "grade": grade,
                "verification": "V2",
                "role": role,
                "accepted_claim": claim,
                "evidence_boundary": boundary,
                "original_followup": follow,
                "status": status,
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
