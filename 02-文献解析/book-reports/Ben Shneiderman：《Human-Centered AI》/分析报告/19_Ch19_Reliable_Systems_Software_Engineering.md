# 19 第十九章分析报告 —— Reliable Systems Based on Sound Software Engineering Practices

---

## 一、章节定位与功能

### L245 定位描述
本章是Part 4治理结构的**第一层、也是篇幅最长的章节**，聚焦于软件工程团队层面的五项技术实践。其功能是将HCAI的理想转化为**工程师可以直接执行的具体操作**——这五节构成了全书"操作手册"的核心：审计轨迹与分析工具→软件工程工作流→验证与确认测试→偏差测试→可解释用户界面。

### L246 核心功能
1. 建立软件工程团队层面的五项实践清单
2. 以航空飞行数据记录器（FDR）为原型推广审计轨迹概念
3. 从瀑布到敏捷的工作流演变，适应ML/HCAI项目的特殊性
4. 系统展示五种测试技术：传统基于案例、差分、蜕变、用户体验、红队
5. 偏差的类型学分析（从Batya Friedman到USC团队的23+种偏差）
6. 可解释UI的"预防哲学"——宁可预防错误，不要事后解释

---

## 二、结构分析

### L247 章节结构（5个子节）
1. **Audit Trails and Analysis Tools（¶1-10）**：飞行数据记录器的原型价值；工业机器人、汽车EDR、高频交易的审计轨迹案例
2. **Software Engineering Workflows（¶11-30）**：Zhang等人5种ML问题类型；瀑布vs.敏捷（12条敏捷原则全文）+IBM的数据集敏捷性+Microsoft的9阶段ML工作流
3. **Verification and Validation Testing（¶31-50）**：三种ML的测试方法；五种测试技术（传统、差分、蜕变、UX、红队）；MITRE ATT&CK矩阵；Microsoft Datasheets for Datasets + Google Model Cards
4. **Bias Testing to Enhance Fairness（¶51-75）**：Cathy O'Neil的"数学毁灭武器"三性论；Friedman & Nissenbaum三种偏差；Baeza-Yates的地域/语言/文化偏差；USC团队23+种偏差；Intersectional bias（黑人女性的交叉偏差）；Google对Timnit Gebru的解雇风波
5. **Explainable User Interfaces（¶76-110 + 三个子节）**：GDPR的"解释权"→可解释AI研究热潮；四种路径：固有可理解模型→后置解释→渐进式分步→前瞻探索界面；大量案例（临床决策、癌症治疗选择、音乐推荐、OECD幸福指数）

---

## 三、内容分析

### L248 五项实践速览
| 实践 | 核心原则 | 关键案例/工具 |
|------|----------|---------------|
| **Audit Trails** | 每台机器人中的"飞行数据记录器"；事后追溯分析失败→持续改进 | 航空FDR、汽车EDR、工业机器人、股票交易日志 |
| **Workflows** | ML项目≠传统软件项目；数据是关键——"software engineering is primarily about code...ML is all about data" | 瀑布→敏捷（12条原则）；IBM数据敏捷性；Microsoft 9阶段 |
| **V&V Testing** | 五种技术互补——传统+差分+蜕变+UX+红队 | MITRE ATT&CK(300战术)；Datasheets for Datasets；Model Cards |
| **Bias Testing** | 偏差的深度类型学→从社会到技术到涌现→交叉性偏差 | O'Neil三性；Friedman三类；Baeza-Yates地域偏差；23+种 |
| **Explainable UI** | **预防优于解释**：用选择代替输入→减少对事后解释的需求 | 日历选择器、Amazon四步结账；TurboTax；癌症"patients like me" |

### L249 审计轨迹的核心隐喻
飞行数据记录器（FDR）的价值被充分展开：
- 调查事故原因 → 航空安全大幅提升
- 记录"什么做对了"以改进培训和设备设计
- 检测设备行为随时间的变化以安排预防性维护
- HCAI版本：机器人/汽车的audit trails需要记录ML算法、代码版本、训练数据

### L250 偏差的深度类型学
| 偏差类型 | 提出者 | 说明 |
|----------|--------|------|
| 先在偏差（pre-existing） | Friedman & Nissenbaum | 基于社会态度——如低收入社区贷款拒绝 |
| 技术偏差（technical） | Friedman & Nissenbaum | 硬件/软件设计约束——如按字母排序的器官捐献列表 |
| 涌现偏差（emergent） | Friedman & Nissenbaum | 使用情境变更——如高识字率国家的教育软件用于低识字率国家 |
| 地域/语言/文化偏差 | Baeza-Yates | "bias begets bias"——流行网站更流行 |
| 23+种偏差 | USC团队 | 统计、用户交互、资金等多种形式 |
| 交叉性偏差 | Buolamwini & Gebru | 黑人女性在面部识别中的性能最差 |

### L251 可解释性中的预防哲学
施奈德曼的核心创新——**宁可预防错误，不要依赖事后解释**：
1. **用选择取代输入**：从"输入MMDDYYYY"到"从日历中选择月/日/年"——预防格式错误
2. **渐进分步过程**：Amazon四步结账、TurboTax——每一步引导用户递增向目标
3. **前瞻探索界面（Prospective/Exploratory UI）**：在决策前让用户探索变量敏感度——比事后解释更能建立理解与满意度

---

## 四、逻辑梳理

