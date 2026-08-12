# 第三章 Plans 分析报告

## 一、章节定位与功能

本章在全书论证中承担"靶子建构"功能——系统地、同情地呈现Suchman将要批判的计划模型（planning model）。Suchman的策略不是漫画式地简化对手，而是从三个相互关联的理论支柱出发，展示计划模型在认知科学和人工智能研究中的内在逻辑与说服力：计划模型本身（行动由预先形成的计划决定）、言语行为理论（意图通过规约性规则表达）和背景知识概念（共享知识库使意图识别成为可能）。与此同时，本章在每个理论支柱的阐述之后都埋下了批判的种子——或通过指出"未解决的问题"，或通过呈现与该理论相悖的经验现象。这种"先立后破"的写法使第4章的情境行动替代方案建立在对其对手的充分理解之上，避免了稻草人谬误。本章还为第7章的案例分析提供了直接的技术背景——STRIPS/SHAKEY、NOAH等系统的设计原理正是专家帮助系统（第6-7章）所采用的计划模型的技术前身。

## 二、结构分析

本章由三个核心部分构成。第一部分（3.1 "The planning model"）阐述计划模型的基本逻辑：计划=实现预设目标的一系列行动；行动由前提条件（preconditions）和后果（effects）描述；计划生成（plan generation）与执行监控（execution monitoring）是两个核心环节。这一部分通过STRIPS/SHAKEY机器人系统和NOAH交互指令系统两个经典AI案例加以说明，最后在3.1.3节对计划的地位提出关键质疑——计划究竟是心理机制还是分析框架？第二部分（3.2 "Speech acts"）讨论言语行为理论如何被AI研究者采纳为沟通的"计划模型"——将语言理解为服务于说话者目标的行动，将言语理解视为计划识别（plan recognition）。通过Gumperz的办公室对话案例，Suchman揭示了言语行为理论在解释实际话语解释方面的局限性。第三部分（3.3 "Background knowledge"）剖析"共享背景知识"概念——从Schank和Abelson的脚本理论（scripts）到Garfinkel的学生实验——揭示"预设的共享知识"不仅是无限的而且是"由解释活动本身产生的"，而非预先存在的心理状态。

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

L050 计划作为行动的决定因素（Plans as Determinants of Action）：认知科学的基本假设——"计划是行动的前提条件并在每一个细节层次上规定行动"（"plans are prerequisite to and prescribe action, at every level of detail"）。在问题解决系统中，"行动由前提条件（行动能够发生所必须为真的事项）、效果（行动发生后必须为真的事项）和分解（行动如何执行的描述，通常是一系列子行动）来描述"（Allen 1984, p.126）。

L051 计划识别问题（The Problem of Plan Recognition）：如果行动是由计划决定的，那么理解他人行动就等同于识别其背后的计划。但Suchman指出致命困难——"同一"行动（如"开灯"）可通过无限多的物理行为实现，"取决于情境而非行动的定义属性"（Allen 1984, p.126）。行为与意图之间不存在一对一的映射关系。

L052 计划地位的混淆（The Confusion over the Status of Plans）：Suchman诊断出计划模型的核心问题——在研究文献中，"计划"在三种不同含义之间滑动：（1）分析者对行动的建构（研究者用来描述行动的框架）；（2）行动者的心理状态（头脑中实际存在并指引行为的表征）；（3）行动的指令/程序（可执行的详细操作步骤）。Miller、Galanter和Pribram（1960）明确将计划定义为"控制操作顺序的层级过程"并断言"对生物体而言，计划本质上等同于计算机的程序"，从而将三种含义合并为一。

L053 背景知识作为"被生成"而非"被预设"的（Background Knowledge as Generated, Not Pre-existing）：通过Garfinkel的学生实验（要求学生写下对话中"实际被理解的内容"），Suchman论证"背景假设"不是行动前就存在于头脑中的知识体，而是"当行动的前提被质疑时，由解释活动本身产生的"。Garfinkel的学生发现任务"不可能完成"——不是因为他们不够努力，而是因为"他们被要求做的不是对话参与者在实际对话中为达成共享理解而做的事"。

### 关键论点与案例

