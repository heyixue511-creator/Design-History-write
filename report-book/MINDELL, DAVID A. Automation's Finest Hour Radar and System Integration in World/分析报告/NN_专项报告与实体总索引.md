# NN 专项报告与实体总索引

---

## 第一部分：专项报告

---

### 专项报告一：Ivan Getting与"系统集成者"的制度创新

**核心问题**：Ivan Getting如何将一种模糊的技术实践转化为一个明确的制度角色——系统集成者（system integrator）？

**分析框架**：
Getting的制度创新可以被理解为三个递进的步骤：

**第一步：重新定义"系统"的知识基础（技术层面）**
在Getting之前，火控系统被理解为物理组件的组合——雷达+指挥仪+炮+操作者。Getting重新定义它为：信号、动态、时间常数和反馈的抽象关系网络。物理设备仅仅是这些关系的固化。这个重新定义至关重要，因为它赋予了拥有雷达专业知识（而非机械火控传统）的辐射实验室一个独特的认知优势。

**第二步：创建部门身份的叠加（制度层面）**
Getting不是简单地创建一个新部门，而是在已有部门上叠加新的身份层：
- 他加入Division 7（火控）但保留在Rad Lab（雷达）的位置
- 他创建7.6节——"将那些被组织、个性、历史或多或少人为地分离开的必要元素聚集在一起"的尝试
- 他将Rad Lab的非正式协调角色固化为8项职责+7项特权的正式地位

这种"双重身份"策略避免了正面挑战已有机构的权威（Division 7和BuOrd仍然存在），同时渐进地转移了实际控制权。

**第三步：将"人"与"技术"同步重新定义（操作者层面）**
Getting的4点自动化论证不仅是技术论证，也是制度论证——如果你接受人类操作者在根本上是不可靠的，那么你就需要一个独立的、全程控制技术设计的整合者。人的排除和系统集成者的入场是一体两面。

**制度创新的永恒特征**：
Getting的八项职责和七项特权清单具有超越其时代的范式意义。这些条目——工程、生产、测试、校准、训练，以及通信权、图纸权、测试通知权、会议参与权、工厂进入权——定义了系统集成者角色的基本内涵。值得注意的是，这些条目中的大多数在本质上都是信息权利（有权知道、有权参与、有权审查），而非生产权利（有权制造）。系统集成者的权力是信息的权力。

**历史后果**：
Getting的制度创新通过两条路径得以制度化：(1) Rad Lab Series（知识固化），(2) 战后系统承包商的兴起（RAND, MITRE, TRW）——这些组织可以被视为Getting的八项职责清单的机构化版本。

### L###

---

### 专项报告二：噪声——从"不幸的事实"到"系统的认识论基础"

**核心问题**：噪声如何从一个技术障碍转变成系统工程的认识论基础？

**分析框架**：
噪声在本章的叙事中经历了三重转变：

**第一重：噪声作为"麻烦"（战前观念）**
在战前的Sperry指挥仪（M-4, M-7）中，噪声不是一个理论问题。操作者（"人的伺服机构"）通过目视望远镜跟踪目标、用手轮消除抖动——噪音被人的判断所吸收，不进入机器的计算过程。在这种模式下，系统确实是"部件之和"——每一个部件（望远镜、计算机、炮）由操作者粘合在一起。

**第二重：噪声作为"不可消除的系统特征"（雷达引入后）**
当SCR-584的雷达信号直接驱动计算机时，噪声不再能被人的判断所过滤。跟踪误差在通过预测计算机的微分器时被放大，产生"主导性的预测误差"。重要的是，噪声不是外部干扰，而是雷达信号的固有部分——飞机的"闪烁"效应意味着噪声始终存在。

此时Bell Labs的通信工程传统（Nyquist, Bode）提供了关键的概念工具：将噪声系统化。Ridenour的数据平滑器、频率响应分析、信号/噪声的权衡曲线——这些将噪声从一个不幸的物理事实转变为一个可优化的系统参数。

