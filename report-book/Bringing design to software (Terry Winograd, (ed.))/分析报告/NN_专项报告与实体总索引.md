# NN_专项报告与实体总索引

## 《Bringing Design to Software》跨章专项分析与实体总索引

---

## 专项报告一：全书核心概念网络分析

### 概念聚类与关联图谱

全书 14 章 + 14 篇 Profile 构成了一个密集的概念网络。以下按六大概念聚类进行整理。

#### 聚类 A：设计的本体论（"设计是什么"）

| 概念 | 提出者 | 核心定义 | 关联概念 |
|------|--------|----------|----------|
| Design as bringing two worlds together | Kapor (Ch.1) | "foot in two worlds—technology and human purposes" | Architecture analogy (P1) |
| Design as determining user experience | Liddle (Ch.2) | "has nothing to do with how the code works inside" | Conceptual model (Ch.2) |
| Design as conversation with materials | Schön (Ch.9) | "backtalk" from the medium; no direct path from intention to outcome | Creative leap (Ch.8), Foothold (Ch.11) |
| Design as creating, not problem solving | Kelley (Ch.8) | "dream that goes beyond what exists" | Messiness (Ch.8), Intuition (Ch.8) |
| Design as social activity | Winograd (Intro) | "designed artifacts communicate content" | Organizational support (Ch.13), Social consequences (Ch.14) |
| Design as keeping things simple | Brown & Duguid (Ch.7) | "allowing increasing amounts to be underrepresented" | Periphery, Genre, Border (Ch.7) |

L### 分析说明：这六种定义不是互斥的，而是从不同角度描述同一活动的不可还原的维度。它们共同否定了"设计=从规格推导产品的线性过程"（Denning & Dargan 批判的"软件工程幻觉"）。

#### 聚类 B：设计的认知过程（"设计如何发生"）

| 概念 | 提出者 | 核心机制 |
|------|--------|----------|
| Reflection-in-action | Schön (Ch.9) | Surprise → reflection while acting → new understanding → new moves |
| Creative leap | Kelley (Ch.8) | Uncomfortable act of choosing a direction from zillions of possibilities |
| Conversation with materials | Schön (Ch.9) | Designer makes move → material "talks back" → designer re-understands |
| Foothold seeking | Gal (Ch.11) | Safe, stable pause point → summarize progress → plan next step |
| Constraints propagation | Gal (Ch.11) | Multiple constraints from top and bottom converge → design emerges |
| Five-stage circulation | Crampton Smith & Tabor (Ch.3) | Understanding → Abstracting → Structuring → Representing → Detailing (circling, not linear) |

L### 分析说明：这些过程理论共同描绘了一个"非线性、对话式、涌现性"的设计认知模型——与"线性、规划性、推导性"的传统工程模型形成根本对立。

#### 聚类 C：设计的方法论工具（"用什么来设计"）

| 工具/方法 | 提出者 | 核心要点 |
|-----------|--------|----------|
| Design Language | Rheinfrank & Evenson (Ch.4) | Elements + Organizing principles + Qualifying situations；C→R→D→E→E |
| Conceptual Model | Liddle (Ch.2) | Priority: Conceptual Model > Control Mechanism > Information Display |
| Action-Centered Design | Denning & Dargan (Ch.6) | Domain ontology；6 pattern types；Speech acts as action motivators |
| Prototyping Culture | Schrage (Ch.10) | Specification-driven vs. Prototype-driven；Media franca；Periodic prototyping |
| Participatory Design | Kuhn (Ch.14) | Workers + designers co-design；Mockups + scenarios；Industrial democracy |
| IDEO Five-Step Process | Kelley / Profile 8 | Understand → Observe → Visualize → Evaluate → Implement |

L### 分析说明：这些方法论工具覆盖了"语言层"（Ch.4）、"模型层"（Ch.2）、"行动层"（Ch.6）、"文化层"（Ch.10）、"政治层"（Ch.14）——从最"软"的（语言的意义生成）到最"硬"的（组织的原型节奏）。

#### 聚类 D：设计的语境维度（"设计在什么条件下工作"）

| 语境因素 | 提出者 | 核心机制 |
|----------|--------|----------|
| Threshold of Indignation | Saffo (Ch.5) | Willingness to endure hassle = f(task importance, tool friendliness) |
| Periphery / Border / Genre | Brown & Duguid (Ch.7) | Shared social conventions → less needs to be said explicitly |
| Organizational Culture | Norman (Ch.12) | Unstated assumptions → "we didn't even realize we had the option" |
| Clarity / Customer / Empowerment | De Young (Ch.13) | Three pillars of organizational support for design |
| Tacit Work / Workaround | Kuhn (Ch.14) | Systems ignore tacit work → workers create workarounds → "worst of both worlds" |

