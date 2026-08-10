# 09_第9章分析报告：Avoiding Missing and Undesirable Results

## L### 一、章节定位与功能

第9章处理搜索结果中的"零结果"和"不理想结果"的恢复策略——这是移动搜索中最常见但也最常被忽视的UX失败点。Nudelman开篇指出，"mistakes are not errors. They are a natural outcome of mobile computing"，将用户在小型触摸屏上产生的错误输入重新框架为"系统的预期行为"而非"用户的过错"。全章以3个反模式+3个模式的对称结构展开，核心理念是"recovery boils down to three essential elements: telling the searcher that the system did not understand him; focusing on providing a way out; leveraging sensor and history information"。该章是第7至8章的搜索/过滤架构讨论的收尾——回答了"当搜索失败时该怎么办"这一关键问题。

## L### 二、结构分析

- **9.1 Antipattern: Ignoring Visibility of System Status** — Yelp将"Coppertine"（误输）静默解析为"West Jordan"→用户完全不知系统未理解其意图。L### 违反Jakob Nielsen的第一可用性启发式原则。
- **9.2 Antipattern: Lack of Interface Efficiency** — Target弹出"Sorry, No Results Found"错误对话框→需额外点击确认→然后跳转到Shopping Basket标签→需再点击返回Products标签。L### "the extra tap acts as a sort of punishment added to an insult"。
- **9.3 Antipattern: Useless Controls** — TripAdvisor的零结果页面保留了Filter Search Results链接→过滤零结果等于零结果。"zero divided by a number always yields zero"。
- **9.4 Pattern: Did You Mean?** — Booking.com的"先假设你输入有误"策略——为每一次输入主动提供受控词汇替代建议（如城市名+国家作为元数据）。
- **9.5 Pattern: Partial Match** — Amazon移动网站的"Nike Ruskie Red"→删除问题关键词"Ruskie"→展示剩余查询的结果+删除线提示。L### 解决"anchoring（锚定）"——用户固执地保留一个错误关键词的心理偏见。
- **9.6 Pattern: Local Results** — Target的本地店铺查找器（GPS定位后即使关键词查询失败也展示附近店铺）+Booking.com的Around Me标签。L### Pet Shop集成案例展示三种恢复策略（Did You Mean?+Partial Match+Local Results）共同工作。

## L### 三、内容分析（核心论题+关键论点案例）

**核心论题1：移动端的错误输入不是异常而是常态。** L### "customers attempt to operate tiny mobile screens with a fat thumb, using only one hand, or while being jostled in the metro and eating a sandwich"——错误是移动多任务乱境中人类手指与微小屏幕交互的必然产物。

**核心论题2："blame the user"的错误对话框是反模式。** L### Target的"Sorry"弹窗→"the error dialog...signal to the customer that he did something wrong and committed a sin...maybe even one of the unforgivable ones." Nudelman以宗教术语重构技术问题——额外的点击是"hitting the customer's knuckles with a metaphorical ruler"（戒尺打手指）。

**核心论题3：Anchoring（锚定效应）是零结果的最大心理障碍。** L### 引用《Designing Search》中的"Harry Potter and The Sleepy Hollows"案例：被试坚信书名包含"Sleepy"，反复添加更多错误信息，最终结论是"这家店一定不卖哈利波特书。"Partial Match通过明确标识问题关键词和展示删除该词后的结果来打破锚定。

**核心论题4：Local Results（本地结果）是"纯移动优势"的典范。** L### 桌面搜索无法获得用户精确位置。GPS→可在关键词查询失败后自动提供本地相关结果→这是"mobile-first advantage"——不仅是移动适配，而且是移动超越。

**核心论题5：Humour（幽默）是零结果恢复的必需品。** L### Pet Shop零结果页面的"Bow-wow!"+多样化的随机俏皮话→参考Siri的幽默回答+《侏罗纪公园》的"Uh uh uh! You didn't say the magic word!"→应避免同一句重复（"gets obnoxious in a hurry"）。"Humor can be a wonderful tool to keep the search conversation going, despite momentary hiccups in human-mobile communication."

## L### 四、逻辑梳理（论证链条+因果转折）

**主论证链：** 移动输入必然产生错误→错误不应被视为"错误"→三反模式（静默误解/无效弹窗/无用控件）→三恢复模式（拼写纠正→Partial Match→Local Results）→三种策略可组合成一个强大的恢复页面→幽默作为"沟通润滑剂"。

**关键因果转折：**
- 系统检测到可能的错误输入 **但** 静默纠正→违反信任（9.1）
- 系统检测到零结果 **但** 弹出错误对话框→惩罚用户→破坏流程（9.2）
- 零结果页面保留了正常结果页面的过滤控件 **但** 过滤0结果=0结果→浪费用户时间（9.3）
- → 核心恢复策略: Did You Mean?（拼写层）→ Partial Match（减少约束层）→ Local Results（GPS增强层）→ 三重保险。

**历史缓存方案：** Did You Mean?的受控词汇可缓存在设备本地（10万+条目），使用正则表达式本地匹配→即使无网络也可进行拼写纠正。未缓存的查询发送到服务器进行分析和改进。

## L### 五、材料使用方式