**第三重：噪声作为"系统整体性的证明"（战后认识论）**
Hazen在1945年提出的"系统大于部件之和"命题，其技术内涵正是：噪声使得部件间的动态耦合不可忽视，因此系统不可分解。如果你的系统没有噪声，你可以分别设计雷达和指挥仪，然后在界面上指定几个参数（如Weaver最初设想的"三个参数"）；如果噪声存在，你必须在设计阶段就考虑整个系统的频率响应、时间常数和动态行为。

换言之，噪声是"部件之和"世界与"系统整体"世界的本体论分界线。

**向后看——"信息"：**
文章最后一句话将噪声的讨论引入"信息"概念——信息是噪声的逻辑对偶。1948年Shannon的信息论将表明：一个通信系统的通道容量由信号功率与噪声功率之比决定。Weaver（同年为Shannon的书作序的人恰好就是同一个Warren Weaver）已经通过火控的例子理解到：噪声不仅仅是一个困扰，它是任何通信/控制系统的构成性条件。

### L###

---

### 专项报告三：V-1对抗——第一个自动化战场的历史形态

**核心问题**：1944年夏的V-1对抗战在何种意义上是一个"自动化战场"，其局限性又是什么？

**战术场景的技术对称性**：
V-1飞弹和M-9/SCR-584防空系统之间存在结构性的技术对称：
- V-1：无人类飞行员 → 恒高度、恒速、直线飞行 → 完美符合M-9的"恒高度假设"
- M-9/SCR-584：雷达自动跟踪+电指挥仪自动计算+VT近炸引信自动引爆 → 人类仅保留目标选择和pip matching

英国防空司令Pile将军的话捕捉了这一对称性："对我们来说，飞弹这个机器人目标的明显答案是机器人防御。"

**战果数据与解释**：
- 第一阶段（伦敦南郊防线，6.18-7.17）：击落343架（占攻击总数10%，被击落数22%）
- 第二阶段（海岸部署，7.17-8.31）：击落1286架（占攻击总数34%，被击落数55%）
- 效率提升的部分原因：从限制开火（避免误伤友机）转为无限制开火（海上），以及辐射实验室工程师的现场调校

**"自动化的接缝"**：
BTL的战后评估报告揭示了系统自动化的不完全性：
- SCR-584不能同时搜索和跟踪（BTL的SCR-545可以）
- 雷达、光学跟踪器、测距仪的多源输入要求操作者不断判断和切换
- 低空目标的地面杂波、密集编队目标的不确定性、电子干扰的可能性——使手动跟踪在许多场景中仍不可替代
- 操作者注意力超载的问题被明确记录

这些"接缝"恰好为Getting的Mark 56（"全集成系统"）提供了设计要求的负面清单。

**自动化战场的军事想象与现实**：
明德尔指出这一场景"即使在今天仍是军事技术者的梦想"（remains a dream of military technologists）。1944年的V-1对抗提供了自动化战场理念的原型：机器对抗机器，人类退居幕后。但这个梦想在实践中的实现依赖于极为特殊的条件——目标本身也是自动的。当面对有人驾驶的、做规避机动的、低空攻击的飞机时，M-9/SCR-584的效能急剧下降。

这一观察具有当代意义：自动化系统在"理想条件"下的卓越表现与"非理想条件"下的脆弱性之间的张力，是军事自动化至今未被解决的重大问题。

### L###

---

### 专项报告四："系统不等于部件之和"——一个认识论命题的系谱学

**核心问题**：Hazen在1945年提出的"系统大于部件之和"命题的历史条件和意涵是什么？

**文本系谱**：

1. **1940年12月 Weaver的"铁丝篱笆"**：暗示了两个领域（D-1, D-2）之间需要"有门的篱笆"——承认系统有边界但假定边界是清晰的、"三个参数"即可定义接口。这仍然属于"部件之和"模型。

2. **1941-1942年 D-1.5委员会**：一个过渡性的制度安排——在认识到仅靠"铁丝篱笆"不够之后，试图通过委员会来管理不可预见的技术交互。委员会"约只存在了一年"——其短命本身说明这种折中方案不能解决根本问题。