L### 分析说明：五个维度共同构成了设计的"外部条件"——市场条件（Ch.5）、文化条件（Ch.7）、组织条件（Ch.12-13）、政治条件（Ch.14）——设计从来不是在"真空"中进行的。

#### 聚类 E：设计的关键角色

| 角色 | 提出者 | 核心特征 |
|------|--------|----------|
| Software Designer (独立专业) | Kapor (Ch.1) | "champion of the user experience"——区别于程序员和管理者 |
| Artist-Designer | Crampton Smith & Tabor (Ch.3) | "detecting, creating, and controlling cultural and emotional meanings" |
| Software Architect | Denning & Dargan (Ch.6) | "mapping from human actions to software functions" |
| Reflective Practitioner | Schön (Ch.9) | 在行动中思考正在做的行动——在爵士乐、建筑、教学中均如此 |
| Design Team (跨功能) | Kelley (Ch.8) / IDEO | "different brains working on the problem"——先广后窄 |
| User as Co-Designer | Kuhn (Ch.14) / Profile 14 | "design with the user, not for the user"——民主化设计 |

L### 分析说明：这些角色共同构成了一个"设计者谱系"——从独立艺术家到组织化的团队到作为共同设计者的用户——"设计者"的定义随全书的展开而不断扩展和民主化。

#### 聚类 F：设计的评价标准

| 标准 | 提出者 | 核心内容 |
|------|--------|----------|
| Firmness, Commodity, Delight | Vitruvius → Kapor (Ch.1) | 无Bug + 适合目的 + 使用愉悦 |
| Customer Satisfaction | Denning & Dargan (Ch.6) | 替代"符合规格"——"quality means customer satisfaction" |
| Taste (Gyroscope) | Schön (Ch.9) | 不可完全分析但可培养——"they can say 'Oh damn, this is terrible!'" |
| Quality-in-Use | Reflection / Qualiteque | 不能仅靠量化——"通过持续的观察和批评" |
| Love | Schön (Ch.9) | "not a bad description of what good design is trying to achieve" |

L### 分析说明：全书的评价标准从"客观可测量"（firmness）逐步过渡到"主观但可培养"（taste）最终到"情感且不可还原"（love）——这不是对"客观标准"的否定，而是对其边界的揭示和超越。

---

## 专项报告二：全书 Profile-Chapter 配对分析

本书采用独特的"Chapter + Profile"交替结构。以下分析每对 Chapter-Profile 的配对逻辑。

