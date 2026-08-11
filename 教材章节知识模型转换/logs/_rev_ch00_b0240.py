# -*- coding: utf-8 -*-
"""BATCH-009 CH00 语义复核：B0240 Attfield《Wild Things》。"""
import json
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-009-CH00-INTRO\review_data\B0240_review.json")
p.parent.mkdir(parents=True, exist_ok=True)

data = {
    "source_id": "B0240",
    "title": "Wild Things: The Material Culture of Everyday Life",
    "author": "Judy Attfield",
    "version": "Berg Publishers，2000年初版（2020年Bloomsbury Visual Arts再版，含Claudia Marina前言与Jo Turney后记）；Radical Thinkers in Design丛书；全书约55万字符、约685条引用",
    "type": "物质文化研究／设计史理论专著（P1）",
    "scope": "日常物质文化理论：Introduction＋三部九章（Part I概念奠基：有态度的物、小写设计、物与社会变迁；Part II主题展开：本真性与复制、身份的短暂物质性、个人财物的容纳；Part III语境整合：空间、时间、身体）",
    "duplicate_group": "无精确哈希重复；Attfield另撰B0440第十章（女性主义设计批评），同作者不同书；与B0311（Csikszentmihalyi《The Meaning of Things》）共享日常物意义研究谱系，同一对象P0只计一份；2020再版仅新增前言后记，命题以2000年版为基准",
    "summary": "本书是20世纪末物质文化研究与设计史交汇的里程碑（2000，Berg）：Attfield在三个“之间”定位学科——设计史与人类学之间、生产研究与消费研究之间、学术分析与日常经验之间。核心概念贡献：“有态度的物”（things with attitude，重新定义设计）、“小写设计”（design in the lower case，日常非专业设计实践）、“反设计”（undesign，未经专业设计过程的日常物品）、“合理的家具”（reasonable furniture，1939年Heal's目录的理性现代家具）、“织理性”（textility，从文本性转向织物物质性）。方法论贡献：建立“后学科”（post-disciplinary）跨学科范式、为案例研究提供理论辩护、示范微观物质分析（梳妆台台面）与宏观社会诊断（郊区化、现代化）的连接、开创“从物出发”（thing-centred）而非“从文本出发”的研究路径。政治贡献：挑战现代主义“好设计/坏设计”精英二分法、为日常物质实践（DIY、复制品消费、郊区生活）提供文化合法性、揭示“品味”论述中的阶级与性别政治、将消费者重新定义为创造性的“使用者/制作者”。根本理论命题：物不是社会关系的被动“反映”或“表征”，而是社会关系的“物理表达”（physical articulation）与“积极中介”（active mediator）——物在“做”事物而不仅仅是“意味”事物。",
    "strengths": [
        "0.1设计定义扩展的A级当代文献：“有态度的物”“小写设计”（日常非专业设计）、“反设计”（未设计）——0.1“设计是对象、活动还是制度”的核心理论资源",
        "0.4人工物作为史料的系统理论：物作为社会关系的物理表达与积极中介、梳妆台微观分析连接郊区化宏观诊断、“从物出发”研究路径——0.4“人工物如何成为史料”的理论支柱",
        "0.3物质文化转向的方法论宣言：拒绝生产/消费二分法、物的“社会生命”（Appadurai/Miller资源）、后学科跨学科范式——从英雄谱系到关系史的物质文化侧",
        "0.6正典批判的政治维度：挑战现代主义“好设计/坏设计”精英二分法、揭示品味论述中的阶级与性别政治、为DIY/复制品消费/郊区生活提供文化合法性——0.6“正典偏差”的批判资源",
        "0.2现代性条件下的物：郊区化、现代化进程中的日常物（spec builder's vernacular投机建造商本土风格）——现代性日常侧案例",
        "跨章可用：12.6性别政治（梳妆台、身体作为自然/文化门槛）；9.x消费研究（消费者作为创造性的使用者/制作者）；Ch8时间（赋予物以生命）与B0115时间性讨论互参",
        "结构完整可追溯：三部九章对称结构、约685条引用、30幅插图；2020再版前言（Marina）与后记（Turney）提供接受史线索",
    ],
    "limits": [
        "理论专著性质：概念建构（有态度的物、织理性等）为作者框架，教材引用须标注命题身份",
        "英国语境：案例（Heal's家具目录、战后英国郊区、DIY文化）集中于英国经验，跨文化适用性须谨慎",
        "2000年出版时点：数字物质文化（虚拟物、平台物）未涵盖",
        "理论密度高：精神分析、现象学资源（Ch5、Ch8）解读有争议性，引用须说明理论立场",
        "与B0311（The Meaning of Things）等共享日常物意义研究谱系，同一研究传统只计一份P0",
    ],
    "checks": [
        "packet 00整体分析报告：L000.1.2.1概念贡献（有态度的物、小写设计、反设计、合理的家具、织理性）；L000.1.2.2方法论贡献（后学科、案例研究辩护、从物出发）",
        "L000.1.2.3政治贡献：挑战好设计/坏设计二分法、品味论述中的阶级性别政治、消费者作为使用者/制作者",
        "3.1第一级论题：物作为社会关系的物理表达与积极中介（“物在做事物而不仅仅是意味事物”）",
        "2.3章节结构：三部九章的递进逻辑（概念奠基→主题展开→语境整合）",
        "Ch4 Heal's“合理的家具”（1939目录）、Ch6梳妆台微观研究、Ch8时间哲学",
    ],
    "maps": [
        ["0.1", "A", "things_with_attitude_lowercase_design", "设计定义的系统扩展：“有态度的物”（things with attitude）、“小写设计”（design in the lower case，日常非专业设计实践）、“反设计”（undesign，未经专业设计过程的日常物品）——0.1“设计”概念讨论的核心当代文献", "作者建构概念（2000）；作为设计定义论与Heskett/Buchanan等并置，不替代制度定义", "packet 00整体分析报告L000.1.2.1", "ACCEPTED_AS_CORE_SOURCE"],
        ["0.4", "B", "things_as_physical_articulation", "人工物作为史料的系统理论：物是社会关系的“物理表达”与“积极中介”（在做事物而不仅仅是意味事物）、微观物质分析（梳妆台台面）连接宏观社会诊断（郊区化、现代化）、“从物出发”研究路径——0.4“人工物如何成为史料”的理论支柱", "理论框架（2000）；个案方法示范（Heal's、梳妆台）为英国案例，跨文化适用须谨慎", "packet 00整体分析报告L000.1.2.2、3.1第一级论题", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.3", "B", "material_culture_turn_manifesto", "物质文化转向的方法论宣言：拒绝生产/消费二分法、物的“社会生命”（Appadurai/Miller资源）、后学科跨学科范式——从英雄谱系到关系史的物质文化侧", "作者方法论立场；物的社会生命概念须回溯Appadurai原著", "packet 00整体分析报告1.1学科定位（三个“之间”）", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.6", "B", "good_design_dichotomy_critique", "正典批判的政治维度：挑战现代主义“好设计/坏设计”精英主义二分法、揭示“品味”论述中隐含的阶级与性别政治、为日常物质实践（DIY、复制品消费、郊区生活）提供文化合法性——0.6“正典偏差”的批判资源", "作者政治立场（文化合法性辩护）；批判对象（好设计标准）须与MoMA/CoID档案并置", "packet 00整体分析报告L000.1.2.3", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.2", "C", "modernity_everyday_things", "现代性条件下的日常物：郊区化与现代化进程中的物（spec builder's vernacular投机建造商本土风格）、日常物质实践作为现代性经验——0.2现代性的日常侧案例", "英国郊区化案例（战后）；现代性框架为作者综合", "packet 00整体分析报告L000.1.2.3、2.1结构", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["12.6", "C", "gender_politics_of_taste", "品味与性别政治（跨章）：梳妆台的微观研究、身体作为自然与文化之间的门槛、品味论述中的性别政治——12.6女性主义设计批评的物质文化侧", "作者分析（Ch6、Ch9）；与B0440第十章（Attfield女性主义批判）互参", "packet 00整体分析报告Ch6、Ch9", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
    ],
}

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("B0240 完成, maps =", len(data["maps"]))