1. **Yelp "Coppertine"截图（Figure 9.1）：** 9.1反模式的核心证据（静默误解用户意图）。
2. **Target错误弹窗截图（Figure 9.2）：** 9.2反模式的直观展示（额外点击+意外标签跳转）。
3. **TripAdvisor零结果页面截图（Figure 9.3）：** 9.3反模式（零结果页面保留过滤链接）。
4. **Booking.com的Did You Mean?截图（Figure 9.4）：** "先假设输入有误"的独特策略。
5. **Amazon移动网站的Partial Match截图（Figure 9.5）：** 删除线+对比颜色标识问题关键词。Amazon app（Figure 9.6）的缺失对比——同一公司的移动网站比app做得更好。
6. **Target门店查找器截图（Figure 9.7）：** GPS定位+关键词搜索→失败后回退到本地门店展示。
7. **Pet Shop组合线框图（Figure 9.9）：** 三重恢复策略（DM?+PM+LR）的教科书级集成展示。

## L### 六、论辩与阐述方法

1. **"natural outcome"框架重塑：** Nudelman以"errors are not errors"重新定义移动输入错误——从"用户犯错"的惩罚导向转换为"系统预期"的包容导向。
2. **代数类比：** "zero divided by a number always yields zero"——以数学定律证明Useless Controls反模式的不合理性。
3. **认知心理学引用：** Anchoring（锚定效应）+ Churning（无效循环）——将UI问题定位于已知的心理学现象中。
4. **自我研究的引用：** 《Designing Search》中的"Harry Potter and The Sleepy Hollows"是Nudelman自己的用户研究案例——以一手数据增强论证的说服力。
5. **幽默的实用化建议：** 将幽默从"nice to have"提升为"恢复策略的核心组成部分"——以Siri、《侏罗纪公园》、Pet Shop的"Bow-wow!"为证据链。

## L### 七、语言文风（原文摘录+L###）

**原文摘录1**（错误常态化）：
> "You must realize that those mistakes are not errors. They are a natural outcome of mobile computing, which takes place in a fast-paced, multitasking world."

L### 分析：以"must realize"传达道德责任——设计师有义务重新理解"错误"的本质，而不是将技术限制的责任转嫁给用户。

**原文摘录2**（Anchoring案例）：
> "The person in question anchored on the erroneous word 'Sleepy' and no amount of failure would get her unstuck. She was so anchored on that term that at the end of the test, she erroneously concluded, 'The store must not carry any Harry Potter books.'"

L### 分析：以第一人称叙事再现用户测试场景——展示锚定效应的戏剧性后果（将整个库存否定归因于一个错误关键词）。

**原文摘录3**（Humour建议）：
> "Recall the timeless scene from the first Jurassic Park in which the security system keeps saying 'Uh uh uh! You didn't say the magic word!' over and over."

L### 分析：以《侏罗纪公园》中计算机系统的固执重复作为反面教材——幽默需多样化，重复则成为折磨。

## L### 八、实体清单（六类，每类≥3项+L###）

### 8.1 核心人物实体

1. **Peter Morville & Jeff Callender** — "churning"概念来源（《Search Patterns》）。L### 无效重复查询的行为模式命名。
2. **Alan Cooper** — "dialog boxes stop the proceedings with idiocy"。L### 作为对错误对话框的理论批评来源。
3. **Luke Wroblewski** — 表单设计权威。L### 间接影响零结果页面的"简洁"理念。

### 8.2 核心概念/术语实体

1. **Anchoring（锚定效应）** — 认知偏见：过度依赖第一个信息片段（错误关键词）。L### 导致用户"churning"——反复无效查询。
2. **Churning（无效循环）** — 反复运行相似查询但得到相同零/不理想结果。L### Peter Morville术语。
3. **Controlled Vocabulary Substitution（受控词汇替代）** — Did You Mean?的技术基础。L### 源自预定义的"允许关键词"数据库。
4. **Partial Match（部分匹配）** — 删除问题关键词后重新运行查询。L### 以删除线和对比色展示哪些关键词被移除。

### 8.3 核心应用/产品实体

1. **Yelp** — 9.1 Ignoring System Status反模式案例。
2. **Target** — 9.2 Lack of Interface Efficiency反模式+9.6 Local Results正面案例。
3. **TripAdvisor** — 9.3 Useless Controls反模式案例。
4. **Booking.com** — Did You Mean?的独特正面案例（主动拼写预筛选）。
5. **Amazon移动网站** — Partial Match的黄金标准实现。
6. **Amazon App** — Partial Match缺失的对比案例（"同一公司、移动网站优于app"的讽刺）。

### 8.5 核心模式/反模式实体

1. **9.1 Antipattern: Ignoring Visibility of System Status**
2. **9.2 Antipattern: Lack of Interface Efficiency**
3. **9.3 Antipattern: Useless Controls**
4. **9.4 Pattern: Did You Mean?**
5. **9.5 Pattern: Partial Match**
6. **9.6 Pattern: Local Results**

## L### 九、与前后章关联

**与第7章的关系：** Auto-Complete/Auto-Suggest的"主动预防零结果"→第9章的"事后恢复零结果"——两者共同构成"零结果管理的全生命周期"（预防→检测→恢复）。Tap-Ahead（7.3）使用本地受控词汇数据库→与Did You Mean?（9.4）的本地缓存策略复用同一数据源。

**与第8章的关系：** Parallel Architecture的"基本搜索"默认使用本地结果（8.4）→9.6 Local Results作为零结果恢复的GPS增强策略。Facet过滤（8.2）缺少项目计数（item counts）→更容易导致零结果→加强第9章恢复模式的重要性。

**与第10至11章的关系：** 第9章的零结果恢复策略→第10章数据输入中的Slider with Histogram和Slider Based on Inventory Counts——通过可视化和库存数据防止用户选择导致零结果的参数范围。
