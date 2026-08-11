# -*- coding: utf-8 -*-
"""BATCH-009 CH00 语义复核：B0115 Hendon & Massey《Design, History and Time》。"""
import json
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-009-CH00-INTRO\review_data\B0115_review.json")
p.parent.mkdir(parents=True, exist_ok=True)

data = {
    "source_id": "B0115",
    "title": "Design, History and Time: New Temporalities in a Digital Age",
    "author": "Zoë Hendon, Anne Massey (eds.)",
    "version": "Bloomsbury Visual Arts，2019年精装初版（2023年平装版）；源自2016年设计史学会年会“Design and Time”；13章",
    "type": "设计史学术论文集（P1）",
    "scope": "以“时间”为核心分析范畴的设计史13篇论文：三部分按时间尺度编排（千年/世纪：石头材料厚时间、Traquair深层时间、Ghan号列车殖民时间；世纪/年代：东德公共艺术、葡萄牙传统发明、High and Over住宅、eBay数字档案、酷儿情感档案；日/小时/秒：伦敦地铁时间机器、Archigram/Price建筑乌托邦、慢设计、万年钟与当代时间想象、Kindle非共时性）",
    "duplicate_group": "无精确哈希重复；导论确认Judy Attfield《Wild Things》（B0240）为设计史时间讨论的先行者，本书记载并推进该路径；与B0440（Walker）共享设计史学科史对象（1976年米德尔塞克斯会议以来的学科发展），同一对象只计一份P0",
    "summary": "本书是2016年设计史学会年会“Design and Time”的论文集（Bloomsbury，2019），以“时间”为核心分析范畴统摄13篇跨领域论文（设计史、建筑史、考古学、档案研究、策展实践、酷儿研究）。导论建构时间观念的社会建构史：从E. P. Thompson的“时钟时间”、Benedict Anderson的“同质空时间”到Robert Hassan的“网络时间”，确认Judy Attfield为设计史时间讨论先行者，并指出数字化时代设计史面临的“去历史化”（ahistorical）危机。全书按“千年/世纪—世纪/年代/年—日/小时/秒”三个时间尺度编排（编者承认“某种程度上的任意性”），核心案例：虚拟环境使建筑绘图时间性从静态转向动态（Ch1）、东德公共艺术统一后的“抛弃—怀旧—调适”三阶段（Ch4）、葡萄牙极右独裁“发明传统”（Ch5）、eBay作为“非官方数字档案馆”以关键词标签重塑战后英国设计史叙事（Ch7）、酷儿“情感档案”作为对抗时间规范性的替代史学路径（Ch8）、伦敦地铁作为“时间机器”（Ch9）、慢设计将时间商品化（Ch11）、万年钟与当代时间想象（Ch12）、Kindle的“非共时性”（Ch13：同时指向过去现在未来，六种时间运动框架）。Barry Curtis前言回顾设计史四十年学科发展（1976年米德尔塞克斯“休闲”会议起），援引Banham 1960年“跟上技术文化是历史学家的义务”。",
    "strengths": [
        "0.6档案政治与历史叙事生产的当代案例：eBay作为“非官方数字档案馆”（关键词标签重塑战后英国设计史叙事）、东德公共艺术“抛弃—怀旧—调适”的记忆政治、酷儿“情感档案”（archive of feelings）——0.6证据偏差与正典建构的数字时代样本",
        "0.2时间观念的社会建构史：Thompson时钟时间→Anderson同质空时间→Hassan网络时间的谱系、数字化时代设计史“去历史化”危机、非规范性时间（酷儿/殖民/原住民多重时间性）——0.2现代性时间叙事的当代批判资源",
        "0.5数字痕迹与档案类型扩展：eBay关键词标签、Kindle阅读数据、GPS数据可穿戴化（Silver Lining首饰）——0.5“数字痕迹”史料类型的当代案例",
        "0.3替代史学路径：酷儿设计史（对抗时间规范性）、殖民时间与原住民梦幻时间的多重共振——从英雄谱系到多元时间性的方法论拓展",
        "跨章可用：第13章Kindle“非共时性”与六种时间运动框架（怀旧/复古/遗产/先锋/去未来化/当代—经典）为14.x数字媒介分析；第9章伦敦地铁（Harry Beck 1933示意图、速度被设计进地下城市）为14.x/9.x基础设施设计案例；第12章万年钟、慢设计为15.x批判/推测设计资源",
        "学科史锚点：Curtis前言将本书置于1976年米德尔塞克斯会议以来四十年设计史学科发展谱系，Banham 1960“快速伙伴”警告——0.3学科史叙事的参照",
    ],
    "limits": [
        "论文集体裁：13篇独立署名论文，立场与文体差异大（编者明言“多声性”），引用须区分作者与篇目",
        "2019年出版时点：数字媒介案例（eBay、Kindle第一代2007）部分已过时，平台机制须更新核实",
        "理论建构性大于史料性：时间性框架（非共时性、时间运动、情感档案）为作者建构概念，教材引用须标注命题身份",
        "案例集中于英美与欧洲，全球南方时间经验覆盖有限",
        "部分章节（如Ch3文学报告式）文体实验性强，作史料使用时证据密度不均衡",
    ],
    "checks": [
        "packet 分析报告.md：导论时间观念谱系（Thompson/Anderson/Hassan）；Attfield为先行者；“去历史化”危机",
        "Ch7：eBay作为非官方数字档案馆（“原子风格”球棒家具关键词标签重塑叙事）；Ch8：情感档案（Muñoz“Who owns rigor?”）",
        "Ch4：东德公共艺术“抛弃—怀旧—调适”三阶段；Ch5：巴塞罗斯公鸡与传统发明",
        "Ch9：伦敦地铁时间机器（Beck 1933、Leslie Green彩釉瓷砖1905、Holden售票亭1930s、Dell程序机器1957—60）",
        "Ch13：Kindle非共时性与六种时间运动；Ch12：万年钟（Long Now）、慢设计、思辨设计（Popper单程票2012）",
        "Curtis前言：1976年米德尔塞克斯“休闲”会议以来的学科史；Banham 1960警告",
    ],
    "maps": [
        ["0.6", "B", "digital_archives_and_narrative_production", "档案政治与历史叙事生产的当代样本：eBay作为“非官方数字档案馆”（关键词标签重塑战后英国设计史叙事）、东德公共艺术统一后的记忆政治（抛弃—怀旧—调适）、酷儿“情感档案”——0.6证据偏差与正典建构的数字时代案例", "单篇案例研究（Ch4/7/8）；eBay平台机制变化快，引用须注明考察时点", "packet 分析报告.md Ch7、Ch4、Ch8", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.2", "B", "social_construction_of_time", "时间观念的社会建构史：Thompson时钟时间→Anderson同质空时间→Hassan网络时间谱系、数字化时代设计史“去历史化”危机、非规范性时间（酷儿/殖民/原住民多重时间性）——0.2现代性时间叙事的当代批判", "编者导论框架；时间理论谱系须回溯Thompson/Anderson原著", "packet 分析报告.md 导论部分", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.5", "C", "digital_traces_as_sources", "数字痕迹史料类型的当代案例：eBay关键词标签、Kindle阅读数据（非共时性分析）、iPhone GPS数据转化为可穿戴首饰（Silver Lining）——0.5“数字痕迹”能证明什么、不能证明什么的案例", "平台数据为2000s—2010s时点样本；数字档案的保存与取用机制（平台关闭、数据删除）须说明", "packet 分析报告.md Ch7、Ch13、Ch12", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["0.3", "C", "queer_and_alternative_temporalities", "替代史学路径：酷儿设计史以“情感档案”对抗时间规范性（chrononormativity）、殖民时间与原住民梦幻时间在铁路空间中的多重共振——从英雄谱系到多元时间性的方法论拓展", "单篇立场（Ch8酷儿理论、Ch3文学报告式）；作为方法路径引用，非学科共识", "packet 分析报告.md Ch8、Ch3", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["14.4", "C", "kindle_nonsynchronicity_digital_media", "数字媒介的时间性（跨章）：Kindle“非共时性”——设计物同时指向过去、现在与未来，六种时间运动框架（怀旧/复古/遗产/先锋/去未来化/当代—经典）——14.4数字交互与媒介分析的理论资源", "作者建构框架（Ch13）；六格图表（Figure 13.2）为可视化工具", "packet 分析报告.md Ch13", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["15.1", "C", "long_now_and_speculative_time", "当代设计重新想象时间（跨章）：万年钟（Long Now Clock）、慢设计（时间商品化）、思辨设计（Popper《单程票》2012）——15.1批判/推测设计的案例资源", "案例时点（2010s）；思辨设计谱系（RCA传统）须另以专门文献支撑", "packet 分析报告.md Ch11、Ch12", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
    ],
}

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("B0115 完成, maps =", len(data["maps"]))