| Chapter | Profile | 配对逻辑 |
|---------|---------|----------|
| Ch.1 Kapor (Manifesto) | P1 Software Design and Architecture | 展开建筑类比（宣言的核心论证工具） |
| Ch.2 Liddle (Conceptual Model) | P2 The Alto and the Star | 展示概念模型优先方法论的历史载体 |
| Ch.3 Crampton Smith & Tabor (Artist-Designer) | P3 Kid Pix | 展示"功能与体验不可分离"的实践案例 |
| Ch.4 Rheinfrank & Evenson (Design Language) | P4 Macintosh HIG | 展示设计语言的系统化应用实例 |
| Ch.5 Saffo (Consumer Spectrum) | P5 Mosaic and WWW | 展示"阈值突破"的技术实例——将Internet推向大众 |
| Ch.6 Denning & Dargan (Action-Centered) | P6 Business-Process Mapping | 提供行动中心设计的具体映射工具 |
| Ch.7 Brown & Duguid (Keeping It Simple) | P7 Microsoft Bob | 展示"periphery设计"的有意识大规模尝试 |
| Ch.8 Kelley (Designer's Stance) | P8 IDEO | 展示Kelley的设计立场在组织中的制度化 |
| Ch.9 Schön (Reflective Conversation) | P9 Apple Interface Design Project | 展示设计教育如何在实践中实施 |
| Ch.10 Schrage (Prototyping Cultures) | P10 HyperCard/Director/Visual Basic | 展示三种原型媒体与三种设计文化的对应 |
| Ch.11 Gal (Footholds) | P11 The Spreadsheet | 将"foothold"概念从结构工程扩展到金融建模 |
| Ch.12 Norman (Design as Practiced) | P12 The Design of Everyday Things | 展示Norman的设计哲学和其学术基础 |
| Ch.13 De Young (Organizational Support) | P13 Quicken | 展示"客户中心设计"的商业成功验证 |
| Ch.14 Kuhn (Design for People at Work) | P14 Participatory Design | 提供北欧参与式设计的历史与方法 |

L### 分析说明：Profile 不是 Chapter 的简单"例证"，而是起到了三种功能——(1) 案例具化（P2, P3, P7, P8, P13）；(2) 方法论配套（P6, P10, P14）；(3) 概念扩展（P1, P4, P5, P9, P11, P12）。

---

## 专项报告三：全书对话网络——章节间的呼应与张力

以下追踪全书中最显著的跨章对话线路。

### 线路 1：设计 vs. 工程（贯穿全书的最高量级对话）
```
Kapor (Ch.1): "merely engineered" → 
Liddle (Ch.2): "viewed as a philistine if you wanted to argue too much about implementation" →
Crampton Smith & Tabor (Ch.3): "function and aesthetics are indivisible" →
Denning & Dargan (Ch.6): "fundamental blindness" of engineering →
Kelley (Ch.8): "assume a spherical cow" →
Schön (Ch.9): "no direct path" →
Norman (Ch.12): engineers and programmers "feel empowered to design the user side"
```

### 线路 2：个人创造力 vs. 系统化方法
```
Kelley (Ch.8): "You can't put design in a structure" →
Rheinfrank & Evenson (Ch.4): Five-step design language development →
Schön (Ch.9): "reflection-in-action" as middle ground →
De Young (Ch.13): "framework and freedom" balance
```
L### 张力：Kelley 坚持"不能方法化"，Rheinfrank & Evenson 提供了"五步法"——Schön 的"reflection-in-action"和 De Young 的"framework and freedom"提供了调和——方法作为"fall back on"的结构，而非"follow"的食谱。

### 线路 3：从个体到社会（全书的维度扩展）
```
Kapor/Ch.1: Individual designer as champion →
Ch.8-9-11: Individual cognitive/creative process →
Ch.10: Organizational prototyping culture →
Ch.12-13: Organizational constraints and support →
Ch.14: Social-political consequences and workplace democracy
```

### 线路 4：Macintosh 的跨章命运
Macintosh 作为一个"案例"在全书的不同章节中以不同方式出现——反映了"同一设计作品的多重解读"：
```
Profile 1: Macintosh as architecture analogy (Word processor = Cathedral)
Ch.2 (Liddle): Macintosh "just missed" the Star's conceptual model
Profile 4: Macintosh HIG as design language
Profile 7: Macintosh packaging as "border design" pioneer
Ch.12 (Norman): Macintosh power switch as organizational failure
```

### 线路 5：Growltiger 的双重出场
```
Ch.9 (Schön): Growltiger as unexpected teaching tool
  — "they couldn't discover that until someone was able to observe the program in use"
Ch.11 (Gal): Growltiger as "image foothold" in Ray's design process
  — "Growltiger provided the critical piece: It was an image foothold in the jigsaw puzzle"
```

---

## 实体总索引

以下整合全书 14 章 + 14 篇 Profile + 前言 + 反思中出现的所有命名实体，按六类编排。每项标注首次或核心出现的章节。

### 一、人物实体总索引

| 编号 | 姓名 | 角色 | 核心关联章节 |
|------|------|------|-------------|
| P-01 | Mitchell Kapor | Lotus 1-2-3 设计者 | Ch.1, P11, Intro |
| P-02 | David Liddle | Xerox Star 开发主管 | Ch.2 |
| P-03 | Gillian Crampton Smith | RCA 教授, 平面设计师 | Ch.3, P9 |
| P-04 | Philip Tabor | Bartlett 建筑学院 | Ch.3 |
| P-05 | John Rheinfrank | Doblin Group 策略师 | Ch.4 |
| P-06 | Shelley Evenson | Doblin Group 设计策略师 | Ch.4 |
| P-07 | Paul Saffo | Institute for the Future | Ch.5 |
| P-08 | Peter Denning | ACM 前主席 | Ch.6, P6 |
| P-09 | Pamela Dargan | 高级软件工程师 | Ch.6 |
| P-10 | John Seely Brown | Xerox PARC 主任 | Ch.7 |
| P-11 | Paul Duguid | Xerox PARC 顾问 | Ch.7 |
| P-12 | David Kelley | IDEO 创始人 | Ch.8 |
| P-13 | Bradley Hartfield | 软件设计顾问 | Ch.8, P8 |
| P-14 | Donald Schön | MIT 教授 | Ch.9, Ch.11 |
| P-15 | John Bennett | 前 IBM 研究员 | Ch.9 |
| P-16 | Michael Schrage | MIT Sloan 研究员 | Ch.10 |
| P-17 | Shahaf Gal | 教育技术研究者 | Ch.11 |
| P-18 | Donald Norman | Apple VP, 认知心理学家 | Ch.12, P12 |
| P-19 | Laura De Young | Windrose Consulting | Ch.13, P13 |
| P-20 | Sarah Kuhn | UMass Lowell 教授 | Ch.14, P14 |
| P-21 | Terry Winograd | 本书主编, Stanford 教授 | 全书, Reflection |
| P-22 | Dan Bricklin | VisiCalc 发明者 | P11, Ch.1, Ch.2 |
| P-23 | Alan Kay | Dynabook 概念提出者 | Ch.2, P2 |
| P-24 | Doug Engelbart | 鼠标/超文本先驱 | Ch.2, Ch.5 |
| P-25 | Bill Verplank | Star 用户测试 | Ch.2, P2 |
| P-26 | Charles Simonyi | Bravo 设计者 | Ch.2 |
| P-27 | Steve Jobs | Apple 联合创始人 | Ch.8 |
| P-28 | Leonardo da Vinci | 文艺复兴通才 | Ch.8 |
| P-29 | Jim Adams | Stanford 创造力学者 | Ch.8 |
| P-30 | Bill Moggridge | ID2 创始人 | P8 |
| P-31 | Michael Polanyi | 默会知识哲学家 | Ch.9 |
| P-32 | Miles Davis | 爵士乐革新者 | Ch.7 |
| P-33 | Christopher Alexander | 模式语言创立者 | Ch.6, Ch.4 |
| P-34 | Vitruvius | 古罗马建筑理论家 | Ch.1, P1 |
| P-35 | Scott Cook | Intuit 创始人 | P13, Ch.13 |
| P-36 | John Monson | Intuit VP | Ch.13 |
| P-37 | Pelle Ehn | 北欧参与式设计 | Ch.14, P14 |
| P-38 | Kristen Nygaard | SIMULA 开发者 | P14 |
| P-39 | Patricia Sachs | TTS 研究者 | Ch.14 |
| P-40 | Gordon Moore | Intel 联合创始人 | Ch.5 |
| P-41 | Vannevar Bush | Memex 概念提出者 | Ch.7 |
| P-42 | Marshall McLuhan | 媒体理论家 | Ch.3, Ch.7 |
| P-43 | John Searle | 言语行为哲学家 | Ch.3, Ch.6 |
| P-44 | Stephen Covey | 管理学作者 | Ch.13 |
| P-45 | Joy Mountford | Apple HCI 研究 | P9 |
| P-46 | Fred Brooks | 人月神话作者 | P1 |
| P-47 | Hannah Arendt | 政治哲学家 | Ch.9 |
| P-48 | Sōetsu Yanagi | 日本民艺哲学家 | Ch.5 |

### 二、组织/公司实体总索引

| 编号 | 名称 | 关联章节 |
|------|------|----------|
| O-01 | Xerox PARC | Ch.2, P2, Ch.7 |
| O-02 | Xerox System Development Division | Ch.2 |
| O-03 | Apple Computer | Ch.12, P1, P4, P7, P9, P12 |
| O-04 | IDEO | Ch.8, P8, Ch.10 |
| O-05 | Intuit, Inc. | Ch.13, P13, Intro, Ch.6 |
| O-06 | Microsoft | P7, P10, P13, Intro |
| O-07 | Association for Software Design (ASD) | Ch.1, Intro |
| O-08 | ACM (Association for Computing Machinery) | Intro, Ch.6, Reflection |
| O-09 | Interval Research Corporation | Preface, Ch.2 |
| O-10 | Royal College of Art (RCA) | Ch.3, P9 |
| O-11 | MIT | Ch.9, Ch.11, P9 |
| O-12 | Stanford University | Ch.1, P9 |
| O-13 | Doblin Group | Ch.4 |
| O-14 | Fitch / Fitch RichardsonSmith | Ch.4 |
| O-15 | Institute for the Future | Ch.5 |
| O-16 | Lotus Development Corporation | Ch.1, P11 |
| O-17 | Nike | Ch.4, Ch.10 |
| O-18 | Sony | Ch.4, Ch.10 |
| O-19 | Toyota | Ch.10 |
| O-20 | General Motors | Ch.10 |
| O-21 | Honda | Ch.10 |
| O-22 | IBM | Ch.5, Ch.12, Ch.10 |
| O-23 | 3M | Ch.9, Ch.10 |
| O-24 | Emerson Electric (FRS) | Ch.4 |
| O-25 | SRI (Stanford Research Institute) | Ch.2 |
| O-26 | 挪威铁金属工人工会 | P14 |
| O-27 | 北欧图形工人工会 | P14 |
| O-28 | Brøderbund Software | P3 |
| O-29 | Knight-Ridder | Ch.7 |
| O-30 | Action Technologies, Inc. | P6 |
| O-31 | Macromedia | P10 |
| O-32 | Windrose Consulting | Ch.13 |

### 三、产品/系统实体总索引

| 编号 | 名称 | 关联章节 |
|------|------|----------|
| S-01 | Xerox Star (8010) | Ch.2, P2 |
| S-02 | Xerox Alto | P2, Ch.2 |
| S-03 | Macintosh / Macintosh OS | Ch.12, P1, P4, P7 |
| S-04 | Lotus 1-2-3 | Ch.1, P11 |
| S-05 | VisiCalc | P11, Ch.1, Ch.2 |
| S-06 | Kid Pix (Brøderbund) | P3 |
| S-07 | Quicken (Intuit) | P13, Ch.13, Ch.6 |
| S-08 | QuickBooks (Intuit) | Ch.13 |
| S-09 | Microsoft Bob | P7 |
| S-10 | Microsoft Money | P13 |
| S-11 | Mosaic / Netscape | P5 |
| S-12 | Growltiger (MIT) | Ch.9, Ch.11 |
| S-13 | McCavity (MIT) | Ch.9 |
| S-14 | HyperCard (Apple) | P10, Ch.1 |
| S-15 | Macromedia Director | P10 |
| S-16 | Visual Basic (Microsoft) | P10 |
| S-17 | TTS (Trouble Ticketing System) | Ch.14 |
| S-18 | HELP System ("Spy in the Sky") | Ch.14 |
| S-19 | Big Bank Teller System | Ch.14 |
| S-20 | TIPS (UTOPIA 项目) | P14 |
| S-21 | Apple 鼠标 (首款) | P8 |
| S-22 | Microsoft 鼠标 | Ch.10 |
| S-23 | Xerox 复印机 (重新设计线) | Ch.4 |
| S-24 | Emerson FRS 过程控制系统 | Ch.4 |
| S-25 | Die Brücke (Ray 的桥梁) | Ch.11 |
| S-26 | Scotch Tape (3M) | Ch.9 |
| S-27 | Viewtron (Knight-Ridder) | Ch.7 |
| S-28 | World Wide Web | P5 |
| S-29 | ActionWorkflow Analyst | P6 |
| S-30 | CHRP (共同硬件参考平台) | Ch.12 |

### 四、概念/理论实体总索引

| 编号 | 名称 | 提出者 / 核心章节 |
|------|------|-------------------|
| C-01 | Reflection-in-Action（行动中反思） | Schön, Ch.9 |
| C-02 | Conceptual Model（概念模型） | Liddle, Ch.2 |
| C-03 | Design Language（设计语言） | Rheinfrank & Evenson, Ch.4 |
| C-04 | Threshold of Indignation（愤慨阈值） | Saffo, Ch.5 |
| C-05 | Action-Centered Design（行动中心设计） | Denning & Dargan, Ch.6 |
| C-06 | Periphery / Border / Genre（外围/边界/文类） | Brown & Duguid, Ch.7 |
| C-07 | Prototyping Culture（原型文化） | Schrage, Ch.10 |
| C-08 | Foothold / Image Foothold（立足点/图像立足点） | Gal, Ch.11 |
| C-09 | Creative Leap（创造性跳跃） | Kelley, Ch.8 |
| C-10 | Conversation with Materials（与材料的对话） | Schön, Ch.9 |
| C-11 | Backtalk（回话） | Schön, Ch.9 |
| C-12 | Tacit Knowledge（默会知识） | Polanyi → Schön, Ch.9 |
| C-13 | Taste as Gyroscope（品味作为陀螺仪） | Schön, Ch.9 |
| C-14 | Software Design Viewpoint（软件设计视角） | Kapor, Ch.1 |
| C-15 | Firmness-Commodity-Delight（坚固-适用-愉悦） | Vitruvius → Kapor, Ch.1 |
| C-16 | WYGIWYS（你得到的就是你看到的） | Crampton Smith & Tabor, Ch.3 |
| C-17 | Pattern Language（模式语言） | Alexander → Denning & Dargan, Ch.6 |
| C-18 | Ontology of the Domain（领域本体论） | Denning & Dargan, Ch.6 |
| C-19 | Speech Acts（言语行为） | Searle → Denning & Dargan, Ch.6 |
| C-20 | Participatory Design（参与式设计） | Kuhn / Profile 14 |
| C-21 | Human-Centered Design（人本设计） | Denning & Dargan (Ch.6) / Kuhn (Ch.14) |
| C-22 | Explicit vs. Tacit View of Work（显性/隐性工作） | Sachs → Kuhn, Ch.14 |
| C-23 | Consumer Universe Matrix（消费者宇宙矩阵） | Saffo, Ch.5 |
| C-24 | Media Franca（媒介通用语） | Schrage, Ch.10 |
| C-25 | Transparent Box / Black Box（透明盒子/黑盒子） | Rheinfrank & Evenson, Ch.4 |
| C-26 | Soft Power Control（软电源控制） | Norman, Ch.12 |
| C-27 | Organizational Intervention（组织干预） | Kuhn, Ch.14 |
| C-28 | Goal Transmutation（目标畸变） | De Young, Ch.13 |
| C-29 | Follow-Me-Home（跟回家观察） | De Young / Intuit, Ch.13 |
| C-30 | Idea Fluency（想法流利度） | Kelley, Ch.8 |
| C-31 | Underrepresentation（欠表征） | Brown & Duguid, Ch.7 |
| C-32 | Social Warrants（社会担保） | Brown & Duguid, Ch.7 |
| C-33 | Virtual Worlds / Virtuality（虚拟世界/虚拟性） | Winograd, Introduction |
| C-34 | Progressive Disclosure（渐进揭示） | Liddle, Ch.2 |
| C-35 | Direct Manipulation（直接操纵） | Profile 2 / Ch.2 |
| C-36 | Unintended Consequences（非预期后果） | Schön, Ch.9 |
| C-37 | Messiness（混乱性） | Kelley, Ch.8 |
| C-38 | Designer Empowerment（设计者赋权） | De Young, Ch.13 |
| C-39 | Industrial Democracy（工业民主） | Kuhn, Ch.14 / Profile 14 |
| C-40 | Tool Perspective（工具视角） | Ehn, Profile 14 |

### 五、事件实体总索引

| 编号 | 名称 | 时间 | 关联章节 |
|------|------|------|----------|
| E-01 | 1992 Stanford 软件设计研讨会 | 1992 | Preface |
| E-02 | Kapor PC Forum 宣言演讲 | 1990 | Ch.1 |
| E-03 | ASD 成立 | 1992 | Introduction, Ch.1 |
| E-04 | interactions 杂志创刊 | 1994 | Introduction |
| E-05 | Xerox Alto 开发 | 1972 | P2 |
| E-06 | Xerox Star 开发启动 | 1978 | Ch.2 |
| E-07 | Xerox Star 发布 | 1981年5月 | Ch.2 |
| E-08 | 400页Star功能规格完成 | 1978-1981间 | Ch.2 |
| E-09 | 600-700小时Star用户视频测试 | 1978-1981间 | Ch.2 |
| E-10 | Apple Interface Design Project 启动 | 1991 | P9 |
| E-11 | Macintosh 发布 | 1984 | P7, P12 |
| E-12 | Macintosh HIG 发布 | 1987 | P4 |
| E-13 | Intuit 成立 / Quicken 发布 | 1984 / 1986 | P13, Ch.13 |
| E-14 | QuickBooks 的意外发现 | ~1990s早期 | Ch.13 |
| E-15 | Microsoft Intuit收购尝试 | 1995 | Intro, P13 |
| E-16 | Microsoft Bob 发布 | 1995 | P7 |
| E-17 | Mosaic 发布 → WWW 爆炸 | 1993-1994 | P5 |
| E-18 | IBM-Apple CHRP 宣布 | 1995 | Ch.12 |
| E-19 | MIT 第四届桥梁设计竞赛 | 1988年冬 | Ch.11 |
| E-20 | RCA 计算机相关设计课程建立 | 1989 | Ch.3, P9 |
| E-21 | 1979 GAO 软件项目审查 | 1979 | Ch.6 |
| E-22 | 挪威共同决策协议 | 1970s早期 | P14 |
| E-23 | DEMOS 项目（瑞典） | 1970s下半 | P14, Ch.14 |
| E-24 | UTOPIA 项目（瑞典/丹麦） | 1980s | P14, Ch.14 |
| E-25 | Scotch Tape 发明及分化 | 1940s- | Ch.9 |
| E-26 | VisiCalc 电子表格发布 | 1979 | P11 |
| E-27 | 1994 Participatory Design Conference | 1994 | P14 |
| E-28 | 1994 HCI 期刊专刊（Brown & Duguid 论文+24回应） | 1994 | Ch.7 |
| E-29 | Knight-Ridder Viewtron 失败 | 1980s | Ch.7 |
| E-30 | IDEO 成立（DKD + ID2 合并） | 1991 | P8 |
| E-31 | "Denning report" 发表 | 1989 | Ch.6 |

### 六、文献/文本实体总索引

| 编号 | 名称 | 关联章节 |
|------|------|----------|
| B-01 | Kapor, "A Software Design Manifesto" (Dr. Dobb's, 1991) | Ch.1 |
| B-02 | Schön, The Reflective Practitioner (1983) | Ch.9 |
| B-03 | Schön, Educating the Reflective Practitioner (1987) | Ch.9 |
| B-04 | Norman, The Design of Everyday Things (1988/1990) | P12 |
| B-05 | Norman, Things That Make Us Smart (1993) | P12 |
| B-06 | Alexander, A Pattern Language (1977) | Ch.6 |
| B-07 | Alexander, The Timeless Way of Building (1979) | Ch.6 |
| B-08 | Polanyi, The Tacit Dimension (1966) | Ch.9 |
| B-09 | Searle, Speech Acts (1969) | Ch.3, Ch.6 |
| B-10 | Winograd & Flores, Understanding Computers and Cognition (1987) | Ch.6 |
| B-11 | Bush, "As We May Think" (Atlantic, 1945) | Ch.7 |
| B-12 | McLuhan, Understanding Media (1964) | Ch.3, Ch.7 |
| B-13 | McLuhan, The Gutenberg Galaxy (1962) | Ch.7 |
| B-14 | Apple, Human Interface Guidelines (1987) | P4 |
| B-15 | Brown & Duguid, "Borderline issues" (HCI, 1994) | Ch.7 |
| B-16 | Denning & Dargan, "A discipline of software architecture" (interactions, 1994) | Ch.6 |
| B-17 | Gal, "Building Bridges" (1991) | Ch.11 |
| B-18 | Schrage, No More Teams (1995) | Ch.10 |
| B-19 | Adams, Conceptual Blockbusting (1974/1986) | Ch.8 |
| B-20 | Covey, The Seven Habits of Highly Effective People (1989) | Ch.13 |
| B-21 | Land & Jarman, Breakpoint and Beyond (1992) | Ch.13 |
| B-22 | Sachs, "Transforming work" (1995) | Ch.14 |
| B-23 | Salzman & Rosenthal, Software By Design (1994) | Ch.14 |
| B-24 | Ehn, Work-Oriented Design of Computer Artifacts (1988) | P14 |
| B-25 | Greenbaum & Kyng, Design at Work (1991) | P14 |
| B-26 | Schuler & Namioka, Participatory Design (1993) | P14 |
| B-27 | Nielsen, Usability Engineering (1993) | P13 |
| B-28 | Johnson et al., "Xerox Star, a retrospective" (IEEE, 1989) | Ch.2 |
| B-29 | Rheinfrank, Hartman & Wassermann, "Design for usability" (1992) | Ch.4 |
| B-30 | Tufte, The Visual Display of Quantitative Information (1983) | Ch.3 |
| B-31 | Tufte, Envisioning Information (1990) | Ch.3 |
| B-32 | Nardi, A Small Matter of Programming (1993) | P11 |
| B-33 | Neumann, Computer-Related Risks (1995) | Ch.6, P1 |
| B-34 | Laurel (ed.), The Art of Human-Computer Interaction (1990) | P9 |
| B-35 | Gibson, The Ecological Approach to Visual Perception (1979) | Ch.7 |
| B-36 | Ong, Orality and Literacy (1982) | Ch.7 |
| B-37 | Rosmarin, The Power of Genre (1985) | Ch.7 |
| B-38 | Illich, Tools for Conviviality (1973) | Ch.5 |
| B-39 | Yanagi, The Unknown Craftsman (1972) | Ch.5 |
| B-40 | Karasek & Theorell, Healthy Work (1990) | Ch.14 |
| B-41 | Brooks, The Mythical Man-Month (1975/1995) | P1 |
| B-42 | Richards, Artful Work (1995) | Ch.13 |
| B-43 | Moggridge, "Design for the information revolution" (1992) | P8 |
| B-44 | ACM Code of Professional Conduct (1995) | Ch.14 |
| B-45 | Lave & Wenger, Situated Learning (1991) | Ch.4 |
| B-46 | Medina-Mora et al., "The ActionWorkflow approach" (1993) | P6 |

---

## 专项报告四：全书方法论谱系

以下将全书提出的所有可用作设计实践指导的方法/框架/流程按"抽象→具体"排列。

| 层级 | 方法/框架 | 来源 | 适用范围 |
|------|----------|------|----------|
| 哲学层 | Reflection-in-action / Conversation with materials | Schön (Ch.9) | 所有设计活动的认识论基础 |
| 哲学层 | Design = Creating, not Problem Solving | Kelley (Ch.8) | 设计者心态的哲学定位 |
| 哲学层 | Center-Periphery / Genre | Brown & Duguid (Ch.7) | 设计的社会文化本体论 |
| 策略层 | Design Language (C→R→D→E→E) | Rheinfrank & Evenson (Ch.4) | 产品线级的系统化设计策略 |
| 策略层 | Action-Centered Design (Domain Ontology) | Denning & Dargan (Ch.6) | 从行动域出发的设计方法论 |
| 策略层 | Prototyping Culture (Spec-driven vs. Proto-driven) | Schrage (Ch.10) | 组织级的设计文化策略 |
| 战术层 | Conceptual Model → Control → Display (优先级) | Liddle (Ch.2) | 交互设计的优先序决策 |
| 战术层 | Five-Stage Interaction Design (U-A-S-R-D) | Crampton Smith & Tabor (Ch.3) | 个体设计师的工作循环 |
| 战术层 | IDEO Process (U-O-V-E-I) | Profile 8 | 产品设计团队的流程框架 |
| 战术层 | Participatory Design (Mockups + Scenarios + Role-play) | Kuhn (Ch.14) / Profile 14 | 与用户/工人的协作设计 |
| 操作层 | Follow-Me-Home | De Young / Intuit (Ch.13) | 用户真实环境观察 |
| 操作层 | Just Call 10 Customers | Monson / Intuit (Ch.13) | 快速低成本用户输入 |
| 操作层 | Character Maps + Scenarios + Storyboards | IDEO (Profile 8) | 可视化用户理解 |
| 操作层 | Business-Process Mapping (ActionWorkflow Loop) | Profile 6 | 组织工作流的映射和分析 |
| 操作层 | Periodic Prototyping | Schrage (Ch.10) | 制度化原型节奏 |

L### 分析说明：全书没有给出"唯一正确的方法"——这正是本书的核心立场：设计不能被简化为一份食谱。上述方法论形成了一个"工具箱"——不同层级的方法适用于不同的设计情境。设计师的核心能力不是"知道所有方法"，而是"知道在何时使用何种方法，以及在何时放下方法"。

---

## 专项报告五：全书关键引语汇编

以下选录全书最具代表性和可引用性的语句，按主题排列。

### 主题 1：什么是设计

1. "It's where you stand with a foot in two worlds—the world of technology and the world of people and human purposes—and you try to bring the two together." — Kapor (Ch.1)

2. "Software design is the act of determining the user's experience with a piece of software. It has nothing to do with how the code works inside." — Liddle (Ch.2)

3. "There is no direct path between the designer's intention and the outcome. As you work a problem, you are continually in the process of developing a path into it." — Schön (Ch.9)

4. "The designer has a dream that goes beyond what exists, rather than fixing what exists." — Kelley (Ch.8)

### 主题 2：设计 vs. 工程

5. "The lack of usability of software and the poor design of programs are the secret shame of the industry." — Kapor (Ch.1)

6. "Assume a spherical cow." — Kelley (Ch.8)

7. "The standard engineering design process produces a fundamental blindness to the domains of action in which the customers of software systems live and work." — Denning & Dargan (Ch.6)

### 主题 3：形式与内容

8. "As far as the user is concerned, WYGIWYS: What you get is what you see. The interface is the product." — Crampton Smith & Tabor (Ch.3)

9. "The future of design...lies not in developing means of increasingly full re-presentation, but rather in allowing increasing amounts to be underrepresented." — Brown & Duguid (Ch.7)

### 主题 4：用户与市场

10. "We do not use tools simply because they are friendly. We use tools to accomplish tasks, and we abandon tools when the effort required to make the tool deliver exceeds our threshold of indignation." — Saffo (Ch.5)

### 主题 5：组织与实践

11. "When you are asked to solve a problem, look beyond it. Ask why that particular problem arose in the first place." — Norman (Ch.12)

12. "Always treat your employees exactly as you want them to treat your best customers." — Covey, cited by De Young (Ch.13)

### 主题 6：社会与伦理

13. "For them, the use of computers can be an oppressive experience, rather than a liberating one." — Kuhn (Ch.14)

14. "To design computer-based systems is to make an organizational intervention—an intervention that can have powerful effects on how people work and live." — Kuhn (Ch.14)

### 主题 7：设计的终极目标

15. "Not every designer can produce a design that evokes love, but that's not a bad description of what good design is trying to achieve." — Schön (Ch.9)

---

*报告生成时间：2026-08-04*  
*全书分析覆盖：14 章 + 14 篇 Profile + Preface + Introduction + Reflection + Bibliography*  
*实体索引总项数：人物 48 项 / 组织 32 项 / 产品 30 项 / 概念 40 项 / 事件 31 项 / 文献 46 项*  
*使用分析方法论：L### 分层标注系统 + 跨章关联分析 + 概念网络图谱*