**STRIPS与SHAKEY**：L054 Fikes和Nilsson（1971）的STRIPS程序使用手段-目的分析（means-ends analysis）从目标状态反向推导至初始状态以生成计划。SHAKEY机器人在受控环境中执行该计划，由PLANEX程序监控。但Suchman指出PLANEX监控的是"世界模型"（world model）而非真实世界——只有当"累积误差"足够大时才通过摄像头重新校准。这一设计暴露了计划模型的核心问题：计划与世界的联系是脆弱且间接的。

**NOAH与交互指令**：L055 Sacerdoti（1977）的NOAH系统将计划模型扩展到交互情境。系统向用户提供指令，接受用户的"动机响应"（"为什么需要做这个？"）、"错误响应"（"这个指令无法执行"）以及"肯定/否定"（"这个步骤是否已完成？"）。Suchman关注NOAH中"用户理解"的问题——"系统将用户对'动作已完成'查询的肯定回复视为用户理解并成功执行了指令的证据"，但这恰恰预设了（而非证明了）共享理解的存在。

**Gumperz的办公室对话**：L056 两位秘书之间的简短交流——A问"你十分钟内会在这吗？"，B回答"去休息吧。想长一点也可以。"——展示了言语行为理论无法解释的是：B如何知道A实际上在询问自己是否可以离开去休息？"我们可以事后建构一个解释：在休息时间附近的办公室，秘书询问同事关于休息时段的计划"——但这种事后建构恰恰说明我们不知道B事前是如何做到的。规约性规则（felicity conditions）无法桥接"一般条件"与"特定情境"之间的鸿沟。

**脚本理论（Scripts）与日常知识**：L057 Schank和Abelson（1977）提出日常知识以"脚本"（scripts）形式组织——"定义了一个众所周知的典型情境的预定的、定型化的行动序列"。每个脚本都有其典型的"干扰"（distractions）、"障碍"（obstacles）和"错误"（errors）以及相应的补救措施。Suchman的批评是双重的：不仅"脚本极其众多"（餐厅脚本、生日派对脚本、足球比赛脚本……），而且将背景知识列举为脚本清单"每次都呈现为'如果作者有足够时间和篇幅就可以完成'的部分清单"——这是一种无限后退的逻辑困境。

## 四、逻辑梳理（论证链条+因果转折）

本章的论证链条以"展现问题—揭示困难—预埋伏笔"的节奏推进。

第一段论证（3.1）：Suchman首先公允地呈现计划模型——从Allen的经典定义到Miller、Galanter和Pribram的层级指令模型——展示其内在逻辑的一致性。然后通过STRIPS/SHAKEY的执行监控问题（"机器人无法区分世界模型和真实世界"）揭示第一个困难：计划与行动之间的差距。NOAH系统进一步表明，即使将"用户行为"纳入监控范围，系统仍然无法真正判断用户是否"理解"了指令。

第二段论证（3.2）：言语行为理论似乎提供了一个出路——如果意图通过规约性规则（conventional rules）表达，那么识别意图的问题就转化为识别规则的使用。但Gumperz的办公室对话案例展示了一个关键裂痕：规则能够解释"这是某种意图"（例如"这是一个请求"），但无法解释"这是关于休息的请求"——具体情境的细节永远超出规则的捕获范围。

第三段论证（3.3）：背景知识概念试图填补这个裂痕——如果共享知识提供了"不言自明"的内容，那么话语中的空白就有了填充物。但Garfinkel的学生实验揭示了一个深层逻辑困境：背景知识的"列举"不是对预先存在的心理内容的描述，而是一个无限生成的过程。"它不是说或想的事情太过庞大——而是说或想的行为本身就在扩展它，产生一个不断后退的理解地平线。"

关键因果转折点在于Suchman指出：计划的"模糊性"（vagueness）不是缺陷而是功能——"正是因为我们的计划本质上是模糊的——因为我们可以陈述意图而不必描述行动将实际采取的进程——意图性词汇对我们的日常事务才如此有用"。这意味着，试图"改进"计划使之更精确的认知科学方案恰恰瓦解了计划在实际生活中的作用。

## 五、材料使用方式

