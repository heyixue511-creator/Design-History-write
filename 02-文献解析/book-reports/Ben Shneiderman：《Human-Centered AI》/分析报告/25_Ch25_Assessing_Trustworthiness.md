# 25 第二十五章分析报告 —— Assessing Trustworthiness

---

## 一、章节定位与功能

### L323 定位描述
本章是全书在方法论上最具原创性的章节之一。面对"你不能测量它就不能改进它"（Lord Kelvin）的工程传统，施奈德曼系统反思了HCAI品质（尤其信任度）如何被评估的难题，并提出了自己的**HCAI信任度量表**（Table 25.3，12条×0-2分=0-24分）。本章的独特贡献在于：面对"无法客观度量"的困境，以"评分+开放报告+社会过程"的混合方法寻找出路。

### L324 核心功能
1. 呈现30+ HCAI属性的五类组织型Table 25.1——"General virtues"、"Performs well in practice"、"Clarity to stakeholders"、"Enables independent oversight"、"Complies with accepted practices"
2. 反思客观度量、组件评分和社会化评估三种评估路径的适用性
3. 提出HCAI信任度量表（Table 25.3）——12项×0-2分=0-24分的主观评分体系
4. 讨论IEEE P7001透明度标准、Dukakis Center AI社会契约指数等已有尝试

---

## 二、结构分析

### L325 章节结构
1. **测量传统与局限（¶1-3）**：Lord Kelvin——"If you cannot measure it, you cannot improve it"——但企业成功/候选能力/制造安全等远比温度或重量更难测量
2. **HCAI属性的评估困境（¶4-6 + Table 25.1）**：30+属性的五类组织——"there is a great deal of discussion of ethical principles...but very few suggestions about how to assess"
3. **Trusted vs. Trustworthy（¶7-8）**：作者的徒步经历——专业地图《被信任但不可信》，手绘地图却可信——"Appearances can be deceiving, so validations of trustworthiness are needed"
4. **三种评估路径（¶9-22）**：
   - **Objective Measurement**：客观度量目前对HCAI属性不可行
   - **Scoring by Components**：Wine Spectator（50-100评分）、品酒五品质（外观/香气/酒体/口感/余味）、UC Davis葡萄酒评分（10个组件）、奥运会评委打分（花样滑冰/跳水/拳击/体操）、Apgar新生儿健康评分（5个组件各0/1/2）
   - **Assessment by Social Processes**：招聘委员会、学术论文审查、企业董事会、Delphi方法、SWOT分析、UK REF研究评估、河流/森林环境报告、Conference Board消费者信心指数(5000人)、密歇根消费者信心指数(500人电话50题)
5. **独立监督的社会过程（¶23-27）**：三种形式——规划监督+持续监控+灾难回顾分析
6. **HCAI Trustworthiness Scale（¶28-37 + Table 25.3）**：12项×0-2分=0-24分
7. **其他评估计划（¶38-40）**：IEEE P7001透明度标准、Dukakis AI社会契约指数、Will Griffin的建议——透明度=信任度的可操作度量
8. **总结（¶41）**

---

## 三、内容分析

### L326 核心论题
HCAI系统的信任度无法像温度或重量那样客观测量——但我们在品酒、奥运会和新生儿健康评分中发展了**带评分规范的主观/组件评判法**，这些方法可以启发HCAI评估。

### L327 Table 25.3: HCAI Trustworthiness Scale（施奈德曼量表）
| 条目 | 评分规则 |
|------|----------|
| 1) 实施前的内部独立审查 | 如有可公开的全面报告，最多1分 |
| 2) 已实施审计轨迹 | 如报告有正面结果，再加1分 |
| 3) 训练数据已采集并评估 | +1/条 |
| 4) 软件已验证和确认 | +1/条 |
| 5) 公平性已经测试 | +1/条 |
| 6) 可解释性已实施并测试 | +1/条 |
| 7) 使用前2个月的性能 | +1/条 |
| 8) 使用前6个月的性能 | +1/条 |
| 9) 利益相关者报告/提问/报告事件与险兆 | +1/条 |
| 10) 针对事件有内部审查和纠正流程 | +1/条 |
| 11) 持续审查以支持改进 | +1/条 |
| 12) 由独立监督机构进行的外部审查 | +1/条 |
| **总分范围：0-24** | (每项最多2分=1分报告+1分正面结果) |

总原则：**透明性通过报告**："The scale emphasizes transparency by way of reports for each item"

### L328 三种评估路径的比较
| 路径 | 适用 | HCAI适用性 | 关键挑战 |
|------|------|------------|----------|
| **客观度量** | 温度、体重、时间 | 不可用（目前） | 信任度没有"信任度计" |
| **组件评分** | 品酒（50-100）、奥运会（0-10）、Apgar（0-10） | 最有希望路径 | 需要评分规范+培训评分员+跨评分员一致性 |
| **社会过程** | 招聘委员会、NTSB调查、UK REF | 补充路径 | 依赖专家群体、可能缓慢且昂贵 |

### L329 关键洞见
- **"trusted vs. trustworthy"的区分通过个人故事阐明**：徒步中的两个地图——"I trusted this professional map...but it was not trustworthy"——"可信"不等于"被信任"
- **"nutrition label for HCAI"的提议**：如食品包装的营养成分标签——IBM Factsheets/Microsoft Datasheets/Google Model Cards
- **Will Griffin的"透明度=信任度代理"提议**：类比核不扩散审查——"允许核查其核设施的国家是被信任的"——IEEE P7001标准正在开发这一方向

