# 第二章 Interactive Artifacts 分析报告

## 一、章节定位与功能

本章在全书论证中承担"对象构造"功能——将"交互性人工制品"（interactive artifacts）建构为一个需要理论分析的对象类别。Suchman的目标不是直接展开对计划模型的批判（那是第3章的任务），而是首先回答一个前提性问题：为什么计算机会被视为"交互的"对象？她从三种属性（反应性、语言性、内部不透明性）入手，论证计算机的独特性质使得人们倾向于用"交互"而非"使用"来描述人与计算机的关系。本章还区分了"自解释人工制品"（self-explanatory artifacts）的两种含义——作为设计意图可被用户发现的可使用工具，以及作为能够像人一样解释自身的智能实体——从而揭示实用性的指令设计问题如何通向理论性的机器智能问题。本章在逻辑上为第3章对计划模型的批判提供了靶子（计划模型正是将第二种含义推向极端的理论框架），同时其讨论的ELIZA程序和Turing测试直接预示了第7章案例分析的诸多发现。

## 二、结构分析

本章分为三个主要部分。第一部分（2.1 "Automata and cognitive science"）追溯自动机（automata）的历史渊源和认知科学的基本前提——智能可以从人脑中抽象出来并在其他物理基底上实现。第二部分（2.2 "The idea of human-computer interaction"）分析计算机的三种交互属性：反应性（reactivity）、语言性（linguistic control）和内部不透明性（internal opacity）。Suchman在此讨论了Hayes和Reddy关于"优雅交互"（graceful interaction）的研究，以及自然语言交互与工具使用两种范式的张力。第三部分（2.3 "Self-explanatory artifacts"）区分了自解释人工制品的两种含义，通过WEST计算机教练系统和ELIZA/DOCTOR程序这两个案例，展示实用指令问题如何与机器智能理论问题交织在一起。

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

L023 计算机作为"唤起性对象"（Computer as Evocative Object）：Suchman借用Turkle的概念指出，计算技术人工制品"唤起"了关于人工制品与智能他者之间区别的新问题。计算机挑战了"物理的"（被设计、制造、使用的）与"社会的"（与之进行沟通的）之间的传统二分法。

L024 交互性的三种属性（Three Properties of Interactive Artifacts）：Suchman提出计算机之所以被视为交互对象，是因为它具备三种独特属性。（1）反应性：用户每个行动都会触发机器的即时反应，这与早期批处理形成对比。（2）语言性：对计算机的控制越来越通过语言（自然语言或类语言指令）而非机械操作来实施。（3）内部不透明性：计算机的整体行为不可通过局部事件来描述，这种复杂性使得人们被迫使用意图性词汇（intentional vocabulary）来谈论机器的"行为"。

L025 自解释人工制品的两种含义（Two Senses of Self-Explanatory Artifacts）：第一种含义——工具的设计应使其预期用途可以被用户发现（古老的设计问题）。第二种含义——人工制品能够像人一样"解释自己"（即展示对其行为的理性可说明性）。Suchman指出，正是第二种含义将实用的指令设计问题与理论性的机器智能问题绑定在一起。

### 关键论点与案例

**WEST计算机教练系统**：L026 Burton和Brown设计的WEST系统试图模拟人类教练的诊断能力——通过观察学生的行为（而非直接提问）来推断学生的知识状态。该系统在学生玩"How the West Was Won"算术游戏时，将学生的每一步与假设的专家模型进行比较，累积证据以识别需要指导的技能缺陷，并在"适当的时机"（tactically opportune moments）插入建议。Suchman注意到WEST的设计体现了对人类教练"少说多观察"策略的洞察，但也指出"从学生的行为中直接识别问题"比预期困难得多。

**ELIZA与DOCTOR程序**：L027 Weizenbaum的ELIZA程序（特别是DOCTOR脚本，模拟Rogerian治疗师）在本书论证中占据关键位置。Suchman详细分析了DOCTOR如何"利用"人类对话者赋予计算机回应的意义——用户将计算机看似奇怪的回答理解为"必定有某种精神病学意图"。这是Karl Mannheim首先提出的"文献解释法"（documentary method of interpretation）的体现：人们将表面现象视为某种被归因的底层现实（underlying reality）的证据（document），同时又用这个被归因的现实来解释这些表面现象。

L028 Turing测试与理性可说明性（Turing Test and Accountable Rationality）：Suchman重新解读了Turing测试，指出其核心不是机器"真的在思考"，而是机器的行为在观察者看来是"可说明地理性的"（accountably rational）。这一解读将"智能"的标准从内部机制转移到交互表面，从而将智能问题转化为交互问题。

