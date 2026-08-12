# Ch04 分析报告：Animal, Vegetable, or Mineral?（动物、植物还是矿物？）

## 章节定位与功能（行号范围）

第四章（L1103-1192），副题"WHY USERS LIKE MINDLESS CHOICES（为什么用户喜欢无脑选择）"（L1105）。属第一部"指导原则"。功能：提出并论证 Krug 第二定律——"点击多少次无所谓，只要每次点击都是无脑、明确无误的选择"（L1107-1109），把"别让我思考"落到"点击决策"这个最小单元。

## 结构分析

- 引子：第二定律宣言（L1107-1109）
- 批判"点击次数"指标（L1111-1113）
- 引入"信息气味"与"三次无脑点击=一次需要思考的点击"经验法则（L1115-1121）
- 正例：二十问游戏"动物、植物还是矿物"（L1123-1125）
- 反例：办公产品厂商首页"Home Office"式分类（L1129-1133）；"已盖章/已机打邮件"信箱困惑（L1135）；杂志会员三栏登录页（L1141-1149）
- 正例：《纽约时报》逐步登录流程（L1151-1155）
- 表单里的难问题：引 Jarrett《Forms that Work》（L1157-1165）
- 复杂选择的兜底：即时指引"Brief/Timely/Unavoidable"（L1167-1191），以伦敦街头"LOOK RIGHT"地面提示为例
- 小结（L1191）

## 内容分析

作者把"点击次数"指标解构为"每次点击的思考成本"：用户在意的不是点击数量，而是点击时"是否确信自己在正确轨道上"（L1113-1115）。"信息气味（scent of information）"源自 Xerox PARC 的 Peter Pirolli & Stuart Card"信息觅食"研究（L1117），链接命名越清楚，气味越强。

"动物、植物还是矿物？"是"无脑选择"的完美示范：前提一接受（非植物非动物皆矿物），回答几乎零思考（L1123）。反面：厂商网站让用户在"Home Office/Home/Home Entertainment"里猜自己属于哪类（L1129-1133）；杂志站让读者分辨"已是订户但不是在线会员/已是在线会员/都不是"三栏流程（L1147），把"如何回答问题"逼成"我到底多想要这篇文章"（L1149）。

《纽约时报》的解法是"分层呈现"：先选大方向（登录/订阅），再进入只含相关问题的页面（L1151-1155）。这对应原则：把难以一次性回答的问题拆成无脑步骤。

当难选择无法避免时，需要"即时指引"，三要件：**简短**（Brief，最小必要信息）、**及时**（Timely，恰在需要时出现）、**不可回避**（Unavoidable，格式保证会被注意到）（L1173-1179）。伦敦街头"LOOK RIGHT"地面标语是典范（L1183-1189）——它是简短、及时、不可回避的救命提示。

## 逻辑梳理

"点击次数论"是伪指标 → 真实指标是点击的思考负担 → 清晰命名的链接提供强"信息气味" → 把难选择拆成无脑小步 → 实在拆不开则给"简短/及时/不可回避"的即时指引。全章把第 1 章"别让我思考"转化为点击路径层面的可操作准则，并预示第 5 章"命名与文字"的主题。

## 材料使用方式

- 研究文献：Pirolli & Card 信息觅食研究（脚注，L1117）
- 游戏类比：Twenty Questions（L1123）；www.20q.net 神经网络版（脚注，L1125）
- 真实站点：厂商"Home Office"页（L1129-1133）；杂志会员登录页与《纽约时报》登录流（L1141-1155）
- 著作引用：Jarrett & Gaffney《Forms that Work》（L1157-1161）
- 城市空间案例：伦敦地面"LOOK RIGHT"提示（L1183-1189）
- 日常困惑类比：Stamped Mail/Metered Mail 两个邮箱（L1135）

## 论辩与阐述方法

以"定律→反指标→正反例对仗→兜底方案"展开。最有力的论证手段是"同一任务的两种站"对照（难选 vs 无脑），以及把抽象"思考负担"具象为邮箱、杂志栏位、伦敦路面等生活场景。作者还主动给反例与例外（重复深钻同一路径、页面加载慢时点击次数更有价值，L1121），保持"看情况"的常识立场。

## 语言文风摘录（附行号）

- "It doesn't matter how many times I have to click, as long as each click is a mindless, unambiguous choice."（L1107-1109，第二定律）
- "three mindless, unambiguous clicks equal one click that requires thought."（三次无脑点击等于一次需要思考的点击。L1119）
- "What do they think it is—stamped or metered?"（他们觉得这是盖章的还是机打的？L1135）
- "Just how interested am I in this article?"（我到底多想要这篇文章？L1149）

## 实体清单（六类，附行号证据）

**人物**：Peter Pirolli、Stuart Card（L1117）；Caroline Jarrett、Gerry Gaffney（L1157-1161）；Robin Burgener（20q.net 作者，L1125）
**著作/作品**：《Forms that Work: Designing Web Forms for Usability》（L1157-1159）；Twenty Questions 游戏（L1123）；www.20q.net（L1125）
**概念**：mindless choice（L1107-1109）；scent of information（L1115）；information foraging / informavores（L1117）；Brief/Timely/Unavoidable 即时指引（L1173-1179）
**机构**：Xerox PARC（L1117）；The New York Times（L1151）；www.20q.net（L1125）
**地点**：London（伦敦，L1183）
**事件**：无

## 与前后章关联

承接第 2 章"满足性选择"（用户会点第一个合理选项，故选项必须无脑、无歧义）与第 3 章"可点击性"。第 5 章"删字"进一步处理命名与文字——链接命名直接决定"信息气味"强弱；第 9 章测试方法论中"表单难回答问题"（Jarrett 章节）也在本章被预告。