3. **1942年 T-10最终报告**：记录了协调设计的实际经验但未上升到理论——"应在指挥仪设计者和雷达设计者之间保持密切联络……每个单元的规格说明应在充分考虑另一单元的特性和能力后撰写。"——作为实践建议是合理的，但缺乏认识论上的自觉。

4. **1943-1945年 Getting的制度实践**：将"整体设计"从技术建议变为制度安排（7.6节，系统集成者角色）。

5. **1945年 Hazen的系统整体论宣言**："One must always remember that a fire-control system is more than the sum of component parts."——将前面的所有实践经验凝结为一个认识论命题。

6. **1947年 Rad Lab Series #25**：将这个命题背后的技术知识（伺服理论、控制论）固化为教材——使系统整体论从经验命题变为可传授的知识体系。

**认识论意涵**：
"大于部件之和"中的"大于"具体指什么？从本章的技术叙事中可以提取出：
- **大于 = 部件间的动态耦合**（一个部件的输出噪声成为另一个部件的时间滞后源）
- **大于 = 不可预测的涌现效应**（Weaver的"铁丝篱笆"无法预先定义所有交互）
- **大于 = 设计过程中的协调成本**（必须在设计阶段反复交流、测试界面）
- **大于 = 信息流本身**（战后"信息"被定义为一个穿透所有组件的独立量）

**制度意涵**：
如果系统真的不可分解为部件之和，那么BuOrd的分解式合同模型在技术上就是不合理的——不是因为管理不善，而是因为认识论错误。这就是为什么Getting不仅需要更好的技术，还需要一种新的制度形式（系统集成者）来承担"更大"的那部分治理任务。

### L###

---

## 第二部分：实体总索引

以下索引汇总自本册全部章节分析报告（01_章节分析报告 第八节 实体清单）。索引按六大类别分列，每类实体按英文字母顺序排列（中文译名紧随其后），后附简要定位信息。

---

### 索引一：人物

