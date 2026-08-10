# Chapter_04_Cognitive Aspects_分析报告

## 一、章节定位与功能

L001 本章是"理解用户"三部曲（第4-6章）的第一部，专门处理人类认知的各个方面及其对交互设计的启示。在全书结构中，第1章建立了交互设计的基本概念框架，第2章提供了设计流程，第3章引入概念化思维——而本章为这些方法论提供了人类认知能力的"科学基础"。本章的核心功能是回答一个基本问题：人类擅长什么和不擅长什么，以及这些知识如何指导我们设计既扩展人类能力又弥补人类弱点的技术。

L002 本章在全书中承担着"心理学基础层"的角色——它为后续所有关于可用性（第1章）、界面设计（第7章）、数据收集与分析（第8-10章）和评估（第14-16章）的讨论提供了认知科学的理论依据。例如，第1章提出的"memorability"可用性目标在本章第4.2.3节中获得全面的认知心理学阐释；第3章的Gulf of Execution and Evaluation模型在本章4.3.2节被详细展开。本章还是读者理解"为什么某种界面设计有效或无效"的关键——认知限制（注意力瓶颈、记忆负荷、学习曲线）解释了为什么某些设计违反用户的自然认知倾向。

L003 本章对第5章（社交互动）和第6章（情感交互）起着"先导作用"——作者在引言中明确指出："Other ways of conceptualizing human behavior that focus on the social and emotional aspects of interaction are presented in the following two chapters."这意味着第4-6章共同构成了交互设计中"人的维度"的完整图景：认知（第4章）→社会（第5章）→情感（第6章）。

## 二、结构分析

L004 本章共3大节，形成"认知是什么→认知过程详解→认知理论框架"的三层递进：

- **4.1 Introduction**：以极具代入感的多任务切换叙事（写报告→回短信→刷Facebook→接电话→看球赛→回WhatsApp→惊慌地发现已到午夜）开篇，引出"注意力持续在多任务间切换"的当代认知现象，以及认知科学对理解这一现象的重要性。

- **4.2 What Is Cognition?**：认知定义与过程分析。引入两种认知模式的区分：体验式vs.反思式（Norman, 1993）和快速vs.慢速思维（Kahneman, 2011），以21×19的心算vs.笔算为例展示两种模式的区别。随后依次展开6个认知过程子节：
  - 4.2.1 Attention（注意力）：含明确目标（4.2.1.1）、信息呈现（4.2.1.2，以Tullis（1997）的酒店信息检索实验为核心案例）、多任务处理（4.2.1.3，含开车使用手机的DILEMMA）
  - 4.2.2 Perception（感知）：信息分组（边框vs.颜色对比）、白空间（white space）原则
  - 4.2.3 Memory（记忆）：包含个人信息管理（PIM）、Miller的7±2理论（BOX 4.1）、密码记忆负荷（BOX 4.2数字遗忘）
  - 4.2.4 Learning（学习）：附带学习vs.有意学习、通过做来学（learning through doing）
  - 4.2.5 Reading, Speaking, and Listening（阅读、说话与聆听）：三种语言处理模式的对比
  - 4.2.6 Problem-Solving, Planning, Reasoning, and Decision-Making（问题解决与决策）：快速节省启发式vs.理性决策、含DILEMMA（App一代的决策依赖）

  每个认知过程后附"Design Implications"设计启示框，直接转化理论为实践建议。

- **4.3 Cognitive Frameworks**：六大认知框架的综述：
  - 4.3.1 Mental Models（心智模型）：恒温器与烤箱的误解案例、Valve Theory vs. On-Off Switch
  - 4.3.2 Gulfs of Execution and Evaluation（执行与评估鸿沟）：Whitenton（2018）蓝牙耳机连接困境的当代案例
  - 4.3.3 Information Processing（信息加工）：人类处理器模型（Card et al., 1983）
  - 4.3.4 Distributed Cognition（分布式认知）：航空驾驶舱作为认知系统的经典案例
  - 4.3.5 External Cognition（外部认知）：记忆负荷降低、计算卸载、注释与认知追踪
  - 4.3.6 Embodied Interaction（具身交互）：Dourish（2001）、Kirsh（2013）的舞者"marking"研究

