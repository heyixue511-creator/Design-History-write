#!/usr/bin/env python3
"""Complete the CH01 regional-comparison group in BATCH-002."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-002-CH01-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0130": {
        "title": "Ottoman Manufacturing in the Age of the Industrial Revolution",
        "author": "Donald Quataert",
        "version": "Cambridge University Press, 1993",
        "type": "奥斯曼制造业、劳动史与区域经济史专著",
        "scope": "奥斯曼帝国1800—1914年，以纺织、丝和地毯为主",
        "summary": "Quataert反对把行会或出口市场的衰落等同于制造业整体消失。他把乡村家庭、非行会城市作坊、外放制、机械工厂、女性与儿童劳动以及国内市场同时纳入，证明不同地区和部门出现衰退、适应、重组与增长的混合轨迹。该书对第一章最重要的作用，是将英国工厂中心叙事置于区域比较中；但其低工资解释不能被美化为地方韧性。",
        "strengths": [
            "区分绝对产量、相对全球地位、出口市场和国内市场，避免单一‘衰落’指标。",
            "以英国领事报告、奥斯曼档案、行业数据和区域比较恢复家庭与作坊生产。",
            "把进口机纺纱、合成染料、地方织造和机械工厂的共存写成具体重组机制。",
        ],
        "limits": [
            "领事报告是外部观察者材料，且量化口径不稳；1914高于1800的总量判断仍需核计算链。",
            "制造业存续部分依赖女性、儿童和极低工资，不能用‘活力’遮蔽劳动代价。",
            "巴勒斯坦、阿拉伯半岛、埃及及资本积累问题覆盖不足。",
            "本书不是纹样作者、设计职业或消费者接受史，相关外推须降级。",
        ],
        "checks": [
            "clean第85—114行：作者提出衰退、适应、重组并要求计入乡村、家庭和非行会生产。",
            "clean第319—387行：区分绝对产量增长与相对全球地位下降。",
            "clean第563—694行：进口机纱、女性儿童劳动、外放网络与手纺的区域差异。",
            "clean第1394—1433行：织造、印花、刺绣的性别与城乡组织并不遵循单一模式。",
        ],
        "maps": [
            ("0.3","A","decline_paradigm_and_bottom_up_manufacturing_history","制造业史须分别检查家庭作坊行会工厂国内市场和出口而不能用工厂或行会单一指标判断衰落","作者的修正主义结论仍受领事档案和统计口径限制","回奥斯曼档案、地区数据及反方去工业化研究","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("0.6","B","women_children_and_consular_archive_bias","女性儿童乡村家庭和非行会劳动是制造业结构性组成且易被城市与工厂档案遮蔽","领事报告仍以外部管理和商业视角记录劳动者","补女性主体材料、工资、家庭账簿与地方档案","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("1.1","A","household_workshop_and_putting_out_knowledge","家庭作坊外放制和城乡联系可长期承载纺织技能与市场生产","不能把存续自动解释为自由自主或技术不变","补工具、工序、学徒、家庭与劳动合同材料","ACCEPTED_WITH_LIMITS"),
            ("1.2","A","hand_machine_imported_yarn_and_scale","手纺进口机纱地方织造和机械工厂按地区与市场条件并存并改变生产尺度","本书不提供统一机器性能比较且部分数据估算不稳","补机器、动力、产量、成本和质量记录","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.3","B","putting_out_and_gendered_division_of_labor","商人外放网络、家庭劳动和城市作坊重组工序与监督关系","不足以重建图样制模规格与设计指令权力","补图样、订单、监督、承包和工资档案","ACCEPTED_AS_SUPPORT"),
            ("1.4","A","cotton_yarn_dyes_and_material_substitution","原棉、进口纱、天然与合成染料及羊毛丝料的替代直接改变生产和产品类型","材料替代的具体形式效果仍需对象与技术分析","补纤维染料配方样品和供应链资料","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.5","B","distributed_actors_in_ottoman_manufacturing","家庭成员、商人、行会、工场、工厂主与国家共同组织制造","不能据此确定特定地毯或纺织品的作者与设计责任","逐对象补委托、样稿、生产和销售责任链","ACCEPTED_AS_SUPPORT"),
            ("1.7","A","ottoman_regional_mixed_production","奥斯曼各区域呈现家庭手工、外放制和机械生产的非同步混合路径","奥斯曼经验不能代表印度、中国或全部伊斯兰地区","与B0086、B0259、B0334及地方研究比较","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4","B","domestic_market_and_demand","国内市场和地区消费者需求可支撑制造业适应与产品调整","不是百货商店、广告、信用或普通消费者声音的专门史","补零售档案、价格、账本、广告和使用材料","ACCEPTED_AS_STRUCTURAL_SUPPORT"),
            ("2.7","A","imports_local_adaptation_and_regional_modernity","进口纱与染料、出口地毯需求和地方技能之间形成选择性重组而非简单替代","跨境适应可能以低工资和不平等贸易为条件","补样稿、买方规格、地方生产者与使用者材料","ACCEPTED_WITH_LABOR_LIMIT"),
        ],
    },
    "B0086": {
        "title": "Cloth in West African History",
        "author": "Colleen E. Kriger",
        "version": "AltaMira Press, 2006",
        "type": "西非纺织物质史、历史考古与技术史专著",
        "scope": "下尼日尔河及几内亚海岸，约公元前500年至20世纪末",
        "summary": "Kriger从纤维、捻向、织纹、幅宽、接缝、染料和磨损等对象特征出发，再同考古、语言、植物、口述、贸易文献与博物馆记录互证。她拒绝把纺织物当作可透明阅读的文本，也拒绝把进口材料与地方传统写成替代关系。垂直织机与脚踏织机、地方纤维与进口机纱、天然与合成染料长期并存，生产者和消费者会主动选择、仿制、拒绝和改造。",
        "strengths": [
            "把技术分析从鉴定提升为可检验历史论证，适合0.4史料实验。",
            "恢复女性、农村工匠和被奴役劳动者，但同时公开证据不完整。",
            "以消费者拒绝欧洲仿制布等案例证明地方市场不是被动终点。",
        ],
        "limits": [
            "地理主要限于今尼日利亚，不能以‘西非’标题外推整个区域。",
            "早期时段证据稀疏，若干织机、棉花与靛蓝起源判断明确属于推测。",
            "博物馆目录可能混淆制造地、使用地、取得地和收藏地。",
            "消费者偏好常经商人和殖民档案间接呈现，实际接受仍有缺口。",
        ],
        "checks": [
            "clean第165—214行：物质与视觉证据可校正文献，消费者和生产者作用须纳入。",
            "clean第249—357行：纤维、捻向、织纹与织机痕迹的技术证据；纺织物不是文本。",
            "clean第518—543行：垂直织机长时段追溯同时明确证据不足与推测。",
            "clean第740—769行：进口布经过地方选择，欧洲仿制因消费者辨识而失败。",
        ],
        "maps": [
            ("0.4","A","textile_object_as_multilayer_evidence","纤维捻向织纹幅宽接缝染层和磨损可提出生产贸易与使用问题","纺织物不是自足文本且对象归属与年代须互证","补对象检验、馆藏史、考古、口述和贸易记录","ACCEPTED_WITH_LIMITS"),
            ("0.5","A","triangulation_of_material_linguistic_and_archival_sources","技术分析可同考古语言植物口述和书面档案形成多链互证","不同证据尺度和不确定性不能被合并抹平","逐项记录证据类型、定位、置信和冲突","ACCEPTED_AS_METHOD"),
            ("0.6","A","museum_archive_and_silent_labor_bias","收藏与殖民档案会错置地点并压低女性乡村与被奴役劳动者的可见性","恢复缺席主体仍需主体证据不能只靠形式推断","补来源社群、劳动身份、征集史和地方档案","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","A","local_objects_and_global_networks","地方纺织对象可连接跨撒哈拉、大西洋、印度洋和化学工业网络","连接不等于单向传播或同质全球化","建立接触、选择、制作、交易和使用链","ACCEPTED_WITH_CAUSAL_LIMIT"),
            ("1.1","A","distributed_textile_knowledge","纺纱织造染色裁缝与刺绣知识分布在家庭、性别化工序、作坊和贸易网络中","性别分工并非固定且地区技术复合体差异显著","补工具、工序、训练、劳动和对象材料","ACCEPTED_WITH_LIMITS"),
            ("1.4","A","fiber_loom_dye_and_pattern_system","纤维、织机、纱线、染料与图案技术共同限定纺织形式","部分早期材料与染料证据只达推测层级","补材料检测、考古断代与技术复原","ACCEPTED_WITH_VERIFICATION_GAP"),
            ("1.5","B","anonymous_artisan_and_trade_network","生产者、裁缝、染工、商人和消费者共同改变纺织品而常未被署名","对象形式不能单独确定个人作者与动机","补订单、口述、作坊、交易与使用记录","ACCEPTED_AS_SUPPORT"),
            ("1.7","A","west_african_mixed_technical_trajectories","地方织机、进口布、工厂纱与新染料长期并存并被选择性重组","下尼日尔案例不能代表整个非洲","补其他西非区域、印度布来源和殖民政策比较","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4","B","consumer_choice_and_market_mediation","消费者对颜色材料与仿制质量的选择会改变商人订货和生产策略","商人记录不能完整代表普通消费者声音","补价格、交易、家庭与穿用材料","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6","B","colonial_collection_and_classification","殖民记录和博物馆目录如何命名地点族群与传统可作为分类史材料","不得把收藏标签当成中性制造地或族群发明证明","补征集记录、来源社群和对象技术证据","ACCEPTED_AS_CRITICAL_CONTEXT"),
            ("2.7","A","selection_refusal_imitation_and_reproduction","跨境纺织流动包含地方选择、拒绝、仿制、再织与材料替换","形式相似不能独立证明直接影响或文化意义一致","逐对象补贸易、样品、买方规格和地方使用","ACCEPTED_WITH_LIMITS"),
        ],
    },
    "B0259": {
        "title": "The Great Divergence",
        "author": "Kenneth Pomeranz",
        "version": "Princeton University Press, 2000",
        "type": "全球经济史与比较工业化研究专著",
        "scope": "约1500—1850年的西欧、中国、日本、印度及新大陆关系",
        "summary": "Pomeranz以互惠比较和核心区比较反对把欧洲道路预设为正常终点。他认为18世纪若干欧亚核心区共享市场化增长和生态约束，西欧的持续突破需要把煤炭与新大陆土地密集型资源、殖民制度和奴隶劳动放在一起解释。对第一章，该书提供能源、材料和区域非同步的宏观比较框架；它不能替代机器、作坊、图样与具体对象史。",
        "strengths": [
            "比较英格兰与江南等功能相近核心区，而非任意文明整体。",
            "把煤、新大陆资源、奴隶制、生态约束与制造业连接。",
            "明确把‘为什么英格兰没有成为江南’与反向问题同等提出。",
        ],
        "limits": [
            "1750年前中欧相似程度、生活水平和鬼田估算均存在持续争议。",
            "中国数据的代表性、国家能力及欧洲内部差异处理受到批评。",
            "宏观生态解释不能直接说明某项机器、形式或设计职业如何生成。",
            "知识涌现报告对论证网络的命名只作研究假设，不作为原著命题。",
        ],
        "checks": [
            "clean第124—150行：互惠比较、核心区比较和1750年前相似性。",
            "clean第173—186行：共同生态约束及化石燃料、新大陆资源造成的不连续。",
            "clean第246—315行：消费、殖民、奴隶制、土地密集资源与煤共同进入解释。",
            "clean第2590—2761行：奴隶制、新大陆资源与鬼田估算的机制和边界。",
        ],
        "maps": [
            ("0.2","A","nonsynchronous_modernization_and_comparison","全球分期不能把工业化设为各地区同时追求的单一终点","相似性和1750节点是争议性历史判断","补后续大分流争论与区域数据","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("0.3","A","reciprocal_core_region_comparison","互惠比较要求同时解释欧洲与亚洲为何偏离彼此而不预设欧洲正常路径","核心区选择本身仍可能制造代表性偏差","公开比较单位、指标、数据和反例","ACCEPTED_AS_METHOD"),
            ("0.6","B","aggregate_data_and_core_region_selection_bias","国家平均与核心区选择会产生相反叙事，统计口径和材料缺口须公开","不能用方法批评自动证明任一相似性结论","补区域微观数据和国家能力研究","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","A","reciprocal_and_encompassing_global_history","全球史须结合对称区域比较与跨区域资源关系","关系史不能消除殖民暴力或地方差异","与商品史、殖民档案和区域史互证","ACCEPTED_WITH_LIMITS"),
            ("1.1","B","shared_protoindustrial_growth","欧亚多个核心区在前工业市场化和原工业生产上存在可比发展","不证明技术、劳动制度或生活水平完全相同","补工序、家庭、工资和区域产业研究","ACCEPTED_AS_COMPARATIVE_CONTEXT"),
            ("1.2","A","coal_land_constraint_and_global_resources","煤炭和新大陆资源使英国突破土地能源约束但作用依赖交通市场与全球制度","不能把资源存在写成自动因果","补矿业、运输、价格、机器与国家政策材料","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.4","A","ecological_material_system","制造材料和能源必须连同土地森林粮食棉花和海外资源供给分析","鬼田数字及生态可比性仍有争议","补环境史、供应链和量化复核","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.7","A","regional_divergence_and_contingency","劳动密集与能源密集路径并非文明本质而受区域资源、人口和全球关联塑造","宏观模型不能抹平区域内部不平等","补区域微观史和不同工业化路径","ACCEPTED_WITH_LIMITS"),
            ("2.4","B","consumption_similarity_and_global_goods","欧洲消费差异也受美洲白银、亚洲需求和种植园商品网络塑造","不是百货商店或具体消费者接受史","补零售、家庭账本和商品对象材料","ACCEPTED_AS_STRUCTURAL_CONTEXT"),
            ("2.7","B","new_world_resources_and_coercive_exchange","跨境物质流动建立在殖民制度、奴隶劳动和不对称交换之上","较少处理纹样、误读和地方再生产","与B0040、B0086、B0304及对象史互证","ACCEPTED_AS_STRUCTURAL_SUPPORT"),
        ],
    },
    "B0334": {
        "title": "Why Europe Grew Rich and Asia Did Not",
        "author": "Prasannan Parthasarathi",
        "version": "Cambridge University Press, 2011",
        "type": "全球经济史、大分流与工业化比较专著",
        "scope": "1600—1850年的英国、印度，并比较法国、奥斯曼、中国和日本",
        "summary": "Parthasarathi拒绝从19世纪工业化结果倒推18世纪各经济体都以工业化为目标。他把英国路径解释为对印度棉布竞争、木材短缺与国家政策组合的回应，并以印度技术能力和殖民条件反驳能力缺失论。该书能强化第一章的棉—煤—国家机制与多路径框架，但‘压力—回应’模型、损失厌恶借用及印度内部同质化均需反方校正。",
        "strengths": [
            "把印度棉布从被动原料背景提升为欧洲技术和政策回应的竞争性对象。",
            "比较英国、法国、奥斯曼、中国、日本的不同压力与政策回应。",
            "以印度工业移植档案反驳殖民地缺乏技术能力的先验判断。",
        ],
        "limits": [
            "压力—回应三因素不足以穷尽工业革命，供给侧技术、教育和知识制度可能被低估。",
            "印度地区差异和中国国家能力处理较薄，部分比较依赖二手研究。",
            "损失厌恶用于长时段历史解释的外部效度尚未得到独立检验。",
            "棉布竞争不能独立证明某项发明、图样或设计职业的直接因果。",
        ],
        "checks": [
            "clean第77—91行：多元路径、印度棉布、木材短缺和国家政策的总论。",
            "clean第145—190行：反时代错置及工业化作为非预期结果。",
            "clean第196—236行：棉、煤、中国与日本的不同问题和国家回应。",
            "clean第295—314行：欧洲回应印度棉布、煤炭采用与殖民政治条件。",
        ],
        "maps": [
            ("0.2","A","anti_anachronism_and_plural_paths","不能从十九世纪工业化结果倒推早期各地区都以工业化为目标","多元路径主张仍需说明比较节点和历史行动者目标","补同期概念、政策与行动者材料","ACCEPTED_AS_METHOD"),
            ("0.3","A","contextual_pressure_response_comparison","历史解释应比较各地区面对的具体压力、需求与政策回应","压力模型不是充分解释且损失厌恶外推有风险","同技术供给、教育制度和反方研究比较","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("0.6","B","orientalist_and_geographic_evidence_bias","东方主义与英国中心史料会把亚洲能力缺失预设为解释","作者自身对印度内部和中国材料也不均衡","补地区档案、中文研究与殖民知识生产史","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","A","multiscalar_global_comparison","全球史可在英国印度、欧洲内部、欧亚与帝国尺度间检验不同机制","尺度切换不能掩盖材料不对称和地区异质性","公开比较单位、来源与外推边界","ACCEPTED_WITH_LIMITS"),
            ("1.1","B","indian_textile_skill_and_scientific_capacity","印度棉纺与科技能力构成欧洲工业化之前的高度组织化知识背景","不是所有印度地区和行业的统一事实","补区域工艺、作坊、教育和生产者材料","ACCEPTED_AS_COMPARATIVE_SUPPORT"),
            ("1.2","A","cotton_coal_state_and_scale","棉布竞争、煤炭采用和国家政策共同塑造英国技术与生产尺度变化","不能把三因素写成单一或已终结的因果解释","补专利、工厂、煤运、成本与政策记录","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.3","C","skills_and_technical_response_context","技术回应涉及技能积累与生产重组可作为图样权力的外围背景","本书不足以证明图样制模规格和监督如何分离","补设计与工程图纸、职位和工序档案","CONTEXT_ONLY"),
            ("1.4","A","cotton_coal_ecology_and_state_material_system","棉花、煤、木材与全球商品竞争构成由国家中介的材料能源系统","资源禀赋与政策作用权重仍有争议","与B0259、B0040及材料环境史互证","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("1.7","A","plural_development_and_colonial_constraint","英国、印度、中国、日本和奥斯曼对不同压力采取不同路径且殖民统治会限制技术移植","不能将印度或亚洲处理为同质整体","补地区比较和殖民地企业档案","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4","B","global_cotton_competition_and_demand","印度棉布的全球消费与竞争会改变欧洲市场、政策和生产激励","不是商店陈列、信用或消费者经验的直接研究","补订单、零售、广告和穿用材料","ACCEPTED_AS_STRUCTURAL_SUPPORT"),
            ("2.7","A","indian_cottons_and_european_response","欧洲对印度棉布的禁止、模仿和技术回应体现跨境竞争中的选择与再生产","技术变化不能只归因于竞争且挪用与殖民权力须保留","补图样、样品、政策、生产者和地方使用链","ACCEPTED_WITH_CAUSAL_LIMIT"),
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
        "duplicate_group": None,
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
        "| 字段 | 内容 |", "|---|---|", f"| 来源ID | {source_id} |", f"| 作者 | {data['author']} |",
        f"| 版本 | {data['version']} |", f"| 类型 | {data['type']} |", f"| 范围 | {data['scope']} |",
        f"| clean SHA-256 | `{card['clean_source_sha256']}` |",
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
