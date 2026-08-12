# NN 专项报告与实体总索引

---

## L501 专项报告一：HCAI二维框架与设计哲学体系

### L502 框架的起源与演进
施奈德曼的HCAI二维框架（Ch8, Figure 8.2）是全书最具原创性的理论贡献。它起源于对Sheridan & Verplank (1978)一维"自主性十级量表"四十年统治的系统性不满。作者承认自己直到1987年的教科书还在传播这一错误的一维思维，认知转变来自观察现实设计案例——"某些特征有高人类控制、另一些有高自动化"——从而"解耦"（decouple）了这两个维度。

### L503 框架的深层结构
四象限并非平等的——右上象限（高水平人类控制+高水平计算机自动化）是明确的设计目标。其他三个象限各有其合理的适用情境（快速响应、人类掌握、简单设备），而灰色危险区域（过度自动化、过度人类控制）是设计师必须避免的陷阱。

### L504 框架的操作化
框架通过三条路径操作化：
1. **Ch9的设计指南**（八条黄金规则+HCAI模式语言）
2. **Part 3的四对设计隐喻**——每组对映框架的两个维度
3. **Part 4的四层治理结构**——为框架中的"可靠、安全、可信"目标提供制度保障

### L505 框架的影响与局限
框架被26章直接用于轮椅设计（Figure 26.1），在全书末章的"管弦乐综合"中，框架与设计隐喻、治理结构一起构成全书的三大思想支柱。其最大局限是：**客观度量"人类控制"和"计算机自动化"的水平仍然缺失**——这是作者在Ch10和Ch25中承认的核心挑战。

---

## L510 专项报告二：设计隐喻的四元体系

### L511 隐喻对的结构逻辑
Part 3的四对隐喻并非随机——它们分别对应人机关系的四个层次：

| 层次 | 隐喻对（左=Science Goal / 右=Innovation Goal） | 章节 |
|------|------|------|
| **语言/认知层** | Intelligent Agents ⟷ Supertools | Ch13 |
| **社会关系层** | Teammates ⟷ Tele-bots | Ch14 |
| **控制模型层** | Assured Autonomy ⟷ Control Centers | Ch15 |
| **身体/形态层** | Social Robots ⟷ Active Appliances | Ch16 |

每一层的左侧隐喻对应Science Goal（模拟人类），右侧对应Innovation Goal（增强人类）。

### L512 综合解决方案：Combined Design
施奈德曼在每对隐喻中都强调"combined design"——不是二选一，而是"粒度级"的组合：哪些特征可以可靠地由自动化处理（左侧隐喻的精华），哪些特征需要或应由人类控制（右侧隐喻的精华）。数码相机是全书的贯穿案例——自动设置光圈/快门/防抖（自动化部分）+用户构图/变焦/快门时机（人类控制部分）。

### L513 隐喻对中的价值排序
尽管作者声称两个Goal都有价值，**事实上全书的论证持续偏向Innovation Goal**——Supertools优于Agents、Tele-bots优于Teammates、Control Centers优于Assured Autonomy、Active Appliances优于Social Robots。Mumford的"animism"批判（Ch12, Ch16）为这一价值排序提供了历史哲学的支撑。

---

## L520 专项报告三：四层治理结构的操作体系

### L521 四层嵌套逻辑
Figure 18.2的四层嵌套椭圆图是全书仅次于二维框架的最重要图表。它建立了一个"俄罗斯套娃"式的治理架构：个人团队被嵌入组织、组织被嵌入行业、行业被嵌入政府规制。