L005 结构特征：4.2节采用"认知过程逐一介绍+每个过程附带Design Implications"的标准化格式，这种重复性结构为读者建立了可预测的学习节奏。4.3节则从"大脑内部"的信息加工模型逐步过渡到"大脑外部"的分布式认知、外部认知和具身交互框架，呈现出从"内在主义"到"情境主义"的认知科学范式转换。

## 三、内容分析（核心论题+关键论点与案例）

L006 **核心论题一**：人类的认知能力有其固有的优势和局限——了解这些优势和局限是交互设计的基础。设计应既扩展人类能力（认知增强），又弥补人类弱点（认知辅助）。

L007 **核心论题二**：认知并非仅仅发生在大脑内部——分布式认知、外部认知和具身交互等框架表明，认知分布在人、人工物和环境之间，交互设计应利用外部表征和物理工具来减轻认知负荷、支持创造性思维。

**关键论点**：

L008 （1）**两种认知模式的区分具有设计意义**。体验式认知（experiential cognition）是直觉的、轻松的、自动化的——开车、读书、交谈；反思式认知（reflective cognition）需要心理努力、注意力和判断力——设计、学习、写作。Kahneman的"快思维与慢思维"与之平行。为体验式活动设计的界面应流畅无阻，为反思式活动设计的界面应提供信息支持和决策辅助。

L009 （2）**注意力的有限性是界面设计中最关键的认知约束**。Tullis（1997）的经典实验表明，同样密度的信息，通过垂直分类和适当的列间距可将搜索时间从5.5秒降至3.2秒——差异源于信息分组而非信息量。多任务处理的代价是显著的：Bowman et al.（2010）发现即时通讯使阅读教科书的时间增加50%。开车使用手机即使使用免提设备也同样危险，因为"视觉意象竞争同样的处理资源"。

L010 （3）**人类更擅长识别（recognition）而非回忆（recall）**。这一基本认知事实对界面设计具有深远影响——菜单、图标和一致放置的对象应支持视觉扫描和识别，而非要求用户从记忆中检索操作序列。Miller的7±2理论被大量误用——菜单不必限制为7个选项，因为菜单项可被反复扫描而无需从短期记忆中回忆，这与听到一次后就需回忆的数字串是完全不同的任务。

L011 （4）**技术正在改变记忆的本质**。Sparrow et al.（2011）的经典研究表明，预期有互联网可访问会降低人们记忆信息本身的意愿，但增强他们对"在哪里可以找到"的记忆——互联网正在成为"认知假体"（cognitive prosthesis）。密码认证造成的记忆负荷极大（银行要求随机的第N个字符），推动了生物识别技术（面部ID、指纹）取代密码的趋势。

L012 （5）**心智模型（Mental Models）可能系统性地错误**。人们在日常生活中发展出的"核心抽象集"（如"阀门理论"——越多等于越多）被不加区分地应用于各种设备——将恒温器设到最高不会使房间更快变暖（恒温器是开关式而非阀门式），但大多数人持相反信念。这一发现对用户教育和界面透明性设计具有深远意义。

L013 （6）**认知分布在人类-人工物-环境之间，而非局限于大脑内部**。航空驾驶舱的分布式认知分析显示，飞行高度的信息在不同媒介间传播（无线电口述→飞行员心理→仪表旋钮），设计的核心任务是确保信息的"传播"不被中断。外部认知则强调外部表征（购物清单、便签笔记）的认知功能——通过注释和认知追踪（如重新排列扑克牌）来减轻记忆负担。

L014 （7）**具身交互理论表明我们"用身体思考"**。Kirsh（2013）对舞者的研究表明，"marking"（用简化动作部分模拟舞蹈）优于完整排练和心理模拟——因为前者降低了"心理复杂性"而非仅仅是节省体力。这暗示着"与其开发完整的VR模拟来教高尔夫，不如设计增强现实的简化动作教学系统"。

**关键案例**：

L015 （1）**Tullis（1997）酒店信息检索实验**：两张包含相同信息密度的酒店信息屏幕——一张按垂直类别分组（地点、住宿类型、电话、价格），另一张信息混杂——搜索时间分别为3.2秒和5.5秒。该案例展示了信息呈现方式对注意力绩效（进而对可用性）的决定性影响。图4.1提供了两张屏幕的对比。

L016 （2）**开车使用手机的DILEMMA分析**：Caird et al.（2018）的元分析显示手机通话使司机对外部事件的反应时间延长。关键发现是"免提并不比手持更安全"——因为认知处理（视觉意象）的性质相同，而非物理操作的区别。车内乘客与远程通话者的关键区别在于前者能观察路况并适时停止交谈——这是一个"情境共享"问题。

