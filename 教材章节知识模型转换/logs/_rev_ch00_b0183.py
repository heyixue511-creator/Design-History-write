# -*- coding: utf-8 -*-
"""BATCH-009 CH00 语义复核：B0183 Conway《Design History: A Students' Handbook》。"""
import json
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-009-CH00-INTRO\review_data\B0183_review.json")
p.parent.mkdir(parents=True, exist_ok=True)

data = {
    "source_id": "B0183",
    "title": "Design History: A Students' Handbook",
    "author": "Hazel Conway (ed.)",
    "version": "Unwin Hyman，1987年第一版（1989年第二次印刷）；英国七位设计史学者集体编写",
    "type": "设计史学科方法论文册（P1）",
    "scope": "设计史研究方法导论：设计史基础（学科界定、史料、生存偏差、英雄叙事批判）、服装与纺织品、陶瓷史、家具史、室内设计、工业设计、平面设计、环境设计七个领域的研究方法、史料类型与学术史回顾",
    "duplicate_group": "无精确哈希重复；与B0440（Walker《Design History and the History of Design》1989）为互补姊妹篇（英语世界第一、二本设计史方法论导论），同一学科史对象只计一份P0；Heskett（Ch6作者）另著有B0189《Industrial design》，同作者不同书",
    "summary": "本书是英语世界第一部系统介绍设计史研究方法的入门著作（1987），由Hazel Conway主编、英国七位设计史学者集体编写，标志设计史学科的初步成熟。全书围绕“如何研究设计史”展开：Conway第一章界定学科边界（设计史关注“特定设计在其生产时期语境中”的理解而非孤立审美鉴赏）、史料类型（原始/二手）、生存偏差（幸存物品不具代表性）、英雄式叙事批判（heroic approach）；Heskett工业设计章提出“design as object/process/concept”三维框架并批判Pevsner 1937年“90%英国工业艺术毫无审美价值”的横扫性判断；后续各章（服装、陶瓷、家具、室内、工业、平面、环境）分别给出领域史料指南、研究陷阱与学术史回顾（Kirkham的Hepplewhite偶然性案例、Woodham的伪造辨识、Aynsley的符号学方法）。全书以案例展示研究路径：Richmond Park铸铁座椅、Volkswagen Beetle意义的语境转换、Ham House真伪辨识等，并持续引入女性主义与口述历史方法。",
    "strengths": [
        "0.1设计史学科界定的奠基手册：设计史关注“语境中的设计”而非孤立鉴赏、Heskett“design as object/process/concept”三维框架——0.1“设计是对象、活动还是制度”的学科方法论文献",
        "0.3英雄叙事批判的系统样本：heroic approach（名家名作主线）批判、日常设计/匿名设计/普通消费者所用之物的倡导、Hepplewhite“无足轻重小厂主”因遗孀图册留存被奉为伟大名字的偶然性案例",
        "0.4人工物如何成为史料的领域指南：生存偏差问题（幸存物通常是最贵最好的，日常用品已磨损丢弃）、实物一手经验（观察/触摸/测量）、伪造与复制辨识（Ham House 1670原品与1813仿品）、专利局记录",
        "0.5史料类型与一手经验：各章原始材料定位指南（博物馆、档案、专利局、贸易目录、广告、商业档案）、口述历史方法推荐、博物馆展陈本身带有解释性立场须批判审视",
        "0.6证据质量评估：Conway二手文献评估四标准（作者身份、初版日期、原始证据质量、注释完整性）、“生存偏差”作为普遍方法问题贯穿各章",
        "跨章可用：12.6女性维度（服装与女性历史不可分割、女性设计师“从历史中被隐藏”）；7.x现代运动史学批判（Pevsner/Read/Giedion谱系批判与第七章制度史可互参）",
        "案例密度高且可追溯：Richmond Park铸铁座椅、VW Beetle、Syon House、El Lissitzky Pelikan宣传册、Penguin封面等均有完整语境分析",
    ],
    "limits": [
        "欧洲中心：全书以英国/西欧经验为主体框架（作者自认），非西方传统仅提及未展开——0.7全球模型缺口侧",
        "1987年时效性：出版后设计史学已有重大发展（全球化研究、数字设计史、物质文化转向），方法论部分判断已过时",
        "章节整合度有限：各章作者学科背景差异导致方法论述缺乏统一理论语言（主编自认领域划分“在许多方面是人为的”）",
        "消费端薄弱：全书提示关注使用者但对消费者/使用者研究的系统论述不足",
        "源文件为扫描文本（OCR），第4/5章边界模糊，引用须返回纸质版页码",
    ],
    "checks": [
        "packet 00整体分析报告：命题一至六（语境理解、对象—过程—社会三维、风格分析必要不充分、跨学科、英雄叙事批判、原始材料一手经验）",
        "生存偏差：第1/2/4/5章反复出现（“很少有18世纪以前的服装标本幸存”“中下阶层家具大多无文献记录”）",
        "Heskett对Pevsner 1937年论断的批判（第6章）；Hepplewhite案例（第4章）",
        "Conway二手文献评估四标准（第1章）；Aynsley符号学方法（第7章）",
        "女性维度：第2/4/5/8章（服装与女性历史、女性设计师被隐藏）",
    ],
    "maps": [
        ["0.1", "A", "design_history_discipline_handbook", "设计史学科界定奠基手册：设计史关注“特定设计在其生产时期语境中”的理解而非孤立审美鉴赏；Heskett“design as object／process／concept”三维框架；风格分析必要但不充分——0.1“设计”概念与学科对象讨论的方法论文献", "1987年学科共识总结（方法论手册）；概念界定为编者/作者框架，须与其他定义论并置", "packet 00整体分析报告命题一、二、三", "ACCEPTED_AS_CORE_SOURCE"],
        ["0.3", "B", "heroic_approach_critique", "英雄式研究路径批判的系统样本：以名家名作（Adam、Wedgwood、Aalto、Dior）为主线的叙述方式批判、日常设计/匿名设计倡导、Hepplewhite偶然性案例（小厂主因遗孀图册留存被奉为伟大名字）——从英雄谱系到关系史的方法论依据", "方法论文献；批判立场为1980s学科共识，具体案例（Hepplewhite）有据", "packet 00整体分析报告命题五、第4章案例", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.4", "B", "survival_bias_and_object_evidence", "人工物史料化的核心方法问题：生存偏差（幸存物品不具代表性——通常是最贵最好的得以保存、日常用品已磨损丢弃）、实物一手经验（观察/触摸/测量）不可替代、伪造与复制辨识（Ham House 1670原品与1813仿品）、专利局记录作为制度痕迹", "领域案例（服装、家具）为作者举例；偏差原理具普遍性，应用于教材各章史料时须结合具体案例", "packet 00整体分析报告：生存偏差问题、伪造与复制问题", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.5", "B", "source_guides_and_oral_history", "史料类型与一手经验指南：原始材料定位（博物馆、档案机构、专利局、贸易目录、广告材料、商业档案）、口述历史方法（推荐用于20世纪研究）、博物馆展陈本身带有解释性立场须批判审视", "1987年指南性内容，机构信息（V&A、Ironbridge等）须核实现状；方法原则仍适用", "packet 00整体分析报告：原始材料的使用、口述历史", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.6", "C", "evidence_evaluation_criteria", "证据质量评估方法：Conway二手文献评估四标准（作者身份、初版日期、所依据原始证据质量、注释与参考文献完整性）；“生存偏差”作为普遍方法问题——0.6证据偏差的评估工具", "评估标准为教学工具，非实证研究；应用于教材写作时须与其他评估框架并置", "packet 00整体分析报告：二手文献的使用", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["12.6", "C", "women_in_design_history", "设计史的女性维度：服装与女性历史不可分割、女性在家具业被局限于缝纫工种、女性设计师“从历史中被隐藏”（Miller、Kirkham、Conway）——12.6女性主义设计批评的学科史资源（跨章）", "1980s女性主义史学初步成果；与Attfield（B0440）的系统批判并置", "packet 00整体分析报告：设计史中的女性维度", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
    ],
}

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("B0183 完成, maps =", len(data["maps"]))