### L522 每层的关键创新
| 层 | 最原创的贡献 |
|----|------------|
| **Team (Ch19)** | 将航空飞行数据记录器(FDR)类比推广为"每台HCAI系统中的审计轨迹"；提出"预防优于解释"的UI设计策略 |
| **Organization (Ch20)** | 将四种组织安全理论(Mumford/Perrow/HRO/Leveson)整合为五条HCAI安全管理策略；提出"奖励报告险兆多的管理者" |
| **Industry (Ch21)** | 将会计事务所审计-保险公司承保-NGO倡导-专业标准四者同时纳入独立监督体系；以建筑法规（"building codes"）为类比 |
| **Government (Ch22)** | "规制可以加速创新"的反直觉论点；已有监管机构（NTSB, FDA, FAA, NIST, FTC）的"AI化"策略 |

### L523 15条建议的可实施性评估
作者本人在Ch23中承认："No industry will implement all fifteen recommendations." 每条建议需要研究验证，系统复杂度使全局评估困难。这一诚实的自我评估使四层治理结构从"教条"降级为"出发点"——"These governance structures are a starting point."

---

## L530 实体总索引

### L531 人物索引（按出场频率排序，精选25位）

| 人物 | 身份 | 首次出现章 | 核心角色 |
|------|------|-----------|----------|
| Ben Shneiderman | 本书作者、UMD教授 | Ch1 | 全书的叙述者与论证者 |
| Lewis Mumford | 技术史家/哲学家 | Ch12 | "animism"批判——全书设计隐喻部分的理论支柱 |
| Tom Sheridan | MIT教授 | Ch6 | 1978十级自主量表提出者——全书要超越的"旧范式" |
| Fei-Fei Li | Stanford CS教授 | Ch1/Ch6 | Stanford HAI联合创始人——HCAI运动的代表人物 |
| Douglas Engelbart | HCI先驱 | Ch12/Epilogue | 智力增强(IA)之父——supertools传统的奠基人 |
| Clifford Nass | Stanford教授 | Ch14 | CASA范式——"Nass's fallacy"的源头 |
| Gary Marcus & Ernest Davis | NYU教授 | Ch11 | 《Rebooting AI》作者——深度学习批评者 |
| Cathy O'Neil | 华尔街量化分析师 | Ch1/Ch19 | 《Weapons of Math Destruction》——偏差研究标志性人物 |
| Joy Buolamwini | MIT研究员 | Ch19/Ch21 | Algorithmic Justice League——面部识别偏差突破 |
| Timnit Gebru | AI伦理研究者 | Ch19 | 被Google解雇——Intersectional bias研究 |
| Shannon Vallor | 爱丁堡哲学家、前Google伦理学家 | Ch26 | 关怀哲学——老龄关怀的道德基础 |
| Joanna J. Bryson | Hertie School教授 | Ch18 | "治理的是人对技术的使用" |
| Daniela Rus | MIT CSAIL主任 | Ch12 | "AI只是一个工具" + "parallel autonomy" |
| Michael Jordan | UC Berkeley ML权威 | Ch6 | 呼吁新工程学科 |
| Cynthia Rudin | Duke教授 | Ch19 | "停止解释黑箱ML模型" |
| Frank Pasquale | 法律学者 | Ch23 | 《New Laws of Robotics》 |
| Shoshanna Zuboff | Harvard商学院教授 | Ch22 | "surveillance capitalism" |
| Kate Crawford | Microsoft研究者 | Ch23 | "AI的采掘本质" |
| J.C.R. Licklider | MIT/ARPA | Ch13 | "Man-Computer Symbiosis"(1960) |
| Gary Klein | 心理学家 | Ch14 | "十项挑战"——使机器如队友般行为的障碍 |
| Geoffrey Hinton | 图灵奖得主 | Ch5 | "停止培训放射科医生"——Skeptic's Corner代表 |
| Alan Turing | 计算机科学之父 | Ch11/Ch13 | Turing Test——AI的起点 |
| Grace Hopper | 美国海军指挥官/计算机先驱 | Ch17 | "It's always been done that way"是最具破坏性的话 |
| Brian Cantwell Smith | 多伦多大学教授 | Ch10 | "我们应该敬畏人类心智的成就" |
| Frederick Douglass | 美国废奴主义者 | Ch27 | "Trust is the foundation of society" |