L017 （3）**恒温器与烤箱的心智模型误解**（Activity 4.4）：大多数人错误地认为将恒温器调到最高能加速升温——这是一种基于"阀门理论"的错误心智模型。恒温器和电烤箱都是开关式工作（到达目标温度后切断），但大多数人的心智模型将它们与"越多转动越多输出"的水龙头混淆。

L018 （4）**Miller的7±2的误用**（BOX 4.1）：一些设计师将此理论误解为"菜单只能有7个选项""只能有7个标签"等，但Bailey（2000）指出这些全部是视觉扫描任务（而非短期记忆回忆任务），因此7±2的限制不适用。

L019 （5）**Mrs. B与SenseCam（BOX 4.2）**：Hodges et al.（2006）描述了一位失忆症患者佩戴Microsoft Research开发的SenseCam（自动拍照的可穿戴相机）后，对事件的回忆能力增加了近三倍——从数天内完全遗忘到几乎能记住所有细节。

L020 （6）**航空驾驶舱的分布式认知分析**（图4.9）：飞行员、机长和空中交通管制员之间通过无线电、仪表旋钮、视觉观察等多个媒介传播"改变高度"的信息——分析这些信息如何在不同表征状态之间转换，为驾驶舱显示设计提供改进建议。

## 四、逻辑梳理（论证链条+因果转折）

L021 本章的论证结构可分为两大逻辑板块：

**板块一（4.1-4.2）：认知过程的"是什么→为什么重要→如何设计"循环**。4.1以生动的多任务叙事建立"注意力是稀缺资源"的直觉认知。4.2随后系统展开6个认知过程，每个过程遵循同一模板：定义认知过程→展示心理学研究发现→讨论其对交互设计的启示→提供具体的设计建议（Design Implications框）。这一模板化论证确保了理论到实践的每个转化步骤都清晰可见。

L022 **板块二（4.3）：从"内在"到"外在"的认知框架演进**。4.3的六个框架呈现出一个有意的理论演进轨迹：心智模型（4.3.1）和鸿沟理论（4.3.2）仍以内在于个体的心理过程为焦点→信息加工模型（4.3.3）到达"内部主义"的巅峰（将心智类比为计算机）→分布式认知（4.3.4）实现第一次"外部转向"（分析认知系统而非个体心智）→外部认知（4.3.5）进一步聚焦外部表征的认知功能→具身交互（4.3.6）将身体和物理环境纳入认知的核心。这一演进轨迹反映了HCI领域从"认知主义"到"后认知主义"的范式转换。

L023 **因果转折与限定**：
- 4.2.1.3中对多任务处理的讨论呈现了"两面性"——Lotteridge et al.（2015）发现如果分心源与任务相关，多任务处理不一定有害，由此限定了"多任务总是有害"的简单结论。
- 4.2.3中BOX 4.1对7±2神话的祛魅是一个关键的"纠正"时刻——作者主动澄清被广泛误用的理论，引导读者建立更精确的认知。
- 4.3中从信息加工模型到分布式/外部/具身认知的过渡，本质上是对"认知仅发生在大脑内部"这一假设的批判性超越——每一后续框架都包含对前一框架局限性的隐式批评。

## 五、材料使用方式

L024 （1）**叙事性开篇（Narrative Opening）**：4.1节的多任务崩溃叙事是全书最生动的章节开篇之一——"你瞥了一眼笔记本电脑上的时间。午夜了。你真的恐慌了..."——这段接近意识流的叙事将抽象的"注意力"概念嵌入到读者可切身感受的日常经验中，具有极强的教学感染力。叙事中每一个打断（短信→Facebook→电话→WhatsApp→体育比分）都精确展示了注意力切换的代价。

（2）**DILEMMA**：本章的两个Dilemma（开车使用手机，4.2.1.3；App一代的决策依赖，4.2.6）均涉及当代日常生活中具有争议性的技术使用问题，鼓励学生权衡安全与便利、自主与依赖之间的复杂关系。

（3）**Design Implications框**：这是本章最独特的教学材料——每个认知过程后附有一个专门的"Design Implications"框，将心理学理论直接转化为可操作的设计建议。这些框以项目符号列表呈现（如"Use techniques...such as animated graphics, color, underlining, ordering of items, sequencing of different information, and spacing of items"），满足了读者"理论如何用于实践"的核心需求。