本章材料使用的突出特点是"双重焦距"——Suchman同时使用AI研究的技术文献（Allen 1984; Fikes & Nilsson 1971; Sacerdoti 1977; Schank & Abelson 1977）和来自社会科学的概念分析（Garfinkel 1967; Gumperz 1982b; Dreyfus 1982），使之相互对话。技术文献被用来展示计划模型的明确表述——Suchman通过大量直接引用（如Allen对行动的描述定义、Miller/Galanter/Pribram对计划的定义）让AI研究者"自己表述自己的立场"。社会科学文献则被用来揭示这些表述中的隐性困难。例如，Garfinkel的学生实验不是作为独立的社会学发现被引用的，而是在"背景知识"讨论的内部语境中，作为对Schank和Abelson脚本理论之逻辑困境的经验性证明被引入的。

这种材料组织方式使本章获得了跨学科论证的力量——Suchman不是从外部指责AI研究"错了"，而是从内部展示其理论承诺与经验现实之间的错位。

## 六、论辩与阐述方法

本章采用了四种核心论辩策略。第一，"同情性重构"（sympathetic reconstruction）：Suchman在批判之前充分呈现计划模型的内在逻辑和合理性——她承认计划模型"与西方理性传统一样古老"，是"行为科学的基础"——从而避免了简单的"打倒"姿态。第二，"概念辨析"（conceptual clarification）：在3.1.3节，Suchman精辟地将计划的三层含义（分析框架、心理状态、行动程序）区分开来，指出认知科学将这三层混淆在一起——这正是其错误的根源。第三，"极端案例测试"（limiting case test）：Garfinkel的学生实验作为"背景知识"概念的极端压力测试，展示了一个理论承诺在逻辑终点的崩溃。第四，"反向定义"（definition by inversion）：Suchman不断使用"不是……而是……"的句式结构——"计划不是行动的决定因素，而是行动的表述资源"——来建立分析距离。

## 七、语言文风（原文摘录+L###）

Suchman在本章的语言展现出精密的论证控制力——大量使用让步句（"while..."、"insofar as..."）来承认对方论点的合理部分，然后通过转折（"however..."、"but..."）引入关键限制条件。

L058 原文摘录：*"The planning model, however, takes over our common-sense preoccupation with the anticipation of action, and the review of its outcomes, and attempts to systematize that reasoning as a model for action itself, while ignoring the actual stuff, the situated action, which is the reasoning's object."*
中文阐释：这句浓缩了Suchman对计划模型的全部批判。"common-sense preoccupation"（常识性的关注）这一措辞暗示计划推理是日常生活中人们确实在做的事情——Suchman并非否认计划的存在或价值，而是指出认知科学将"关于行动的推理"误认为"行动本身的机制"。三个动词——"takes over"（接管）、"systematize"（系统化）、"ignoring"（忽略）——精确描绘了认知科学的操作流程：它吸收了常识实践，将之提升为科学模型，在此过程中排除了该模型试图解释的实际现象。

L059 原文摘录：*"The dependency of significance on a particular context, every particular context's open-endedness, and the essential ad hocness of contextual elaboration are resources for practical affairs, but perplexities for a science of human action."*
中文阐释：Suchman在此揭示了一个深刻的悖论——对日常行动来说至关重要的东西（情境的开放性、解释的灵活性），对试图建立关于行动的科学理论来说恰恰是最大的障碍。这句话的修辞力量来自"资源"（resources）与"困惑"（perplexities）的鲜明对比——同一组属性在不同目的下具有完全相反的价值。

L060 原文摘录：*"Garfinkel's exercise, as well as the phenomenology of experience, suggest that there is reason to question the view that background assumptions are part of the actor's mental state prior to action: As I dash out the door of my office, for example, I do not consciously entertain the belief that the floor continues on the other side, but if you stop me and ask me whether, when I charged confidently through the door, I believed that the floor continued on the other side, I would have to respond that indeed, I did."* (Suchman引述Dreyfus 1982, p.25)
中文阐释：通过Dreyfus的"冲出办公室的门"这一现象学案例，Suchman生动地说明：我们声称"相信地板在门后继续延伸"这一事实，并不意味着这种信念在行动前就存在于意识中。它是被"提问"这一行为召唤出来的，是事后解释的产物。

## 八、实体清单（六类每类≥3+L###）