---

## 四、逻辑梳理

### L330 论证链
```
前提：Lord Kelvin——"不能测量就不能改进"→HCAI品质需要被评估
    ↓
困境：客观度量不可行——30+属性没有"仪表"
    ↓
替代路径1：组件评分——借鉴品酒/奥运会/Apgar的模型
    ↓
替代路径2：社会过程——独立监督/NTSB调查/委任审计
    ↓
替代路径3：透明度代理——"透明度=信任度的可度量代理"(Griffin)
    ↓
施奈德曼量表：12项×2分——以"公开报告+正面结果"为标准
    ↓
谦虚的收束："requires testing and refinement"
```

---

## 五、材料使用方式

1. **品酒评分的细致描述**：Wine Spectator(50-100)→UC Davis(10个组件)→奥运会(Code of Points)→Apgar(5组件0/1/2)——建立"主观评分但规范严格"的连续谱系
2. **个人叙事**：徒步中两个地图的故事——将"trusted vs. trustworthy"的抽象区分压缩为亲身故事
3. **量表提案**：Table 25.3是本书中施奈德曼最具操作性的建议——完整、可实施、可测试
4. **政策引述**：IEEE P7001透明度标准、Dukakis AI社会契约指数——证明"别人也在做"
5. **比较法**：EU委员会、US NIST、许多公司——"all working to develop assessments"——建立"这是正在兴起的领域"的印象

---

## 六、论辩与阐述方法

1. **从"测量"到"评分"到"社会过程"的递进**：当客观度量不可能时→组件评分；当组件评分也不确定时→社会过程——一种"认知退路"的递进结构
2. **品酒→奥运会→Apgar的类比链**：以成熟领域的主观评判法为HCAI评估建立类比合法性
3. **量表提案的"谦虚"修辞**：不声称量表完美——"will require testing and refinement"、"Other items could be added"——保持学术谨慎
4. **食物营养标签的类比**：将抽象评估问题转化为熟悉的日常体验

---

## 七、语言文风

### L331 原文摘录
> "If you cannot measure it, you cannot improve it." ——Lord Kelvin (¶1)

> "Trust is the foundation of society. Where there is no truth, there can be no trust, and where there is no trust, there can be no society." ——Frederick Douglass (Ch27引语——但在Ch25中被引出)

> "Appearances can be deceiving, so validations of trustworthiness are needed." (¶8)

### L332 文风特征
- L332｜本章将日常体验（品酒、远足、家庭婴儿Apgar测试）与抽象评估方法连接——全书最具"类比论证"特征的章节
- L332｜Table 25.1（30+属性）是全书最长的单表——具有"概念目录"的参考工具价值

---

## 八、实体清单

### L333 人物实体（≥3）
| 名称 | 身份 | 语境 |
|------|------|------|
| Lord Kelvin | 19世纪物理学家 | "If you cannot measure it, you cannot improve it" |
| Virginia Apgar | 麻醉科医生 | Apgar新生儿健康评分(1952)——5组件0/1/2 |
| Will Griffin | HyperGiant首席伦理官 | 透明度=信任度的可操作度量 |
| Robert Hoffman & Peter Hancock | 人因工程专家 | 27项开发程序的恢复力度量 |
| Frederick Douglass | 19世纪美国废奴主义者和作家 | "Trust is the foundation of society"（Ch27引语） |

### L334 概念实体（≥3）
| 术语 | 定义 |
|------|------|
| HCAI Trustworthiness Scale | 施奈德曼量表——12项×0-2分=0-24分 |
| scoring by components | 组件评分法——品酒/奥运会/Apgar的评估模式 |
| inter-rater reliability | 评分者间一致性——不同评判者给出相似分数 |
| repeatability | 可重复性——同一评判者在不同时间给出相似分数 |
| SWOT analysis | 优势/劣势/机会/威胁分析——评估计划/组织的结构方法 |
| Delphi method | 德尔菲法——多轮讨论→共识或投票 |
| APGAR scale | Apgar评分——新生儿健康的5组件0-2分模型 |
| nutrition label for HCAI | HCAI的营养标签——IBM Factsheets/Microsoft Datasheets/Google Model Cards |

### L335 组织/机构实体（≥3）
| 名称 | 类型 | 语境 |
|------|------|------|
| Wine Spectator | 葡萄酒杂志 | 50-100评分→90+为"Outstanding" |
| Olympic Committee | 体育组织 | "Code of Points"——主观评分的极限案例 |
| Conference Board (US) | 商业研究组织 | 月度消费者信心调查——5000人 |
| University of Michigan Consumer Sentiment Index | 大学研究 | 500人/月×50题——1966年12月=100基准 |
| IEEE P7001 | 专业标准 | 自主系统透明度标准 |
| Dukakis Center for AI and Digital Policy | 政策研究中心 | AI社会契约指数——25国12属性0-1评分 |

---

## 九、与前后章关联

### L336 关联
- **Ch24（前）**：从未来Grand Challenges回到"我们如何知道进展了？"——评估方法论
- **Ch26（后）**：将HCAI理念应用于老龄关怀——框架的具体用例
- **Ch19（远）**：Table 25.3的12条中有多条（审计轨迹、V&V、公平性测试、可解释性、内部审查）直接基于Ch19-20的实践推荐