（4）**ACTIVITY**：4个Activity分布在注意力（4.1：信息搜索对比实验）、记忆（4.2：生日vs.App图标回忆）、记忆（4.3：在线银行安全与记忆负荷）和心智模型（4.4：恒温器与烤箱）等位置，以实践体验巩固理论理解。

（5）**BOX**：BOX 4.1（7±2的误用）是最具教学价值的内容之一——它展示了理论如何被误用以及应该如何正确应用。BOX 4.2（数字遗忘）介绍SenseCam和RemArc，将前沿研究带入课堂。

（6）**In-Depth Activity**：章末的非接触式卡片心智模型调查练习是一个完整的研究方法训练——从自我反思到访谈他人再到分析结果——让学生体验认知研究的基本流程。

（7）**Further Reading**：推荐6本书，涵盖数字内容管理（Bergman & Whittaker）、HCI经典论文（Erickson & McDonald）、认知基础（Eysenck & Brysbaert）、决策心理学（Gigerenzer）、HCI手册（Jacko）和思维心理学（Kahneman），为不同兴趣方向的学生提供了拓展阅读路径。

## 六、论辩与阐述方法

L025 （1）**模板化循环论证**：4.2节对6个认知过程的处理采用了高度一致的论证模板——定义→研究证据→对交互设计的启示→设计建议——形成"理论-证据-应用"的三段循环。这种模板化结构在教学上极为有效，因为读者在第一个过程（注意力）中学会了阅读模式后，可以自主地将同一模式应用于后续过程。

L026 （2）**对比实验举证**：Tullis（1997）的酒店信息检索对比实验、Weller（2004）的边框vs.颜色对比分组效果实验、Ophir et al.（2009）的重度vs.轻度多任务者对比——作者频繁使用A/B对比实验设计来建立因果主张。这种实证对比方法比单纯的断言式论述具有更强的说服力。

L027 （3）**错误信念纠正（Misconception Correction）**：BOX 4.1对7±2误用的纠正、Activity 4.4对恒温器心智模型错误的暴露——作者精于通过"揭示读者可能已有的错误信念"来建立认知冲突，从而开启深度学习。这种"先破坏再重建"的教学策略比直接教授正确概念更令人印象深刻。

L028 （4）**范式演进叙事**：4.3节从信息加工到具身交互的六个框架呈现出一个有历史感的理论演进故事——"1980年代...""如今..."——使读者不仅知道"有哪些理论"，更理解"为什么理论会演变"。这种将理论史融入教材的写作策略培养了学生的学科历史意识。

L029 （5）**因果机制的揭示**：在讨论开车使用手机时，作者不仅报告了"手机通话延长反应时间"的发现，更深入揭示了因果机制——"电话交谈使司机视觉化地想象谈话内容...视觉意象竞争了处理资源"——这种从"是什么"到"为什么"的深层分析使论证具有理论穿透力。

## 七、语言文风（原文摘录+L###）

L030 本章的语言风格在保持全书对话式基调的同时，因主题的学术性而比第1-3章更为严谨。对认知过程的定义和使用精确的心理学概念时，语言准确度和技术性显著提高。但作者始终坚持用日常经验（多任务崩溃、恒温器误解、购物清单、扑克牌游戏）来锚定抽象理论，保持了教科书应有的可读性。

**原文摘录一**：

L031 "You realize 30 minutes have passed, and you return your attention to your report. But before you realize it, you click your favorite sports site to check the latest score of the football game and discover that your team has just scored again. Your phone starts buzzing. Two new WhatsApp messages are waiting for you. And on it goes. You glance at the time on your laptop. It is midnight. You really are in a panic now and finally close everything down except your word processor."

【中文简评】这段叙事以现在时态和短促的句子节奏模拟了"被打断-重新聚焦-再次被打断"的注意力切换体验。短语"you realize...before you realize it"的重复制造了注意力失控的荒诞感，而"it is midnight"的简洁宣告突然将节奏拉回现实，制造出戏剧性的时间压缩效果。这段文字本身就是对"注意力碎片化"的文体学演示。

**原文摘录二**：

