# NN 专项报告与实体总索引

---

## 专项报告A：机制与条件框架的操作手册

**LNA01** 本专项报告将本书的核心框架——机制与条件框架（The Mechanisms and Conditions Framework）——提炼为可操作的分析工具手册，供研究者和设计者直接使用。

### A.1 框架的核心分析问题

**LNA02** 框架要求分析者回答一个双重问题：
> "How does this object/technology afford, and for whom and under what circumstances?"

这一双重问题替代了传统可供性分析的单一问题："What does this object afford?"

### A.2 六个机制范畴的操作定义

**LNA03**

| 机制 | 方向 | 力度 | 操作定义 | 判断标准 |
|------|------|------|----------|----------|
| **Request**（请求） | 器物→用户 | 弱 | 器物表明对某行为方向的偏好，但其他选项保持开放 | 用户可忽略、可部分遵循、可完全遵循 |
| **Demand**（要求） | 器物→用户 | 强 | 器物坚持某一行为方向，其他选项变得不可行/不可信 | 用户必须服从，否则须放弃使用或进行创造性规避 |
| **Encourage**（鼓励） | 用户→器物 | 正向响应 | 器物使某行为方向变得轻松、显而易见、顺畅 | 行为被执行时无障碍或障碍极低 |
| **Discourage**（阻碍） | 用户→器物 | 负向响应 | 器物设置障碍，行为仍可行但需要额外努力、技能或创造性 | 行为可执行但需要变通（workaround）、高技能或冒险 |
| **Refuse**（拒绝） | 用户→器物 | 强负向响应 | 器物使某行为方向变得不可行或不可信 | 行为看似不可能，但非绝对（存在规避和重新设计的可能） |
| **Allow**（允许） | 双向 | 中性 | 器物对某行为方向既不推动也不阻碍 | 行为可执行，无压力无阻碍，类似"分叉路口" |

### A.3 三个条件维度的操作定义

**LNA04**

| 条件 | 核心问题 | 分析维度 |
|------|----------|----------|
| **Perception**（感知） | 主体是否意识到器物的功能？ | 意识vs.无意识；专家感知vs.普通感知；感知的解放效应vs.约束效应 |
| **Dexterity**（灵巧度） | 主体是否有能力操作器物的功能？ | 物理能力（身体）；认知能力（知识/技能）；能力的可变性（学习/退化） |
| **Cultural and Institutional Legitimacy**（文化与制度合法性） | 主体的使用是否被规范/规则/法律所支持？ | 文化规范（informal）；制度规则（formal）；法律（coercive）；交叉性（intersectionality） |

### A.4 框架使用步骤

**LNA05**
1. **识别目标技术/器物**及其关键特征（features）
2. 对每个特征，判断其**首要机制范畴**（request/demand/encourage/discourage/refuse/allow），并意识到其可能与其他范畴有边界重叠
3. 对每个机制判断，追问**for whom?**——考虑不同社会位置的主体（种族、阶级、性别、性向、能力、年龄等）
4. 对每个"for whom"，继续追问**under what circumstances?**——感知条件、灵巧度条件、文化-制度合法性条件
5. **记录分析中的不确定性和可争议点**——将"模糊地带"视为分析洞察的来源而非缺陷
6. **反思分析者自身的社会位置**——我的判断在何种程度上受我自己的感知/灵巧度/合法性条件所影响？

---

## 专项报告B：可供性概念谱系图

**LNB01** 本专项报告以图表形式呈现可供性概念从1966年到2020年的学术演化轨迹。

### B.1 谱系演化主线

**LNB02**