## 四、逻辑梳理（论证链条+因果转折）

本章的论证逻辑呈螺旋上升的结构。

第一层：Suchman从历史角度追溯了自动机传统——从古希腊的自主移动雕像，到18世纪de Vaucanson的机械鸭，再到de la Mettrie的《人是机器》——从而将认知科学"智能可以从生物基底中抽象出来"的前提历史化，暗示这一前提并非科学事实而是文化传统的延续。

第二层：Suchman从三个属性论证计算机被视为交互对象的合理性。关键逻辑转折在于：这些属性的结合产生了一个悖论——计算机既因其反应的可预测性而被视为有目的的行动者，又因其内部的不透明性和偶尔的"惊喜行为"避免了"完全可预测=机械"的贬低。

第三层：自解释人工制品的两种含义之间的张力构成关键论证转折。第一种含义延续了古老的工具设计传统，第二种含义则是计算机技术独有的。Suchman通过ELIZA案例展示：当机器能够利用人类"寻找意义"的天然倾向时，它可以制造交互的假象——但这本质上不是机器的智能，而是人类对话者的"文献解释"工作。

第四层：本章埋下了一个贯穿全书的伏笔——"优雅交互需要检测和修复误解的能力"（Hayes和Reddy的观点）。Suchman接受了这一诊断，但在后续章节将揭示：问题不是尚未找到正确的修复算法，而是人机之间在获取交互情境资源方面存在根本的不对称性。

## 五、材料使用方式

本章的材料使用呈现显著的历史—概念双重结构。历史材料方面，Suchman引用McCorduck的《机器思维者》（1979）追溯自动机历史，展示自动化思想的悠久谱系。技术材料方面，她详细描述了STRIPS/SHAKEY系统的架构（但完整展开在第3章）和WEST、ELIZA程序的工作原理。概念材料方面，她大量援引Hayes和Reddy（1983）关于"优雅交互"的论述，以及Dennett（1978）关于"意图性立场"（intentional stance）的哲学论证，特别是后者关于内部不透明性使得意图性解释"不可避免"的观点。值得注意的是，Suchman在这一章中基本采取"中立描述"的姿态——引用AI研究者的观点时不立即反驳，而是让材料本身揭示内部矛盾（如Hayes和Reddy既承认现有系统远未达到优雅交互的标准，又声称单个组件"并非远超当前技术水平"的乐观判断）。

## 六、论辩与阐述方法

Suchman在本章运用了三种核心论辩策略。第一，"谱系学悬置"（genealogical suspension）：通过追溯自动机的历史，将认知科学的基本前提（智能=符号处理）去自然化，揭示其历史偶然性。第二，"内部批判"（immanent critique）：不直接攻击AI研究者的目标（优雅交互），而是通过详细引述其自身的问题诊断（如Hayes和Reddy列举的所需能力清单），暴露研究纲领的内部困难。第三，"案例分析中的理论结晶"：WEST和ELIZA不仅是技术系统的描述，更被Suchman用作理论命题的载体——WEST体现了"观察行为以推断知识"的困难，ELIZA体现了"文献解释法"的力量与局限。这种将技术案例理论化的写作策略是全书方法论的预演。

## 七、语言文风（原文摘录+L###）

Suchman在本章的语言兼具技术精确性和哲学反思性，大量使用意图性词汇（intentional vocabulary）来描述机器行为，但同时保持分析距离。

L029 原文摘录：*"Marginal objects, objects with no clear place, play important roles. On the lines between categories, they draw attention to how we have drawn the lines. Sometimes in doing so they incite us to reaffirm the lines, sometimes to call them into question, stimulating different distinctions."* (引自Turkle, p.31)
中文阐释：Suchman以Turkle的这句话作为章节引语，奠定了本章的核心主题——计算机是"边缘对象"，它位于"人工制品"和"智能他者"之间的模糊地带，正是这种模糊性迫使人们重新审视既有的范畴划分。引语中的"有时让人 reaffirm 界限，有时让人质疑界限"精确预示了AI领域内部关于"模拟人际对话"还是"承认机器的非人属性"的争论。

L030 原文摘录：*"The overall behavior of the computer is not describable, that is to say, with reference to any of the simple local events that it comprises; it is precisely the behavior of a myriad of those events in combination that constitutes the overall machine. To refer to the behavior of the machine, then, one must speak of 'its' functionality. And once reified as an entity, the inclination to ascribe actions to the entity rather than to the parts is irresistible."*
中文阐释：这是Suchman对计算机"内部不透明性"最精辟的表述。她揭示了从"局部事件的组合"到"机器自身的功能"到"'它'的行为"的语义转化过程——这是一个逐渐"物化"（reification）的过程，最终使得人们难以避免地使用意图性语言来描述机器。