L032 "According to a survey by Bob Bailey (2000), several designers have been led to believe the following guidelines and have created interfaces based on them: Have only seven options on a menu. Display only seven icons on a menu bar. Never have more than seven bullets in a list. Place only seven tabs at the top of a website page. Place only seven items on a pull-down menu. He points out how this is not how the principle should be applied."

【中文简评】作者以五个排比句式列举了7±2原则的误用清单，这种修辞上的"罗列"产生了一种累积效果——读完后读者自然得出结论"这确实荒谬"。随后用"this is not how the principle should be applied"断然纠正，形成"错误主张的夸张呈现→权威来源的清晰反驳"的强反驳结构。

**原文摘录三**：

L033 "People are much better at recognizing things than recalling things. Furthermore, certain kinds of information is easier to recognize than others. In particular, people are good at recognizing thousands of pictures even if they have only seen them briefly before."

【中文简评】这一核心认知原则以三个递进句表述——"better at recognizing than recalling→some things easier to recognize than others→people good at recognizing thousands of pictures briefly seen"——从一般到特殊逐步精确化。"thousands of pictures"的具体数量增强了论断的冲击力。

## 八、实体清单（六类每类≥3+L###）

### 一、核心概念与术语

L034 （1）**Experiential vs. Reflective Cognition**（体验式认知vs.反思式认知）：Norman（1993）的二分法——前者直觉、轻松、自动（如开车）；后者需要心理努力和判断（如写作）。（2）**Fast and Slow Thinking**（快思维与慢思维）：Kahneman（2011）的区分——快思维本能、直觉、不费力；慢思维有逻辑、需要努力和专注。（3）**Mental Models**（心智模型）：对外部世界某些方面的内部建构，使人能够进行预测和推理（Craik, 1943）。（4）**Gulf of Execution and Evaluation**（执行与评估鸿沟）：Norman（1986）模型——执行鸿沟描述用户到物理系统的距离，评估鸿沟描述物理系统到用户的反向距离。（5）**Distributed Cognition**（分布式认知）：分析认知现象如何分布在个体、人工物和外部表征之间（Hutchins, 1995）。（6）**External Cognition**（外部认知）：解释与外部表征（图表、多媒体、VR）互动时的认知过程，其核心利益包括记忆负荷降低、计算卸载、注释和认知追踪。（7）**Personal Information Management（PIM）**：个人如何决定保留什么信息、如何组织存储、采用什么策略检索。（8）**Embodied Interaction**（具身交互）：通过与社会和物理环境的实践性参与来进行交互——"creating, manipulating, and making meaning through our engaged interaction with physical things"（Dourish, 2001）。

### 二、人物与学派

L035 （1）**Don Norman**：本章多处引用——体验vs.反思认知区分（1993）、执行与评估鸿沟模型（1986）、外部认知工具论（2013）。（2）**George Miller**：1956年提出短期记忆容量的7±2理论，虽被广泛误用，但仍是心理学最知名的发现之一。（3）**Daniel Kahneman**：2011年提出"快思维与慢思维"二分法，本章将其与Norman的体验/反思区分并列。（4）**Edwin Hutchins**：分布式认知理论的奠基人，1995年提出分析"认知系统"而非个体心智的方法论。（5）**David Kirsh**：具身交互研究者，2013年通过对舞者"marking"行为的研究提出"用身体思考"的理论。（6）**Ofer Bergman & Steve Whittaker**：个人信息管理（PIM）研究，2016年提出基于策展的数字内容管理模型。

### 三、方法与技术框架

L036 （1）**Human Information Processing Model**：信息加工模型——感知→认知→运动处理器的阶段模型，Card et al.（1983）的人类处理器模型可预测任务完成时间。（2）**Distributed Cognition Analysis**：分布式认知分析方法——追踪信息如何在认知系统中通过不同媒介传播和转换（representational state changes）。（3）**External Cognition Analysis**：外部认知分析——识别外部表征的三种认知功能：记忆减负（externalizing to reduce memory load）、计算卸载（computational offloading）、注释与认知追踪（annotating and cognitive tracing）。（4）**Mental Model Elicitation**：心智模型提取方法——通过提问"它如何工作"来揭示用户对技术产品的内部理解结构（In-Depth Activity详细演示）。

### 四、案例与设计实例