| 时间 | 学者/事件 | 贡献 | 学科 |
|------|-----------|------|------|
| 1930s | Koffka, Lewin | 格式塔心理学："demand-character" | 心理学 |
| 1966 | Gibson | 首次定义"affordance" | 生态心理学 |
| 1979 | Gibson | The Ecological Approach to Visual Perception（经典著作） | 生态心理学 |
| 1984 | Warren | 楼梯攀登实验：可供性的程度量化 | 实验心理学 |
| 1988 | Norman | The Psychology of Everyday Things：可供性进入设计/HCI | 设计研究/HCI |
| 1990s | Turvey, Michaels等 | effectivity概念；affordance-effectivity complementarity | 生态心理学 |
| 2000 | Ingold | 人类学中的可供性：突破nature/culture二分 | 人类学 |
| 2003 | Chemero | 情境适配：affordance需要object-subject-circumstance三者适配 | 哲学/心理学 |
| 2009 | Maier & Fadel | Affordance-Based Design (ABD) | 工程学 |
| 2009 | Schraube | Technology as Materialized Action（全书理论支点） | 批判心理学 |
| 2012 | DiSalvo | Adversarial Design | 设计研究 |
| 2013 | Norman | DOET修订版：real vs. perceived affordances | 设计研究 |
| 2015 | Nagy & Neff | Imagined Affordance | 传播学 |
| 2017 | Evans et al. | 特征→可供性→结果中介模型 | 传播学 |
| 2018 | Bivens & Hasinoff | App Feature Analysis | 传播学/STS |
| 2020 | Jenny L. Davis | 机制与条件框架 | 社会学/STS |

### B.2 三大批判的对应解决

**LNB03**

| 持久批判 | 来源 | 框架的解决方案 |
|----------|------|----------------|
| 定义混乱（Definitional confusion） | Gibson自身的内在矛盾 + Norman的再表述 + 跨学科扩散 | 六个机制提供了跨学科共享的"简单语汇" |
| 二元化应用（Binary application） | 尽管Gibson/Norman都强调程度，实际应用仍以"是否可供"为主 | what→how的提问转换 + 机制的力度梯度 |
| 忽视主体与情境（Failure to account for diverse subjects and contexts） | 普适化假设 + "默认用户"的隐形 | for whom and under what circumstances + 三个条件维度 |

---

## 专项报告C：全书跨章节论证脉络图

**LNC01** 本专项报告展示全书七章之间的论证递进关系和核心概念在章间的流动。

### C.1 论证递进结构

**LNC02**

```
Ch.1 Introduction ──── 问题提出 + 框架预告
    │                    (购物车承诺 → 三大问题 → 框架初现)
    ↓
Ch.2 History ──── 概念谱系 + 批判缺口
    │                    (Gibson/Norman → 跨学科 → 三大批判 → 前行路径)
    ↓
Ch.3 Politics ──── 政治基础 + 不对称性前提
    │                    (McLuhan → ANT → Winner → Schraube/materialized action)
    ↓
Ch.4 Mechanisms ──── 六机制范畴
    │                    (Request/Demand + Encourage/Discourage/Refuse + Allow)
    ↓
Ch.5 Conditions ──── 三条件维度
    │                    (Perception + Dexterity + Cultural/Institutional Legitimacy)
    ↓
Ch.6 Practice ──── 方法论配对
    │                    (五项标准 → CTDA/Walkthrough/AppFA/ValuesReflection/Adversarial)
    ↓
Ch.7 Conclusion ──── 前瞻与呼吁
                         (AI语境化 → 五个Big Questions → "get to work")
```

### C.2 核心概念跨章流动

**LNC03**

| 概念 | 首次出现 | 主要展开 | 跨章贯穿 |
|------|----------|----------|----------|
| affordance（可供性） | Ch.1 | Ch.2, Ch.4 | 全七章 |
| mechanisms（机制） | Ch.1预告 | Ch.4 | Ch.1, 3, 4, 5, 6, 7 |
| conditions（条件） | Ch.1预告 | Ch.5 | Ch.1, 3, 4, 5, 6, 7 |
| efficacy vs. agency | Ch.3 | Ch.3 | Ch.1, 3, 4, 5, 6, 7 |
| asymmetry（不对称性） | Ch.3 | Ch.3 | Ch.3, 4, 5, 6, 7 |
| materialized action | Ch.1提及 | Ch.3 | Ch.1, 3, 4, 5, 7 |
| politics of artifacts | Ch.1 | Ch.3 | Ch.1, 3, 4, 5, 6, 7 |
| shopping cart | Ch.1 | Ch.1 | Ch.1, 2, 4, 5, 7 |
| ANT | Ch.1提及 | Ch.3 | Ch.2, 3, 6 |
| binary affordance | Ch.1 | Ch.2, Ch.4 | Ch.1, 2, 4 |