L031 原文摘录：*"Intentional explanations relieve us of the burden of understanding mechanism, insofar as one need assume only that the design is rational in order to call upon the full power of common-sense psychology and have, ready at hand, a basis for anticipating and construing an artifact's behavior."*
中文阐释：Suchman在此借用Dennett的"意图性立场"理论，解释为什么人们倾向于用意图来解释计算机行为——这减轻了理解底层机制的认知负担。但她同时暗示这种"便利"是有代价的：它掩盖了机器与人在获取交互资源方面的根本差异。

## 八、实体清单（六类每类≥3+L###）

### 核心概念

L032 反应性（Reactivity）：计算机对用户行动的即时反馈，使得实时控制成为可能。

L033 内部不透明性（Internal Opacity）：计算机整体行为无法通过局部事件描述的属性，促使用户采用意图性解释。

L034 文献解释法（Documentary Method of Interpretation）：Mannheim首先提出、Garfinkel加以发展的概念——人们将表面现象视为底层现实的"文献"或"证据"，同时用该底层现实来解释表面现象。

### 关键人物/学者

L035 Sherry Turkle：MIT社会学家，《The Second Self》（1984）作者，研究计算机对儿童自我认知的影响。

L036 Joseph Weizenbaum：MIT计算机科学家，ELIZA程序的创建者，尽管ELIZA表现出表面上的"对话能力"，Weizenbaum本人坚决否认其具有智能。

L037 Daniel Dennett：哲学家，提出"意图性立场"（intentional stance）理论，被Suchman借鉴来解释人们如何以及为何将意图归因于机器。

### 代表性案例/实验

L038 ELIZA/DOCTOR程序：Weizenbaum设计的自然语言对话程序，DOCTOR脚本模拟Rogerian治疗师。用户在与DOCTOR交互时倾向于将机器回应解读为有意义的治疗性干预。

L039 WEST计算机教练系统：Burton和Brown设计的智能教学系统，通过观察学生学习算术游戏的行为来诊断其知识缺陷并提供适时指导。

L040 Turing测试：Turing 1950年提出的机器智能测试——如果问询者无法区分机器回答与人类回答，则该机器应被视为具有智能。

### 关键文本/著作

L041 Turkle, S. (1984). *The Second Self: Computers and the Human Spirit*. New York: Simon and Schuster.

L042 Hayes, P. & Reddy, D. R. (1983). "Steps toward graceful interaction in spoken and written man-machine communication." *International Journal of Man-Machine Studies*.

L043 Weizenbaum, J. (1983). "ELIZA: a computer program for the study of natural language communication between man and machine." *Communications of the ACM*.

### 技术系统/人工制品

L044 ELIZA程序系列：包括DOCTOR在内的多个脚本，是早期自然语言处理的标志性项目。

L045 WEST系统：基于专家模型差异诊断的智能教学系统，运行于"How the West Was Won"游戏环境。

L046 SCHOLAR系统：Carbonell（1971）开发的对话系统，在有限领域内展示了对用户输入的敏感性。

### 理论流派/传统

L047 认知科学（Cognitive Science）：将心智视为可在多种物理基底上实现的信息处理系统的跨学科纲领。

L048 意图性立场理论（Intentional Stance Theory）：Dennett提出的解释策略——通过将意图、信念和欲望归因于系统来预测其行为，而不必理解其内部机制。

L049 人机交互研究（Human-Computer Interaction / HCI）：研究人与计算机系统之间交互的设计和评估的交叉学科领域。

## 九、与前后章关联

**与前章（第1章）的关联**：第1章提出了"计划模型混淆了计划与情境行动"的核心论题，第2章将这一抽象论题落地——具体展示了计算机为何被视为"交互的"对象，从而解释了计划模型为何在人机交互设计中具有"天然的"吸引力。第1章提出的"artifact as test of theory"在本章通过ELIZA和WEST的具体分析获得了初步例示。

**与后章（第3章）的关联**：第2章最后关于自解释人工制品的讨论——特别是"机器应能以可说明地理性的方式行为"——直接引向第3章对计划模型的系统考察。ELIZA案例在本章中被用来展示"文献解释法"的作用，但Suchman保留了关键的分析结论供第3-4章展开：即认知科学将"计划"等同于"行动机制"是错误的。第2章结尾处对Hayes和Reddy"修复对话中的误解"方案的讨论，为第5章（人类对话中的修复机制）和第7章（人机交互中的修复失败）预埋了问题线索。