| 编号 | 英文名 | 中文译名 | 身份/角色 | 首次出现段落 |
|------|--------|---------|----------|------------|
| P01 | Henry Abajian | 亨利·阿巴吉安 | Rad Lab Project II电气工程师 | 导言段后第3段 |
| P02 | Kenneth T. Bainbridge | 肯尼思·T·班布里奇 | 哈佛物理学家、将Getting引入Rad Lab | 导言段后第5段 |
| P03 | William Blandy | 威廉·布兰迪 | 海军军械局（BuOrd）局长 | 第三节 |
| P04 | Hendrik Bode | 亨德里克·博德 | BTL工程师、反馈放大器理论 | 第一节（噪声讨论） |
| P05 | Vannevar Bush | 范内瓦·布什 | NDRC主席 | 导言段后第5段 |
| P06 | Earl Chafee | 厄尔·查菲 | Sperry火控总监、主持Chafee调查 | 第一节末尾 |
| P07 | Karl Compton | 卡尔·康普顿 | MIT校长、NDRC Division D负责人 | 导言段后第5段（Getting本科论文导师） |
| P08 | Lee Davenport | 李·达文波特 | Rad Lab Project II物理学家 | 导言段后第5段 |
| P09 | Charles Stark Draper | 查尔斯·斯塔克·德雷珀 | MIT仪表实验室、陀螺专家 | 第三节（7.6委员会成员） |
| P10 | Sidney Godet | 西德尼·戈德 | GE工程师、提供amplidyne伺服 | 导言段后第7段 |
| P11 | Ivan A. Getting | 伊万·A·格廷 | Rad Lab Division 8负责人、7.6节主席 | 章首题词/导言段后第5段 |
| P12 | George Harris | 乔治·哈里斯 | Rad Lab Project II电气工程师 | 导言段后第5段 |
| P13 | Harold L. Hazen | 哈罗德·L·黑曾 | MIT EE系主任、Division 7负责人 | 第三节 |
| P14 | Ernest O. Lawrence | （E.O. Lawrence，物理学家，辐射实验室命名来源） | — | （未直接出现，实验室以他命名） |
| P15 | Clarence A. Lovell | 克拉伦斯·A·洛弗尔 | BTL T-10/M-9设计团队负责人 | 第一节（与Rad Lab交流） |
| P16 | Emerson Murphy | 埃默森·墨菲 | BuOrd火控研究负责人 | 第三节 |
| P17 | Nathaniel B. Nichols | 纳撒尼尔·B·尼科尔斯 | Rad Lab Division 8伺服工程师 | 第一节末尾/第五节 |
| P18 | Harry Nyquist | 哈里·奈奎斯特 | BTL工程师、取样定理和反馈理论 | 第一节（噪声讨论） |
| P19 | Robert M. Page | 罗伯特·M·佩奇 | Naval Research Lab早期雷达研究者 | 第三节（7.6成员） |
| P20 | Ralph S. Phillips | 拉尔夫·S·菲利普斯 | Rad Lab Division 8数学家 | 第一节末尾/第五节 |
| P21 | Walter Pitts | 沃尔特·皮茨 | Rad Lab Division 8伺服组成员 | 第一节末尾 |
| P22 | Louis Ridenour | 路易斯·里德诺尔 | Rad Lab、战后Rad Lab Series编辑 | 第一节（D-1.5成员） |
| P23 | Paul Samuelson | 保罗·萨缪尔森 | 经济学家、Rad Lab伺服组成员 | 第一节末尾 |
| P24 | Leo Sullivan | 利奥·沙利文 | Rad Lab Project II物理学家 | 导言段后第5段 |
| P25 | Antonin (Tony) Svoboda | 安东宁·斯沃博达 | 捷克流亡火控专家、Mark 56计算机设计者 | 第三节 |
| P26 | Merle Tuve | 默尔·图夫 | Division T负责人、开发近炸引信 | 第四节 |
| P27 | Warren Weaver | 沃伦·韦弗 | NDRC D-2主席、洛克菲勒基金会 | 章首题词/导言段 |
| P28 | Norbert Wiener | 诺伯特·维纳 | MIT数学家、预测控制 | 第四节（曲线飞行预测） |

### L###

---

### 索引二：机构/组织

| 编号 | 英文名 | 中文译名 | 性质 | 首次出现段落 |
|------|--------|---------|------|------------|
| O01 | Arma Engineering Company | 阿尔马工程公司 | 海军火控传统承包商 | 第二节 |
| O02 | Bell Telephone Laboratories (BTL) | 贝尔电话实验室 | AT&T工业研究实验室 | 章首题词 |
| O03 | Bureau of Ordnance, U.S. Navy (BuOrd) | 美国海军军械局 | 海军火炮与火控管理机构 | 导言段 |
| O04 | Chrysler Corporation | 克莱斯勒公司 | SCR-584生产商之一 | 第一节 |
| O05 | Division T (OSRD/NDRC) | T处（OSRD/NDRC） | 近炸引信开发部门 | 第四节 |
| O06 | D-1.5 Committee | D-1.5委员会 | 雷达-火控联络委员会 | 第一节末尾 |
| O07 | Ford Instrument Company | 福特仪器公司 | 海军火控传统承包商 | 第二节 |
| O08 | General Electric (GE) | 通用电气公司 | 海军火控供应商/SCR-584生产商 | 第一节 |
| O09 | Librascope Corporation | 历镜公司（加州） | Mark 56弹道计算机生产商 | 第三节 |
| O10 | MIT Radiation Laboratory (Rad Lab) | MIT辐射实验室 | NDRC微波雷达中央实验室 | 导言段 |
| O11 | NDRC Division 7 / Section D-2 (Fire Control) | NDRC第七处/D-2科（火控） | OSRD火控研发管理机构 | 导言段 |
| O12 | NDRC Division 14 / Section D-1 (Radar) | NDRC第十四处/D-1科（雷达） | OSRD雷达研发管理机构 | 导言段后第4段 |
| O13 | NDRC Applied Mathematics Panel | NDRC应用数学小组 | 新设部门（Weaver离开D-2后领导） | 第三节 |
| O14 | Naval Research Laboratory (NRL) | 海军研究实验室 | 海军雷达早期研发机构 | 第三节 |
| O15 | Section 7.6 (Navy Fire Control with Radar) | 7.6节（海军火控与雷达） | Division 7下Getting主持的特殊部门 | 第三节 |
| O16 | Sperry Gyroscope Company | 斯佩里陀螺仪公司 | 火控系统制造商 | 导言段后第2段 |
| O17 | Westinghouse | 西屋公司 | SCR-584生产商之一 | 第一节 |
| O18 | Western Electric | 西部电气 | AT&T制造子公司 | 导言段后第2段 |