---

## 实体总索引

### 索引A：核心学者/人物总表

**LNN01**

| 编号 | 姓名 | 首次出现章节 | 主要学科 | 核心贡献 |
|------|------|-------------|----------|----------|
| A01 | James J. Gibson | Ch.1 | 生态心理学 | 可供性概念创始人 (1966, 1979) |
| A02 | Donald A. Norman | Ch.1 | 设计研究/HCI | 将可供性引入设计研究 (1988, 2013) |
| A03 | Marshall McLuhan | Ch.3 | 传播学 | "媒介即讯息" (1964) |
| A04 | Bruno Latour | Ch.1 | STS/社会学 | 行动者网络理论 (ANT) |
| A05 | Langdon Winner | Ch.3 | STS/政治学 | "Do Artifacts Have Politics?" (1980) |
| A06 | Ernst Schraube | Ch.1 | 批判心理学 | Technology as Materialized Action (2009) |
| A07 | Virginia Eubanks | Ch.1 | 政治学/社会政策 | Automating Inequality (2018) |
| A08 | Safiya Umoja Noble | Ch.1 | 信息研究/种族研究 | Algorithms of Oppression (2018) |
| A09 | André Brock | Ch.6 | 传播学/种族研究 | CTDA方法创始人 |
| A10 | Carl DiSalvo | Ch.6 | 设计研究 | Adversarial Design (2012) |
| A11 | William H. Warren | Ch.2 | 实验心理学 | 楼梯攀登经典实验 (1984) |
| A12 | Batya Friedman | Ch.1 | 信息科学 | 价值敏感设计 (Value-Sensitive Design) |
| A13 | Mary Flanagan | Ch.1 | 游戏研究/设计 | Values at Play (2014) |
| A14 | Helen Nissenbaum | Ch.1 | 信息科学/哲学 | Values at Play (2014) |
| A15 | Peter Nagy & Gina Neff | Ch.2 | 传播学 | Imagined Affordance (2015) |
| A16 | Sandra K. Evans et al. | Ch.2 | 传播学 | 特征→可供性→结果模型 (2017) |
| A17 | Rena Bivens & Amy Adele Hasinoff | Ch.6 | 传播学 | App Feature Analysis (2018) |
| A18 | Peter-Paul Verbeek | Ch.3 | 技术哲学 | 设计作为道德事业 (2011) |
| A19 | Zeynep Tufekci | Ch.3 | 社会学 | 数字技术与社会运动 (2017) |
| A20 | Tim Ingold | Ch.2 | 人类学 | 人类学中的可供性 (2000) |
| A21 | Anthony Chemero | Ch.2 | 哲学/心理学 | 情境适配理论 (2003) |
| A22 | Andrea Scarantino | Ch.2 | 哲学 | surefire vs. probabilistic affordances |
| A23 | Stefanie Duguay | Ch.5 | 传播学 | LGBTQI+社交媒体研究 |
| A24 | Christopher M. Julien | Ch.4 | 社会学 | Imgur种族话语研究 |
| A25 | Frank Pasquale | Ch.3 | 法学 | 算法与法律 |
| A26 | Sylvan Goldman | Ch.1 | 商业/发明 | 购物车发明者 (1937) |
| A27 | Robert Moses | Ch.3 | 城市规划 | 纽约长岛桥梁设计者 |
| A28 | Kurt Koffka | Ch.2 | 格式塔心理学 | "demand-character"概念 (1930s) |
| A29 | Kurt Lewin | Ch.2 | 格式塔心理学 | 感知与意义建构 |
| A30 | Galon Higdon | Ch.4 | 美国政治 | HB37法案提出者 (2017) |

### 索引B：核心案例/器物总表

**LNN02**