### L532 组织/机构索引（按类别，精选40个）

**政府与监管机构**：NTSB, FDA, FAA, FTC, SEC, NIST, NSF, US National Academy of Sciences, OMB, EU

**国际组织**：UN (ITU, IAEA, SDGs), OECD, G20/GPAI

**大学与研究中心**：Stanford HAI, MIT CSAIL & Media Lab, UC Berkeley, CMU SEI, IHMC, Johns Hopkins (Institute for Assured Autonomy & Capacity Command Center), NYU (AI Now Institute), Oxford Internet Institute, Harvard Berkman Klein Center, Monash University (Human-Centered AI), University of Toronto (Ethics of AI Lab)

**企业**：Google (PAIR, DeepMind, Waymo), Microsoft, IBM, Apple, Amazon, Facebook, Intuitive Surgical, iRobot, Boston Dynamics, SoftBank Robotics, SONY

**专业协会**：IEEE, ACM, AAAI, A3 (formerly RIA), ISO

**NGO与公民社会组织**：Algorithmic Justice League, Partnership on AI, Future of Life Institute, Electronic Privacy Information Center (EPIC), Brookings Institution, Data & Society, ForHumanity, Foundation for Responsible Robotics, AI4ALL, Center for AI and Digital Policy (Dukakis Institute), Underwriters Laboratories

**会计/咨询/保险公司**：PwC, Deloitte, E&Y, KPMG, Accenture, McKinsey, Boston Consulting Group, Travelers Insurance

### L533 概念/术语索引（精选50个核心术语）

| 术语 | 英原文 | 章 |
|------|--------|-----|
| 人本人工智能 | Human-Centered AI (HCAI) | Ch1+全书 |
| 新综合 | new synthesis | Ch1, Ch18, Ch23, Ch27 |
| 二维HCAI框架 | Two-Dimensional HCAI Framework | Ch8 |
| 超级工具 | supertools | Ch1, Ch12, Ch13 |
| 可靠、安全、可信 | reliable, safe, trustworthy | Ch7+全书 |
| 八条黄金规则 | Eight Golden Rules | Ch9 |
| HCAI模式语言 | HCAI Pattern Language | Ch9 |
| 审计轨迹 | audit trails / product logs | Ch7, Ch19 |
| 设计隐喻 | design metaphors | Part 3 |
| 科学目标 vs. 创新目标 | Science Goal vs. Innovation Goal | Ch11, Ch12 |
| 智能代理 | intelligent agents | Ch13 |
| 队友 | teammates | Ch14 |
| 远距机器人 | tele-bots | Ch14 |
| 保证自主 | assured autonomy | Ch15 |
| 控制中心 | control centers | Ch15 |
| 社交机器人 | social robots | Ch16 |
| 主动电器 | active appliances | Ch9, Ch16 |
| 组合设计 | combined designs | Part 3 |
| 理性主义 / 经验主义 | rationalism / empiricism | Ch2 |
| 万物有灵论障碍 | animism (Mumford) | Ch12, Ch16 |
| Nass谬误 | Nass's fallacy | Ch14, Ch16 |
| 过度自动化 / 过度人类控制 | excessive automation / excessive human control | Ch8 |
| 算法傲慢 | algorithmic hubris | Ch8 |
| 四层治理结构 | four-layer governance structures | Ch18+Part 4 |
| 能力成熟度模型 | Capability Maturity Model (CMM) | Ch7, Ch20 |
| 信任度成熟度模型 | Trustworthiness Maturity Model (TMM) | Ch20 |
| 解释权 | right to explanation (GDPR) | Ch19, Ch22 |
| 可解释UI防止哲学 | preventing the need for explanations | Ch19 |
| 偏差的类型学 | bias typologies (Friedman/Nissenbaum + Baeza-Yates + USC) | Ch19 |
| 直接操纵 | direct manipulation | Ch2, Epilogue |
| 信息可视化箴言 | overview first, zoom and filter, then details-on-demand | Ch9, Epilogue |
| 人-机共生 | man-computer symbiosis (Licklider) | Ch13, Epilogue |
| 人类在组群中，计算机在循环中 | Humans in the Group; Computers in the Loop | Ch2, Ch9 |
| 飞行数据记录器类比 | FDR analogy | Ch7, Ch19 |
| 建筑规范类比 | building code analogy (Landwehr) | Ch21 |
| 营养标签类比 | nutrition label analogy | Ch19, Ch25 |
| 正常事故理论 | normal accident theory (Perrow) | Ch20 |
| 高可靠性组织 | high reliability organizations (HRO) | Ch20 |
| 韧性工程 | resilience engineering (Woods) | Ch20 |
| 安全文化 | safety culture (Leveson) | Ch20 |
| 失败与险兆报告 | failure and near miss reporting | Ch20 |
| 红队测试 | red team testing | Ch19 |
| 蜕变测试 | metamorphic testing | Ch19 |
| 监督资本主义 | surveillance capitalism (Zuboff) | Ch22 |
| 巴斯德象限 | Pasteur's Quadrant (Stokes) | Ch24 |
| HCAI信任度量表 | HCAI Trustworthiness Scale | Ch25 |
| 透明度代理 | transparency as proxy for trustworthiness | Ch25 |
| Apgar评分类比 | APGAR scale analogy | Ch25 |
| 原地老龄化 | aging in place | Ch26 |
| 非我也，关乎我也 | Nothing about us without us! | Ch26 |

