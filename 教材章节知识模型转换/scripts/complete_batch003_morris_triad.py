#!/usr/bin/env python3
"""Complete the Morris enterprise, movement genealogy, and political thought triad."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-003-CH02-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0070": {
        "title": "William Morris: Design and Enterprise in Victorian England",
        "author": "Charles Harvey、Jon Press",
        "version": "Manchester University Press, 1991",
        "type": "设计企业史、商业史与生产组织史",
        "scope": "1861—1896年的Morris企业活动，兼及合伙制、生产、劳动、市场、继承和Kelmscott Press",
        "duplicate_group": "莫里斯共享史料组：与B0133、B0318等会引用相同书信和行动者文本；解释可比较，重合引文不得重复计作独立证据",
        "summary": "Harvey与Press把莫里斯从单一艺术家或社会主义思想家的形象中分离出来，借助账簿、通信、工资、合伙协议、产品与销售记录重建其企业实践。它尤其适合解释设计构思、协作者、工场劳动、外包、质量控制、价格和市场如何共同形成所谓“Morris look”。该书同时显示，莫里斯的社会主义论述并未转化为一家社会主义企业：高工资、技艺自主与严格监督、计件工资和雇主权力并存。教材应以此处理理想与企业现实的张力，而不能把商业成功或善意雇佣等同于劳动解放。",
        "strengths": [
            "以企业账簿、合伙文件、书信、工资和销售材料校正艺术家中心传记。",
            "重建自产、外包、垂直整合、质量控制、定价、零售和分销之间的组织链。",
            "区分Morris、Burne-Jones、工场经理、熟练工人和外部制造者在具体生产中的不同作用。",
            "正面处理社会主义政治与常规雇佣、利润、纪律和所有权之间的矛盾。",
            "把Kelmscott Press的审美项目放回订阅、限量、定价和分销机制。",
        ],
        "limits": [
            "作者旨在恢复莫里斯的经营能力，可能弱化企业失败、家庭资本和结构性特权。",
            "工人多经企业档案和管理者通信出现，普通工人、女性和外包劳动者的自述不足。",
            "企业存续与财务表现不能证明产品实现了莫里斯宣称的社会理想。",
            "产品的视觉、触觉、室内使用和消费者再解释不是全书强项。",
            "同一莫里斯书信亦见于政治传记和综合传记，不能把多书引用误算为多份独立原始证据。",
            "知识涌现报告中的‘结构奇点’、‘能量守恒’和元策略是P4重组，不是原著的历史事实。",
        ],
        "checks": [
            "clean第1—4行：作者说明本书重点是莫里斯作为设计者、制造者、零售商和企业家的商业生涯。",
            "clean第3152—3155行：Merton Abbey的设厂意图与生产抱负。",
            "clean第3219—3225行：选址、租赁、设备与建筑条件说明生产空间不是纯粹审美选择。",
            "clean第3845—3853行：作者把Morris界定为常规的善意雇主，并讨论利润分享、工资与分配。",
            "clean第3861—3867行：较高工资、计件制、监督与劳动纪律并存。",
            "clean第4669—4672行：Kelmscott Chaucer的订阅与价格。",
            "clean第4727—4733行：Kelmscott Press的商业性、25%分销条件与内部化销售。",
        ],
        "maps": [
            ("0.3", "A", "enterprise_production_market_and_actor_method", "设计史须把企业组织、生产选择、协作者、价格和市场纳入对象解释", "企业档案不能完整呈现工人、家庭和消费者经验", "补工人自述、家庭资本、消费者与对象使用材料", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "accounts_letters_partnership_wage_and_sales_records", "账簿、合伙协议、书信、工资与销售记录可互证艺术家自述和企业行为", "局部clean回查未完成全部数字、引注和档案号核定", "回纸本页码、档案号、表格和计算过程", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "entrepreneur_worker_gender_consumer_and_visual_bias", "企业家中心、工人中介、女性不足、消费者缺口与形式分析偏弱须进入审计", "识别偏差不等于已经恢复沉默主体", "补多主体劳动史、性别史、对象和使用史", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.3", "A", "partnership_workflow_make_or_buy_and_control", "合伙分工、图样转化、自产／外包和质量控制重组构思与制作权力", "公司名称或Morris品牌不能自动确定逐件作者", "逐对象补图样、工序、工资、合同与署名", "ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.4", "B", "materials_dyes_printing_and_production_site", "染料、印花、织造和生产地点的选择把材料性能、质量与企业成本相连", "不是完整技术史，不能仅由经营叙述推出材料效果", "补配方、样品、设备、工艺记录和物质检测", "ACCEPTED_WITH_TECHNICAL_FOLLOWUP"),
            ("1.5", "A", "collective_authorship_and_hidden_labour", "艺术家、制图／放大、经理、工人和外部制造者共同完成产品，个人品牌遮蔽集体劳动", "协作存在不等于权力平等或署名清楚", "补对象级任务、工资、性别、署名和工场记录", "ACCEPTED_AS_CORE_SOURCE"),
            ("1.6", "A", "designer_craftsman_owner_manager_and_worker_roles", "设计者、工匠、业主、经理、零售者与印刷者等角色在同一企业内交叠", "不能把这些角色直接等同于20世纪职业工业设计师", "补同期职位、合同、行业组织与职业称谓", "ACCEPTED_AS_CONCEPT_HISTORY"),
            ("2.3", "A", "socialist_ideal_enterprise_labour_and_price_contradiction", "社会主义劳动伦理、高价手工商品、常规雇佣与市场生存构成工艺美术的核心张力", "企业史不能单独解释莫里斯思想体系或工人的真实认同", "与B0133、工人材料、工资比较和消费史对读", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.4", "A", "middle_class_home_retail_pricing_and_market_creation", "产品系列、零售、宣传、价格与中产家庭共同塑造Morris市场", "销售和知名度不证明所有消费者的欲望、使用或接受", "补订单、家庭清单、读者／顾客、使用和二手流通", "ACCEPTED_AS_CORE_MARKET_SOURCE"),
            ("2.5", "A", "total_interior_product_range_and_morris_look", "跨家具、织物、壁纸、玻璃和室内装饰的产品体系形成可识别的整体环境", "风格一致性不能抹去不同设计者、工序和用户改造", "补具体室内、对象、委托、图像和使用材料", "ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.7", "B", "american_distribution_and_transatlantic_market_transfer", "代理、展览、订单与分销为工艺美术跨大西洋传播提供可检验的商业路径", "市场接触不等于形式影响或地方接受", "补美国代理、客户、评论、对象与地方再生产", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("5.5", "C", "design_enterprise_as_professionalization_prehistory", "设计、制造、零售和品牌管理的结合可作职业工业设计形成的企业前史", "19世纪工艺企业不能直接代表20世纪专业制度", "补企业设计部门、职业协会、合同和教育材料", "CONTEXT_ONLY_AS_PREHISTORY"),
        ],
    },
    "B0168": {
        "title": "The Arts and Crafts Movement: A Study of Its Sources, Ideals and Influence on Design Theory",
        "author": "Gillian Naylor",
        "version": "MIT Press, 1971",
        "type": "工艺美术运动思想谱系与跨国设计理论史",
        "scope": "Pugin、Ruskin、Morris至Ashbee、Lethaby，再到Muthesius、Gropius与斯堪的纳维亚的观念迁移",
        "duplicate_group": "工艺美术谱系组：与B0133、B0070及包豪斯／Werkbund研究共享人物与文本；影响链须以直接传播材料另证",
        "summary": "Naylor以‘来源—理想—影响’组织工艺美术运动，追踪Pugin、Ruskin、Morris、Ashbee和Lethaby的社会—审美命题如何经学校、协会、出版、旅行与改革话语进入德国及斯堪的纳维亚。它能为第二章建立工艺美术的思想与制度谱系，也能为第四章发现跨国转译线索。其1971年的叙述带有明显的目的论：英国理想因贵族化而失败，德国和北欧则通过工业与教育把它推进到现代主义。教材必须把这种结论降为史学立场，并用企业史、直接交流档案和区域研究检验。",
        "strengths": [
            "把建筑、室内、工艺、教育和社会改革放在同一思想谱系中。",
            "追踪文本、学校、组织和跨国中介，而非只列举风格相似。",
            "把民主理想与昂贵商品、手工理想与机器生产的矛盾置于中心。",
            "可作为英国工艺美术进入Werkbund、包豪斯和北欧叙事的检索路线。",
            "保留Ashbee等行动者对运动狭窄、贵族化和产业关系的自我批评。",
        ],
        "limits": [
            "1971年研究强烈朝向‘从莫里斯到格罗皮乌斯’的现代主义目的论。",
            "英国失败／德国与北欧成功的国别对照过度概括，内部差异和反例不足。",
            "把工艺美术描述为反机器容易遮蔽自产、外包和机械协作的混合生产。",
            "相似原则或后来的认可不能自动证明直接影响，传播链仍需信件、课程、旅行、翻译和组织档案。",
            "女性、殖民材料、工场劳动和消费者的覆盖不足。",
            "P4报告的‘语义鸿沟’、‘强制进化’等模型不是原著命题。",
        ],
        "checks": [
            "clean第1行：题名与作者；版本信息指向MIT Press 1971年版。",
            "clean第45—51行：精英产品问题与Ashbee对狭窄贵族化的批评。",
            "clean第57—62行：作者借Banham的‘precious vessel’隐喻定位并修正运动影响。",
            "clean第98—104行：Pugin的设计实践、原则和中世纪社会理想。",
            "clean第238—244行：Ruskin《哥特的性质》经Working Men's College和Kelmscott传播到Morris的链条。",
            "clean第1110—1117行：工艺家具、量产、斯堪的纳维亚与英国断裂的作者判断。",
            "clean第1381—1387行：Ashbee关于学校、产业、标准化和机器之美的讨论。",
            "clean第1411—1417行：Central School与包豪斯关联的谱系性判断。",
        ],
        "maps": [
            ("0.2", "B", "modernist_genealogy_and_periodization_case", "‘从莫里斯到格罗皮乌斯’可作为需要批判的设计史分期范式", "该谱系是1971年史学建构，不是自然发生的历史进程", "补反目的论研究、区域断裂和未实现路径", "ACCEPTED_AS_HISTORIOGRAPHY_CASE"),
            ("0.3", "A", "ideas_institutions_practice_and_transfer_method", "思想、学校、组织、实践和跨国中介须共同解释运动形成与转译", "谱系框架可能把后见之明写成前定方向", "以同时期传播文件和反例约束", "ACCEPTED_AS_METHOD_WITH_TELEOLOGY_AUDIT"),
            ("0.5", "B", "actor_texts_objects_and_institutional_sources", "行动者文本、学校和组织材料可追踪理想的表述与传播", "当前仅V2且未完成全书引文页码与图像核验", "回原版、档案、课程、组织记录和对象", "ACCEPTED_WITH_P0_FOLLOWUP"),
            ("0.6", "A", "teleology_national_gender_colonial_and_machine_bias", "现代主义目的论、国别本质化、女性／殖民缺口与反机器简化须进入审计", "批判偏差不能替代新的地区和劳动证据", "补企业史、性别史、殖民史、区域史与技术史", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("2.1", "B", "great_exhibition_and_design_reform_context", "博览会后的设计改革为工艺美术论争提供国家竞争与审美治理背景", "不是1851年展览组织、对象或观众史的核心来源", "与B0049、B0339、B0175及官方材料对读", "ACCEPTED_AS_CONTEXT"),
            ("2.2", "A", "schools_working_mens_college_and_central_school", "设计学校、Working Men's College与Central School连接思想、教学和工艺实践", "学校存在或名师任职不证明教学成效与学生去向", "补课程、作业、招生、师生、就业和官方档案", "ACCEPTED_AS_INSTITUTIONAL_SOURCE"),
            ("2.3", "A", "pugin_ruskin_morris_ashbee_labour_ethics_genealogy", "Pugin—Ruskin—Morris—Ashbee的劳动、社会与艺术命题构成运动内部既连续又分歧的谱系", "不能把多位作者压缩成单一反工业立场", "逐文本区分作者、年代、对象、机器观与政治条件", "ACCEPTED_AS_CORE_SOURCE"),
            ("2.4", "B", "elite_market_and_democratic_ideal_contradiction", "民主改革理想与昂贵、精英化产品市场之间存在结构张力", "作者的总体判断不能替代企业价格、顾客与使用证据", "与B0070、销售账簿、家庭清单和消费者材料对读", "ACCEPTED_WITH_MARKET_FOLLOWUP"),
            ("2.5", "A", "architecture_interior_craft_and_total_environment", "建筑、家具、室内与手工艺的统一构成工艺美术到整体环境设计的重要路径", "风格和原则谱系不能确定具体对象作者、制作和使用", "补对象、图纸、工场、委托、室内与使用材料", "ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.7", "A", "britain_germany_scandinavia_translation_route", "出版、教育者、组织和改革讨论形成英国观念向德国及北欧转译的候选链", "相似性、继承宣称或后世评价不等于直接因果影响", "补翻译、书信、旅行、课程、组织会议和地方再生产", "ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
            ("4.1", "A", "arts_crafts_to_werkbund_translation_prehistory", "工艺美术关于质量、机器、教育和社会改革的争论构成Werkbund形成的跨国前史", "不能据此写成英国模式单向造成Werkbund", "补Muthesius、Werkbund档案、德国企业和论争原文", "ACCEPTED_AS_CORE_PREHISTORY"),
            ("4.2", "B", "central_school_and_bauhaus_genealogy_claim", "Central School和工艺教育可作为包豪斯课程谱系的待证线索", "该书的连续谱系带有后见之明，不能独立证明包豪斯制度来源", "补包豪斯课程、师生、书信、旅行和直接引用", "ACCEPTED_WITH_DIRECT_TRANSFER_GAP"),
            ("4.6", "B", "school_workshop_industry_transmission_comparison", "学校—工场—产业关系可与呼捷玛斯及其他设计教育制度比较", "英国和德国材料不能替代苏联学校的治理、课程和学生项目", "补呼捷玛斯P0课程、招生、工作室、治理与作品档案", "ACCEPTED_AS_COMPARATIVE_CONTEXT"),
            ("4.7", "A", "canonical_migration_selection_and_reframing", "跨国传播是选择、改写和制度适配，不应简化为风格影响", "作者自身仍有英国源头到大陆完成的目的论", "补接收方行动者、翻译差异、拒绝与失败案例", "ACCEPTED_WITH_HISTORIOGRAPHIC_LIMIT"),
            ("7.6", "C", "scandinavian_arts_crafts_genealogy", "北欧工艺—工业关系可获得19世纪末至20世纪初的谱系入口", "1971年概括过旧，不能承担战后北欧福利、工业或消费史", "补北欧本地语言研究、企业、政策、劳动和战后对象", "CONTEXT_ONLY"),
        ],
    },
    "B0133": {
        "title": "William Morris: Romantic to Revolutionary",
        "author": "E. P. Thompson",
        "version": "1955初版、1976修订；Stanford University Press 1988重印",
        "type": "政治思想史、文学—社会史与解释性传记",
        "scope": "莫里斯的浪漫主义、艺术实践、社会主义组织活动与‘必要／欲望’思想；重点至1896年",
        "duplicate_group": "莫里斯共享史料组：与B0070、B0318等会引用相同书信、讲演和作品；汤普森的解释可独立讨论，共享原文不能重复计证",
        "summary": "Thompson以政治—思想传记说明莫里斯的浪漫主义、艺术实践与革命社会主义并非断裂的三段人生，而是在不同历史条件下逐步重组。他把莫里斯对艺术和劳动的论述从多篇讲演、文章与实践中重构，强调其批判对象主要是利润导向的资本主义生产，而不是工业技术本身。1976年后记又修正了早期马克思主义框架，承认‘欲望教育’与乌托邦想象具有不可被科学社会主义吸收的地位。因此本书是2.3的核心解释文献，但不是企业经营、产品形式或工人经验的替代证据；‘必要与欲望’首先是Thompson的分析编排。",
        "strengths": [
            "以作品、讲演、书信、社会主义报刊和组织档案连接文学、艺术和政治行动。",
            "反对把莫里斯简化为装饰艺术家或脱离现实的反机器浪漫主义者。",
            "详细重建SDF、Socialist League、议会政治与宣传策略之间的内部争论。",
            "作者在1976年后记公开交代立场变化、解释失败和修订原则，便于史学审计。",
            "把艺术、劳动、使用、必要、欲望和乌托邦想象连成可争辩的思想结构。",
        ],
        "limits": [
            "‘必要与欲望’是作者从分散材料重构的分析体系，不是莫里斯在单一著作中完成的理论。",
            "马克思主义政治传记以莫里斯为中心，家庭、女性、工场普通劳动者与消费者相对不足。",
            "早期版本含作者自认的道德化评论和政治套语；1976年修订虽删改，解释承诺仍鲜明。",
            "思想连续性不能替代企业账簿、工场记录、工资、产品和使用材料。",
            "后记对马克思主义和乌托邦的重新评价属于Thompson的1976年判断，须与1955正文分层。",
            "P4知识涌现报告的统一模型和网络指标不应反写为原著或莫里斯的自觉理论。",
        ],
        "checks": [
            "clean第1—3行：1955／1976版权、Stanford 1988重印及题名作者信息。",
            "clean第6218—6223行：作者明确说艺术—劳动理论散见历史与描述文本，必须从多处材料重构。",
            "clean第6230—6236行：莫里斯批判资本主义利润生产而非工业本身，并把Ruskin、历史研究和Marx连接起来。",
            "clean第7170—7174行：1976后记承认艺术实践章节不足及旧有‘Morris movement’影响叙述需要修正。",
            "clean第7488—7506行：作者修正‘马克思主义者或非马克思主义者’二选一，强调乌托邦和欲望教育。",
            "clean第7698—7708行：Thompson公开说明莫里斯对其自身政治思想的影响与解释立场。",
            "clean第7998—8008行：修订版删去作者自认的道德化插话，保留莫里斯原文。",
        ],
        "maps": [
            ("0.3", "A", "political_intellectual_biography_and_reconstruction", "思想史可把文学、讲演、组织行动和历史条件相互校验，并公开说明重构过程", "重构的体系不能归为行动者亲自完成的单一理论", "逐命题注明莫里斯原文或Thompson解释", "ACCEPTED_AS_METHOD"),
            ("0.5", "A", "works_letters_press_and_socialist_archives", "作品、书信、讲演、报刊和组织档案可追踪概念在不同时期的变化", "当前V2抽查未完成所有引文、档案和版次核定", "回莫里斯原集、同期报刊、组织档案和实际页码", "ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6", "A", "author_commitment_morris_center_gender_worker_and_version_bias", "作者政治承诺、莫里斯中心、家庭／女性／工人缺口和1955／1976层次须进入审计", "作者自我反思不消除这些限制", "补企业史、劳动史、女性与家庭材料及不同版本对照", "ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.6", "B", "art_architecture_decorative_art_and_worker_artist_concepts", "莫里斯对建筑、装饰艺术、艺术家与工人的区分可用于19世纪设计概念史", "政治思想传记不能独立说明行业职位和职业制度", "补同期职位、企业、学校与行业组织材料", "ACCEPTED_AS_CONCEPT_HISTORY_SUPPORT"),
            ("2.3", "A", "morris_labour_capitalism_socialism_and_utopian_desire", "莫里斯把艺术—劳动问题指向利润生产、阶级关系、使用价值和欲望教育，构成工艺美术政治的核心解释", "‘必要与欲望’是Thompson重构；莫里斯政治不能代表企业实际劳动关系", "与莫里斯原文、B0070、工人材料和反对者文献对读", "ACCEPTED_AS_CORE_INTERPRETATION"),
            ("2.4", "C", "use_profit_luxury_and_consumption_critique", "使用、利润、奢侈与社会必要之间的关系可为消费批判提供思想背景", "不含百货、广告、信用或消费者行为的充分材料", "补零售制度、价格、广告、消费者与家庭使用材料", "CONTEXT_ONLY"),
            ("2.5", "B", "architecture_as_total_art_and_life_framework", "建筑作为关联装饰艺术、劳动与生活的总体框架可解释整体环境理想", "思想框架不能替代具体室内、对象、作者和使用史", "补图纸、对象、委托、工场、家庭和视觉核验", "ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.6", "C", "anti_imperial_politics_without_display_history", "莫里斯的反帝国政治可提示工艺美术与帝国的内部矛盾", "本书不能承担世界博览会分类、殖民物质流动或被殖民者经验", "补展览、贸易、殖民档案和来源社会材料", "CONTEXT_ONLY_NOT_COLONIAL_CORE"),
            ("2.7", "C", "ideas_translation_without_material_transfer_chain", "莫里斯文本的国际传播可作为思想转译入口", "不等于棉布、陶瓷、纹样或日本主义的物质迁移机制", "补翻译、出版、旅行、贸易、对象和地方生产", "CONTEXT_ONLY"),
            ("11.5", "C", "anti_capitalist_design_critique_prehistory", "对资本主义劳动、商品和欲望的批判可作为战后设计批评的长时段前史", "不能用19世纪思想直接证明战后反设计运动的组织、对象或接受", "补战后行动者文本、团体、对象和政治语境", "CONTEXT_ONLY_AS_PREHISTORY"),
            ("15.5", "C", "necessity_desire_and_utopian_imagination_genealogy", "必要、欲望与乌托邦想象可作为当代转型设计讨论的一条思想谱系", "不能把Thompson重构当作当代设计方法或文明尺度结论", "补当代理论、实践、参与者和效果研究", "CONTEXT_ONLY_AS_GENEALOGY"),
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