| 编号 | 案例/器物 | 首次出现 | 主要讨论 | 所属机制/条件示例 |
|------|-----------|----------|----------|-------------------|
| C01 | 购物车/硬币锁 | Ch.1 | Ch.1, 2, 4, 5 | request→demand, 全六机制 |
| C02 | Robert Moses低悬桥梁 | Ch.3 | Ch.3, 4 | refuse (公共汽车) |
| C03 | 绳索围栏→木栅栏→电围栏 | Ch.4 | Ch.4 | request→demand梯度 |
| C04 | 警察隔离带 | Ch.4 | Ch.5 | cultural/institutional legitimacy |
| C05 | Facebook实名/性别/分享 | Ch.1 | Ch.1, 4, 5 | demand, encourage, all six |
| C06 | Twitter 280字符限制 | Ch.4 | Ch.4 | refuse→discourage→用户规避 |
| C07 | Instagram发帖频率规范 | Ch.4 | Ch.4, 5 | discourage (文化性) |
| C08 | Imgur投票机制 | Ch.4 | Ch.4 | discourage (异议) |
| C09 | 反性侵App数据集 | Ch.6 | Ch.6 | encourage (受害者保护) |
| C10 | 大盘子vs.小盘子 | Ch.4 | Ch.4 | encourage (非意图) |
| C11 | 楼梯攀登(Warren实验) | Ch.2 | Ch.2, 5 | 程度性可供性 |
| C12 | 量杯当酒杯 | Ch.5 | Ch.5 | perception (感知激活) |
| C13 | Google/Facebook广告种族主义 | Ch.4 | Ch.4 | allow (政治性) |
| C14 | 学术出版付费墙 | Ch.4 | Ch.4 | demand (付费/机构) |
| C15 | 搜索引擎算法(Noble) | Ch.1 | Ch.1 | encourage (种族主义) |
| C16 | 自动化决策系统(Eubanks) | Ch.1 | Ch.1 | demand, refuse |
| C17 | 恒温器家庭规则 | Ch.5 | Ch.5 | cultural legitimacy |
| C18 | 屏幕阅读器+网页 | Ch.5 | Ch.5 | dexterity→辅助技术 |
| C19 | 沙特女性驾驶禁令 | Ch.5 | Ch.5 | institutional legitimacy变迁 |
| C20 | MySpace个性化 | Ch.4 | Ch.4 | encourage (vs. Facebook refuse) |
| C21 | 搅拌机/灯光调光器 | Ch.4 | Ch.4 | allow (经典) |
| C22 | Occupy Albany WiFi | Ch.3 | Ch.3 | ANT案例 |
| C23 | 前置摄像头/自拍 | Ch.1 | Ch.1, 4 | encourage |
| C24 | Portions Master Skinny Plate | Ch.4 | Ch.4 | encourage (意图性) |
| C25 | CCD-me-not Umbrella | Ch.6 | Ch.6 | 对抗性设计 |

### 索引C：核心概念/术语总表

**LNN03**