L037 （1）**Tullis酒店信息检索实验**（1997）：相同信息密度的两种屏幕布局——分组垂直排列vs.混杂排列——搜索时间差异（3.2秒vs.5.5秒）。（2）**SenseCam与失忆症患者Mrs. B**（Hodges et al., 2006）：可穿戴自动拍照相机使失忆症患者的记忆恢复提升近三倍。（3）**蓝牙耳机连接困境**（Whitenton, 2018）：执行与评估鸿沟的当代案例——开关标签的不一致性导致用户一小时无法连接设备。（4）**舞者"marking"研究**（Kirsh, 2013）：舞蹈编排中使用简化动作（marking）优于完整排练和心理模拟——具身交互的证据。（5）**航空驾驶舱分布式认知系统**（Hutchins, 1995）：飞行高度变更信息通过无线电→飞行员→仪表旋钮的多媒介传播。

### 五、学术文献与理论

L038 （1）**Miller (1956)**：短期记忆7±2容量的经典论文。（2）**Card, Moran & Newell (1983)**：The Psychology of Human-Computer Interaction——人类处理器模型。（3）**Hutchins (1995)**：Cognition in the Wild——分布式认知理论的开创性著作。（4）**Sparrow et al. (2011)**：Google Effects on Memory——互联网作为"认知假体"的实验证据。（5）**Kahneman (2011)**：Thinking, Fast and Slow——快慢思维二分法。（6）**Dourish (2001)**：Where the Action Is——具身交互理论的基础文献。（7）**Kirsh (2013)**：Embodied Cognition and the Magical Future of Interaction Design。

### 六、机构与产品

L039 （1）**Microsoft Research Cambridge**：开发SenseCam可穿戴记忆辅助相机和RemArc数字记忆应用。（2）**Apple**：Spotlight搜索工具——支持部分文件名甚至内容搜索整个系统。（3）**LastPass**：密码管理器——通过记住所有密码来降低用户的记忆负荷（只需记住一个主密码）。（4）**Nielsen Norman Group**：Whitenton（2018）利用"执行与评估鸿沟"分析蓝牙连接问题。（5）**Shazam**：音乐识别应用——作为"认知假体"的典型案例。

## 九、与前后章关联

L040 **承接第3章**：本章直接延续第3章的理论框架——3.6.4节介绍了Norman的执行与评估鸿沟模型，4.3.2节将其完整展开并结合Whitenton（2018）的当代案例进行深度分析。3.6.3节提及"认知理论"为交互设计提供分析工具，本章4.2-4.3节全面兑现这一承诺。第3章中"概念模型"的讨论在4.3.1节（心智模型）中获得认知心理学的理论基础——概念模型是设计者构建的，心智模型是用户拥有的，两者之间的对齐程度决定了可用性。

L041 **为第5章（Social Interaction）做铺垫**：本章引言明确宣告："Other ways of conceptualizing human behavior that focus on the social and emotional aspects of interaction are presented in the following two chapters." 4.3.4的分布式认知分析涉及"人与人之间的互动"作为认知系统的一部分，为第5章的社交机制（face-to-face conversations, co-presence, social engagement）提供了认知维度的理论基础。4.2.6节结尾提到"collaborating together"在学习中的作用，在第5章被展开为技术支持下的协作与社交参与。

L042 **为第6章（Emotional Interaction）做铺垫**：4.2节中多任务场景所描述的"panic""frustration"等情绪状态为第6章的情感设计讨论建立了现象学基础。BOX 4.2（Digital Forgetting）中关于"分手后如何忘记与前任的共享数字记忆"的讨论（Sas & Whittaker, 2013）直接涉及情感交互——这为第6章的"情感AI""情绪检测"和"设计以唤起或避免特定情感状态"的讨论提供了前期案例。

L043 **与第7章（Interfaces）的跨章关联**：4.2.5节的"阅读、说话与聆听"讨论在第7章的语音界面、自然语言界面和触觉界面中获得应用。4.2.6节中关于增强现实和可穿戴技术辅助"信息节俭决策"（information-frugal decision-making）的讨论直接指向第7章中讨论的AR和可穿戴界面。

L044 **与第8-10章（数据）和第14-16章（评估）的关联**：本章4.2.1.2中Tullis实验使用的"搜索时间"测量是第15章中可用性测试和实验设计的典型因变量。4.3.4分布式认知分析方法是第9章中定性数据分析框架（如DiCoT）的理论基础。本章建立的"认知负荷"概念是第14-16章评估方法中"认知走查"（cognitive walk-through）的理论前提。