### L###

---

### 索引三：技术系统/装备

| 编号 | 英文名 | 中文译名/功能 | 年代 | 首次出现段落 |
|------|--------|-------------|------|------------|
| T01 | SCR-268 Radar | SCR-268对空搜索/火控雷达 | 1937设计/1940生产 | 第一节第1段 |
| T02 | SCR-270 Radar | SCR-270远程预警雷达 | 1940（珍珠港） | 注释4 |
| T03 | SCR-584 Radar (XT-1) | SCR-584微波火控雷达 | 1941原型/1942标准化 | 第一节 |
| T04 | XT-1 / SCR-584 Radar | （同T03，原型/生产型号） | — | — |
| T05 | SCR-545 Radar | SCR-545 BTL竞争雷达（长波搜索+微波跟踪） | 1942 | 第四节（BTL批评） |
| T06 | Cavity Magnetron | 腔磁控管（微波产生器） | 1940（Tizard Mission） | 导言段后第4段 |
| T07 | M-4 Gun Director | M-4机械指挥仪（Sperry） | 战前/战时 | 第一节第1段 |
| T08 | M-7 Gun Director | M-7机械指挥仪（Sperry） | 战时 | 第一节 |
| T09 | M-9 / T-10 Gun Director | M-9/T-10电指挥仪（BTL） | 1940-1943 | 第一节 |
| T10 | Mark 56 Gun Fire Control System | Mark 56全集成舰用火控系统 | 1943设计/1947服役 | 导言段/第三节 |
| T11 | Conical Scan | 锥形扫描（雷达自动跟踪技术） | 1941 | 导言段后第7段 |
| T12 | Plan Position Indicator (PPI) | PPI（平面位置显示器） | 1942 | 导言段后第9段 |
| T13 | Proximity Fuze (VT Fuze) | 近炸/变时引信（炮弹微型雷达） | 1944 | 第四节 |
| T14 | Amplidyne Servo | Amplidyne伺服系统（GE） | 1941 | 导言段后第7段 |
| T15 | Vickers Servo | Vickers伺服系统（MIT Servo Lab） | 战时（Mark 56未采用） | 第三节 |
| T16 | Line-of-Sight Gyro | 视线陀螺（Mark 56基准） | 1944 | 第三节 |
| T17 | Differential Analyzer | 微分分析器（Bush, MIT） | 1930年代初 | 第三节/注释14 |
| T18 | 90mm AA Gun | 90毫米防空炮 | 战时 | 第一节/第四节 |

### L###

---

### 索引四：概念/理论