| 编号 | 术语 | 英文 | 首次出现 | 核心含义 |
|------|------|------|----------|----------|
| T01 | 可供性 | affordance | Ch.1 | 器物与技术之间的多面关系结构 |
| T02 | 机制与条件框架 | Mechanisms and Conditions Framework | Ch.1 | 全书核心贡献 |
| T03 | 请求 | request | Ch.1 | 器物表明偏好，留有弹性 |
| T04 | 要求 | demand | Ch.1 | 器物坚持方向，其他不可行 |
| T05 | 鼓励 | encourage | Ch.1 | 使行为轻松、显而易见 |
| T06 | 阻碍 | discourage | Ch.1 | 设置障碍，行为仍可行 |
| T07 | 拒绝 | refuse | Ch.1 | 使行为不可行或不可信 |
| T08 | 允许 | allow | Ch.1 | 中性的双向适用 |
| T09 | 感知 | perception | Ch.1 | 主体对功能的意识和理解 |
| T10 | 灵巧度 | dexterity | Ch.1 | 操作功能的物理/认知能力 |
| T11 | 文化与制度合法性 | cultural and institutional legitimacy | Ch.1 | 规范/规则/法律的中介 |
| T12 | 技术作为物化行动 | technology as materialized action | Ch.1 | Schraube, 全书理论支点 |
| T13 | 效力vs.能动性 | efficacy vs. agency | Ch.3 | 技术有效力，唯人类有能动性 |
| T14 | 行动者网络理论 | actor-network theory (ANT) | Ch.1 | Latour, 对称性共构 |
| T15 | 技术决定论 | technological determinism | Ch.1 | McLuhan被批判的立场 |
| T16 | 媒介即讯息 | the medium is the message | Ch.3 | McLuhan (1964) |
| T17 | 人造物的政治 | politics of artifacts | Ch.3 | Winner (1980) |
| T18 | 想象的可供性 | imagined affordance | Ch.2 | Nagy & Neff (2015) |
| T19 | 敌意建筑 | hostile architectures | Ch.3 | Savić & Savičić |
| T20 | 对抗性设计 | adversarial design | Ch.6 | DiSalvo (2012) |
| T21 | 批判性技术文化话语分析 | critical technocultural discourse analysis (CTDA) | Ch.6 | Brock |
| T22 | 漫游法 | walkthrough method | Ch.6 | Light, Burgess & Duguay |
| T23 | App特征分析 | app feature analysis | Ch.6 | Bivens & Hasinoff |
| T24 | 价值反思 | values reflection | Ch.6 | Friedman等 |
| T25 | 预期使用环境 | environment of expected use | Ch.6 | vision/operating model/governance |
| T26 | 分析性停顿点 | analytic stopping points | Ch.4 | 机制范畴的认识论定位 |
| T27 | 多孔边界 | porous boundaries | Ch.4 | 机制范畴间的模糊地带 |
| T28 | 多稳态性 | multistable | Ch.3 | 技术效果的多样性 |
| T29 | 本体论矛盾 | ontologically ambivalent | Ch.3 | Schraube, 技术效果不可预见 |
| T30 | 直接知觉 | direct perception | Ch.2 | Gibson的反表征主义 |

---

## 索引D：核心方法论/方法总表

**LNN04**

| 编号 | 方法 | 创始人/代表 | 首次出现 | 与框架的关系 |
|------|------|-----------|----------|-------------|
| M01 | Critical Technocultural Discourse Analysis (CTDA) | André Brock | Ch.6 | 拟合度最高 |
| M02 | The Walkthrough Method | Light, Burgess, Duguay | Ch.6 | 框架替代ANT作为理论基础 |
| M03 | App Feature Analysis | Bivens & Hasinoff | Ch.6 | 框架增强"for whom/under what circumstances" |
| M04 | Values Reflection | Friedman等 | Ch.6 | 框架结构化价值想象 |
| M05 | Adversarial Design | Carl DiSalvo | Ch.6 | 框架提供 agonism 语汇 |
| M06 | Value-Sensitive Design | Batya Friedman | Ch.1 | 框架的"实践转向"背景 |
| M07 | Affordance-Based Design (ABD) | Maier & Fadel | Ch.2 | 工程学中的可供性方法论 |

---

## 索引E：核心制度/组织/平台总表

**LNN05**

| 编号 | 名称 | 类型 | 首次出现 | 在书中的角色 |
|------|------|------|----------|-------------|
| O01 | Facebook | 社交媒体平台 | Ch.1 | 贯穿性案例（实名/性别/分享/广告/政治操纵） |
| O02 | Twitter | 社交媒体平台 | Ch.4 | 字符限制/用户名柄/政治表达 |
| O03 | Instagram | 社交媒体平台 | Ch.4 | 发帖规范/内容审查/LGBTQI+ |
| O04 | Imgur | 图像分享平台 | Ch.4 | 投票机制/种族话语 |
| O05 | Google | 搜索引擎+广告 | Ch.1 | 搜索偏见/广告关键词定向 |
| O06 | MySpace | 社交媒体平台 | Ch.4 | 个性化 vs. Facebook标准化的对比 |
| O07 | Tinder | 约会App | Ch.5 | LGBTQI+审查 |
| O08 | Vine | 短视频平台 | Ch.5 | 放任政策/毒性技术文化 |
| O09 | MIT Press | 学术出版社 | Ch.1 | 本书出版方 |
| O10 | W3C | 标准制定机构 | Ch.5 | 无障碍网页标准 |
| O11 | ProPublica | 新闻机构 | Ch.4 | 调查Facebook广告定向 |
| O12 | BuzzFeed | 新闻机构 | Ch.4 | 调查Google广告关键词 |
| O13 | Cambridge CFI | 研究机构 | Ch.7 | AI研究（Leverhulme Centre for the Future of Intelligence） |
| O14 | Stanford HAI | 研究机构 | Ch.7 | AI研究（Human-Centered AI） |
| O15 | NYU AI Now | 研究机构 | Ch.7 | AI研究 |
| O16 | Google DeepMind | 企业研究 | Ch.7 | AI研究 |
| O17 | OpenAI | 非营利研究 | Ch.7 | AI研究 |
| O18 | Tsinghua University AI Institute | 学术研究 | Ch.7 | AI研究 |
| O19 | Allen Institute for AI | 研究机构 | Ch.7 | AI研究 |
| O20 | Silicon Valley | 产业区域 | Ch.6 | "white guy problem"的所指 |

