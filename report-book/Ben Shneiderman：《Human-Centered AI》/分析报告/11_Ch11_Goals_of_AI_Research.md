# 11 第十一章分析报告 —— Introduction: What Are the Goals of AI Research?

---

## 一、章节定位与功能

### L144 定位描述
本章是Part 3"Design Metaphors"的引入章。它定义了AI研究的两个基本目标——科学目标（理解并模拟人类智能）和创新目标（开发有益的产品与服务）——并在此基础上引出四对设计隐喻，作为Part 3后续五章（Ch12-Ch16）的内容纲要。引语来自Virginia Dignum关于责任与AI的论述，强调了"委托不等于免责"的核心伦理立场。

### L145 核心功能
1. 定义两个AI研究目标：Science Goal与Innovation Goal
2. 提出四对设计隐喻作为两个目标的组合可能性
3. 建立Part 3的内容路线图（Figure 11.1）
4. 讨论AI的历史成就与失败——建立批判性但非敌意的立场
5. 引入"combined designs"（组合设计）作为超越"二择一"的路径

---

## 二、结构分析

### L146 章节结构
1. **开篇引言（¶1-2）**：60年前的AI研究目标——Turing Test及其演变
2. **Science Goal深描（¶3-5）**：模式识别、自然语言处理、翻译、游戏对弈、情感识别
3. **AI成就与失败（¶6-7）**：IBM Deep Blue不使用AI方法？知识型专家系统的失败vs.规则系统的成功
4. **深度学习脆弱性批评（¶8-9）**：Gary Marcus & Ernest Davis的批评；Mitchell Waldrop——"how far AI still has to go"
5. **HCAI替代路径（¶10）**：透明化、可解释UI、审计轨迹、独立监督
6. **四对隐喻的路线图（¶11-17）**：逐一预告Ch12-Ch16
7. **组合设计总结（¶18）**

---

## 三、内容分析

### L147 两个AI目标的对比
| 维度 | Science Goal | Innovation Goal |
|------|-------------|-----------------|
| 核心追求 | 理解人类知觉/认知/运动能力→构建匹配或超越的机器 | 开发广泛使用的产品与服务 |
| 典型应用 | 下棋、识别肿瘤、社交机器人 | 导航系统、自然语言翻译、搜索查询补全 |
| 描述词汇 | 智能代理、智能行为、AGI | 超级工具、远距机器人、主动电器 |
| 隐喻偏好 | 人形机器人、队友、自主系统 | 工具、器械、控制中心 |
| 理论基础 | 理性主义传统 | 经验主义传统 |
| 代表教科书 | Russell & Norvig | Poole & Mackworth |

### L148 关键论点
- **IBM Deep Blue案例**：领衔研究者Feng-hsiung Hsu明确声明他们没有使用AI方法——他们使用硬件暴力搜索（"brute force hardware solution"），这对"AI成功叙事"构成讽刺性解构
- **知识型专家系统的失败**："AI-guided knowledge-based expert systems have failed, but carefully engineered rule-based systems with human-curated rule sets have succeeded"——暗示AI的"智能"标签可能与实际成功脱钩
- **Marcus & Davis的批评**：深度学习"brittle"（脆弱的）——实验室有效但真实世界失败；种族主义聊天机器人、医疗建议失败、撞上消防车的自动驾驶汽车
- **终结目标**："a new synthesis of human-centered design thinking with the best of AI methods"

---

## 四、逻辑梳理

### L149 论证链
```
定义两个目标：Science Goal vs. Innovation Goal
    ↓
历史追溯：Turing→Deep Blue→Deep Learning→当前
    ↓
批判：许多"AI成功"并非真的用了AI方法
      深度学习脆弱——需要common-sense reasoning
      "brute force"有时比"intelligent"更有效
    ↓
提出方案：HCAI综合——透明化+人控+审计+监督
    ↓
引出Part 3路线图：四对隐喻（Ch12-16）+组合设计
```

---

## 五、材料使用方式

