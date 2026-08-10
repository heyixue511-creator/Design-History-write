# Ch13 分析报告：《Using Contextual Inquiry to Discover Physicians' True Needs》

## 一、章节定位与功能（行号范围 L3671-L3889）

本章是第五主题簇"EXAMPLES OF CONTEXTUAL INQUIRY AND CONTEXTUAL DESIGN"（L542-L544）第三篇，作者为 Janette M. Coble、Judy S. Maffitt、Matthew J. Orland、Michael G. Kahn（Section of Medical Informatics, Washington University School of Medicine；BJC Health System，L3675-L3677）。功能：展示把 **Contextual Inquiry** 用于医生临床工作站需求生成的全过程——规划、执行、分析、合并、需求生成与优先级评定（L3681），是"CI 产出传统需求文档"的最完整案例。

## 二、结构分析

- Executive Summary（L3679-L3681）
- Background of the Study（L3683-L3689）：Project Spectrum、UI 团队
- Planning the Study（L3691-L3697）：为何选 CI、改进
- Conducting the Study（L3699-L3737）：用户、过程概览、CI 会话
- Analyzing and Interpreting the Data（L3741-L3770）：模型与合并
- Physician Requirements Generation Meeting（L3775-L3777）
- The Requirements Generation and Prioritization Process（L3779-L3837）：542 条需求与评级
- Impacting the Design（L3839-L3848）
- Assessing the Cost/Benefit（L3850-L3856）
- Reflections（L3858-L3870）
- Acknowledgments（L3872-L3874）
- References（L3876-L3888）

## 三、内容分析

**背景**：Project Spectrum 是华盛顿大学医学院、BJC Health System、IBM、Kodak、SBC Corp. 组成的联合技术联盟（L3685）。目标是为 BJC 的 15 家医院及附属门诊提供全面的纵向临床信息（L3685）。UI 团队任务：为第一阶段（医生从办公室/家/医院查看检测结果）定义需求；目标用户为全科/普外临床医生（L3685）。因以往给医生引入信息系统的经验，各级经理强调工作站必须真正满足医生需求且高度可用（L3687）。

**为何选 CI**：团队一名成员参加 CHI '94 后确定 CI 为最佳路径（L3687）。反对"召集医生开会生成需求"的离情境方法——"人们不在自己的环境里执行任务时，往往无法说出自己的需求"（L3693）。文中的红墨水例子证明：医生在情境中才显示出"红字=上次是住院"这一隐性线索（L3695）。

**用户**：十名全科/普外医生，代表六家医院与医学院；刻意含"会用电脑/有电脑不用/没有电脑"三种（L3705-L3707）；全为男性（当时控制医院差异优先，L3709）。

**过程**：先在办公室后住院部做 CI 会话；中途与结束各做一次跨医生合并；从最终合并信息生成需求，再让医生独立评级（L3715）。前半段焦点宽（处理任何类型信息），后半段收窄到检测结果处理（L3717）。

**CI 会话三阶段**（L3721-L3727）：orientation（10-15 分钟，重述目的、参观、签同意书）、interview（1-6 小时，医生照常工作并描述、被追问）、wrap-up（约 5 分钟）。医生选不太忙但仍正常的日子；急诊时只观察并事后走查（L3731）。音频录制+笔记+收集制品（消毒后，L3733）。每会话后发感谢信与摘要（L3735）。后半程请其他项目团队观察员参与，但观察员插话干扰了"用户-访谈者"关系（L3737）。

**分析**：每会话产出序列模型、流模型、情境模型、详细观察、用户画像、问题清单（L3743）；观察是需求主源（L3754）。中途与结尾两次合并（流模型+情境模型合并；序列模型因时间限制未合并——后来后悔，L3768）。亲和图在"走墙"中组织观察（L3770）。

**需求生成**：从亲和图观察逐条生成需求；医生单独生成、三人再合议；每条需求标注观察标识（L3781）。产出 **542 条需求**，加 1-10 评级量表（"必需 8-10/可选 4-7/不必要 1-3"）让医生独立评级（L3785-L3817）；411 条均值 ≥8，仅两条满分（L3817）。需求文档含执行摘要（2 页）、引言（6 页）、需求（95 页）、CI 过程说明、合并情境模型、合并流模型、制品清单（L3821-L3836）；缺"中层"内容（L3837）。

**设计影响**：观察与需求被项目内外团队使用（L3841）；用两个真实场景做全员演示（幻灯片+真实制品，覆盖约一半需求）（L3846）；正在以需求+评级做第一阶段范围化（L3848）。

**成本**：约 300 小时执行 CI（80 医生小时+130 员工小时+90 事后文档），另 1300 员工小时分析（L3852）。CI 不提供时序基准——后续将再访医生做无干预计时观察以建立可用性指标（L3856）。