### L534 技术/产品/系统索引（精选35个）

| 名称 | 类型 | 出现章 |
|------|------|--------|
| Digital Cameras | 消费电子 | Ch1, Ch9, Ch17 |
| Roomba (iRobot) | 吸尘机器人 | Ch2, Ch16 |
| AlphaGo (DeepMind/Google) | AI博弈程序 | Ch1, Ch11 |
| AlphaFold 2 (DeepMind/Google) | 蛋白折叠AI | Ch24 |
| Boeing 737 MAX (MCAS) | 航空/软件 | Ch1, Ch6, Ch8, Ch15 |
| Tesla Autopilot | 自动驾驶 | Ch2, Ch6, Ch8, Ch15, Ch20, Ch22 |
| Waymo (Google) | 自动驾驶技术 | Ch8 |
| Patriot Missile System | 军事系统 | Ch6, Ch15 |
| DaVinci Surgical System (Intuitive Surgical) | 手术机器人 | Ch14, Ch16 |
| NASA Mars Rovers | 航天/机器人 | Ch14 |
| Bloomberg Terminal | 金融数据终端 | Ch14 |
| Google Nest Thermostat | 智能家居 | Ch9, Ch16 |
| PCA (Patient-Controlled Analgesia) | 医疗设备 | Ch8 |
| Mercedes-Benz Active Parking Assist | 汽车技术 | Ch8 |
| Boston Dynamics Spot | 工业四足机器人 | Ch16 |
| PARO (therapeutic seal robot) | 治疗机器人 | Ch16 |
| Joy for All (Hasbro) | 伴宠机器人 | Ch16 |
| AIBO (SONY) | 宠物机器人 | Ch16 |
| Alexa / Siri / Google Home | 语音虚拟助手 | Ch3, Ch16 |
| Xiaoice (小冰) | 中国聊天机器人 | Ch16 |
| DeepDream (Google) | 神经网络可视化 | Ch3 |
| Flight Data Recorders (FDR) | 航空安全 | Ch1, Ch7, Ch19 |
| Google Flu Trends | 预测算法(已退役) | Ch8 |
| Google Search auto-completion | 搜索推荐 | Ch9 |
| Seek by iNaturalist | 儿童物种识别APP | Ch24 |
| IBM Watson | 认知计算/增强智能 | Ch1, Ch11 |
| iNaturalist | 公民科学平台 | Ch24 |
| eBird (Cornell) | 公民科学 | Ch24 |
| Zooniverse (Oxford) | 公民科学 | Ch24 |
| High-Frequency Trading Algorithms | 金融算法 | Ch8, Ch15 |
| GitHub | 代码托管与审计 | Ch19, Ch20 |
| Bugzilla | Bug追踪 | Ch20 |
| AI Incident Database (Partnership on AI) | AI事故档案 | Ch1, Ch20 |
| FDA Adverse Event Reporting System (FAERS) | 不良事件报告系统 | Ch20 |
| Wheelchairs (4 designs) | 辅助设备 | Ch26 |

