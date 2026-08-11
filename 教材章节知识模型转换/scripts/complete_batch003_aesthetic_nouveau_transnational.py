#!/usr/bin/env python3
"""Complete aestheticism, Art Nouveau, and transnational Arts & Crafts sources."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0035": {
        "title": "The Aesthetic Movement: Prelude to Art Nouveau",
        "author": "Elizabeth Aslin",
        "version": "Elek Books, London, 1969",
        "type": "英国唯美主义运动、装饰艺术与新艺术前史",
        "scope": "约1855—1885年的英国与美国，兼及英国设计向欧洲大陆的传播；建筑、室内、家具、日本趣味、商业、服装与印刷",
        "duplicate_group": "唯美主义—新艺术前史组：与Liberty企业史、时尚史和新艺术图录共享对象与行动者；相同目录、期刊、图像和行动者文本不重复计证",
        "summary": "Aslin以跨媒介专题和大量同期材料重建英国唯美主义运动，把建筑、室内、家具、陶瓷、服装、童书、商业目录与讽刺媒体置于同一历史问题中。它能为第二章提供唯美主义整体环境、艺术工业、Liberty与日本趣味的核心线索，也能显示形式传播怎样经过商店、博览会、期刊和商品发生选择性转译。然而‘唯美主义直接孕育新艺术并通向20世纪功能主义’是作者1969年的连续性框架，不可当作已经证实的单线因果；关于大众品味改善、社会使命效果和跨文化接受的判断尤其需要普通商品、销售、使用者与来源社会材料补证。",
        "strengths": [
            "以期刊、政府听证、展览评论、回忆录、讲演、商业目录、私人文件与实物互校。",
            "将讽刺和流行媒体作为社会可见性材料，而不只把它们当作品图像。",
            "跨建筑、室内、家具、陶瓷、服装、印刷和商业讨论运动的非单一视觉统一性。",
            "提供日本物品进入英国、被选择和再设计的较早时间节点与具体中介。",
            "注意工业框架中的手工、商业标签、签名生产与女性陶艺劳动。",
        ],
        "limits": [
            "1969年的‘审美运动→新艺术→功能主义’连续性有明显先驱史与目的论风险。",
            "英国—美国—欧陆框架仍以英国为源头，来源社会、殖民贸易强制和日本行动者不足。",
            "以精英、签名和博物馆保存对象为主，普通廉价商品及工人阶级使用证据薄弱。",
            "女性频繁出现但缺乏系统性别、工资、职业与组织分析。",
            "Punch等讽刺材料可证明媒体表征，不能独立证明公众接受、运动规模或因果效果。",
            "知识涌现报告中的作者身份三轴、三重异化和周期模型是P4推演，不是原著命题。",
        ],
        "checks": [
            "clean第1—16行：题名、1969年版权、出版信息、十章结构与图版配置。",
            "clean第211—232行：作者修正维多利亚审美荒漠叙事，并引同期文本主张好品味向各阶层扩散。",
            "clean第353—389行：日本艺术、Morris社会使命、期刊、Home Arts and Industries Association及Punch证据。",
            "clean第475—478行：学校建筑社会改良主张与作者对实际效果的保留。",
            "clean第543—553行：维多利亚风格多样、批量生产与‘艺术附加’问题。",
            "clean第711—773行：Art Nouveau前史与fitness for purpose通向功能设计的作者连续性判断。",
            "clean第773—802行：日本趣味三阶段、1854展览、1858印花棉布与Burges收藏。",
            "clean第893—929行：费城／巴黎博览会、铸铁、日本式商品注册与英国消费端再编码。",
            "clean第1064—1103行：Punch作为社会编年材料及1877年编辑攻击政策。",
        ],
        "maps": [
            ("0.2", "B", "aestheticism_as_contested_modern_design_prehistory", "唯美主义可被视为维多利亚现代设计改革的一种自觉实践", "不得把作者的前史框架写成通向新艺术或功能主义的必然阶段", "与较新唯美主义、新艺术及多线现代性研究对读", "ACCEPTED_AS_HISTORIOGRAPHIC_POSITION"),
            ("0.3", "A", "cross_media_form_social_and_commercial_history", "跨媒介对象须同制度、商业、传播与社会话语共同解释", "运动的情绪／氛围统一性是作者分析概念，不是对象自然具有的属性", "逐对象核对制作、销售、使用和反例", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "periodicals_hearings_catalogues_memoirs_archives_and_objects", "期刊、听证、目录、回忆、讲演、档案与实物可形成互证链", "讽刺、广告和回忆录各有立场与记忆偏差，图版仍须返回原件", "核定版次、页码、图版、档案号与传播范围", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "museum_survival_class_gender_empire_and_media_bias", "精英藏品、签名对象、媒体讽刺和英国中心造成系统性可见性偏差", "作者识别普通商品并不等于保存与使用缺口已经补齐", "补销售、家庭清单、工人、女性、来源社会与普通对象", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.5", "B", "art_industry_signed_workers_and_distributed_authorship", "艺术陶瓷、印刷和商业制造显示设计、制作、签名、企业与销售的分工", "署名不等于全部作者权，女性劳动与工资／职位材料不足", "补工厂账册、工序、工资、商标、订单和对象标记", "ACCEPTED_AS_ACTOR_SUPPORT"),
            ("1.6", "B", "art_prefix_aesthetic_designer_and_commercial_category", "‘art’前缀、审美家和专业设计者说明艺术制造与设计身份的概念竞争", "标签的商业扩散不能证明职业制度已经稳定", "补行业名录、职位、学校、协会、目录和合同", "ACCEPTED_AS_CONCEPT_HISTORY_SUPPORT"),
            ("2.3", "B", "social_mission_labour_ethics_and_market_conversion", "社会改良、劳动伦理、工业框架手工与高价／奢侈化形成内在张力", "社会使命多由设计者与评论者陈述，不能证明劳动或大众生活实际改善", "与工资、价格、产量、劳动者和消费者材料互证", "ACCEPTED_AS_REFORM_CONTEXT"),
            ("2.4", "B", "liberty_catalogues_art_industry_and_taste_marketing", "Liberty、商业目录和‘art’标签显示商店如何分类并营销审美生活方式", "不是百货制度、信用或消费者接受的完整研究", "与B0006、B0305及销售／顾客材料对读", "ACCEPTED_AS_AESTHETIC_RETAIL_SUPPORT"),
            ("2.5", "A", "aesthetic_movement_total_interior_fashion_print_and_art_nouveau_prehistory", "建筑、室内、家具、服装、陶瓷与印刷共同构成唯美主义整体环境", "‘Art Nouveau序曲’是作者中心命题，形式相似不自动证明直接传播", "逐案例补接触、展览、出版、交易、制造与地方改写", "ACCEPTED_AS_CORE_SOURCE_WITH_TELEOLOGY_AUDIT"),
            ("2.6", "X", "british_aesthetic_history_without_colonial_experience", "不以该书证明殖民分类、殖民生产者经验或帝国展示效果", "日本与其他外来物主要从英国收藏、展示和消费端出现", "改用殖民档案、贸易强制、来源社群和被展示者材料", "EXCLUDE_AS_COLONIAL_CORE_SOURCE"),
            ("2.7", "A", "japanese_goods_prints_textiles_exhibitions_retail_and_redesign", "日本物品经贸易、展览、收藏、商店、印刷和英国再设计形成多环节传播链", "‘影响’仍以英国接收端为主，1850年代优先权和直接传播须回P0核定", "补日方生产／出口、外交、贸易、设计者接触和地方使用", "ACCEPTED_AS_CORE_TRANSFER_SOURCE_WITH_SOURCE_SIDE_GAP"),
            ("3.6", "B", "childrens_books_cards_colour_printing_and_typography_prehistory", "童书、贺卡、套色印刷与版面不对称构成现代平面传播的19世纪前史", "不是先锋排版或大众媒体制度的完整专史，图像尚未逐件复核", "补印刷工序、出版档案、版本、发行、读者和实际图版", "ACCEPTED_AS_GRAPHIC_PREHISTORY"),
            ("11.6", "C", "satire_media_typing_and_style_commercialization_prehistory", "讽刺媒体、类型化人物与商业标签可作为亚文化被媒介化和市场化的长时段比较", "审美运动不是20世纪亚文化，媒体退场不等于实践消失", "只作比较并补参与者、场景、传播、消费和反例", "CONTEXT_ONLY"),
            ("12.6", "B", "women_craft_workers_fashion_and_signature_visibility", "女性陶艺者、刺绣者、服装参与者与签名制度显示性别化设计劳动的可见与遮蔽", "零散人物不能代表女性劳动结构或实际职业改善", "补工资、职位、训练、家庭劳动、企业档案和女性自述", "ACCEPTED_AS_GENDERED_LABOUR_SUPPORT"),
        ],
    },
    "B0338": {
        "title": "Art Nouveau 1890–1914",
        "author": "Paul Greenhalgh主编；多作者",
        "version": "V&A Publications / Harry N. Abrams, 2000",
        "type": "新艺术运动国际展览图录、专题论文集与物质文化史",
        "scope": "1890—1914年，以欧洲与北美为主；意义资源、八类材料工艺、十三座城市及展览传播",
        "duplicate_group": "新艺术综合图录组：与唯美主义、工艺美术、维也纳及各城市专史共享人物与对象；同一图版、展品、引文和博览会数据不重复计证",
        "summary": "Greenhalgh主编的30篇论文以‘意义的生产—材料的发明—城市与设计师’三部分重写新艺术运动，拒绝把它压缩成单一曲线风格。它为2.5提供最强综合来源，也能把纸、木、纺织、陶瓷、玻璃、金属、珠宝和雕塑同城市、企业、期刊、商店和博览会连接起来。其‘第一个自觉且国际化的现代视觉文化改造尝试’、1893—1914三阶段与‘奇怪的死亡’属于Greenhalgh的解释框架；展览图录的名作选择、巴黎引力、欧美范围、女性生产者和殖民权力分析不足，必须同对象档案、区域研究和来源社会材料分层。",
        "strengths": [
            "以意义、材料、城市三个维度组织30篇专业论文，兼顾概念、工艺与地方条件。",
            "图版、展品目录、同期宣言、期刊、商业记录与城市个案形成密集检索网络。",
            "把博览会、商店、期刊、学校、博物馆和企业视为风格传播的制度机器。",
            "明确新艺术具有多中心、多材料和地方化变体，抵制单一法国曲线范式。",
            "东方与西方、女性表征、民族浪漫主义及风格衰落均有独立专题或实证章节。",
        ],
        "limits": [
            "展览图录优先保存、可借展、具名和视觉突出的作品，普通产品与失败对象不足。",
            "十三座城市和欧美重心不能代表全球；殖民地与来源社会多作为视觉资源或展览背景。",
            "‘现代性’是统摄性解释，可能压平宗教、民族、商业与反现代实践的差异。",
            "女性身体表征材料较强，女性设计生产者、工坊劳动和组织权力仍偏弱。",
            "观众人数、影响、首创、风格诞生和终结等强判断须回统计口径、同期材料和较新研究。",
            "知识涌现报告的中心性、移除实验和假设均为P4解释性建模，不能作为原著量化事实。",
        ],
        "checks": [
            "clean第2—18行：书目分类、2000年V&A／Abrams出版与版权信息。",
            "clean第57—61行：30章五部分目录、注释、书目、展览对象清单与索引。",
            "clean第177—210行：矛盾定义史、现代性统一框架及‘第一个自觉国际尝试’命题。",
            "clean第338—370行：1893—95首阶段、Beardsley、Horta、van de Velde与Bing。",
            "clean第424—445行：1902都灵、商品化与展示—营销—传播机器。",
            "clean第454—500行：国家机构、博览会传播、殖民展示空间与1910—11缺席。",
            "clean第500行：作者明确否定第一次世界大战直接杀死新艺术的简化解释。",
            "clean第1575—1653行：Orient and Occident章的问题、贸易／博览会／Bing网络和西方再现。",
            "clean第1314—1437行：女性劳动、‘新女性’、身体图像、厌女与雌雄同体表征。",
        ],
        "maps": [
            ("0.2", "A", "art_nouveau_modernity_periodization_and_multiple_endings", "新艺术的现代性、1893—1914分期与衰落可作为可争论的史学模型", "‘第一个’、三阶段和1910—11终结均为作者综合，不能自然化为全球时间", "与区域年表、同期命名、生产／展览延续和反例互证", "ACCEPTED_AS_HISTORIOGRAPHIC_CORE"),
            ("0.3", "A", "meaning_material_city_and_institution_matrix", "意义资源、材料工艺、城市地方化与传播制度须联合解释风格", "现代性统一概念不能消除各章差异或多作者立场", "保持作者署名并逐案例建立机制链", "ACCEPTED_AS_METHOD"),
            ("0.4", "A", "objects_as_material_visual_and_exhibition_evidence", "对象材质、工艺、构造、图版与展览著录共同支持形式—制作分析", "本地OCR不能替代图版，展品状态也不等于原使用情境", "返回实物、高清图、尺寸、修复、来源与使用记录", "ACCEPTED_AS_OBJECT_METHOD_WITH_VISUAL_FOLLOWUP"),
            ("0.5", "A", "catalogue_periodicals_manifestos_archives_and_bibliography", "展览清单、期刊、宣言、企业／馆藏记录和书目可组成多层史料入口", "论文间材料密度不同，原文引述与数字仍须逐项核定", "核定页码、版本、档案号、展品号和引文上下文", "ACCEPTED_AS_SOURCE_NAVIGATION"),
            ("0.6", "A", "curatorial_masterpiece_city_gender_colonial_and_survival_bias", "展览选物、名家、城市、欧美、性别与殖民来源偏差须显式审计", "专章触及女性／东方不等于生产者和殖民权力缺口已补足", "补普通物、劳动、女性生产者、殖民网络和来源社会材料", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7", "A", "multi_center_local_adaptation_with_asymmetric_networks", "国际传播由多中心、商业中介、城市制度与地方资源共同改写", "仍以欧美城市为主，不能据此声称全球覆盖或对等交流", "补东亚、殖民地、拉美、非洲及不对称流通研究", "ACCEPTED_AS_GLOBAL_RELATIONAL_METHOD"),
            ("1.4", "A", "paper_wood_textile_ceramic_glass_metal_jewellery_material_systems", "八类材料章显示技术、工艺、企业与形式创新互相制约", "‘材料能动性’是解释语言，技术首创和性能需专史／实物核验", "补专利、配方、工序、企业、劳动、供应链和对象检测", "ACCEPTED_AS_CORE_MATERIAL_SOURCE"),
            ("1.5", "B", "designers_firms_workshops_publishers_and_makers", "跨材料设计师、企业、作坊、出版者和工匠构成分布式作者关系", "名家与具名企业偏重，匿名劳动和内部权力未系统展开", "补工资、岗位、工序、合同、印记和工人材料", "ACCEPTED_AS_ACTOR_SUPPORT"),
            ("1.6", "A", "art_nouveau_naming_ensemblier_and_design_categories", "Art Nouveau命名、ensemblier与装饰艺术平权显示设计身份和门类重组", "店名传播为风格名不等于全体行动者接受统一自称", "补各地同期称谓、协会、职位、教育和行业文件", "ACCEPTED_AS_CONCEPT_HISTORY_CORE"),
            ("2.1", "B", "international_exhibition_sequence_after_1851", "1889—1911博览会序列可比较展览如何组织商品、国家竞争和风格传播", "不直接解释1851起源，观众数字及影响需核定且多为欧美视角", "与1851官方档案、B0339及各届目录／统计对读", "ACCEPTED_AS_LATER_EXHIBITION_COMPARISON"),
            ("2.2", "B", "museums_schools_state_agencies_and_design_quality", "博物馆、学校、国家展览和政府机构参与商品质量与现代性治理", "跨章概述不能替代各机构的课程、治理、预算和成效材料", "补机构档案、课程、采购、评审、财政和学生／企业记录", "ACCEPTED_AS_INSTITUTIONAL_SUPPORT"),
            ("2.4", "A", "bing_liberty_department_stores_publicity_and_consumption_machine", "Bing、Liberty、百货空间、期刊和展览构成新艺术的展示—营销—销售机器", "消费数量不证明相同理解，商业普及也不等于社会理想实现", "补价格、销售、顾客、信用、使用、仿制和拒绝", "ACCEPTED_AS_CORE_COMMERCIAL_MEDIATION_SOURCE"),
            ("2.5", "A", "art_nouveau_meaning_material_city_and_total_environment", "新艺术须作为多种意义、材料、城市制度和总体环境的组合而非单一曲线", "全书的现代性统一框架与名作选取须保留史学／策展边界", "逐对象补制作、委托、使用、地方称谓和反例", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.6", "B", "world_fairs_imperial_taxonomy_and_colonial_display_context", "博览会被作者概括为商业实用、帝国夸示与分类执念的传播装置", "殖民空间在书中多为背景，不能承担被殖民者经验或分类后果", "补殖民展览档案、来源社群、征集、劳工和观众材料", "ACCEPTED_AS_EXHIBITION_CONTEXT_NOT_COLONIAL_CORE"),
            ("2.7", "A", "japan_islam_trade_collecting_exhibitions_publications_and_local_representation", "日本与伊斯兰艺术经贸易、收藏、博览会、期刊和设计再现进入地方新艺术实践", "东方章节仍由西方接收端组织，吸收／抽象不能替代来源社会能动性", "补出口者、工匠、外交／贸易、殖民权力、译介和地方对象", "ACCEPTED_AS_CORE_TRANSFER_SOURCE_WITH_COLONIAL_AUDIT"),
            ("3.6", "A", "paper_periodicals_posters_typography_and_international_visual_network", "纸张、期刊、海报、插图和印刷技术构成跨城市视觉传播网络", "视觉创新与受众效果不能由图版或发行存在直接推出", "补印刷工序、发行、编辑、广告、读者与实际图版", "ACCEPTED_AS_GRAPHIC_MEDIA_CORE"),
            ("4.1", "B", "art_nouveau_to_werkbund_aeg_and_standardization_prehistory", "地方改革、企业、标准化与艺术工业联盟构成Werkbund／AEG的制度前史", "新艺术图录不提供联盟治理、合同、生产和标准争论全链", "补Werkbund、AEG、Muthesius、企业与政府P0", "ACCEPTED_AS_INSTITUTIONAL_PREHISTORY"),
            ("5.1", "B", "art_nouveau_decline_and_art_deco_transition_problem", "1910年前后新艺术的商品化、退出与多条后继路径可作为装饰艺术前史问题", "风格缺席不等于生产停止，不能建立新艺术自动进化为Art Deco的单线", "补1910—25展览、企业、对象、术语与区域研究", "ACCEPTED_AS_TRANSITION_CONTEXT"),
            ("12.6", "B", "gendered_representation_new_woman_and_missing_female_producers", "新女性、身体、厌女图像和雌雄同体表征显示性别在新艺术意义生产中的作用", "表征分析不能代表女性经验；女性设计生产者和劳动制度不足", "补女性行动者、工坊、职业、工资、接受与多样主体材料", "ACCEPTED_AS_GENDER_REPRESENTATION_SOURCE_WITH_ACTOR_GAP"),
        ],
    },
    "B0450": {
        "title": "The Arts & Crafts Movement in Europe & America: Design for the Modern World",
        "author": "Wendy Kaplan主编；多作者",
        "version": "LACMA / Thames & Hudson英国首版, 2004",
        "type": "欧美工艺美术运动跨国展览图录与比较史",
        "scope": "约1880—1920年，英国、德国、奥地利、匈牙利、斯堪的纳维亚、比利时、法国与美国；300余件展品",
        "duplicate_group": "跨国工艺美术组：与英国工艺美术、Werkbund、维也纳、新艺术及美国专史共享行动者与展品；同一Morris／Ruskin文本和对象只计一次",
        "summary": "Kaplan主编的图录以‘艺术与工业—设计与民族认同—艺术与生活’为纵轴，以英国思想和制度经出版、展览、旅行、商业和政府委派被各地选择性改写为横轴。它能纠正工艺美术运动整体反机器、单一风格和英国孤立源头的叙事，并为2.3、2.5、2.7及4.1提供跨国比较。其所谓‘国际’实际限于欧洲与美国，中心—边缘组织仍可能夸大英国单向输出；展览佳品、名家和国别章也压低普通商品、殖民网络、女性与工人。‘传统的发明’和‘人们发明其所需的运动’适合作为分析命题，不能替代具体政治与制度证据。",
        "strengths": [
            "以三大共同问题比较各国选择性接受，避免用一种形式定义工艺美术运动。",
            "将手工／机器、标准化／个体表达、社会理想／奢侈市场作为各国不同制度选择。",
            "通过对象清单、注释、同期文献、机构和展览建立可追溯的策展史料入口。",
            "具体呈现出版物、博览会、商店、旅行、政府派驻与个人中介的传播路径。",
            "把Werkbund、AEG、Wiener Werkstätte、民族工艺机构与美国民主设计置于同一比较框架。",
        ],
        "limits": [
            "标题中的Europe & America不能扩展为全球史，非洲、亚洲、拉美与殖民地主体缺席。",
            "英国来源—各国接受的横轴仍有中心—边缘和单向扩散风险。",
            "展览图录偏向可展、精美、具名对象，普通工业品、失败产品和实际使用较少。",
            "国别章篇幅与问题意识不均，不能把平行论文自动视为完全可比样本。",
            "女性、慈善工艺和家庭工业多有出现，但无系统性别、工资、权力与阶级分析。",
            "知识涌现报告提出的网络枢纽和潜在链接是P4推论，必须回原章及外部证据验证。",
        ],
        "checks": [
            "clean第13—29行：LACMA展览、2004年英国版、目录、Checklist及图录性质。",
            "clean第34—46行：展览方自称首次国际评估及二十年研究背景。",
            "clean第67—112行：现代性策略、三大主题、非整体反工业与德国标准化。",
            "clean第114—119行：Wiener Werkstätte奢侈品与业余／专业工艺矛盾。",
            "clean第160—195行：浪漫民族主义、Hobsbawm、艺术与生活及选择性Morris。",
            "clean第210—225行：英国工业化、Ruskin反题与Morris所谓商业暴政。",
            "clean第346—389行：Arts and Crafts Exhibition Society命名、参展者构成及变化。",
            "clean第597—665行：英国海外声誉、Muthesius、出版／展览传播及德国机器路径。",
            "clean第1717—1775行：比法通过出版、商业和展览的选择性接受。",
            "clean第1921—1997行：美国机器／民主设计、女性组织、职业机会与阶级边界。",
        ],
        "maps": [
            ("0.2", "A", "arts_crafts_as_multiple_modernity_strategies_and_endings", "工艺美术运动包含现代／反现代、手工／机器与多个终点，不能作单线时期标签", "作者纠正反工业神话仍不能消除英国章更强反工业性的区域差异", "按国家、机构、对象与时段分别核验", "ACCEPTED_AS_HISTORIOGRAPHIC_CORE"),
            ("0.3", "A", "three_theme_by_local_translation_comparative_matrix", "共同问题轴须同传播渠道、地方语境和制度结果交叉比较", "中心—边缘矩阵不能把地方写成被动接收者", "逐案区分来源、选择、误读、再生产与无直接接触", "ACCEPTED_AS_METHOD"),
            ("0.4", "A", "exhibition_objects_checklist_material_and_provenance", "展览实物、材质、尺寸、年代、藏地和来源可作为对象研究入口", "策展对象不是系统样本，OCR图像也不能承担精确视觉判断", "回展品、馆藏记录、修复、来源、制作和使用材料", "ACCEPTED_AS_OBJECT_NAVIGATION"),
            ("0.5", "A", "notes_checklist_periodicals_archives_and_multilingual_sources", "注释、Checklist、同期刊物、讲演、书信和机构材料构成多语种证据入口", "图录正文的综合句不能替代原文页码与档案核验", "核定版次、注释、档案号、展品号和引文上下文", "ACCEPTED_AS_SOURCE_NAVIGATION"),
            ("0.6", "A", "curatorial_regional_gender_class_labour_and_colonial_bias", "展览佳品、欧美范围、国别不均、女性／劳动／阶级与殖民缺口须进入审计", "女性和家庭工业案例存在不等于结构性缺席被解决", "补普通物、工人、工资、殖民网络、非欧美区域和使用者", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7", "A", "selective_reception_translation_and_asymmetric_network", "出版、展览、旅行、商业与国家中介使英国资源在各地被选择性重组", "仍由英国来源组织横轴，不能直接推广为全球互惠网络", "补反向流动、无英国中介路径和非欧美研究", "ACCEPTED_AS_GLOBAL_TRANSLATION_METHOD"),
            ("1.3", "B", "making_process_design_execution_and_standardization", "制作过程、设计—执行关系与Typisierung说明构思、制造和重复的重新分工", "不是工业劳动分工或技术标准化的完整专史", "补图纸、规格、工序、工厂、工资、专利与标准文件", "ACCEPTED_AS_DIVISION_OF_LABOUR_SUPPORT"),
            ("1.5", "A", "workshops_firms_amateurs_students_women_and_distributed_authorship", "作坊、制造商、业余者、学生、女性、贸易商与设计者共同构成运动生产网络", "名单与展品不能自动说明职责、权力、报酬或作者权", "补印记、合同、工资、岗位、工序、协会与个人材料", "ACCEPTED_AS_CORE_ACTOR_SOURCE"),
            ("1.6", "A", "movement_not_style_design_reform_and_local_terms", "运动不是单一风格；design reform、Sachlichkeit、Typisierung等地方术语显示概念竞争", "译名相近不等于语义、职业制度或社会目标相同", "保留原语、时段、行动者、机构和使用语境", "ACCEPTED_AS_CONCEPT_HISTORY_CORE"),
            ("1.7", "A", "hand_machine_workshop_factory_and_regional_hybrid_production", "英国、德国、奥地利、北欧与美国呈现不同手工—机器混合路径", "国别概括内部仍有企业、地区、阶级和对象差异", "以同类对象和组织材料做受控比较", "ACCEPTED_AS_CORE_REGIONAL_COMPARISON"),
            ("2.2", "B", "museums_schools_societies_and_state_reform", "博物馆、学校、协会和国家项目参与设计改革、民族工艺与产业竞争", "图录不提供所有机构治理、课程、预算与受益者成效", "补章程、课程、财政、采购、评审和参与者记录", "ACCEPTED_AS_INSTITUTIONAL_SUPPORT"),
            ("2.3", "A", "arts_crafts_labour_ethics_machine_market_and_price_tensions", "劳动中的快乐、机器使用、商业体制、工资与奢侈市场构成工艺美术的核心矛盾", "运动领袖宣言与图录对象不能证明实际劳动解放或民主可及", "补工资、工时、价格、销量、工人、企业和消费者材料", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.4", "B", "shops_exhibitions_periodicals_and_market_mediation", "画廊商店、展览、期刊和贸易商把改革语言转化为商品分类与市场传播", "不是百货、信用、陈列和普通消费者的完整研究", "与零售史、企业账册、顾客及家庭材料对读", "ACCEPTED_AS_MARKET_MEDIATION_SUPPORT"),
            ("2.5", "A", "art_and_life_total_environment_and_regional_variants", "总体艺术、住宅、作坊共同体与地方风格显示艺术—生活融合的多种实践", "整体环境的策展复原不能等同原住用经验，亦非统一新艺术形式", "补委托、建造、家具、居民、维护、照片和使用记录", "ACCEPTED_AS_CORE_TOTAL_ENVIRONMENT_SOURCE"),
            ("2.6", "X", "euro_american_catalogue_without_colonial_experience", "不以该书证明世界博览会殖民分类、殖民劳动或被展示者经验", "帝国经济和殖民企业仅构成部分国别背景，非系统研究对象", "改用殖民展览、贸易、来源社群、征集和劳工P0", "EXCLUDE_AS_COLONIAL_CORE_SOURCE"),
            ("2.7", "A", "publications_exhibitions_travel_commerce_government_and_local_remaking", "出版、展览、旅行、商业和政府派驻连接英国资源与地方选择、改写和再生产", "英源横轴与日本影响仍缺完整来源社会和殖民权力链", "补双向通信、贸易、日方／殖民地生产者和无直接接触反例", "ACCEPTED_AS_CORE_TRANSFER_SOURCE_WITH_CENTER_PERIPHERY_AUDIT"),
            ("4.1", "A", "werkbund_aeg_standardization_and_wiener_werkstatte_prehistory", "德国标准化、AEG、Werkbund及Wiener Werkstätte显示改革联盟与企业系统的多路径前史", "图录不能承担联盟治理、企业合同、量产或标准争论的完整证据", "补Werkbund／AEG／Werkstätte档案、章程、合同、生产与劳动", "ACCEPTED_AS_CORE_INSTITUTIONAL_PREHISTORY"),
            ("4.2", "B", "art_schools_workshops_and_production_education_prehistory", "艺术学校、工坊、协会展览与学生参展构成包豪斯之前的生产性教育背景", "不是Bauhaus基础课程、师生权力或呼捷玛斯教育体系来源", "补学校课程、师生、招生、治理、财政和作品记录", "ACCEPTED_AS_EDUCATIONAL_PREHISTORY"),
            ("4.6", "B", "replicable_societies_workshops_exhibitions_and_publications", "协会、作坊、展览与出版在多国被选择性复制，说明制度传播不等于形式复制", "未系统追踪哪些制度长期存续、失败或进入通行课程", "补章程版本、人员迁移、课程、财政和后续机构史", "ACCEPTED_AS_REPLICATION_SUPPORT"),
            ("4.7", "B", "people_publications_and_cranbrook_transfer_prehistory", "人员、出版物及Cranbrook等节点提示欧洲改革资源向美国教育机构的后续转译", "相关迁移只被点到，不能承担完整Cranbrook或全球教育史", "补迁徙档案、课程、学生、机构治理和接收方改写", "ACCEPTED_AS_TRANSFER_PREHISTORY"),
            ("12.6", "B", "women_home_industries_charity_profession_and_class", "女性协会、家庭工业、慈善工艺和职业训练显示性别与阶级共同塑造设计劳动", "富裕赞助者、受训设计者和贫困制作妇女不能合并成统一女性经验", "补工资、权力、种族／移民、家庭劳动、个人自述和组织档案", "ACCEPTED_AS_GENDERED_LABOUR_SUPPORT"),
        ],
    },
}


def load_assets():
    with ASSETS.open(encoding="utf-8-sig", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_source(source_id, data, asset):
    clean = Path(asset["clean_source_path"])
    card = {
        "source_id": source_id,
        "corpus": asset["corpus"],
        "folder_name": asset["folder_name"],
        "material_type": data["type"],
        "clean_source_path": str(clean),
        "clean_source_sha256": digest(clean),
        "duplicate_group": data["duplicate_group"],
        "files": [{"report_file_count": int(asset["report_file_count"]), "report_characters": int(asset["report_characters"])}],
        "report_structure": {"review_basis": "overall_and_all_chapter_reports_plus_emergence_gap_audit"},
        "candidate_sections": [{"section_id": row[0], "grade": row[1], "verification": "V2", "role": row[2]} for row in data["maps"]],
        "review_status": "semantic_review_complete",
        "evidence_level": "V2",
        "notes": data["limits"] + ["clean原文仅局部定位；未完成全篇、版次、图版、数字和引注核验。"],
        "original_spot_checks": data["checks"],
    }
    card_dir, map_dir = BATCH / "source_cards", BATCH / "mappings"
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
            writer.writerow({"source_id": source_id, "section_id": section, "grade": grade, "verification": "V2", "role": role,
                             "accepted_claim": claim, "evidence_boundary": boundary, "original_followup": follow, "status": status})


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