| 编号 | 英文名 | 中文译名 | 核心内涵 | 首次出现段落 |
|------|--------|---------|---------|------------|
| C01 | Systems Engineering / System Integration | 系统工程/系统集成 | 从初始即设计整个系统的行为，而非连接独立设计的组件 | 导言段 |
| C02 | Noise | 噪声 | 雷达回波中的非目标信号——闪烁、杂波、电气干扰 | 导言段/第一节 |
| C03 | Signal-to-Noise Ratio / Analogy | 信噪比/信号-噪声类比 | 将通信工程中信号/噪声的框架映射至火控预测 | 第一节（Weaver引言） |
| C04 | "More than the Sum of Component Parts" | "大于部件之和" | 系统整体论——部件间的动态耦合使系统不可分解 | 第五节（Hazen, 1945） |
| C05 | Human Servomechanism | 人的伺服机构 | 操作者在早期系统中承担的感知-判断-执行功能 | 导言段后第6段 |
| C06 | Coordinated Design | 协调设计 | Getting的"全集成努力"理念 | 第三节 |
| C07 | Frequency Response | 频率响应 | 部件对输入变化的响应速度（时间常数） | 第一节 |
| C08 | Data Smoothing | 数据平滑 | 滤除高频噪声、牺牲实时性换取精确性 | 第一节 |
| C09 | Automatic Tracking | 自动跟踪 | 雷达信号直接驱动伺服天线跟踪目标 | 导言段后第6段 |
| C10 | Pip Matching | 信号匹配 | 操作者用手轮操纵光点（pip）手动选择目标回波 | 导言段后第6段 |
| C11 | Blind Firing | 盲射 | 全自动射击——无需目视即可射击 | 第二节 |
| C12 | Constant Altitude Assumption | 恒高度假设 | 防空指挥仪中关于目标保持恒定高度的算法简化 | 第四节 |
| C13 | Feedback Loop | 反馈回路 | 系统中输出回馈输入以修正误差的回路 | 导言段后第7段（锥形扫描） |
| C14 | Time Constant | 时间常数 | 系统对输入变化的响应速度度量 | 第一节 |
| C15 | Information | 信息 | 章末暗示的"流过新集成系统的一般量" | 最后一句话 |
| C16 | Decomposition / Modularity | 可分解性/模块性 | 系统是否可被拆分为独立设计的子部件 | 第五节（Hazen微分分析器对比） |

### L###

---

### 索引五：事件

| 编号 | 英文名 | 中文译名 | 时间 | 首次出现段落 |
|------|--------|---------|------|------------|
| E01 | Tizard Mission | 蒂泽德使团技术转让 | 1940年9月 | 导言段后第4段 |
| E02 | Pearl Harbor Attack | 珍珠港遇袭 | 1941年12月7日 | 第一节（M-9原型交付） |
| E03 | XT-1 Fort Monroe Test | XT-1门罗堡测试 | 1942年2月 | 第一节 |
| E04 | NDRC Reorganization | NDRC重组 | 1942年底 | 第三节 |
| E05 | D-1.5 Committee Survey | D-1.5委员会调查 | 1941-1942 | 第一节末尾 |
| E06 | Chafee Inquiry | 查菲调查 | 1942底-1943初 | 第一节末尾 |
| E07 | M-9/SCR-584 at Anzio | M-9/SCR-584安齐奥滩头部署 | 1944年3月 | 第四节 |
| E08 | V-1 Blitz Defense - Phase 1 | V-1闪电战防空（第一阶） | 1944.6.18-7.17 | 第四节 |
| E09 | V-1 Blitz Defense - Phase 2 | V-1闪电战防空（第二阶段） | 1944.7.17-8.31 | 第四节 |
| E10 | BTL European Assessment | BTL赴欧评估 | 1944年7-8月 | 第四节 |
| E11 | Antwerp V-1 Defense | 安特卫普V-1防御 | 1944年10月 | 第四节 |
| E12 | Getting Appointed to BuOrd | Getting派驻BuOrd | 1945年3月 | 第三节末尾 |
| E13 | NDRC Closure / Contract Transfer | NDRC关闭/合同移交BuOrd | 1945年10月 | 第三节 |
| E14 | Mark 56 Fleet Delivery | Mark 56交付舰队 | 1947年 | 第三节 |
| E15 | Rad Lab Series Published | 辐射实验室丛书出版 | 1947-1948 | 第五节 |
| E16 | Section 7.6 First Formal Meeting | 7.6节首次正式会议 | 1944年1月 | 第三节 |

### L###

---

### 索引六：文献/出版物

