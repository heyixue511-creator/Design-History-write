# 07 第七章分析报告 —— Defining Reliable, Safe, and Trustworthy Systems

---

## 一、章节定位与功能

### L090 定位描述
本章是Part 2的第二章，承担全书的**目标定义**功能。在Ch6破除旧范式后，Ch7正面定义HCAI系统的三核心目标——"reliable, safe, and trustworthy"——并将其映射到Part 4的四层治理结构（软件工程实践→组织安全文化→独立监督认证→政府规制）。这是全书"目标-手段"结构的枢纽章节。

### L091 核心功能
1. 正式定义可靠（reliable）、安全（safe）、可信（trustworthy）的内涵差异
2. 将三目标分配至四层治理主体：软件工程师→业务管理者→独立监督机构→政府
3. 呈现"25属性"全景图（Figure 7.1）——HCAI系统的理想品质清单
4. 为Ch19-22（Part 4）的四层治理建议提供完整的预告式提纲

---

## 二、结构分析

### L092 章节结构
1. **定义段（¶1）**：可靠/安全/可信的四个实现层面
2. **Reliable展开（¶2）**：软件工程五项技术实践——审计轨迹、工作流、验证确认、偏差测试、可解释UI
3. **Safe展开（¶3-4）**：安全管理五项策略——领导承诺、安全招聘培训、失败报告、内部审查、行业标准
4. **Capability Maturity Model提及（¶4）**：卡内基梅隆SEI的CMM模型
5. **Trustworthy展开（¶5-7）**：Fukuyama的信任理论→四类独立监督机构——会计事务所、保险公司、NGO/公民社会、专业组织
6. **政府规制（¶8）**：Ch22的简短预告
7. **25属性全景图（¶9）**：Figure 7.1 + 成熟技术类比（电梯、相机、医疗设备、手术机器人）
8. **总结与过渡（¶10-11）**：用户不关心计算机自主性——他们想要的是"dramatically increase their performance while simplifying their effort"

---

## 三、内容分析

### L093 核心论题
可靠、安全、可信三个目标各有不同的实现主体和方法，需要四层治理结构的分工协作。这套四层结构与传统的三目标体系构成了全书的操作蓝图。

### L094 三目标-四层映射表
| 目标 | 第一层：团队（Ch19） | 第二层：组织（Ch20） | 第三层：行业（Ch21） | 第四层：政府（Ch22） |
|------|---------------------|---------------------|---------------------|---------------------|
| Reliable | 审计轨迹、工作流、V&V测试、偏差测试、可解释UI | — | — | — |
| Safe | — | 领导承诺、安全招聘培训、失败报告、内部审查、行业标准 | — | — |
| Trustworthy | — | — | 外部审计、保险补偿、NGO监督、专业标准 | 立法与监管 |

### L095 "25属性"概述
Figure 7.1展示了从"可靠"到"可持续"的全景式HCAI品质清单，含：trust, reliability, safety, transparency, fairness, accountability, privacy, security, explainability, usability, accessibility, sustainability等——构成全书最丰富的概念集合。施奈德曼承认这些属性都难以测量，甚至难以判断某项设计改变是否会提升或降低这些属性。

---

## 四、逻辑梳理

### L096 论证链
```
定义三目标：reliable + safe + trustworthy（各有侧重）
    ↓
确定四层主体：团队→组织→行业→政府
    ↓
将每层主体与最相关目标配对（映射表见上）
    ↓
扩展至25属性全景（承认测量困难）
    ↓
回到用户视角：他们不关心"自主性"——他们想要更好的表现和更少的努力
```

---

## 五、材料使用方式

1. **Fukuyama信任理论**：引用《Trust: The Social Virtues and the Creation of Prosperity》——从政治科学借入信任概念
2. **消费者类比**：Consumer's Report, Underwriters Laboratory——公众靠这些组织判断产品是否可信
3. **成熟技术类比**：电梯、相机、家用电器、手术机器人——在可靠性、安全性、可信度上已被广泛接受
4. **CMM模型**：SEI/Carnegie Mellon的能力成熟度模型——从软件开发借用管理方法论

---

## 六、论辩与阐述方法

1. **"trusted vs. trustworthy"的区分**：一个系统可能被错误地信任（mistakenly trusted），但"trustworthy"意味着它值得信任——这是一对重要的语义区分
2. **四层嵌套结构**：从微观（软件工程团队）到宏观（政府）的分层治理，形成Figure 18.2嵌套椭圆图
3. **清单式预告**：本章对Part 4各章的内容做了详尽的bullet-point式预告（审计轨迹、Verification & Validation、偏差测试、可解释UI、失败报告系统等）——使Part 2到Part 4的过渡如地图般清晰

---

## 七、语言文风

### L097 原文摘录
> "Most consumers, industrial supervisors, physicians, and airplane pilots are not interested in computer autonomy; what they want are systems to increase their performance dramatically, while simplifying their effort, so they can devote themselves to their higher aspirations." (¶11)

> "Public expectations go beyond trust or trusted systems; users want trustworthy systems. A system could be mistakenly trusted, but a trustworthy system is one that deserves trust." (¶6)

### L098 文风特征
- L098｜本章是全书最"架构性"的章节——大量使用编号列表（5项、5项、4项）和括号内章节引用
- L098｜"trusted vs. trustworthy"的区分体现了施奈德曼作为系统设计者对"客观品质"vs."主观感知"的敏感

---

## 八、实体清单

### L099 人物实体（≥3）
| 名称 | 身份 | 语境 |
|------|------|------|
| Francis Fukuyama | 政治科学家 | 《Trust》作者——信任的社会理论基础 |
| David Lazer | 研究者 | Google Flu Trends分析 |

### L100 组织/机构实体（≥3）
| 名称 | 类型 | 语境 |
|------|------|------|
| Software Engineering Institute (SEI) / CMU | 研究所 | Capability Maturity Model (CMM) |
| Underwriters Laboratory | 产品安全认证机构 | 消费者信任的独立认证 |
| Consumer's Report | 消费者评测杂志 | 作为trustworthy认证的类比 |
| US Securities and Exchange Commission (SEC) | 美国政府监管机构 | 金融界的独立监督 |

### L101 概念实体（≥3）
| 术语 | 定义 |
|------|------|
| reliable | 可靠——系统在需要时产生预期响应 |
| safe | 安全——通过安全管理文化防止伤害 |
| trustworthy | 可信——经由独立监督认证后"值得信任" |
| Capability Maturity Model (CMM) | 能力成熟度模型——SEI的组织改进框架 |
| audit trails | 审计轨迹——类比飞行数据记录器的系统日志 |

---

## 九、与前后章关联

### L102 关联
- **Ch6（前）**：破除旧范式后，本章开始构建新范式的目标体系
- **Ch8（后）**：末段预告——"The HCAI framework (Chapter 8) guides designers..."
- **Part 4（远）**：本章的全部bullet-point列表（审计轨迹、V&V、偏差测试、失败报告、行业标准等）构成了Part 4（Ch19-Ch22）的内容大纲
- **Ch25（远）**：25属性的评估困难在Ch25"Assessing Trustworthiness"中成为核心议题
