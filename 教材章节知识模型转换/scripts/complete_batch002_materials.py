#!/usr/bin/env python3
"""Complete the cotton-and-porcelain material-chain group in BATCH-002."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换")
BATCH = ROOT / "11_语义复核批次" / "BATCH-002-CH01-EXPANDED"
ASSETS = ROOT / "03_来源清单与来源卡" / "来源资产总表.csv"


DATA = {
    "B0169": {
        "title": "Cotton: The Fabric That Made the Modern World",
        "author": "Giorgio Riello",
        "version": "Cambridge University Press, 2013",
        "type": "全球棉花史、物质文化史与工业化研究专著",
        "scope": "约1000—2000年的印度、欧洲、奥斯曼、大西洋世界及全球棉花体系",
        "summary": "Riello以棉花连接纤维、后整理、贸易知识、消费定制、跨境工匠、种植园奴隶制、机械化、设计保护和全球市场。他反对从兰开夏单向解释工业革命，强调欧洲先经历了面向印度棉布的长期学习、模仿、改造与竞争。对教材第一章，本书最有价值的是把材料、产品质量、默会知识、工序重组、机器和制度置于同一链条；但离心／向心体系和长期大分流仍是作者的解释模型，不是对象自动给出的结论。",
        "strengths": [
            "把印度后整理、欧洲印花实验和跨境工匠流动纳入工业化前史，避免机器突然出现的叙事。",
            "以公司通信、贸易统计、博物馆织物、消费者失败案例与技术说明构成多类证据链。",
            "将产品创新、工艺创新、设计保护、消费者规格和原棉供给放在同一产业系统中。",
            "明确把种植园奴隶制视为影响工业化模式与时机的结构条件，而非无争议的单因解释。",
        ],
        "limits": [
            "全书以欧洲与南亚为中心，中国、非洲和波斯等地的一手材料与劳动者视角不均衡。",
            "‘离心／向心体系’和大分流长时段模型需要同B0259、B0334及区域研究保持争论关系。",
            "东印度公司档案中的消费者偏好和生产者行为经过商人中介，不能代替消费者与工匠主体材料。",
            "奴隶劳动、殖民关税与去工业化结论需要种植园账簿、劳动者材料、政策档案和反方研究复核。",
            "图版、产量、价格、土地反事实与专利／设计保护的法律细节尚未逐项核验。",
        ],
        "checks": [
            "clean第1228—1240、1429—1458行：印度优势被定位于后整理质量而非更高纺织生产率，且印染包含高度细分工序。",
            "clean第1643—1660行：公司订货、白底偏好和消费失败推动定制与新的印花技术，但生产者和消费者没有直接接触。",
            "clean第2312—2334、2399—2408行：书面编码不足以转移复杂工艺；亚美尼亚工匠和开放技术网络承载默会知识，欧洲又进行再实验。",
            "clean第2598—2608行：作者拒绝把奴隶制与工业化写成直线单因关系，同时确认种植园对扩张性棉花供给的重要性。",
            "clean第2787—2815、2878—2892行：技术既改变产量也改变质量，英国例外论受到全球联系与比较的校正。",
            "clean第2980—3025行：印花设计保护、工厂不稳定性、劳动—资本—土地重组与机器采用被置于同一机制链。",
            "clean第3401—3471行：英国棉纱／棉布进入亚洲与印度去工业化存在时序和解释争论，地方工匠也发生适应。",
        ],
        "maps": [
            ("0.2","B","long_duration_cotton_systems","棉花体系的中心转移提示现代设计史分期应追踪材料贸易生产和消费关系而不只按机器发明断代","离心向心及漫长分流是作者模型且1000至2000年的尺度会压平地区节奏","与B0259、B0334及区域工业史比较分期节点","ACCEPTED_WITH_COUNTERARGUMENT"),
            ("0.3","A","commodity_chain_global_history_method","以单一材料为透镜可把对象工序公司市场生态和强制劳动连接成可检验问题链","商品链不能取代地方制度史且不能由连接直接推出因果","公开每一环节的来源类型、地理范围和机制证据","ACCEPTED_AS_METHOD"),
            ("0.4","A","textiles_archives_statistics_and_images","织物样品、图像、贸易统计和公司信函可相互校正产品名称技术与市场判断","图像说明和商业分类不等于对象身份或消费者经验","补对象检验、馆藏史、公司原档与使用材料","ACCEPTED_WITH_LIMITS"),
            ("0.5","A","multisource_cotton_evidence_chain","公司档案、统计、器物、技术文本、政策和个人证词能够形成棉花史多链互证","宏观数据、行动者话语和物质证据的尺度不得混合","逐项标明事实、作者解释、当事人主张和当前推论","ACCEPTED_AS_METHOD"),
            ("0.6","A","company_archive_slave_labor_and_audience_bias","公司与殖民档案会放大商人管理视角并压低工匠、被奴役者、妇女和普通消费者声音","从档案缺席恢复主体仍须独立主体材料","补劳动者叙述、种植园账簿、家庭清单、司法和地方档案","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","A","cotton_as_connected_and_coercive_global_history","全球棉花史必须同时书写知识转移、商品流通、殖民权力与奴隶劳动","连接史不能把不平等交换美化为互惠交流","建立订货生产运输销售使用与强制制度链","ACCEPTED_WITH_POWER_LIMIT"),
            ("1.1","A","indian_workshops_finishing_and_distributed_skill","印度纺纱织造印染和后整理知识分布于家庭作坊中间商与专业工序而非单一作者","印度不同区域与工种不能视为统一制度且独立织工不等于没有约束","补作坊账簿、工具、工资、合同、训练与工匠材料","ACCEPTED_WITH_LIMITS"),
            ("1.2","A","mechanisation_quality_scale_and_supply","纺纱机器动力织机与原棉供给共同扩大产量并改变质量和产品范围","技术是必要但不充分条件且动力织机对细布的采用存在长时滞","补机器性能、动力、成本、质量、工厂和原料数据","ACCEPTED_WITH_MECHANISM_FOLLOWUP"),
            ("1.3","A","finishing_division_commissioning_and_design_rights","印染细分、公司规格、机械滚筒和短期设计保护改变了构思制作监督与复制关系","公司命令与法律文本不能自动证明工场实际执行或个人作者权","补样品、订单、刻版、工序、诉讼、工资和车间档案","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.4","A","cotton_fiber_dyes_land_and_plantation_system","棉纤维性能、染料、印花化学、土地与种植园供给共同限定工业棉品的形式和规模","生态潜力和土地反事实仍依赖估算且不得遮蔽奴隶制","补纤维检测、配方、农场与种植园数据、环境和劳动史","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.5","A","distributed_product_and_process_innovation","印度工匠、亚美尼亚印花工、欧洲技师、公司、企业主与消费者共同改造棉布而常被发明家叙事遮蔽","分布式参与不能据此确定每件织物的责任和动机","逐对象补图样、样布、工场、订单、专利与销售责任链","ACCEPTED_WITH_LIMITS"),
            ("1.7","A","india_europe_ottoman_and_atlantic_mixed_trajectories","印度、奥斯曼、欧洲和大西洋棉花体系呈现手工机器贸易与强制劳动的非同步重组","两体系模型可能压平非洲、中国及地方内部差异","与B0086、B0130和更多地区研究交叉校正","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4","A","customisation_consumption_and_company_mediation","消费者对颜色底色尺寸和品种的选择通过公司样品与订货反向改变生产和工艺","公司判断是中介证据且一次销售失败不能代表全部消费者","补零售、价格、家庭清单、穿用、退货和消费者材料","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6","A","slavery_colonial_trade_and_classification","棉布展示与消费必须连同种植园奴隶制、殖民关税和市场分类书写","商业图像可能理想化种植园且分类词不应作为中性事实复述","补被奴役者材料、政策档案、图像生产语境和反方研究","ACCEPTED_AS_CRITICAL_CONTEXT"),
            ("2.7","A","learning_imitation_reworking_and_market_selection","跨境棉布流动包含学习失败、规格传递、工匠迁移、模仿、技术再造和消费者拒绝","不能简化为东方影响西方或直接技术复制","逐对象建立样品订货工匠工序销售和使用链","ACCEPTED_WITH_LIMITS"),
        ],
    },
    "B0154": {
        "title": "The Pilgrim Art: Cultures of Porcelain in World History",
        "author": "Robert Finlay",
        "version": "University of California Press, 2010",
        "type": "全球瓷器史、物质文化史与跨文化交流研究专著",
        "scope": "瓷器地质与技术起源至1850年前后，重点为景德镇、东亚、伊斯兰世界和欧洲",
        "summary": "Finlay把瓷器作为组织世界史材料的透镜，而不把器物拟人化为独立行动者。景德镇的原料、窑炉、劳动分工和商业网络，与波斯钴料、穆斯林商人、东亚仿制、欧洲宫廷工场、梅森技术扩散及Wedgwood工厂形成长时段比较。它最适合支持材料系统、分工、设计跨文化转译和市场竞争；但‘瓷器衰落追踪中国衰落’与‘世界历史转折点’属于Finlay的宏大解释，必须署名、限域并同区域经济史和中国陶瓷史校正。",
        "strengths": [
            "把瓷石、高岭土、钴、釉、燃料、窑炉和废品率同生产组织、贸易和器形设计连接。",
            "以器物、沉船、考古、耶稣会书信、技术文献、商业档案和图像构成跨学科证据网络。",
            "通过景德镇、青花瓷、德尔夫特、梅森和斯塔福德郡呈现模仿、替代、再设计与反向流动。",
            "明确瓷器是观察跨文化接触的组织原则，不声称没有瓷器就不会发生相关世界史过程。",
        ],
        "limits": [
            "从中国瓷器市场衰落推及中国整体世界地位的论证尺度跃迁过大，只能作为作者解释而非事实陈述。",
            "景德镇材料高度依赖殷弘绪等外来观察者，宫廷、精英收藏与贸易资料多于普通工人和使用者声音。",
            "‘中国’与‘伊斯兰世界’等大范围单位内部差异不足，东南亚大陆、中国地区和环境史处理不均衡。",
            "关于景德镇技术停滞、国家领导缺席及欧洲胜利的叙述含目的论风险，需要较新中外研究校正。",
            "Wedgwood、梅森、产量、价格和‘第一’类判断及全部图版尚未逐项核验。",
        ],
        "checks": [
            "clean第184—230行：作者把瓷器界定为跨文化交换的物质证据，同时明确它不是历史因果的独立主角。",
            "clean第294—326、350—388行：殷弘绪书信记录景德镇规模、市场和劳动分工，但观察者身份与估算须保留。",
            "clean第600—615、737—765行：瓷器秘密的搜集是重商主义知识工程，书面信息仍不足以直接复制技术。",
            "clean第1493—1525、1640—1650、1718—1758行：瓷石与高岭土、波斯钴、穆斯林商人、元代政策和专门劳动共同构成青花瓷链。",
            "clean第1853—1864行：面向西南亚市场的器形、模型、装饰与使用方式发生选择性转译。",
            "clean第2815—2831行：德尔夫特生产受移民技术、进口中断、地方灾变、工场扩张和中国恢复出口共同塑造。",
            "clean第2987—3000行：梅森突破来自宫廷强制、多人研发、高岭土与工匠逃离，不能简化为Böttger个人发明。",
            "clean第3108—3142行：Wedgwood把新古典图样、分工、纪律、蒸汽、测温、交通和营销结合，但相关因果仍是作者综合。",
            "clean第3146—3193行：全球市场替代和‘中国衰落’结论混合贸易事实、英国使团记录与象征性解释，必须分层使用。",
        ],
        "maps": [
            ("0.3","A","object_lens_and_scale_control","以瓷器为透镜可从具体物质痕迹扩展到生产贸易与跨文化关系并检验尺度跃迁","器物传播不能自动证明文明兴衰或世界体系因果","区分对象事实、作者解释与宏观推论并补区域史","ACCEPTED_AS_METHOD"),
            ("0.4","A","porcelain_as_material_and_contextual_evidence","胎釉钴料器形纹样窑痕和残片可提供材料技术与流通线索","形式与材料不能脱离出土入藏委托与使用语境解读","补检测、考古层位、馆藏史、订单和使用记录","ACCEPTED_WITH_LIMITS"),
            ("0.5","A","artifact_archaeology_text_and_trade_triangulation","器物、沉船、考古、技术文本、书信与商业数据可形成瓷器史多链互证","不同年代地点和证据尺度不能仅凭叙事并置合并","逐项记录定位、来源类型、冲突和置信等级","ACCEPTED_AS_METHOD"),
            ("0.6","B","jesuit_court_collection_and_worker_visibility_bias","耶稣会、宫廷、商人和收藏材料能见度高而普通工人妇女与使用者声音稀薄","外来观察和精英收藏不能直接代表景德镇社会或全球消费者","补地方档案、工匠记录、工资、家庭、司法与来源社群材料","ACCEPTED_AS_EVIDENCE_AUDIT"),
            ("0.7","A","porcelain_connected_world_history","瓷器可连接中国、伊斯兰世界、东亚、欧洲和海洋贸易中的技术与文化转译","连接与模仿不是无权力差异的对称交流","建立原料委托制作贸易使用仿制和替代链","ACCEPTED_WITH_POWER_LIMIT"),
            ("1.1","A","jingdezhen_distributed_workshop_knowledge","景德镇瓷器由采料制胎绘饰施釉装窑烧成分级运输等专门工序协作完成","殷弘绪的分工描述是外部观察且不能代表各时期各窑","补地方志、窑址、工匠、工资、合同和工序复原","ACCEPTED_WITH_LIMITS"),
            ("1.2","B","kiln_energy_transport_and_mechanised_competition","窑炉燃料、运河海运、蒸汽动力和机械装饰改变陶瓷规模成本与稳定性","本书不是机器性能或能源计量专史且中欧比较可能目的论化","补窑炉数据、燃料、动力、运输、产量和成本记录","ACCEPTED_AS_SUPPORT"),
            ("1.3","A","division_of_labor_models_patterns_and_supervision","景德镇分工、外来器形模型、绘饰工序、梅森保密和Etruria管理显示构思制作与监督权不断重组","不能由分工直接推出现代设计职业或单一源头","补图样、模具、订单、工序签记、职位和管理档案","ACCEPTED_WITH_OBJECT_FOLLOWUP"),
            ("1.4","A","china_stone_kaolin_cobalt_glaze_and_fuel_system","瓷石高岭土钴釉料燃料窑炉和运输共同限定瓷器白度强度颜色器形与废品率","地质禀赋不自动造成技术领先且部分材料来源和数量待核","补矿物检测、窑址、配方、燃料环境与供应链记录","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("1.5","A","anonymous_potters_merchants_and_enterprise_network","采料者陶工画工窑工商人公司宫廷技术人员和企业主共同塑造瓷器而常被个人发明叙事遮蔽","分布式生产不能据此确定特定器物作者和动机","逐对象补模型订单工场账簿签款工资销售与使用链","ACCEPTED_WITH_LIMITS"),
            ("1.6","C","industrial_arts_and_design_vocabulary_context","瓷器生产和市场话语可补art manufacture pattern design等概念的外围语境","本书不是工业艺术装饰艺术或设计职业词源史","补同期词典教育制度职位行业组织和设计改革文本","CONTEXT_ONLY"),
            ("1.7","A","jingdezhen_east_asia_islamic_and_european_mixed_paths","景德镇、东亚、伊斯兰陶业、德尔夫特、梅森与英国工厂呈现不同的手工宫廷市场和机械混合路径","大区域标签与西方胜利结局会压平内部差异和持续手工生产","补中国地区史、东南亚、本地劳动史与反方全球陶瓷史","ACCEPTED_WITH_COUNTERSOURCE_REQUIRED"),
            ("2.4","B","court_household_market_and_customised_consumption","宫廷收藏、餐桌习惯、热饮、定制订单和市场竞争改变器形装饰与产品组合","精英收藏和商人资料不能代表普通消费者或实际使用效果","补家庭清单、价格、破损修补、零售和使用者材料","ACCEPTED_WITH_AUDIENCE_GAP"),
            ("2.6","B","empire_collection_trade_and_hierarchical_naming","帝国贸易、宫廷收藏和‘中国风’分类能揭示异域物被命名展示和等级化的过程","作者的文明单位和同时代术语也需历史化不能中性复述","补征集史、展陈、来源社群、殖民档案和术语批判","ACCEPTED_AS_CRITICAL_CONTEXT"),
            ("2.7","A","porcelain_translation_imitation_and_reverse_flow","瓷器跨境流动包含外来模型、钴料贸易、器形适配、仿制失败、工匠迁移、替代和反向复制","形式相似不能单独证明直接影响且文化意义并不恒定","逐对象补模型样品订单贸易工匠和地方使用链","ACCEPTED_WITH_LIMITS"),
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