| 编号 | 英文名 | 中文译名 | 著者/来源 | 年代 |
|------|--------|---------|----------|------|
| D01 | Theory of Servomechanisms (Rad Lab Series #25) | 《伺服机构理论》 | James, Nichols, Phillips; Introduction by Getting | 1947 |
| D02 | Computing Mechanisms and Linkages (Rad Lab Series #27) | 《计算机构与连杆》 | Antonin Svoboda | 1948 |
| D03 | Radar System Engineering (Rad Lab Series #1) | 《雷达系统工程》 | Louis B. Ridenour | 1948 |
| D04 | "Final Report: D-2 Project #2, Study of Errors in T-10 Gun Director" | 《T-10指挥仪误差研究最终报告》 | Bell Telephone Laboratories | 战时 |
| D05 | "Antiaircraft Artillery Fire Control" | 《防空火炮火控》 | Bell Telephone Laboratories | 1945.5.1 |
| D06 | Chafee Report | 《查菲报告》 | Earl W. Chafee, Sperry Gyroscope Co. | 1943.2.15 |
| D07 | All in a Lifetime | 《毕生回顾》 | Ivan A. Getting | 1989 |
| D08 | Summary Technical Report of Division 7, Vol. I | 《第七处技术总结报告》卷一 | Division 7, NDRC / Harold Hazen | 1945 |
| D09 | Networks of Power | 《电力网络》 | Thomas P. Hughes | 1983 |
| D10 | A History of Control Engineering: 1930-1955 | 《控制工程史：1930-1955》 | Stuart Bennett | 1993 |
| D11 | Principles of Servomechanisms | 《伺服机构原理》 | Gordon S. Brown and Donald P. Campbell | 1948 |
| D12 | Fundamental Theory of Servomechanisms | 《伺服机构基础理论》 | Leroy MacColl | 1945 |
| D13 | Radar in World War II | 《二战中的雷达》 | Henry Guerlac | 1987 |
| D14 | Top Secret Exchange: The Tizard Commission | 《绝密交流：蒂泽德委员会》 | David Zimmerman | 1996 |
| D15 | Ack-Ack: Britain's Defence against Air Attack | 《防空：英国对空防御》 | General Sir Fredrick Pile | 1949 |
| D16 | Naval Ordnance and Gunnery, Vol. 2: Fire Control | 《海军军械与射击·卷二：火控》 | U.S. Navy, Bureau of Personnel (NavPers 10798) | 1955 |
| D17 | United States Army in WW II: The Signal Corps | 《美军二战史：通信兵》 | Thompson et al. | 1957/1966 |

### L###

---

## 第三部分：跨章主题索引

以下主题跨越了本册分析报告的多个部分（整体分析、章节分析、专项报告），在此提供快速定位。

| 主题 | 涉及报告 | 主要位置 |
|------|---------|---------|
| 系统工程的认识论基础 | 00, 01, 专项二, 专项四 | 00-四; 01-四/五/七; 专项二; 专项四 |
| Ivan Getting的制度角色 | 01, 专项一 | 01-三/四/八; 专项一 |
| 噪声与不可分解性 | 01, 专项二 | 01-三/四/五; 专项二 |
| V-1对抗的军事历史意义 | 01, 专项三 | 01-三/四; 专项三 |
| 人的重新定义 | 00, 01, 专项一 | 00-三; 01-三/七; 专项一 |
| 制度竞争（BTL vs Rad Lab vs BuOrd） | 00, 01, 专项一 | 00-五; 01-三/四; 专项一 |
| 战后知识制度化（Rad Lab Series） | 01, 专项四 | 01-五/八; 专项四 |
| 从噪声到信息的概念演进 | 01, 专项二 | 01-五; 专项二 |
| 系统方法的扩散 | 00, 01 | 00-一/三; 01-九 |

### L###

---

**生成日期**：2026-08-05
**涵盖范围**：David A. Mindell, "Automation's Finest Hour: Radar and System Integration in World War II"（单章）
**报告语言**：中文（含英文术语原文标注）
**实体总数**：人物28项 / 机构18项 / 技术系统18项 / 概念16项 / 事件16项 / 文献17项 = 总计113项