1. **教科书引用**：Russell & Norvig, Poole & Mackworth——建立两个目标的学术来源
2. **历史案例解构**：IBM Deep Blue（"非AI"声明）、知识型专家系统——用"历史修正主义"策略削弱AI的宏大叙事
3. **批判性文献引用**：Marcus & Davis《Rebooting AI》、Waldrop PNAS文章——借用知名批评者建立同盟
4. **图解式预告**：Figure 11.1将四对隐喻以表格形式相互对照——视觉化的Part 3路线图

---

## 六、论辩与阐述方法

1. **"简单二分法"的自审**："My critics tell me the separation into science and innovation goals is far from perfect"——在Ch17中，对二分法的承认与辩护更为完整
2. **温和批评**：不全面否定Science Goal，而是指出其局限，并提出组合方案
3. **"combined designs"的反复强调**：以数码相机为例——自动设置光圈和快门（自动化）+用户构图和按快门（人类控制）

---

## 七、语言文风

### L150 原文摘录
> "Even after sixty years, AI is in its early days. I want AI to succeed, and see the way forward is to adopt HCAI design processes." (¶10)

> "Awareness of the different goals can stimulate fresh thinking about how to deal with different contexts by creating combined designs that leads to reliable, safe, and trustworthy systems." (¶18)

### L151 文风特征
- L151｜本章语气是全书最平衡的之一——既有对AI的批评，又反复表达"我希望AI成功"
- L151｜大量引用直接来源（Hsu关于Deep Blue的声明、Marcus & Davis的批评、Waldrop的文章）——建立了与AI社区的对话感

---

## 八、实体清单

### L152 人物实体（≥3）
| 名称 | 身份 | 语境 |
|------|------|------|
| Alan Turing | 计算机科学之父 | Turing Test（1950）——AI科学的起点 |
| Stuart Russell | UC Berkeley计算机科学家 | Science Goal的教科书定义者 |
| Peter Norvig | Google研究员 | Russell的合著者 |
| David Poole & Alan Mackworth | 英属哥伦比亚大学教授 | Innovation Goal的教科书定义者 |
| Feng-hsiung Hsu | IBM Deep Blue领衔 | "我们没有使用AI方法"——对AI叙事的解构 |
| Garry Kasparov | 国际象棋世界冠军 | 1997年被Deep Blue击败 |
| Gary Marcus & Ernest Davis | NYU教授 | 《Rebooting AI》——深度学习批评者 |
| Mitchell Waldrop | 科学作家 | PNAS文章——"how far AI has to go" |
| Virginia Dignum | 于默奥大学教授 | 章首引语——责任与AI |
| Marvin Minsky, John McCarthy, Herb Simon | AI早期先驱 | Marcus & Davis批评的预测失败者 |

### L153 组织/机构实体（≥3）
| 名称 | 类型 | 语境 |
|------|------|------|
| IBM | 科技公司 | Deep Blue, Watson |
| DeepMind (Google) | AI研究公司 | AlphaGo, AlphaFold |

### L154 概念实体（≥3）
| 术语 | 定义 |
|------|------|
| Science Goal | AI科学目标——理解人类智能→构建模拟或超越的机器 |
| Innovation Goal | AI创新目标——开发广泛使用的产品与服务 |
| Turing Test | 图灵测试——如果观察者无法区分人机对话，则机器通过测试 |
| combined designs | 组合设计——在一个产品中结合自动化和人类控制的特征 |
| algorithmic hubris | 算法傲慢——程序员对其自主系统过度自信 |
| brittleness (of deep learning) | 深度学习的脆弱性——实验室有效但真实世界失败 |

---

## 九、与前后章关联

### L155 关联
- **Ch10（前）**：Part 2总结后自然过渡至Part 3的"设计隐喻"
- **Ch12（后）**：对Science Goal和Innovation Goal的展开（科学子目标+创新子目标）
- **Ch13-Ch16（后）**：四对隐喻的逐一剖析——本章已提前布局（¶11-17）
- **Ch17（后）**：Part 3的Skeptic's Corner——重审二分法