---

## 索引F：核心文献/著作总表

**LNN06**

| 编号 | 文献 | 作者/年份 | 首次出现 | 类型 |
|------|------|-----------|----------|------|
| B01 | The Ecological Approach to Visual Perception | Gibson, 1979 | Ch.1 | 专著（可供性奠基文本） |
| B02 | The Psychology/Design of Everyday Things | Norman, 1988/2013 | Ch.1 | 专著（HCI可供性） |
| B03 | Understanding Media: The Extensions of Man | McLuhan, 1964 | Ch.3 | 专著（媒介理论） |
| B04 | "Do Artifacts Have Politics?" | Winner, 1980 | Ch.3 | 期刊论文（技术政治） |
| B05 | Reassembling the Social | Latour, 2005 | Ch.3 | 专著（ANT） |
| B06 | "Technology as Materialized Action" | Schraube, 2009 | Ch.1 | 期刊论文（全书理论支点） |
| B07 | Automating Inequality | Eubanks, 2018 | Ch.1 | 专著（当代批判研究） |
| B08 | Algorithms of Oppression | Noble, 2018 | Ch.1 | 专著（当代批判研究） |
| B09 | Adversarial Design | DiSalvo, 2012 | Ch.6 | 专著（对抗性设计） |
| B10 | Values at Play in Digital Games | Flanagan & Nissenbaum, 2014 | Ch.1 | 专著（价值敏感设计） |
| B11 | "Imagined Affordance" | Nagy & Neff, 2015 | Ch.2 | 期刊论文（传播学可供性） |
| B12 | "Explicating Affordances" | Evans et al., 2017 | Ch.2 | 期刊论文（传播学可供性） |
| B13 | Value Sensitive Design | Friedman & Hendry, 2019 | Ch.5 | 专著（价值敏感设计） |
| B14 | Twitter and Tear Gas | Tufekci, 2017 | Ch.3 | 专著（数字社会运动） |
| B15 | Moralizing Technology | Verbeek, 2011 | Ch.3 | 专著（技术哲学） |
| B16 | "The walkthrough method" | Light, Burgess & Duguay, 2018 | Ch.6 | 期刊论文（方法论） |
| B17 | "Perceiving Affordances: Visual Guidance of Stair Climbing" | Warren, 1984 | Ch.2 | 期刊论文（经典实验） |
| B18 | The Perception of the Environment | Ingold, 2000 | Ch.2 | 专著（人类学可供性） |
| B19 | Unpleasant Design | Savić & Savičić, 2014 | Ch.3 | 会议论文（敌意建筑）【校对修正：年份2013→2014，见源文件L1178/L1710；类型由"专著"改为"会议论文"】 |
| B20 | "Affordance Based Design" | Maier & Fadel, 2009 | Ch.2 | 期刊论文（工程学可供性） |

---

*报告生成日期：2026-08-05*
*源文件：Jenny L. Davis (2020). How Artifacts Afford: The Power and Politics of Everyday Things. Cambridge, MA: The MIT Press.*
*总索引涵盖全书七章，共计：学者30人 | 案例/器物25项 | 概念/术语30条 | 方法7种 | 组织/平台20个 | 文献20部*
