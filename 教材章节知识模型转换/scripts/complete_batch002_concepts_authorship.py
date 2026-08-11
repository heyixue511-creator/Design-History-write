#!/usr/bin/env python3
"""Complete the concepts, production-process, and authorship group in BATCH-002."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-002-CH01-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0225": {
        "title": "Industrial Design",
        "author": "John Heskett",
        "version": "Oxford University Press, 1980（本数字文本题名页；英国版同年由Thames & Hudson出版）",
        "type": "工业设计通史与设计史方法论专著",
        "scope": "约18世纪至1970年代，重点为英国、欧洲大陆与美国",
        "duplicate_group": "VGRP003-PARTIAL",
        "summary": "Heskett把工业设计的生成解释为构思与制作逐渐分离，并用工场、图案书、皇家制造厂、Boulton、Wedgwood、机械交通、美国制造体系、标准化与职业设计等案例展开。它能为第一章提供‘生产组织—形式—市场—使用’的结构骨架，也能校正机器自动产生设计和Whitney单人发明美国体系的神话。但其构思／制作二分、个体创造力权重和1980年的欧美案例范围都须用劳动史、殖民供应链、女性与匿名工匠材料修正。",
        "strengths": [
            "明确反对线性手工到机器叙事，并把商业化、分工、市场和制度置于机械化之前。",
            "以Boulton与Wedgwood展示图案、模型、制模、目录、手工精整和批量生产之间的组织关系。",
            "把可互换零件解释为多人、多机构和长期改进，不沿用Whitney唯一发明者神话。",
            "区分生产者构想与对象在实际使用中的价值，反对只看形式的博物馆式设计史。",
        ],
        "limits": [
            "‘构思与制作分离’是强有力的分析模型，但可能把前工业协作压缩成单人手工统一体。",
            "案例集中欧美且形成于1980年，女性、殖民原料、被奴役劳动、环境和非西方制造史不足。",
            "个人创造力主要决定审美／象征功能的二分过整齐，需要集体作者制与接受史修正。",
            "武器制造只可用于制度、标准化和国家采购的文字分析，不采用或再现武器图像。",
            "与B0084文选中的阅读材料8存在局部重印；重合部分不得算作独立互证。",
        ],
        "checks": [
            "clean第20—42行：非线性工业化、构思／制作分离、形式主义与社会决定论的双重批评。",
            "clean第61—83行：图案书、Gobelins、Meissen与匿名工匠构成工业设计的前工业分工史。",
            "clean第99—151行：Soho与Etruria中的市场、样式、模型、精整、目录、制模和专业人员链。",
            "clean第162—180行：机械化、家庭劳动、小工场与大企业长期并存，设计改革并非单一答案。",
            "clean第494—520行：欧洲先例、Whitney局限、Hall等人和政府需求共同形成美国体系。",
            "clean第537—565、737—749行：标准化向民用产品扩散，同时将工人技能、判断和节奏纳入机器系统。",
        ],
        "maps": [
            ("0.3","A","integrated_design_history_method","设计史须把形式同生产组织、材料制度、市场和实际使用结合，而不能只排名名作","作者仍在形式主义与个体创造力框架内工作且案例老化","与劳动史、企业档案、非西方区域史和使用史互证","ACCEPTED_AS_METHOD"),
            ("0.6","A","museum_formalism_and_context_bias","脱离生产和使用语境的博物馆陈列会把对象建构成自主形式并遮蔽匿名协作","批判方法本身并未充分恢复女性殖民与被奴役劳动者","补来源、劳动、使用、征集和沉默主体材料","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","A","patterns_workshops_and_commercial_craft","图案书、大工场、皇家制造厂和商业化手工生产已使构思、模型与制作发生分工","不能把所有前工业生产都写成单人工匠或同一欧洲模式","补行会、家庭、作坊、地方材料和非欧洲比较","ACCEPTED_WITH_LIMITS"),
            ("1.2","A","machines_interchangeability_transport_and_scale","动力、机床、可互换零件、铁路和装配线改变生产尺度与对象组织","武器制度前史仅作文字分析且机器并非充分原因","补设备、性能、国家采购、劳动与民用扩散档案","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.3","A","patterns_models_specs_and_control","图案书、原型、模具、规格、工序分解和监督把形式控制从执行工人转移到多类岗位","分离不是瞬时完成也不等于设计师已成为唯一作者","补图样、模具、工序签记、职位、工资和争议档案","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.4","B","materials_process_and_form_constraints","陶瓷、金属、木材、玻璃与新交通材料的性能和加工方式限制形式并允许新组合","材料链和殖民来源处理不足且部分视觉判断待图版核验","补材料检测、供应链、环境与对象复原","ACCEPTED_AS_SUPPORT"),
            ("1.5","A","anonymous_designers_workers_and_enterprise","Boulton与Wedgwood案例显示企业主、外部艺术家、制图员、模型师、工匠和销售网络共同参与","资料仍偏企业主且不能为每件对象确定责任","逐对象补设计、制作、管理、销售和使用责任链","ACCEPTED_WITH_LIMITS"),
            ("1.6","A","industrial_design_definition_and_professional_emergence","工业设计概念可追踪构思、视觉形式、机械复制和专业岗位逐步组合的过程","1980年的操作性定义不是跨时期中性词义","补同期词典、industrial art、decorative art、职位、学校和行业组织","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("1.7","A","diversification_and_mixed_production","工业化表现为手工、外包、工场、工厂和机器生产持续分化与共存","欧美通史不足以代表亚洲殖民地和全球区域路径","与B0086、B0130、B0169及区域史比较","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.1","B","great_exhibition_and_manufacturing_comparison","1851年博览会使跨国制造比较和设计质量问题进入公共讨论","本书不是博览会观众、殖民陈列或展览制度专史","补展览目录、评审、对象、参观者和殖民来源材料","ACCEPTED_AS_SUPPORT"),
            ("2.2","B","design_reform_magazine_school_and_state","Cole、设计改革出版物、学校和国家机构把工业产品审美转为治理问题","政策主张不能证明课程执行或产品质量改善","补行政、课程、学生作业、企业采用与就业记录","ACCEPTED_AS_SUPPORT"),
            ("2.4","A","catalogues_mass_markets_and_aesthetic_choice","目录、邮购、产品变体和市场细分使外观成为组织大众消费的重要变量","目录供给不能自动证明消费者偏好或实际使用","补价格、订单、退货、家庭清单和消费者材料","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.7","B","patterns_migration_and_crossnational_manufacturing","图案、工匠、技术与制造模式跨境移动并被不同制度和市场重组","通史叙述不足以证明具体对象的直接影响关系","逐对象补接触、委托、制作、销售和地方回应链","ACCEPTED_AS_SUPPORT"),
        ],
    },
    "B0084": {
        "title": "A John Heskett Reader: Design, History, Economics",
        "author": "John Heskett；Clive Dilnot编",
        "version": "Bloomsbury Academic, 2016",
        "type": "设计史、设计经济学与设计政策文选",
        "scope": "Heskett约四十年文本，涵盖前工业制造、工业化、企业与国家设计政策",
        "duplicate_group": "VGRP003-PARTIAL",
        "summary": "Dilnot编选的文集把Heskett的设计史、经济学与政策写作并置，最重要的第一章资源是生产方式‘层叠’模型、前工业全球制造片段、生产／使用语境区分和设计作为人类能力的定义。阅读材料8重印自B0225《Industrial Design》的美国体系章节，因此该部分只能用于版文互校；文集中其余未刊书稿、晚期方法论与经济学文本仍构成独立材料。",
        "strengths": [
            "以层叠而非替代解释乡村手工、城市手工、前工业、蒸汽、电力和电子生产方式的共存。",
            "连接历史、生产语境、使用语境、经济价值和制度能力，避免把设计缩成风格。",
            "收录未刊全球制造史片段，主动纳入游牧者、商人和被奴役工匠等常被忽略主体。",
            "编者导论和分部导言公开选文过程、缺失文本与纪念性项目的批评限度。",
        ],
        "limits": [
            "文集是纪念性选本，编者承认批判距离不足；选文不能代表Heskett全部写作。",
            "若干全球制造史文本是未完成书稿，论证、引注和地区覆盖不能按正式专著同等使用。",
            "亚洲和中国材料主要依赖有限的二手来源与博物馆观察，不能替代本地研究。",
            "设计作为普遍人类能力的定义若无限外推，会稀释现代设计职业与制度的历史特异性。",
            "阅读材料8与B0225第三章局部重印，不能作为第二个独立来源计证。",
        ],
        "checks": [
            "clean第279—303行：编者说明选文标准、遗漏、未刊稿及快速编纂条件。",
            "clean第347—370、391—420行：设计定义与工业化的商业／文化张力。",
            "clean第541—585行：对Ruskin、Morris和工业化解放／去技能的双向判断。",
            "clean第839—911行：设计史层叠模型反对艺术史式线性替代。",
            "clean第925—1005、1073—1190行：未刊全球制造史的范围、贸易、游牧和被奴役工艺片段。",
            "clean第1259—1315行：美国体系章节与B0225相应章节重合，Whitney神话、民用扩散与Taylor劳动控制均属同一原文。",
        ],
        "maps": [
            ("0.2","A","layered_nonlinear_periodisation","设计史分期应把生产方式看作累积层叠而非新方式完全替代旧方式","六层模型是分析工具且可能过度整齐","以区域案例检验各层的起止、重叠与权力关系","ACCEPTED_AS_METHOD"),
            ("0.3","A","history_economics_policy_and_context","设计史可贯通生产、使用、经济价值与制度政策而不只描述形式","文集跨时期跨文类并置不能自动组成统一因果理论","逐篇注明文类、日期、原出处和论证层级","ACCEPTED_AS_METHOD"),
            ("0.6","A","editorial_selection_unfinished_text_and_regional_bias","文选取舍、未刊稿状态、纪念性目的和区域材料不均必须进入证据审计","编者自陈局限不等于已修复这些偏差","补未收文本、原出处、本地研究和反方评论","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","B","global_history_of_making_fragments","游牧贸易奴役和多种制造层次可扩展全球设计史问题范围","未刊片段不构成完整全球史且地区证据不对称","回原引注并补非西方专史和主体材料","ACCEPTED_WITH_VERIFICATION_GAP"),
            ("1.1","A","layered_preindustrial_making_and_knowledge","家庭作坊贸易与多种制造方式共同保存和重组分布式知识","普遍设计能力不能抹去技能制度和劳动不平等","补训练、工具、合同、家庭与工匠主体材料","ACCEPTED_WITH_LIMITS"),
            ("1.2","B","industrial_layers_and_mass_production","蒸汽电力与大规模生产叠加于既有方式并改变规模和组织","美国体系材料与B0225重印不算独立互证","该部分仅作版文互校；另补机器、工厂和劳动原档","PARTIAL_DUPLICATE_SUPPORT_ONLY"),
            ("1.3","A","production_use_context_and_coordination","设计须桥接生产约束与使用需求并协调多种专门活动","抽象桥接模型不能替代具体图样规格和车间权力证据","补图样、职位、评审、工序与使用反馈","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.4","B","material_technology_and_layered_form","材料与技术在不同生产层次中被反复再利用并形成不同形式","文集不是棉陶瓷金属等材料专史","与B0154、B0169及材料环境史互证","ACCEPTED_AS_SUPPORT"),
            ("1.5","A","design_as_distributed_human_capacity","设计能力分布于工匠、企业、组织和使用者而非职业名家独占","普遍能力命题不能自动确定对象作者或责任","逐对象补构思制作管理销售使用责任链","ACCEPTED_WITH_LIMITS"),
            ("1.6","A","design_definition_value_and_profession","设计可同时作为人类能力、专业活动和经济制度角色分析","三个层级不得混写成同一跨历史词义","补同期词源、职位、学校、协会和企业制度材料","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("1.7","A","coexisting_global_production_layers","不同地区的手工前工业与工业方式长期共存且非同步组合","全球材料仍偏薄且层叠不等于关系平等","与区域劳动史、殖民史和企业史交叉验证","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.7","B","trade_migration_and_local_reconfiguration","贸易、工匠迁移与制度学习使造物方式跨境重组而非简单扩散","未刊片段及日本中国综述不足以证明具体地方接受","补对象贸易、人员、机构和使用者材料","ACCEPTED_AS_SUPPORT"),
        ],
    },
    "B0097": {
        "title": "Printing Types: Their History, Forms, and Use",
        "author": "Daniel Berkeley Updike",
        "version": "第二卷数字文本，原著1922年；当前文件错序、重复且图版缺失",
        "type": "印刷实践者字体史、书籍史与印刷劳动制度史",
        "scope": "现存文件主要为第二卷第15—24章，约1500—1922年的欧美字体与印刷",
        "duplicate_group": None,
        "summary": "Updike以字体标本、印本、书信、铸字厂资料、法规和实践判断书写字体史，并在末章把字体选择、铸字、排印、学徒、工资、罢工、审查和企业条件连接起来。它能补第一章的冲模—字模—铸字—排字—印刷分工，以及第二章的Morris与字体复兴；但当前clean文件开头即处于正文中段，第二卷随后多次重复，367幅图版未保留。因此所有视觉形式判断排除，文字制度线索只作V2路由。",
        "strengths": [
            "把字体从纯形式对象还原为字冲、字模、铸字厂、印刷所、市场、法规和跨国工匠网络。",
            "末章保留学徒、劳资冲突、工资、工时、外国工人和审查制度等生产条件。",
            "作为Merrymount Press经营者，作者能说明字体选择与实际排印、成本和书籍用途的关系。",
            "对复兴持批判态度，指出复兴常以对旧字体缺点的无知替换对当下字体的不满。",
        ],
        "limits": [
            "clean文本严重错序并至少包含多段重复，不能据其行号推定原书连续页序。",
            "367幅图版与原始字体样张在当前资产中不可见，全部视觉比较和可读性判断不准入。",
            "当前资产实质为第二卷，不能用整体报告关于两卷全史的陈述冒充已读第一卷。",
            "作者的旧体偏好、实践者利益、民族传统用语和1922年的欧美中心视角必须历史化。",
            "末章最后把改善寄托于少数有判断力的个人，与其揭示的劳资、法规和资本结构存在张力。",
        ],
        "checks": [
            "clean第1行即从Stereotype Office规则及正文中段开始；第2343行后才出现第二卷题名页，第7069、12034行附近又出现结束与索引，证明错序重复。",
            "clean第2629—2670、2960—3013行：字冲、字模、铸字与跨境采购展示字体生产和所有权网络。",
            "clean第4183—4202行：印刷与铸字逐渐分离，政治限制与进口变化影响行业组织。",
            "clean第5989—6079行：Updike以参与者立场评价Morris、私人出版社、工人理想和书籍整体效果。",
            "clean第6477—6701行：排字房字体选择与印刷商教育属于作者的当代规范主张。",
            "clean第6788—6865行：分工、学徒、人数控制、低薪与罢工形成制度冲突。",
            "clean第6948—7018行：外国工人、工资仲裁、审查、工时与女性行业记录构成劳动和国家权力线索。",
            "clean第7033—7055行：作者最终把高质量归于少数印刷商的学问与意志，须同前述结构证据对读。",
        ],
        "maps": [
            ("0.4","X","missing_visual_type_specimens","当前文件不能验证字体造型、版面、可读性或图版并置所支持的视觉判断","367幅图版缺失且正文错序重复","返回完整扫描本和实际图版后重新做对象核验","EXCLUDE_VISUAL_CLAIMS"),
            ("0.5","B","specimens_letters_law_and_books_as_sources","字体标本、印本、书信、铸字档案与法规可构成多类印刷史证据","当前转换损坏且图版缺失所以仅作来源路由","回完整版次、签名本、图版与档案原件","ACCEPTED_WITH_VERIFICATION_GAP"),
            ("0.6","A","practitioner_preference_national_and_corpus_bias","实践者偏好、民族传统框架、欧美范围和文件残缺会系统影响叙事","识别偏差不能自动决定哪些字体判断错误","补较新字体史、非拉丁传统、劳动史和完整图版","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","B","apprenticeship_typefounding_and_printshop_knowledge","字冲字模铸字排字与印刷的技能通过学徒、工场和跨境工匠流动传递","材料集中欧洲印刷业且末章以法国为主","补合同、工具、作坊账簿和其他地区印刷史","ACCEPTED_AS_SUPPORT"),
            ("1.3","A","punch_matrix_type_composition_and_supervision","字体从字冲、字模、铸造到排字印刷的工序分离会重组形式决策、所有权和监督","缺失图版使具体字形责任和视觉后果不可核","补字体样张、订单、铸造记录、版面和工序签记","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.5","A","distributed_typographic_authorship","字冲雕刻者、铸字商、印刷商、出版者、排字工和复兴者共同塑造字体与书籍","Updike常把品质重新集中到少数大师和印刷商判断","补普通工人、女性、企业账目、客户和读者材料","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("1.6","A","printer_typefounder_designer_and_professional_identity","印刷商、铸字商、工匠、艺术家和专业人士的自我定义可补设计职业分化前史","作者的professional优于trade是1922年规范立场而非中性演进","补行业组织、职业统计、教育和同时代反方文本","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("1.7","B","crossnational_type_trade_and_regulation","字体、字模、工匠与印刷规范在荷英法西美之间移动并受国家制度重组","范围不含全球主要非拉丁印刷传统","补东亚、南亚、伊斯兰和殖民印刷区域史","ACCEPTED_AS_SUPPORT"),
            ("2.3","B","morris_printing_and_labor_ideal_as_participant_history","Updike对Morris印刷与劳动理想的评价可作为1922年实践者解释和复兴史线索","不是Morris劳动实践、读者接受或社会主义成效的一手证明","回Kelmscott印本、账簿、工人材料和Morris原文","ACCEPTED_AS_HISTORIOGRAPHY"),
            ("2.5","B","type_reviving_book_unity_and_private_press","Caslon、Fell与私人出版社复兴说明字体、版式、装饰和出版共同构成整体书籍设计","缺图使具体视觉效果与可读性不可验证","补完整图版、原印本、成本、发行和读者材料","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("2.7","B","type_matrices_printers_and_revival_across_borders","字模、工匠、字体复兴和出版模式的跨境流动包含选择、修改与制度采用","不能以民族风格词汇或形式相似直接证明影响","补交易、书信、人员迁移、样张和地方接受","ACCEPTED_AS_SUPPORT"),
        ],
    },
    "B0031": {
        "title": "American Design Ethic: A History of Industrial Design to 1940",
        "author": "Arthur J. Pulos",
        "version": "MIT Press, 1983；平装版1986",
        "type": "美国工业设计通史与职业史专著",
        "scope": "1607—1940年的美国殖民地、共和国、工业化与职业工业设计",
        "duplicate_group": None,
        "summary": "Pulos以专利、广告、展览、学校、企业、产品和设计师材料构造美国工业设计长史，能为美国制造体系、设计专利、教育机构、商业艺术和职业化提供线索。但他的‘美国设计伦理’把清教、自由企业、民主和功能主义连成国家本质，并以‘荒野’和建国设计神话组织叙事。教材只吸收可核的制度和对象链，把国家本质论降为1983年史学对象，并用原住民史、奴隶制、性别劳动、移民、帝国扩张和较新技术史校正。",
        "strengths": [
            "提供专利法、设计专利、学校、博览会、行业倡议和商业艺术转入产品设计的长时段入口。",
            "大量调用同期广告、政府报告、目录、书信、专利和企业材料，便于进一步回溯P0。",
            "把职业工业设计置于生产、分销、市场、博物馆和教育机构交汇处。",
            "保留流线型、消费工程和职业责任之间的张力，可用于1930年代设计职业史。",
        ],
        "limits": [
            "‘美国设计伦理’与‘美国是第一个被设计的国家’是目的论和国家例外论命题，不作因果模型。",
            "殖民叙事以定居者为主体，使用‘荒野’及对原住民的敌对表述，弱化土地占有与殖民暴力。",
            "奴隶制、种族与性别只零散出现；‘缝纫机解放妇女’等语句把技术意图、市场修辞和实际效果混写。",
            "把美国制造体系归功于Whitney的谱系受到B0225／B0084自身所引研究的直接校正。",
            "作者曾任IDSA主席，职业奠基和伦理叙事具有参与者利益与自我合法化风险。",
            "武器对象只作制度、专利和标准化的文字分析，不采用武器图像。",
        ],
        "checks": [
            "clean第30—45行：作者明确提出‘America did not just happen; it was designed’及清教—自由企业设计伦理。",
            "clean第67—75、132—175行：殖民者中心、原住民威胁、奴隶制、性别化家庭劳动与功能主义被并置。",
            "clean第884—940行：棉轧机、奴隶制复兴、Whitney军工和美国体系被组织为英雄谱系。",
            "clean第1492—1515行：1842年设计专利及形式／效用法律区分提供制度线索。",
            "clean第1616—1653行：设计教育与女性课程材料同时带有性别本质主义表述。",
            "clean第1739—1755行：缝纫机的家庭、工厂、女性就业与营销被作者概括为‘解放’，实际效果须另证。",
            "clean第23—26行及第270页后：商业艺术、Art Moderne、1925与1929展览、职业工业设计构成后续职业化叙事。",
        ],
        "maps": [
            ("0.3","B","national_design_history_as_historiographic_object","国家设计史应检查制度产品与叙事如何共同建构所谓国家伦理","本书的美国例外论不能作为中性解释框架","与殖民史、原住民史、奴隶制、移民史和跨国研究对读","ACCEPTED_AS_HISTORIOGRAPHY"),
            ("0.6","A","settler_professional_gender_and_racial_bias","定居者中心、职业领袖、男性发明家和功能主义谱系会压低被殖民者、奴隶、妇女与普通工人","识别偏差不能以缺席代替主体证据","补原住民、非裔、女性、移民、工人和消费者材料","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","B","colonial_craft_household_and_apprenticeship","殖民地家庭劳动、作坊、学徒和工具改良可补前工业知识与地方适应","不得把殖民地写成空白荒野或把定居者经验代表全部美国","补原住民技术、奴隶工艺、女性与地方贸易材料","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.2","A","patents_interchangeability_state_contracts_and_scale","专利、国家合同、机床、可互换零件和运输网络共同改变美国生产尺度","Whitney唯一奠基人叙事不成立且军工仅作文字制度分析","与B0225、B0084及较新技术史、军械厂档案互证","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("1.3","A","design_patents_specs_and_form_utility_split","1842年设计专利及形式／效用法律区分显示外观、规格和权利被制度化","专利数量和法律分类不证明设计质量或实际执行","补专利图、诉讼、企业设计流程和对象生产链","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.4","B","wood_metal_glass_textile_and_machine_materials","材料替代与加工技术影响殖民工具、压制玻璃、金属器和机器产品形式","供应链、环境代价和被强制劳动处理不足","补材料检测、贸易、环境和劳动史","ACCEPTED_AS_SUPPORT"),
            ("1.5","A","craftsmen_engineers_artists_business_and_profession","工匠、工程师、商业艺术家、制造商、博物馆与顾问设计师共同形成工业设计岗位","职业谱系偏向名人且参与者自我合法化明显","补企业档案、匿名员工、工会、客户与失败项目","ACCEPTED_WITH_LIMITS"),
            ("1.6","A","industrial_arts_commercial_art_and_industrial_design","industrial arts、commercial art与industrial design的组织、教育和职业变化可构成概念史线索","作者的成熟职业结局不能倒推早期术语都指向工业设计","补同期词典、课程、职位、协会章程和统计","ACCEPTED_WITH_CONCEPT_HISTORY_FOLLOWUP"),
            ("1.7","X","american_design_ethic_as_national_essence","不接受清教伦理加自由企业自然生成美国功能主义和工业设计的国家本质论","该模型压低殖民暴力、奴隶制、移民、国家采购和跨国技术且目的论明显","将其作为1983年史学对象并用多路径研究替代","EXCLUDE_AS_CAUSAL_MODEL"),
            ("2.1","B","exhibitions_and_public_design_problem","博览会、博物馆展览与政府报告推动工业艺术和职业设计成为公共问题","展览冲击叙事不能证明全国同步接受或直接职业因果","补展览档案、参展物、媒体、观众和地方机构材料","ACCEPTED_AS_SUPPORT"),
            ("2.2","A","schools_museums_policy_and_industry_organizations","技工学校、设计学校、博物馆、职业教育政策和行业组织构建设计制度化网络","课程存在不等于教学成效且女性教育受性别分工限制","补官方政策、课程、学生作业、师资、就业和组织章程","ACCEPTED_WITH_INSTITUTIONAL_FOLLOWUP"),
            ("2.4","B","advertising_distribution_and_consumer_engineering","广告、邮购、百货、包装和消费工程使设计服务于市场组织","销售主张不能证明消费者被动接受或产品改善","补价格、销售、退货、家庭使用和消费者组织材料","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6","C","national_exhibition_and_colonial_absence","美国国家展览叙事可用于审查哪些主体和地区被纳入工业艺术公共形象","本书不足以写殖民分类且自身弱化原住民和种族问题","仅作史学批评并补殖民展览与来源社群材料","CONTEXT_ONLY"),
            ("2.7","C","europe_us_imitation_and_translation","欧美风格、展览、移民与技术往来说明美国设计并非封闭本土生成","叙事仍以欧美双边为主且模仿不等于地方意义完成转译","补人员、对象、贸易、机构和使用链","CONTEXT_ONLY"),
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
        "report_structure": {"review_basis": "overall_and_relevant_chapter_reports_plus_emergence_gap_audit"},
        "candidate_sections": [{"section_id": m[0], "grade": m[1], "verification": "V2", "role": m[2]} for m in data["maps"]],
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
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |",
        f"| 版本关系 | {data['duplicate_group'] or '未发现重复组'} |",
        f"| 分析资产 | {asset['report_file_count']}个文件，{asset['report_characters']}字符 |",
        "| 核验 | V2：报告复核＋clean关键段落局部回查 |", "", "## 二、核心命题与教材价值", "", data["summary"],
        "", "## 三、论证强项", "",
    ]
    md.extend(f"- {x}" for x in data["strengths"])
    md.extend(["", "## 四、限度与反例", ""])
    md.extend(f"- {x}" for x in data["limits"])
    md.extend(["", "## 五、章节准入", "", "| 章／节 | 等级 | 角色 | 可接受命题 | 边界 | 状态 |", "|---|---|---|---|---|---|"])
    for section, grade, role, claim, boundary, _follow, status in data["maps"]:
        md.append(f"| {section} | {grade} / V2 | {role} | {claim} | {boundary} | {status} |")
    md.extend(["", "## 六、clean原文局部回查", ""])
    md.extend(f"- {x}" for x in data["checks"])
    md.extend(["", "本卡不把P4分析报告或知识涌现命名升级为原著事实。正式引用须返回实际版次、页码、上下文、图版及关键P0材料。", ""])
    (card_dir / f"{source_id}_来源卡.md").write_text("\n".join(md), encoding="utf-8")

    fields = ["source_id","section_id","grade","verification","role","accepted_claim","evidence_boundary","original_followup","status"]
    with (map_dir / f"{source_id}_章节映射.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for section, grade, role, claim, boundary, follow, status in data["maps"]:
            writer.writerow(dict(source_id=source_id, section_id=section, grade=grade, verification="V2", role=role, accepted_claim=claim, evidence_boundary=boundary, original_followup=follow, status=status))


def update_manifest():
    path = BATCH / "batch_manifest.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle)); fields = list(rows[0])
    for row in rows:
        if row["source_id"] in DATA:
            row["semantic_review_status"] = "complete"
            row["mapping_status"] = "complete"
            row["original_verification_status"] = "partial_clean_text_spot_check"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(rows)


def main():
    assets = load_assets()
    for source_id, data in DATA.items():
        write_source(source_id, data, assets[source_id])
    update_manifest()
    print(json.dumps({"completed": list(DATA), "mapping_rows": sum(len(x["maps"]) for x in DATA.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