### L535 出版物/文献索引（精选25个，按全书出场频率）

| 作品 | 作者 | 年 | 类型 |
|------|------|-----|------|
| Technics and Civilization | Lewis Mumford | 1934 | 技术哲学/历史——全书多处引用 |
| Artificial Intelligence: A Modern Approach | Russell & Norvig | 2020(4e) | AI教科书 |
| Weapons of Math Destruction | Cathy O'Neil | 2016 | 通俗/AI批评 |
| Superintelligence | Nick Bostrom | 2014 | 通俗/AI风险 |
| Rebooting AI | Gary Marcus & Ernest Davis | 2019 | 通俗/AI批评 |
| Machines of Loving Grace | John Markoff | 2015 | 通俗/AI vs. IA历史 |
| Designing the User Interface | Ben Shneiderman | 1986(1e) | HCI教科书——八大黄金规则的来源 |
| The Promise of Artificial Intelligence | Brian Cantwell Smith | 2019 | 哲学 |
| New Laws of Robotics | Frank Pasquale | 2020 | 法律/政策 |
| The Oxford Handbook of Ethics of AI | Dubber, Pasquale, Das (eds.) | 2020 | 学术文集 |
| Trust: The Social Virtues and the Creation of Prosperity | Francis Fukuyama | 1995 | 政治科学 |
| Normal Accidents | Charles Perrow | 1984 | 组织社会学 |
| Pasteur's Quadrant | Donald Stokes | 1997 | 科学政策 |
| Future Shock | Alvin Toffler | 1970 | 通俗未来学 |
| The Robots Are Coming | Martin Ford | 2015 | 通俗/AI-失业 |
| Software Psychology | Ben Shneiderman | 1980 | 学术——施奈德曼的早期突破 |
| Understanding Media | Marshall McLuhan | 1964 | 媒体理论——影响作者的早期作品 |
| Human + Machine | Daugherty & Wilson | 2018 | 商业/管理 |
| Computer Power and Human Reason | Joseph Weizenbaum | 1976 | 哲学/AI批评 |
| Encounters with HCI Pioneers | Ben Shneiderman | 2019 | 自传/历史 |
| Exploratory Data Analysis | John Tukey | 1977 | 统计学——信息可视化的基础 |
| Stanford AI 100 Report | Stanford University | 2016 | 学术报告——Ch3的反驳对象 |
| IEEE Ethically Aligned Design | IEEE | 2019 | 专业协会标准报告 |
| Berkman Klein Center AI Ethics Report | Harvard | 2020 | 学术综述 |
| The Age of Surveillance Capitalism | Shoshanna Zuboff | 2019 | 政治经济/批判 |

### L536 事件/运动索引（精选15个）