### 核心概念

L061 手段-目的分析（Means-Ends Analysis）：从目标状态反向推导所需操作子及其前提条件的计划生成策略。

L062 计划识别（Plan Recognition）：基于观察到的行为序列推断行动者底层计划的过程——规划模型的"社交"延展。

L063 脚本（Scripts）：Schank和Abelson提出的概念——"定义了一个众所周知的典型情境的预定的、定型化的行动序列"。

### 关键人物/学者

L064 James Allen：AI研究者，其对行动的形式化定义（前提条件、效果、分解）被Suchman作为计划模型的标准表述加以引用。

L065 George Miller, Eugene Galanter, Karl Pribram：1960年《Plans and the Structure of Behavior》的作者，将计划定义为"控制有机体操作顺序的层级过程"，并将计划等同于计算机程序——这是Suchman批判的计划模型最极端的表述。

L066 Roger Schank & Robert Abelson：脚本理论的提出者，试图通过将日常情境类型化来形式化"常识知识"。

### 代表性案例/实验

L067 STRIPS/SHAKEY机器人：Fikes和Nilsson设计的计划生成与执行系统——SHAKEY机器人在受控房间环境中导航，PLANEX程序监控计划执行。

L068 NOAH交互指令系统：Sacerdoti设计的、将计划模型扩展到人机交互指令领域的系统。

L069 Garfinkel的学生实验（1967/1972）：要求学生完整写出对话中"实际被理解的内容"，结果表明这一任务"不可能完成"——背景知识不是预先存在的可列举内容。

### 关键文本/著作

L070 Miller, G., Galanter, E., & Pribram, K. (1960). *Plans and the Structure of Behavior*. New York: Holt, Rinehart and Winston.

L071 Sacerdoti, E. (1977). *A Structure for Plans and Behavior*. New York: Elsevier.

L072 Schank, R. & Abelson, R. (1977). "Scripts, plans and knowledge." In P. Johnson-Laird & P. Wason (eds.), *Thinking: Readings in Cognitive Science*.

### 技术系统/人工制品

L073 STRIPS（Stanford Research Institute Problem Solver）：使用手段-目的分析的计划生成程序。

L074 PLANEX：SHAKEY机器人的计划执行监控程序——监控"世界模型"而非真实世界。

L075 NOAH（Nets of Action Hierarchies）：Sacerdoti开发的交互式任务指令系统，使用"程序网"（procedural net）表示部分有序的行动层级。

### 理论流派/传统

L076 信息处理心理学（Information-Processing Psychology）：将认知视为符号运算的心理学流派，以Newell和Simon为代表。

L077 言语行为理论（Speech Act Theory）：Austin（1962）和Searle（1969）发展的语言哲学理论——将语言使用视为一种行动形式，受制于"满足条件"（felicity conditions）。

L078 现象学（Phenomenology）：以Heidegger和Merleau-Ponty为代表的大陆哲学传统，强调具身实践和前反思的理解，被Suchman（通过Dreyfus的解读）用作批判认知科学的哲学资源。

## 九、与前后章关联

**与前章（第2章）的关联**：第2章将交互性人工制品建构为分析对象，第3章则揭示了支配这类人工制品设计的理论框架——计划模型。第2章讨论的WEST系统（基于"学生模型"与"专家模型"的差异进行诊断）正是本章讨论的计划模型在教学领域的应用实例。第2章结尾关于Hayes和Reddy建议通过"明确约定"来修复对话误解的讨论，在第3章中被推广为"枚举背景知识"的问题，从而展示计划模型在沟通领域的系统性困难。

**与后章（第4章）的关联**：第3章与第4章构成全书核心的理论对立——计划模型（Ch.3）vs.情境行动（Ch.4）。第3章最后关于"情境的开放性和解释的特设性（ad hocness）是实践行动的'资源'而非'问题'"的论述，直接为第4章将"情境性"从"待消除的缺陷"重新定义为"行动的根本条件"提供了过渡。Garfinkel的学生实验在本章作为对"背景知识"概念的批判被引入，而在第4章同样的实验将被重新解读为对"行动意义不是在行动之前赋予的，而是在行动之中通过互动协商产生的"这一更宏大命题的支持。
