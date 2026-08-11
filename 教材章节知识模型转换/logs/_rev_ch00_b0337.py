# -*- coding: utf-8 -*-
"""BATCH-009 CH00 语义复核：B0337 Greenhalgh《Modernism in Design》。"""
import json
from pathlib import Path

p = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-009-CH00-INTRO\review_data\B0337_review.json")
p.parent.mkdir(parents=True, exist_ok=True)

data = {
    "source_id": "B0337",
    "title": "Modernism in Design",
    "author": "Paul Greenhalgh (ed.)",
    "version": "1990年出版；十篇专题论文＋主编长篇导言（英、美、意、比利时等多国学者）",
    "type": "学术论文集（P1）",
    "scope": "后现代视域下对设计“现代运动”的历史化审视：十九世纪遗产（Pugin/Ruskin谱系）、功能的神话（Benton）、法国家具界斗争1900—1930、德国现代主义室内的文化政治、美国西海岸先驱现代主义、英国推广现代主义1912—1944（BBC/DIA）、比利时Van de Velde与博览会、瑞典1930斯德哥尔摩展中间道路、意大利1945—1972家居转型、西班牙激进现代主义",
    "duplicate_group": "无精确哈希重复；与B0339（Greenhalgh《Ephemeral Vistas》已复核）为同作者不同书；瑞典Vackrare Vardagsvara对象与B0168/B0076等共享，同一对象P0只计一份；意大利反设计与B0143等共享对象",
    "summary": "本书由Paul Greenhalgh主编（1990），汇集十篇国别案例论文，在后现代已然来临的视域中对现代主义设计进行历史化、复杂化审视。导言区分“先驱现代主义”（1920—1933）与“国际风格”（1933—1970s），概括现代运动的十二项核心信条，论证现代运动从理想主义到实用主义、道德—技术—美学三位一体被撕裂的转变。各章：Pugin/Ruskin的道德谱系论（Ch1）、Benton解构“form follows function”为英国批评界发明（Ch2）、法国新艺术因国民品位（bon goût）意识形态被扼杀（Ch3）、德国素朴美学的阶级符号功能（Ch4）、加州现代主义早于欧洲的修正论（Ch5）、BBC广播推广现代主义失败于美国商业文化（Ch6）、Van de Velde在布鲁塞尔1935与巴黎1937的反差（Ch7）、瑞典Vackrare Vardagsvara中间道路（Ch8）、意大利从战后人道主义到消费主义奢侈品（Ch9）、西班牙佛朗哥下的激进现代主义语言抵抗（Ch10）。全书以“复杂化”为目标，拒绝将现代主义本质化，自觉挑战Pevsner—Banham—MoMA的欧洲中心叙事。",
    "strengths": [
        "0.2现代主义概念历史化的核心资源：导言区分“先驱现代主义”与“国际风格”两个阶段、十二项信条（去隔间化、社会道德、真理、总体艺术作品、技术、功能、进步、反历史主义、抽象、国际主义、意识转化、神学性），“Modern不再等于contemporary”——现代性分期与概念边界讨论的A级文献",
        "0.2功能主义概念考古：Benton“功能的神话”——form follows function实为英国批评界发明，勒-柯布西耶本意被英译本扭曲——现代主义核心概念的生成史证据",
        "0.3去中心化关系史：十国案例并置（法/德/比/英/瑞/美/意/西），挑战Pevsner—MoMA单一谱系（加州Gill反装饰早于Loos三年、Schindler Lovell海滩住宅早于Villa Savoye八年）——从英雄谱系到多中心关系史的方法论样本",
        "0.5接受史与媒介证据：Holder用BBC广播听众来信证明现代主义推广失败于美国商业文化——“媒介推广—受众接受”证据链的设计范例",
        "0.6反本质主义史学立场：主编明言“这些论文意在使其复杂化”，不同作者立场并置不统一——0.6史学争议与解释多样性的教学样本",
        "跨章可用：Ch8瑞典中间道路（Vackrare Vardagsvara）为7.6北欧制度基础的关键机制；Ch9意大利从理想主义到消费主义及1968—69反设计为11.3意大利激进设计的转型叙述",
        "原始文献密集：Pugin 1841《真正原则》、Ruskin《七盏灯》、Le Corbusier原文、Paulsson 1919宣言等引文均附行号，可追溯",
    ],
    "limits": [
        "论文集体裁：各章为独立署名案例研究，非统一结论；主编导言框架与各章立场并存，引用须区分",
        "国别案例的选择性：聚焦欧美的十国案例，东亚、拉美、非洲现代主义未覆盖（0.7全球模型的缺口侧）",
        "1990年出版时点的“后现代”视域：部分判断（如国际风格终结）带时代立场，须标注",
        "修正史观本身是论辩性主张：加州“早于”欧洲等比较命题依赖断代与定义，教材引用须注明为作者论证",
        "理论化程度高（本雅明、克拉考尔、商品拜物教等），作为史料使用时其分析范畴（Sachlichkeit、Phantasmagoria）须与档案史实分层",
    ],
    "checks": [
        "packet 00整体分析报告 L003：核心论题与十项关键论点（道德谱系论、功能主义虚构论、风格即政治论、阶级符号论、地域修正论、媒介失败论等）",
        "L004：两重因果转折（约1929—1933先驱→国际风格；约1968—1972意识形态危机）",
        "L007原文摘录：Greenhalgh“Modern no longer means contemporary”、Pugin 1841两大规则、Paulsson 1919“workers should take joy in their work”",
        "L008实体清单：Pevsner 1936、Hitchcock & Johnson 1932、Banham 1960等叙事谱系文献",
        "L009方法论特征：去中心化、政治化解读、接受史转向、地域主义正名、媒介研究先驱",
    ],
    "maps": [
        ["0.2", "A", "modernism_concept_historicization", "现代主义概念的历史化框架：先驱现代主义（1920—1933）与国际风格（1933—1970s）两阶段分期、十二项信条、“Modern不再等于contemporary”——现代性/现代化/现代主义概念边界的核心资源", "主编导言框架（Greenhalgh命题），各章案例可证局部；分期断代有论辩性，教材须标注", "packet L003、L007 Greenhalgh引言", "ACCEPTED_AS_CORE_SOURCE"],
        ["0.2", "B", "myth_of_function_concept_genealogy", "功能主义概念考古：Benton证明“form follows function”为英国批评界的发明而非现代主义建筑师本意，勒-柯布西耶本意被英译本扭曲——“功能主义”概念生成史的修正论", "作者论证主张（Benton章），概念史结论须与建筑原始文献互校", "packet L003论点2、L007 Taut/Read引文", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.3", "B", "decentered_multi_national_design_history", "去中心化的现代主义史样本：十国案例并置（法/德/比/英/瑞/美/意/西）、加州现代主义早于欧洲的修正论、自觉挑战Pevsner—MoMA单一谱系——从英雄谱系到多中心关系史的方法论范例", "论文集体裁：各章独立署名；“早于”类比较命题依赖断代定义，须注明为作者论证", "packet L003论点5、L009方法论特征1与4", "ACCEPTED_AS_SUPPORTING_SOURCE"],
        ["0.5", "C", "reception_history_and_media_evidence", "接受史与媒介证据设计：BBC广播听众来信、DIA季刊、企鹅丛书出版记录证明现代主义推广失败于美国商业文化（“BBC作为民族之音无法对抗英国品位的美国化”）——媒介—受众证据链范例", "单案例（英国1912—1944）研究；效果判断依赖来信样本，样本代表性须注明", "packet L003论点6、L005材料方式3", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["0.6", "C", "anti_essentialist_historiography", "反本质主义史学立场样本：主编明言“这些论文意在使其复杂化”，各章立场并置不统一（Shand宗族主义式瑞典赞美与Wollin工艺保守主义并列）——0.6史学解释多样性与争议的教学样本", "作为史学方法立场引用，非史料；与B0388式史学批判并置教学", "packet L003核心论题、L006论辩方法6", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["7.6", "C", "swedish_middle_path_vackrare_vardagsvara", "瑞典现代主义中间道路：Vackrare Vardagsvara（更美的日常用品，Paulsson 1919）在工艺传统与工业理性之间取得平衡，1930斯德哥尔摩展“可被接受的现代面孔”——北欧制度基础的功能机制（跨章）", "单章案例（Naylor）；与B0168/B0076北欧对象共享只计一份P0", "packet L003论点8、L007 Paulsson引文", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
        ["11.3", "C", "italy_idealism_to_consumerism_transition", "意大利设计转型叙述：1945—1972从战后社会理想主义（Rogers“人类之家”）到1958—1963经济奇迹的消费主义奢侈品，直至1968—69“反设计”起义——意大利激进设计的历史前提（跨章）", "单章案例（Sparke）；与B0143/B0044等意大利对象共享只计一份P0", "packet L003论点9、L004第二重转折", "ACCEPTED_AS_CONTEXTUAL_SOURCE"],
    ],
}

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("B0337 完成, maps =", len(data["maps"]))