| 事件/运动 | 时间 | 出现章 |
|-----------|------|--------|
| 蒙特利尔负责任AI宣言 | 2017 | Ch1 |
| UN AI for Good Global Summit | 2017至今 | Ch1, Ch22 |
| GDPR实施(含"解释权") | 2018 | Ch1, Ch19, Ch22 |
| 波音737 MAX两起坠机 | 2018/2019 | Ch1, Ch6, Ch8, Ch15 |
| Tesla 2016年致命车祸(NTSB调查) | 2016 | Ch6, Ch8, Ch22 |
| Google Flu Trends退役 | 2015 | Ch8 |
| COVID-19大流行(2020-2021) | 2020-2021 | 全书多处 |
| IBM/Amazon/Microsoft停止向警方出售面部识别 | 2020春季 | Ch18, Ch21 |
| Timnit Gebru被Google解雇 | 2020 | Ch19 |
| January 6 US Capitol暴动 | 2021 | Ch24 |
| Apple & Google合作COVID接触追踪APP | 2020 | Ch21 |
| 2019年社交机器人初创倒闭潮(Jibo, Anki, Kuri) | 2019 | Ch16 |
| OECD AI原则被50+国家采纳 | 2019 | Ch22 |
| 中国新一代AI发展规划发布 | 2017 | Ch22 |
| 俄罗斯情报机构"active measures"30年行动 | 1990s-至今 | Ch24 |

---

## L540 专项报告四：方法索引——全书论证策略与工具目录

### L541 全书的重复论证策略

| 策略 | 描述 | 出现频率 | 典型章节 |
|------|------|----------|----------|
| 二元对比→超越(synthesis) | 设置两个对立的立场→在对比中澄清→提出"新综合"或"组合设计"为超越路径 | 极高（每章） | Ch2, Part 3 |
| 案例驱动论证 | 以具体案例（数码相机、电梯、PCA、轮椅等）展示抽象概念的操作化 | 极高 | Ch8, Ch9, Ch26 |
| Skeptic's Corner | 每Part末章设"怀疑者角落"→主动呈现反方立场→温和回应 | 5次 | Ch5, Ch10, Ch17, Ch23, Ch27 |
| 历史谱系法 | 将当前争议追溯至数百年的历史连续体（哲学/技术/艺术） | 高 | Ch2, Ch13, Ch15, Ch16 |
| 类比链 | 以成熟行业的成功机制类比HCAI的缺失机制（航空FDR、建筑规范、营养标签、品酒评分、Apgar评分） | 高 | Ch7, Ch19, Ch21, Ch25 |
| 个人叙事插入 | 在学术论述中插入个人经历（徒步两个地图、NAS评估小组、购买Fisca机器人狗）→增强在场感 | 中 | Ch1, Ch2, Ch16, Ch25 |
| 引语传统 | 每章以历史/当代人物引语开篇→建立思想连续性 | 27章 | 全书 |
| 可视化工具 | 以图形（Figure 1.2, 8.2, 8.4, 18.2, 26.1）将抽象关系转化为空间直觉 | 关键章 | Ch1, Ch8, Ch18, Ch26 |

### L542 全书反复出现的"品牌语句"
1. "amplify, augment, empower, and enhance human performance"——HCAI的核心功能描述
2. "reliable, safe, and trustworthy systems"——HCAI的三核心目标
3. "self-efficacy, creativity, responsibility, and social connections"——HCAI增强的四项人类品质
4. "human rights, justice, and dignity"——HCAI服务的核心人类价值
5. "Researchers, developers, business leaders, and policy-makers"——全书的四大读者/利益相关者
6. "Humans in the Group; Computers in the Loop"——Ch2保险杠贴纸口号，全书反复出现
7. "guidebook to hope and a roadmap to realistic policies"——全书的自我定义（Ch1→Ch27首尾呼应）
8. "a new synthesis"——全书的核心创新标签
9. "bridging the gap from ethics to practice"——Part 4的核心主题
10. "combined designs"——Part 3的解决方案口号

---

*本索引覆盖全书27章的正文章节（不含Notes, Bibliography, Name Index, Subject Index），实体清单以L###编号标注。各章的详细实体清单请参见对应分析报告的第八节。*