**反思**：四大关键发现中两项"让团队惊讶，若无情境研究不可能发现"（L3860）；CI 建立与医生的关系（L3862）；两人训练不足导致流程拉长（L3864）；希望 CI 团队扩大为跨学科受过训的团队、让模型（尤其亲和图）更可见（L3866）；需求文档制作耗时被低估（L3868）；医生的自发好评："印象深刻的全面性"（L3870）。

## 四、逻辑梳理

**需求生成任务（Project Spectrum 第一阶段）→ 反对离情境方法 → 选 CI → 十名医生、办公室+住院部双情境会话 → 每会话模型化+中途/结束合并+亲和图 → 542 条需求生成 → 医生评级优先化 → 需求文档+场景 → 设计影响（范围化）→ 反思（模型可见性、团队扩大、时序基准缺失）**。

## 五、材料使用方式

- **一手材料**：音频录音、笔记、消毒后制品、观察、用户画像、序列/流/情境模型、亲和图、评级问卷。
- **数字证据**：十医生、542 需求、411 条 ≥8、300/1300 小时（L3705、L3785、L3817、L3852）。
- **参考文献**：CI 原理（Wixon/Holtzblatt/Knox 1990；Wixon & Raven 1994；Holtzblatt & Jones 1990）、Project Spectrum（Coble et al. 1995；Fritz & Kahn 1995）。

## 六、论辩与阐述方法

- **情境有效性论证**：以"离情境会议不可靠"立论，以红墨水例子为关键实证（L3693-L3695）。
- **流程透明化**：把 542 条需求生成、评级量表（图 13.5）、文档结构逐项呈现。
- **自我评估**：坦承序列模型未合并的失误（L3768）、需求文档中层缺失（L3837）、时间低估（L3868）。

## 七、语言文风摘录（附行号）

- "People generally can't verbalize their needs when they are not actually performing tasks in their own environment."（L3693）
- "He was surprised that he had not mentioned that need before. It was so ingrained in how he worked that he did not even process that highly relevant detail consciously anymore."（L3695）
- "Of the 542 requirements, 411 had a mean physician rating greater than or equal to 8."（L3817）

## 八、实体清单（六类，附行号证据）

### 人物（Person）
| 编号 | 名称 | 身份 | 行号 |
|---|---|---|---|
| P01 | Janette M. Coble | 医信息学研究助理 | L3675、L398 |
| P02 | Judy S. Maffitt | BJC 资深系统分析师 | L3675、L400 |
| P03 | Matthew J. Orland | 临床医学副教授 | L3675、L402 |
| P04 | Michael G. Kahn | 医信息学部门主任 | L3675、L404 |
| P05 | 十名参与医生 | 用户/需求评级者 | L3705、L3874 |

### 著作/作品（Artifact）
| 编号 | 名称 | 说明 | 行号 |
|---|---|---|---|
| A01 | 需求文档（约 113 页） | 需求生成交付物 | L3821-L3836 |
| A02 | 亲和图（观察） | 观察组织 | L3770 |
| A03 | 序列/流/情境模型 | 会话分析产出 | L3743-L3752 |
| A04 | 评级量表问卷 | 图 13.5 | L3785-L3801 |

### 概念（Concept）
| 编号 | 名称 | 含义 | 行号 |
|---|---|---|---|
| C01 | Contextual Inquiry | 情境查询 | L3687 |
| C02 | Requirements document | 需求文档 | L3819 |
| C03 | Context-of-use scenario | 使用情境场景 | L3819 |
| C04 | Requirements prioritization | 需求优先化（医生评级） | L3785 |
| C05 | Sequence/flow/context model | 序列/流/情境模型 | L3745-L3752 |

### 机构（Institution）
| 编号 | 名称 | 行号 |
|---|---|---|
| I01 | Washington University School of Medicine | L3677 |
| I02 | BJC Health System | L3677 |
| I03 | Project Spectrum（IBM、Kodak、SBC Corp. 等） | L3685 |

### 地点（Place）
| 编号 | 名称 | 行号 |
|---|---|---|
| L01 | 六家医院（办公室+住院部） | L3705、L3713 |

### 事件（Event）
| 编号 | 名称 | 行号 |
|---|---|---|
| E01 | 1994 年 8 月起 CI 会话 | L3852 |
| E02 | 中途/结束两次合并 | L3715 |
| E03 | 医生需求评级 | L3785 |

## 九、与前后章关联

本章与 Ch9（医疗设备）共享"医疗场景+隐性需求"主题，是"CI 生成传统需求文档"的正面示范，直接印证 Ch3 的"隐性知识"论点（L558、L3687）。与 Ch11/Ch12 同属情境设计/CI 案例簇。其"需求评级+场景"做法与 Ch17 的"从数据到需求文档"的组织适应讨论（L5084）呼应；"让模型更可见"的反思也与 Ch17 的"设计室"理念一致。
