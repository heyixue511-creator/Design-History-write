#!/usr/bin/env python3
"""Complete the actor-text, enterprise-history, and survey group in BATCH-002."""

from __future__ import annotations

import csv
import json

from complete_batch002_concepts_authorship import ASSETS, BATCH, ROOT, load_assets, write_source


DATA = {
    "B0318": {
        "title": "Hopes and Fears for Art",
        "author": "William Morris",
        "version": "Longmans, Green and Co., 1917 New Impression；五篇讲演原作于1878—1881年，1882年结集",
        "type": "工艺美术运动参与者讲演集与规范性艺术—劳动论述",
        "scope": "装饰艺术、劳动、生活环境、工艺实践与建筑；以19世纪英国为中心并涉及印度",
        "duplicate_group": None,
        "summary": "这部讲演集适合证明莫里斯如何把艺术定义为劳动中愉悦的表达，如何批判劳动分工、竞争性商业、奢侈和破坏性修复，并以工艺规则、日常环境和‘人民的艺术’提出替代方案。它是工艺美术运动行动者立场的一手文本，不是中世纪劳动、印度工艺衰落或工厂生活的直接调查。教材可用其建立‘规范命题—实践经验—社会诊断’链，但必须由企业、劳动、殖民和接受史分别核验。",
        "strengths": [
            "将装饰艺术、制作劳动、使用者经验和日常环境置于同一问题链，而不把工艺降为风格。",
            "明确说明工艺规则来自长期实践且需在实践中检验，可作为默会知识的参与者证词。",
            "以第一人称说明分工如何迫使从业者跨越多种工艺，保留专业化矛盾的历史声音。",
            "把制造者与使用者并列，并反对把艺术限定为少数天才或富人消费品。",
            "引用Birdwood及印度制造案例，提供英国工艺改革者如何理解殖民商业的可追踪入口。",
        ],
        "limits": [
            "‘艺术是劳动中愉悦的表达’和三类劳动是规范性理论，不是劳动过程的经验分类结果。",
            "中世纪普通工匠普遍自由快乐的叙述带有浪漫化，须由行会、工资、法律、性别和作坊史校正。",
            "‘印度艺术已死且被现代商业杀死’是依据有限转述形成的行动者判断，不能代表印度各地生产者。",
            "人民、工匠和使用者多以男性泛称出现，女性、家庭劳动、帝国资源和企业内部权力不足。",
            "文本把机械劳动与智性／想象性劳动强烈二分，不能推出机器生产必然无艺术。",
            "当前1917数字文本存在双栏交错、OCR符号和长行问题，正式引文须回实体页。",
        ],
        "checks": [
            "clean第7行：题名页确认1917年New Impression；书末广告说明五篇讲演作于1878—1881年。",
            "clean第390行：莫里斯明确把‘真正的艺术’定义为人在劳动中愉悦的表达。",
            "clean第67—69行：分工被描述为竞争性商业的机制；作者自述因此学习多种工艺却难专精。",
            "clean第269—287行：Mechanical Toil、Intelligent Work、Imaginative Work三分及其价值判断。",
            "clean第374—380行：Birdwood、巴黎展览印度馆、监狱地毯和商业导致衰落的论述属于转述与行动者判断。",
            "clean第41、63、406、414行：‘由人民创造、为人民创造’及制造者／使用者双重愉悦反复出现。",
            "clean第55行：有用／美的黄金法则处在反奢侈和朴素生活的规范语境中。",
            "clean第297—303行：‘无意识智慧’到‘有意识智慧’是作者的历史哲学，不是中性分期。",
        ],
        "maps": [
            ("0.3","B","actor_theory_linking_art_labour_and_use","莫里斯把艺术、劳动愉悦、制作与使用连成一个参与者理论框架","这是规范性行动者理论而非已验证的普遍机制","与劳动史、企业史、对象史和接受史对读","ACCEPTED_AS_HISTORICAL_ACTOR_THEORY"),
            ("0.5","A","lecture_testimony_citation_and_mediated_evidence","讲演中的自述、引书、历史例证和动员语言必须区分其证据身份","第一人称工艺经验仍不能证明所有工人或地区状况","逐条标明自述、转述、历史判断和规范主张","ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6","A","romantic_medieval_gender_colonial_and_binary_bias","中世纪浪漫化、男性工匠默认、英国视角和二元劳动分类构成系统性偏差","偏差识别不能代替被忽略主体的材料","补行会档案、女性家庭劳动、殖民生产者和机器工人材料","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","B","craft_rules_practice_and_tacit_knowledge","工艺规则被莫里斯描述为长期实践形成并在师徒与工场中验证的知识","作者经验不能代表所有行业且‘人性根基’不可直接证实","补工序、工具、训练、工资和作坊记录","ACCEPTED_AS_ACTOR_TESTIMONY"),
            ("1.3","B","division_of_labour_as_practitioner_problem","莫里斯把分工与专业隔离视为构思、制作和工艺协作受损的问题","这是参与者诊断且没有量化企业分工或因果效果","与Guild、工厂、职位和工序档案互证","ACCEPTED_AS_HISTORICAL_ACTOR_THEORY"),
            ("1.5","B","maker_user_and_common_worker_authorship","人民的艺术命题把普通制造者和使用者纳入作者制与价值判断","不能由口号证明实际共同作者权或责任分配","补署名、图样、工序、合同和使用材料","ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.6","A","lesser_decorative_popular_art_concept_history","lesser arts、decorative arts、popular art与Architecture的扩展用法可构成19世纪概念史材料","这些用法属于莫里斯立场而非当时唯一或现代通行定义","与同期词典、学校、组织、批评家和职业文本比较","ACCEPTED_AS_PRIMARY_CONCEPT_SOURCE"),
            ("1.7","C","india_commerce_and_eastern_art_as_british_actor_claim","印度案例可显示英国改革者如何把殖民商业、低价与工艺衰落联系起来","材料经Birdwood与展览中介且‘东方艺术死亡’不可作区域事实","回Birdwood、政府档、印度生产贸易和地方主体材料","CONTEXT_ONLY_WITH_COLONIAL_AUDIT"),
            ("2.3","A","arts_crafts_labour_ethics_primary_text","劳动愉悦、艺术民主、反奢侈和人民艺术构成工艺美术劳动伦理的一手主张","主张的传播、执行、价格与社会成效须另证","与企业账簿、工人材料、商品价格和接受史互证","ACCEPTED_AS_PRIMARY_ACTOR_TEXT"),
            ("2.4","B","anti_luxury_use_beauty_and_consumption_norms","黄金法则和反奢侈论显示改革者如何规范家庭物品与消费选择","规范文本不能证明家庭实际购买、阶级可及性或消费者接受","补目录、价格、家庭清单、销售和使用记录","ACCEPTED_AS_CONSUMPTION_DISCOURSE"),
            ("2.5","B","total_environment_craft_and_daily_life","住宅、花园、墙面、地面、家具和建筑被组织为整体生活环境","具体形式和实际空间效果需回对象图版与现场且审美判断属作者","补对象、室内、委托、制作和使用证据","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
        ],
    },
    "B0090": {
        "title": "The Bases of Design",
        "author": "Walter Crane",
        "version": "初版1898；当前clean含1897序言及1901年‘present edition’重印说明，正式引文按1901现版核定",
        "type": "工艺美术运动参与者设计讲义与历史理论著作",
        "scope": "建筑、用途、材料与方法、条件、气候、种族、象征、自然主义、个体和集体影响",
        "duplicate_group": None,
        "summary": "Crane以十类‘设计基础’把形式放回建筑位置、用途、材料、工具、作坊传统、个体变异与集体劳动之中，并在终章对比跨世代协作与面向私人利润的工厂集体劳动。它可作为1890年代设计教育和工艺美术思想的一手文本，也能为材料—方法—形式和分布式作者制提供概念工具。但形态相似推起源、气候决定色彩、‘种族特性’解释艺术的论证均不能作为教材因果模型，只能作为维多利亚知识史批判对象。",
        "strengths": [
            "作者公开说明讲稿面向Manchester Municipal School of Art学生，保留设计教育的参与者语境。",
            "把用途、材料、加工方法、安放位置与最终形式逐层连接，避免孤立形式命名。",
            "将传统具体化为作坊、工具、材料和重复劳动的累积影响，并承认个体变异。",
            "把工厂的集体劳动、机器能力、产品质量与私人利润组织分开判断，并非简单反机器。",
            "明确质疑把跨世代建筑和基本技术发明归于单一作者。",
        ],
        "limits": [
            "从形态同构逆推共同起源常缺少传播链、年代链与独立考古证据。",
            "气候—色彩和‘种族—艺术特性’论述混合文化、环境与生物本质主义，予以排除。",
            "非欧洲对象主要经英国收藏、旅行与比较艺术知识中介，生产者、征集史和殖民权力不足。",
            "大教堂匿名协作被理想化，不能证明工匠自由、平等或无等级。",
            "当前clean重复序言与现版说明；文件夹标1898但正文明确含1901年重印说明。",
            "分析报告中的当代中国和AI延伸是报告作者推论，不是Crane原著观点。",
        ],
        "checks": [
            "clean第1—11、149行：Manchester讲稿、自陈范围有限、1897序言及1901重印说明。",
            "clean第406、601、609行：用途、构造必要性、材料能力与设计成功的关系。",
            "clean第609—825行：材料与加工方法、对象位置和存在条件被分别讨论。",
            "clean第1134—1148行：‘racial influence’把文化偏好、集体沉积与个体选择混写。",
            "clean第1934—1939行：金链／宝石隐喻和从个体人物转向collective man。",
            "clean第1978行：传统被明确联系到作坊、工具和材料。",
            "clean第1991—1999行：工厂分工、集体劳动、私人利润、印花机与产品判断；作者仍设想设计师配合机器。",
        ],
        "maps": [
            ("0.3","B","multicausal_actor_framework_for_design","Crane试图以建筑、用途、材料、条件、个体与集体等多因素解释设计","十项体系是1898年的参与者框架且若干因素含决定论","作为史学对象并用现代材料史、劳动史和区域史检验","ACCEPTED_AS_HISTORICAL_ACTOR_THEORY"),
            ("0.5","B","lecture_illustration_comparison_and_claim_types","讲稿结合示意图、照片、对象比较和作者判断，须区分观察、类比与因果主张","当前未逐图核验且形态相似不证明历史联系","回实际图版、对象来源、年代与传播证据","ACCEPTED_WITH_VISUAL_VERIFICATION_GAP"),
            ("0.6","A","evolutionist_climatic_racial_imperial_and_visual_bias","进化论、气候决定、种族本质和帝国收藏视角会扭曲跨文化设计解释","识别问题不能把全部材料一概作废","保留可核工艺描述并补本地、殖民征集和反方研究","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","B","workshop_tools_repetition_and_tradition","作坊中工具、材料和重复劳动被作者视为传统形式累积的机制","大教堂和前现代作坊被理想化且工人关系未被档案验证","补作坊账簿、训练、工资、合同和考古材料","ACCEPTED_AS_ACTOR_THEORY"),
            ("1.3","A","utility_material_method_condition_and_design_control","用途、材料、加工方法和安放条件共同限制图样与处理方式","形式类比不能直接证明母题起源或单向决定","补工序实验、图样、工具痕迹、年代和传播链","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.4","A","material_process_and_form_treatment","石、木、黏土、蜡、金属和玻璃的物性及工法被具体联系到形式处理","‘忠于材料’是规范性判断且部分视觉例证待图版核验","补材料检测、工艺复原、对象与供应链","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.5","A","collective_workshop_authorship_and_individual_variation","传统、作坊、跨代协作和个体变异共同塑造对象，不能只归功于名家","匿名不等于平等且具体对象责任仍未知","补署名、图样、工序、工匠名册和管理记录","ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.6","B","design_as_unified_but_specialized_field_in_education","各设计门类专业化与艺术统一的张力可作为设计教育和概念史材料","统一艺术树隐喻是Crane的规范立场而非制度现实","补课程、职位、学校档案、行业组织与同期术语","ACCEPTED_AS_PRIMARY_CONCEPT_SOURCE"),
            ("1.7","X","racial_and_climatic_essence_as_regional_cause","不接受以‘种族特性’或气候直接解释地区色彩、形式和艺术能力","概念含本质主义且证据多为选择性比较与形态印象","改用制度、材料、贸易、劳动、委托与地方解释","EXCLUDE_AS_CAUSAL_MODEL"),
            ("2.3","A","arts_crafts_material_labour_and_machine_primary_text","材料、手脑结合、集体劳动与机器生产批评构成工艺美术运动的一手论述","产品‘令人沮丧’是作者审美判断，工厂劳动事实需另证","与工厂、企业、工人、商品和消费者档案对读","ACCEPTED_AS_PRIMARY_ACTOR_TEXT"),
            ("2.5","A","books_wallpaper_glass_metal_and_total_environment","书籍、壁纸、织物、玻璃、金属与建筑位置组成总体环境式设计论","对象图版、委托、制作与使用情境尚未逐件核验","补完整图版、对象档案与室内使用证据","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.7","C","cross_cultural_comparison_as_imperial_knowledge_history","波斯、印度、中国、日本等比较可用于研究英国设计教育如何组织全球知识","不得把其分类、形态相似或种族术语当作地方事实与影响证据","补来源社群、征集、贸易、人员和地方接受材料","CONTEXT_ONLY_WITH_COLONIAL_AUDIT"),
        ],
    },
    "B0091": {
        "title": "C. R. Ashbee: Architect, Designer & Romantic Socialist",
        "author": "Alan Crawford",
        "version": "Yale University Press, 1985",
        "type": "档案型设计师传记、工艺企业史与接受史专著",
        "scope": "Ashbee生平、Guild／School of Handicraft、建筑与工艺作品、跨国活动及声誉史",
        "duplicate_group": None,
        "summary": "Crawford利用Ashbee与Janet日记、Guild会议和财务记录、公司文件、课程政策、展览目录、设计图和同期评论，把工艺美术理念落实到学校、合作工场、有限公司、商店、迁址、库存和清算。其价值不在证明一个浪漫的成败故事，而在展示规范理想如何被资本结构、管理权、工资、市场和家庭生活改写。作者同时公开多数Guild产品归属无法确证，要求读者对‘Ashbee设计’保持疑义，这对教材的集体作者制写法尤其关键。",
        "strengths": [
            "将日记与会议记录、财务数据、公司制度、展览目录和对象档案交叉使用。",
            "以利润分享、资本份额、董事会、劳动董事和委员会冲突具体分析合作制的边界。",
            "比较Ashbee的失败解释、消费数据和同时代乡村工场，拒绝单一原因。",
            "明确区分传主、工匠、办公室助理和企业名称，并公开归属不确定性。",
            "记录妻子、家属和女装订工等有限材料，使共同体的性别盲点可见。",
        ],
        "limits": [
            "工人经验大多仍经Ashbee、会议记录或传记作者中介，普通成员自述不均。",
            "Janet虽重要，妻子、女儿、女工和当地女性仍不是持续分析主体。",
            "1985年的同情性传记和Pevsner论辩需要较新工艺美术、劳动、性别与帝国研究校正。",
            "‘Guild失败’必须区分有限公司清算、共同体延续、个人工场和长期地方影响。",
            "跨国活动和殖民工艺复兴不能从Ashbee观点外推为当地社会的真实需求。",
            "大量图版虽为论证组成部分，但当前只做文本局部回查，视觉判断未达V3。",
        ],
        "checks": [
            "clean第543、658行：1888年6月23日正式开幕，首年约80名学生及课程教师。",
            "clean第600—625行：Adams的制衡作用、委员会、利润分享、资本积累、合作制控制权与规模变化。",
            "clean第813—843行：Technical Instruction Act、whiskey money及制造／商业关联的资助资格问题。",
            "clean第1350—1355行：1898年有限公司、劳动董事、工资扣款及3,864股分布。",
            "clean第1658—1664行：迁址住房、工资争论及22赞成／11反对／1未记录的投票。",
            "clean第2127—2157行：1906年亏损、融资、库存、市场比较及Crawford对Ashbee外因解释的反驳。",
            "clean第2158—2165行：清算后离开者与约12名留守工匠的分散经营。",
            "clean第3038—3044行：办公室档案缺失、多数产品不能确证归属，1903目录另列11名Guildsmen设计。",
            "clean第1742—1743、4875—4876行：妻子被忽略与Annie Power、两名Press wives参与装订工场。",
        ],
        "maps": [
            ("0.3","A","contextual_biography_institution_enterprise_and_object","个人思想、制度、企业、作品与接受史需相互校验而非写成单一名家生平","传记结构仍以Ashbee为中心且作品部分与生平部分有所分离","补工人、女性、地方、企业和对象级材料","ACCEPTED_AS_METHOD"),
            ("0.5","A","diary_minutes_finance_catalogue_drawing_triangulation","日记、会议记录、财务、公司文件、目录和图纸可交叉约束传主自述","材料存续不均且不同材料的沉默不能视为事件不存在","逐项记录出处、日期、作者、保存缺口和冲突","ACCEPTED_AS_SOURCE_METHOD"),
            ("0.6","A","biographical_worker_gender_attribution_and_empire_bias","传主中心、工人中介、性别不均、归属推定和帝国视角均须进入审计","Crawford公开局限不等于已消除这些偏差","补成员自述、妇女家属、地方档案、来源社群和较新研究","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","A","school_guild_apprenticeship_and_workshop_knowledge","School与Guild把课程、学徒、工场生产和共同体理想并置为制度实验","招生和课程存在不等于学习效果且控制权未完全交给工人","补学生作业、考核、就业、工资和成员材料","ACCEPTED_WITH_INSTITUTIONAL_FOLLOWUP"),
            ("1.3","A","committee_board_profit_sharing_and_design_control","委员会、董事会、劳动董事、利润分享和资本份额具体重组了决策权","制度条款不等于实际平等运行且Ashbee权威长期存在","补会议表决、账簿、劳动争议和具体项目流程","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.5","A","documented_and_uncertain_collective_authorship","多数Guild产品不能牢靠归于Ashbee，工匠、助理与共同设计必须逐件区分","作者仍为叙述便利作出部分归属推定","按签名图、目录、工场记录和对象痕迹分级归属","ACCEPTED_WITH_AUTHORSHIP_CAUTION"),
            ("1.6","A","school_guild_designer_craftsman_director_and_company_roles","School、Guild、Hon. Director、craftsman、designer与limited company展示职业和组织称谓竞争","角色名称不自动说明技能边界、控制权或现代设计师身份","补章程、职位、工资、课程和同期用语","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("2.2","A","technical_education_school_policy_and_funding","School资助争议显示技术教育法律、公共拨款和生产联系如何界定制度合法性","不能把关闭只归于个人阻挠或法律单因","补LCC报告、申请、检查、预算、课程与学生结果","ACCEPTED_WITH_POLICY_FOLLOWUP"),
            ("2.3","A","arts_crafts_labour_ethic_tested_by_enterprise","Guild把满意劳动理想置于合作制、工资、订单、管理和资本的实际检验中","共同体叙事不能遮蔽权力不对称、奢侈品市场与成员分歧","与成员材料、账簿、工时、客户和同业比较互证","ACCEPTED_AS_CORE_CASE"),
            ("2.4","A","shop_commissions_stock_retail_competition_and_market","商店、委托、广告、库存、价格、零售竞争和客户距离共同影响Guild生存","Crawford的市场解释仍须回完整账簿且购买不等于使用接受","补销售、成本、退货、客户书信和消费记录","ACCEPTED_WITH_MARKET_FOLLOWUP"),
            ("2.5","B","architecture_furniture_metalwork_printing_and_place","建筑、家具、金属、珠宝、印刷和场所被纳入跨媒介工艺实践","视觉与风格判断未逐图核验且归属不一","补完整图版、对象、委托、制作和使用情境","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.6","C","empire_travel_and_craft_revival_as_actor_history","Ashbee在南非、开罗与耶路撒冷等活动可用于研究英国工艺改革与帝国治理的接触","传主规划和复兴话语不能代表当地需求或文化连续性","补地方档案、当地行动者、委托、劳动和来源社群材料","CONTEXT_ONLY_WITH_COLONIAL_AUDIT"),
            ("2.7","B","britain_us_germany_austria_and_local_translation","展览、出版、旅行、个人网络和工场比较显示工艺思想跨境流动并被重新解释","名人接触或形式相似不能证明直接影响和广泛接受","补书信、展览目录、销售、评论、教学与地方实践","ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
        ],
    },
    "B0101": {
        "title": "History of Modern Design: Graphics and Products since the Industrial Revolution",
        "author": "David Raizman",
        "version": "Laurence King Publishing, 2010, Second Edition",
        "type": "面向大学教学的现代设计通史",
        "scope": "约1700—2010年，产品、平面、室内、时装、制造、消费与制度；欧美为主",
        "duplicate_group": "VGRP004-TRANSLATION；VGRP005-EDITION",
        "summary": "Raizman以生产、消费和设计的动态关系组织长时段通史，第一至三章从法国王室制造厂与行会转向英国企业、Wedgwood，再到新材料、机械化与美国制造体系。它能为第一章提供制造者、消费者、赞助者和工匠共同参与的框架，也能为第二章连接博览会、改革、工艺美术、百货与跨境材料。但这是2010年第二版的本科综述：比较框架常把法国集中与英国市场、欧洲与美国压缩成整齐对照，殖民原料、奴隶制、工人和非西方主体不足；论证性强判断须返回其引注与专史。",
        "strengths": [
            "导论明确反对把设计史写成个人艺术活动，并把制造商与消费者列为关键利益相关者。",
            "以对象、生产流程、企业、市场、文本和社会语境交叉组织，而非仅列风格和名家。",
            "第一至三章建立王室工场／行会—企业与目录—机械化与美国体系的连续问题链。",
            "承认技术进步并非对所有群体同等有利，并强调消费者赋予对象意义。",
            "第二版公开其本科教材所需的简化、选材和多视角平衡问题。",
        ],
        "limits": [
            "2010第二版与B0478中文译本属于同一版次知识内容；重合命题不得算独立互证。",
            "B0102为2023修订版；未变内容不独立计证，新材料必须以版次差异明确标注。",
            "法国中央控制与英国创业市场的对比过整齐，可能遮蔽两地内部混合生产与制度交叉。",
            "把消费扩张称为民主化容易混淆市场选择、政治权利、阶级可及性和殖民剥削。",
            "美国体系仍沿用熟练劳力稀缺、西进需求和军工序列，须补原住民、奴隶制、国家采购和较新技术史。",
            "中国与全球南方多作为灵感、贸易或材料来源出现，不能替代本地制度、劳动和使用史。",
            "当前只核对clean文字关键段落，577幅插图及其图说、视觉比较未达V3。",
        ],
        "checks": [
            "clean第33—40行：题名页确认Second Edition及2010年Laurence King出版。",
            "clean第170—205行：作者说明本科综述需要简化，同时尝试增加多视角、重组章节和新增材料。",
            "clean第244—264行：技术进步的不均等、消费者主动意义及制造商／消费者stakeholders。",
            "clean第283—366行：Gobelins、分工、艺术家／工匠、瓷器、行会与1791年制度变化。",
            "clean第424—490行：Chippendale目录、市场多样性、Wedgwood企业链和Garthwaite丝绸图案。",
            "clean第667—681行：美国体系、国家合同、互换零件、工会传统缺失和消费端装饰。",
            "clean第785行：Albert Memorial段落明确把工业繁荣与殖民扩张、原料联系起来，但未形成完整供应链。",
        ],
        "maps": [
            ("0.2","B","survey_periodisation_and_revision_history","通史分期和第二版重组可作为教学结构参照","分期是作者选择且2010后材料已经老化","与2023版、区域史和专题史比较","ACCEPTED_AS_CURRICULUM_REFERENCE"),
            ("0.3","A","production_consumption_stakeholder_design_history","设计史应同时分析设计者、工匠、制造商、赞助人、消费者与制度语境","stakeholder框架仍可能压低工人、殖民主体和环境","补劳动史、殖民史、性别史与使用史","ACCEPTED_AS_METHOD"),
            ("0.5","B","objects_texts_catalogues_exhibitions_and_secondary_synthesis","对象、宣言、目录、广告、展览和二手研究可互相约束通史叙述","综述经作者选择且本次未逐条回原引注和图版","重要命题回专史、原始文献、实际对象和页码","ACCEPTED_WITH_VERIFICATION_GAP"),
            ("0.6","A","survey_euroamerican_market_colonial_gender_and_image_bias","本科综述简化、欧美重心、市场民主化语言、殖民与性别不足须进入审计","作者承认多视角不等于覆盖已充分","补区域原档、劳动者、女性、殖民主体、环境和图版核验","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","A","royal_manufactories_guilds_workshops_and_specialisation","王室制造厂、行会、小作坊、师徒与商人中介展示前工业知识和专业分工","法国案例不能代表全部前工业生产且质量判断偏精英对象","补家庭生产、地方行业、女性和非欧洲作坊史","ACCEPTED_WITH_LIMITS"),
            ("1.2","A","mechanisation_transport_interchangeability_and_market_scale","蒸汽、新工艺、交通、国家合同和互换零件共同改变生产与市场尺度","机器不是充分原因且美国体系起源叙述需较新研究校正","补设备、采购、资本、劳动、民用扩散和区域比较","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.3","A","models_catalogues_moulds_specs_and_division_of_labour","模型、图录、模具、标准形状、规格与分工使构思、监督和制作逐渐分化","分离并非一次完成且不能把企业主或设计师写成唯一作者","补图样、工序、职位、工资、订单和冲突档案","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.4","A","porcelain_textile_iron_glass_and_material_systems","瓷器、纺织、铸铁、玻璃等材料工艺与市场共同限制和扩展形式","原料来源、殖民供应链、环境与劳动处理不均","补材料检测、贸易、生态、劳动和对象复原","ACCEPTED_WITH_MATERIAL_CHAIN_FOLLOWUP"),
            ("1.5","A","craftspeople_artists_manufacturers_merchants_and_consumers","工匠、艺术家、企业家、商人中介和消费者共同参与产品形成","名家与企业案例仍占优势且具体责任不能由通史确定","逐对象补设计、制作、管理、营销和使用责任链","ACCEPTED_WITH_AUTHORSHIP_FOLLOWUP"),
            ("1.6","A","design_craft_industrial_and_professional_distinctions","设计与艺术、工艺、制作、企业和职业角色的区分可作为概念史框架","导论定义是2010年的回顾性分析，不能倒投早期术语","补同期词典、职位、学校、协会、企业和争论文本","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("1.7","B","france_britain_us_and_mixed_paths_comparison","法国王室／行会、英国企业市场和美国制造体系提供区域路径比较","三分对照过整齐且不能代表亚洲、殖民地和内部差异","与B0130、B0086、B0169、B0259、B0334及区域史对读","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.1","A","great_exhibition_industry_empire_and_public_viewing","1851年博览会把商品、机器、帝国资源、国家竞争和公众观看汇聚为设计问题","通史不能独立证明观众接受、殖民对象来源和评审效应","补展览目录、评审、对象、媒体、观众和来源地档案","ACCEPTED_WITH_EXHIBITION_FOLLOWUP"),
            ("2.2","A","cole_reform_museum_school_and_state_governance","Cole体系、学校、博物馆、出版与国家政策把产品审美变成制度治理","政策与机构成立不证明教学、工业采用或质量改善","补官方政策、预算、课程、学生作品、企业与就业记录","ACCEPTED_WITH_INSTITUTIONAL_FOLLOWUP"),
            ("2.3","A","ruskin_morris_arts_crafts_and_market_contradiction","工艺美术劳动伦理与高价手工商品、企业市场之间存在可追踪张力","通史概括不能替代参与者文本、公司账簿和工人经验","与B0318、B0090、B0091及企业劳动档案互证","ACCEPTED_AS_SYNTHESIS"),
            ("2.4","A","catalogues_shops_advertising_and_active_consumers","目录、商店、广告、商品差异与消费者意义共同组织现代消费","供给与营销不能证明购买、认同或实际使用","补价格、销售、家庭清单、消费者叙述与使用痕迹","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.5","B","aesthetic_art_nouveau_interiors_graphics_and_lifestyle","唯美主义、新艺术及跨媒介室内可用来讨论设计与生活方式的整体关系","风格综述和缺图状态不足以支持逐件视觉因果判断","补对象、图版、室内、委托、生产和使用材料","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.6","B","exhibition_empire_resources_and_colonial_order","博览会和纪念物把帝国资源、国家繁荣与视觉秩序联系起来","殖民生产者、征集强制、分类权力和观众回应不足","补殖民档案、来源社群、贸易、对象与观众材料","ACCEPTED_WITH_COLONIAL_FOLLOWUP"),
            ("2.7","B","trade_patterns_japonisme_and_local_selection","材料、图案、商品与观念跨境移动并在市场和地方实践中被选择重组","通史容易以欧洲接受端替代来源地行动者且相似不等于影响","补贸易、人员、委托、制作、评论与地方回应链","ACCEPTED_WITH_TRANSFER_FOLLOWUP"),
        ],
    },
}


VERSION_ROWS = [
    {
        "version_group": "VGRP004-TRANSLATION",
        "intellectual_work": "David Raizman, History of Modern Design, 2010 Second Edition",
        "canonical_source_id": "B0101",
        "alias_source_id": "B0478",
        "relationship": "2010英文第二版与2013中国人民大学出版社中文第二版译本；语言、版式和OCR不同",
        "counting_rule": "相同章节与命题只计一个独立书目实体；逐字引文分别按英文版或中译本核页",
        "verification_note": "两者题名页均指向2010第二版内容；B0478版权页为2013年中文第2版，尚待逐章差异审计",
    },
    {
        "version_group": "VGRP005-EDITION",
        "intellectual_work": "David Raizman, History of Modern Design, 2010 Second Edition / 2023 Revised Edition",
        "canonical_source_id": "B0102",
        "alias_source_id": "B0101",
        "relationship": "2023修订版继承并更新2010第二版；不是独立著作，也不是完全相同文本",
        "counting_rule": "未变命题只计一次；2023新增或实质修订内容须标明版次后单独计证",
        "verification_note": "2023版权页列2003初版、2010第二版、2023本版；目录新增Global Inspiration等内容，尚待逐章版本差异审计",
    },
]


def update_manifest() -> None:
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


def update_versions() -> None:
    path = ROOT / "01_语料清单" / "版本关系组_人工复核.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fields = list(rows[0])
    replace = {row["version_group"] for row in VERSION_ROWS}
    rows = [row for row in rows if row["version_group"] not in replace]
    rows.extend(VERSION_ROWS)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    assets = load_assets()
    for source_id, data in DATA.items():
        write_source(source_id, data, assets[source_id])
    update_manifest()
    update_versions()
    print(json.dumps({"completed": list(DATA), "mapping_rows": sum(len(x["maps"]) for x in DATA.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