### L252 论证链
```
可靠性的技术基础：审计轨迹→工作流→测试→偏差→可解释性
    ↓ (审计轨迹)
飞行数据记录器→机器人黑匣子→持续改进→归责清晰化
    ↓ (工作流)
瀑布→敏捷(12原则)+AI特定需求(ML数据=核心)
    ↓ (测试)
五法互补：传统+差分+蜕变+UX+红队
    ↓ (偏差)
三性→三类→交叉性→治理：偏差测试领导+数据集库
    ↓ (可解释)
后置解释的失败教训(MYCIN)→渐进分步+前瞻探索→"预防优于解释"
```

---

## 五、材料使用方式

1. **航空业作为"黄金标准"**：FDR、NTSB——在每项实践中反复引用航空安全实践
2. **企业实践**：Microsoft Datasheets、Google Model Cards、IBM FactSheets、IBM Fairness 360 / Explainability 360——展示行业正在行动
3. **学术研究综述**：从O'Neil的通俗著作到USC团队的23+种偏差学术综述——在通俗与学术之间建立桥梁
4. **具体UI截图**：Figure 19.3-19.8展示从文本分类到音乐推荐到癌症治疗选择的具体界面——使抽象概念可视化

---

## 六、论辩与阐述方法

1. **"五步法"结构**：五项实践构成清晰的操作清单——每项都是工程师可以"明天开始做"的
2. **"航空类比"的反复使用**：一项实践、一个类比——FDR、NTSB、FAA——为软件工程建立可信度
3. **"红队"的军事隐喻**：将军事战争演练的思维引入软件测试——新颖且有效
4. **Cynthia Rudin的激进立场**："Stop explaining black box machine learning models"——引用极端观点拓宽讨论空间

---

## 七、语言文风

### L253 原文摘录
> "software engineering is primarily about the code that forms shipping software, ML (machine learning) is all about the data that powers learning models." ——Microsoft研究 (¶22)

> "Stop explaining black box machine learning models." ——Cynthia Rudin (¶75)

> "transparency and disclosure can increase public trust and confidence in AI applications" ——US White House memorandum (¶82)

### L254 文风特征
- L254｜本章是全书最"工程化"的一章——大量技术术语、流程描述、测试方法枚举
- L254｜"with enough eyes, all bugs are shallow"——引用Eric Raymond的开源哲学——适应"bug bounties"的语境

---

## 八、实体清单

### L255 人物实体（≥3）
| 名称 | 身份 | 语境 |
|------|------|------|
| Cathy O'Neil | 华尔街量化分析师/作家 | 《Weapons of Math Destruction》——偏差研究的关键人物 |
| Batya Friedman & Helen Nissenbaum | 学术界 | 三种偏差的早期分类 |
| Ricardo Baeza-Yates | 智利/西班牙/美国的计算机科学家 | 地域/语言/文化偏差 |
| Joy Buolamwini | MIT研究员 | Algorithmic Justice League——面部识别偏差——纪录片《Coded Bias》 |
| Timnit Gebru | AI伦理研究者 | 被Google解雇引发数千员工抗议——交叉性偏差研究 |
| Cynthia Rudin | Duke大学教授 | "停止解释黑箱ML模型"——坚定立场 |
| Margaret Burnett | Oregon State大学 | 文本分类的视觉解释界面 |
| Katrien Verbert | KU Leuven | 音乐推荐、求职等前向探索UI研究 >10年 |
| Fred Hohman | Apple研究员(原Georgia Tech) | 图像理解中ML特征相关性的视觉探索工具 |
| Fan Du | 马里兰大学博士生 | "patients like me"的视觉推荐界面 |

### L256 组织/机构实体（≥3）
| 名称 | 类型 | 语境 |
|------|------|------|
| MITRE Corporation | 美国政府承包商 | ATT&CK矩阵（~300攻击战术的目录） |
| Algorithmic Justice League | NGO | 面部识别偏差的公开斗争 |
| NIST (US National Institute of Standards & Technology) | 美国政府机构 | TREC会议30年；AI信任度评估 |
| Partnership on AI | 行业联盟 | AI事故数据库1000+案例 |
| GitHub | 代码托管平台 | 5600万+开发者——代码每行可追溯 |
| Bugzilla | 开源bug追踪 | 缺陷追踪与解决的工业标准 |

### L257 概念实体（≥3）
| 术语 | 定义 |
|------|------|
| audit trails / product logs | 审计轨迹/产品日志——系统活动的完整记录 |
| waterfall model vs. agile/scrum | 瀑布模型 vs. 敏捷方法——软件开发工作流的两大范式 |
| metamorphic testing | 蜕变测试——利用"反向路径应相同"等关系生成测试 |
| differential testing | 差分测试——新系统与旧系统的输出对比 |
| red team | 红队——外部攻击者模拟——军事隐喻 |
| ante-hoc (prospective) vs. post-hoc explanations | 事前解释 vs. 事后解释——可解释性的两种范式 |
| bug bounties / bias bounties | 漏洞赏金/偏差赏金——用于ML的众包安全测试 |
| underspecification | 指定不足——Google 33+7人论文的核心发现 |
| Datasheets for Datasets / Model Cards / FactSheets | 三大企业文档标准：Microsoft / Google / IBM |

---

## 九、与前后章关联

### L258 关联
- **Ch18（前）**：四层治理的第一层——"团队：可靠的系统基于可靠的SE实践"
- **Ch20（后）**：从团队层上升到组织层——安全管理文化
- **Ch8（远）**：审计轨迹=Ch8中过度自动化问题的"安全网"
- **Ch25（远）**：HCAI信任度量表（Table 25.3）中的12条推荐中有多条引用了本章实践
