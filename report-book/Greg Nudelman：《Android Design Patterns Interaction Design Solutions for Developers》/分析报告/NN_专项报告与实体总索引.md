# NN_专项报告与实体总索引：《Android Design Patterns》知识图谱

## L### 一、全书模式总索引（58项模式 + 12项反模式 + 10项实验模式）

### 1.1 反模式（Antipatterns）12项

| 编号 | 反模式名称 | 所在章节 | 核心问题 |
|------|-----------|---------|---------|
| A01 | EULAs（最终用户许可协议） | 5.1 | 在用户获得价值前强制法律协议 |
| A02 | Contact Us Impediments（联系我们障碍） | 5.2 | 不可点击的电话号码和冗长无预设的联系表单 |
| A03 | Sign Up/Sign In（注册/登录） | 5.3 | 在用户使用应用前强制注册 |
| A04 | Crippled Refinement（残缺过滤） | 8.1 | 移动端以"简化"为名删除桌面端过滤维度 |
| A05 | Ignoring Visibility of System Status | 9.1 | 静默"纠正"用户输入而不告知用户 |
| A06 | Lack of Interface Efficiency | 9.2 | 零结果以错误弹窗出现，需要额外点击确认 |
| A07 | Useless Controls（无用控件） | 9.3 | 零结果页面保留正常结果页面的过滤控件 |
| A08 | Separate Search and Refinement（分离搜索与过滤） | 7.9 | 关键词搜索与过滤选项处于不同页面 |
| A09 | Pogosticking（跳跳球导航） | 13.1 | 列表页信息不足导致反复跳转列表↔详情 |
| A10 | Multiple Featured Areas（多特性区域） | 13.2 | 多个不同品牌的促销区域导致用户困惑 |
| A11 | Disabling Keyboard Keys（禁用键盘键） | 10.8 | 动态禁用键盘键造成混淆 |
| A12 | Separate Homepage Search（分离主页搜索） | 7.9 | 主页搜索与专用搜索页提供不同功能 |

### 1.2 设计模式（Patterns）58项

**第5章：Welcome Experience（2项）**
| 编号 | 模式名称 | 核心价值 |
|------|---------|---------|
| P01 | Welcome Animation | 建立品牌氛围，缓冲应用加载时间 |
| P02 | Tutorial | 非强制集成式教学，使用Watermark叠加层 |

**第6章：Home Screen（6项）**
| P03 | List of Links | 静态功能目录，最直观的默认主屏幕 |
| P04 | Dashboard | 聚合数字和趋势的图形化仪表盘 |
| P05 | Updates | 按时间排序的个人相关更新流 |
| P06 | Browse | 可立即操作的商品/内容浏览 |
| P07 | Map | GPS驱动的本地信息地图展示 |
| P08 | History | 自动记录的最近搜索/浏览历史 |

**第7章：Search（8项）**
| P09 | Voice Search | 语音替代键盘输入 |
| P10 | Auto-Complete and Auto-Suggest | 输入建议（完成原片段+自由联想） |
| P11 | Tap-Ahead | Nudelman原创：逐词渐进式查询构建 |
| P12 | Pull to Refresh | 下拉手势刷新内容列表（Twitter专利） |
| P13 | Search from Menu | 从导航栏菜单进入搜索（已基本弃用） |
| P14 | Search from Action Bar | 从操作栏图标进入搜索 |
| P15 | Dedicated Search | 固定不随内容滚动的搜索框 |
| P16 | Search in the Content Page | 随内容滚动的搜索框，节省屏幕空间 |

**第8章：Sorting and Filtering（4项）**
| P17 | Refinement Page | 专用全屏过滤和排序页面或光箱 |
| P18 | Filter Strip | 半透明条显示已应用的全部过滤条件 |
| P19 | Parallel Architecture | 简单浏览+高级搜索双轨制 |
| P20 | Tabs | 标签切换视图/排序/分类 |

**第9章：Avoiding Missing and Undesirable Results（3项）**
| P21 | Did You Mean? | 受控词汇替代表——"你是不是想找...？" |
| P22 | Partial Match | 删除问题关键词后展示部分匹配结果 |
| P23 | Local Results | GPS驱动的本地结果作为零结果恢复 |

**第10章：Data Entry（9项）**
| P24 | Slider | 单/双滑块（连续或离散位置） |
| P25 | Stepper | +/-按钮输入小整数（0-5），可增强为直接编辑 |
| P26 | Scrolling Calendar | 连续滚动七日列日历（Kayak创新） |
| P27 | Date and Time Wheel | 垂直滚轮日期时间选择器（+Wheelie模式） |
| P28 | Drop Down / Spinner / Select | 从预定义列表中选一项 |
| P29 | Multiple Select | 从列表中选多项（下拉复选框+画廊长按） |
| P30 | Free-Form Text Input and Extract | 标准文本输入+横屏提取模式 |
| P31 | Textbox with Input Mask | 隐式/显式输入格式掩码+键盘类型自适应 |
| P32 | Textbox with Atomic Entities | 搜索式输入离散系统对象（联系人/机场） |

**第11章：Forms（8项）**
| P33 | Inline Error Message | 字段级错误指示+顶部错误摘要 |
| P34 | Toast Alert | 短暂自动消失的确认/状态消息 |
| P35 | Pop-up Alert | 需用户操作才能关闭的模态警告 |
| P36 | Callback Validation | 异步服务器验证（输入延迟触发） |
| P37 | Cancel/OK | 标准表单操作按钮布局约定 |
| P38 | Top-Aligned Labels | 标签在字段上方的表单布局 |
| P39 | Getting Input from the Environment | 传感器（GPS/语音/摄像头/手势）替代键盘输入 |
| P40 | Input Accelerators | 缓存并智能提示以前的输入值 |

**第12章：Mobile Banking（7项）**
| P41 | Login Accelerator | 短码/面部/语音/指纹替代完整密码登录 |
| P42 | Dedicated Selection Page | 全屏页面选择（替代下拉控件） |
| P43 | Form First | 先展示表单→后进入专用选择页 |
| P44 | Dedicated Pages Wizard Flow | 每字段独占一页的移动优化最短路径 |
| P45 | Wizard Flow with Form | 专用选择页在前（向导）→表单在后（含可选字段） |
| P46 | Verification-Confirmation | 提交前最后确认+交易完成后的操作引导 |
| P47 | Near Field Communication (NFC) | 近距离无线通信（支付/签到/数据交换） |

**第13章：Navigation（5项）**
| P48 | Carousel | 可横向滑动的视觉产品浏览行 |
| P49 | Popover Menu | 弹出式扩展操作菜单（替代桌面右键） |
| P50 | Watermark | 半透明手势/动作提示（"温和邀请"） |
| P51 | Swiss-Army-Knife Navigation | 隐藏式多功能导航（单一按钮/角菜单） |
| P52 | Integration: The Final Frontier | 跨应用流程集成+数据聚合仪表盘 |

**第14章：Tablet Patterns（6项）**
| P53 | Fragments | Android响应式碎片布局框架 |
| P54 | Compound View | 双窗格（列表+详情）平板布局 |
| P55 | Side Navigation（实验） | 左侧垂直图标菜单（可折叠为仅图标） |
| P56 | Content as Navigation/Multitouch Gestures | 内容元素本身即导航（多点触控直接操纵） |
| P57 | 2-D More Like This | 二维可滚动分类缩略图矩阵 |
| P58 | C-Swipe（实验） | 拇指"C"形半圆手势触发上下文菜单 |

### 1.3 实验性模式（Experimental Patterns）索引

| 编号 | 实验模式名称 | 所在章节 | 核心创新 |
|------|------------|---------|---------|
| E01 | Slider with Histogram | 10.1 | 价格滑块上方叠加库存数量直方图 |
| E02 | Slider Based on Inventory Counts | 10.1 | 滑块间隔按库存量等分而非绝对价格 |
| E03 | Dual Combo Wheels | 10.4 | 双组滚轮同时设置"从"/"到"日期时间 |
| E04 | Static Inline Input Mask | 10.8 | 静态行内格式掩码（如111-111-1111） |
| E05 | Fluid Labels（平板） | 11.6 | 标签跟随设备方向动态切换（顶对齐↔左对齐） |
| E06 | Voice Recognition Password | 12.1 | 声音印记+挑战问题作为登录凭证 |
| E07 | Side Navigation（平板） | 14.3 | Twitter iPad风格垂直图标菜单 |
| E08 | Four-Corners Swiss-Army-Knife | 13.6 | 四角半透明快捷导航（替代单一菜单按钮） |
| E09 | C-Swipe | 14.6 | 拇指"C"形手势触发半圆形上下文菜单 |
| E10 | Unified Inbox / Contact Panorama | 13.7 | 跨应用通讯聚合+个人联系人多维度仪表盘 |

## L### 二、全书核心概念体系索引

### 2.1 Android 4.0设计原则（第2章）

| 原则 | 英文原名 | 对立面（iOS） | 在Part II中的主要体现 |
|------|---------|-------------|---------------------|
| 扁平化 | Flatland | 拟物化（渐变/圆角/容器） | 第10章扁平控件、第11章无容器表单 |
| 随处可点 | Tap Anywhere | 显式可点标识（>按钮） | 贯穿Part II所有交互设计 |
| 适配所有设备 | Right-Size for Every Device | 固定布局 | 第14章Fragments/Compound View |
| 无界移动空间 | Mobile Space, Unbound | 圆角容器 | 第11章Top-Aligned Labels |
| 全局思维本地行动 | Think Globally, Act Locally | 始终可见的全局导航 | 第13章Swiss-Army-Knife Navigation |

### 2.2 贯穿性隐喻

| 隐喻 | 来源 | 核心含义 | 涉及章节 |
|------|------|---------|---------|
| Iron Man战衣 | Introduction | 移动应用应像钢铁侠装甲——不可见但无处不在的赋能 | 全书 |
| 蘑菇走进酒吧 | 第6章 | "telling about the story" vs "telling the story" | 第6-9章 |
| 瑞士军刀 | Marissa Mayer | 复杂功能的简洁包装——关闭时简单优雅 | 第13章 |
| Robinson Crusoe | 第10章 | 完全自由=完全责任——太多控件选择反而低效 | 第10章 |
| Inukshuk（因纽特石标） | Jared Spool | "有人来过、这可行、你不会出丑"的心理安抚内容 | 第12章 |
| Mobile Organ（移动器官） | 第4章 | 移动设备已超越工具，成为人类新"器官" | 第4章 |

### 2.3 设备人体工程学分类（第3章）

| 设备类别 | 典型代表 | 主要握持方式 | 关键设计约束 |
|---------|---------|------------|------------|
| 紧凑手机 | Kyocera Milano | 单手全屏可及 | 仅一个操作栏，split action bar不可行 |
| 全尺寸手机 | Galaxy SIII | 单手，顶部操作栏难以触及 | 手势替代顶部导航 |
| 平板手机混合体 | Galaxy Note | 不对称单手（一手握，另一手操作） | 手势可使单手操作成为可能 |
| 小平板（7英寸） | Galaxy Tab 2 7" | 竖屏单手/横屏双手 | 竖屏←→横屏表单切换尴尬 |
| 大平板（10英寸） | Galaxy Tab 2 10" | 必须双手或放在支撑面上 | "large tablet elbow"，垂直侧边导航 |

## L### 三、全书引用网络分析

### 3.1 引用频率最高的外部权威

1. **Luke Wroblewski** — 至少15次引用。L### "Forms suck"（第11章）、标签策略研究（第11章）、"Mobile First"概念（第12章）、输入掩码反模式分析（第10章）。
2. **Alan Cooper** — 至少8次引用。L### "stopping the proceedings with idiocy"（第9、11章）、"dialog boxes"批判、"pagination=as old as Gregorian calendar"（第10章）。
3. **Peter Morville** — 至少7次引用。L### "What we find changes what we seek"（第7、8章）、联邦搜索（第13章）、"design dissolves in behavior"（第12章）。
4. **Jared Spool** — 至少5次引用。L### "pogosticking"术语（第1、6、13章）、"Inukshuk"概念（第12章）。
5. **Edward Tufte** — 至少3次引用。L### "simplicity vs simple-mindedness"（第4、8章）。
6. **Steve Krug** — 至少3次引用。L### "Don't make me think!"（第11、12章）。
7. **Josh Clark** — 至少3次引用。L### "tap-worthy areas"（第2章）、"iPad elbow"/"tablet elbow"（第3章）、"buttons are a hack"（第14章）。
8. **Theresa Neil** — Foreword作者。L### "universal patterns vs platform-specific deep dives"框架。
9. **Christopher Alexander** — 模式语言哲学源头。L### "the quality without a name"（Introduction）。
10. **Scott McCloud** — 故事板技巧参考。L### 《Making Comics》（第4章）。

### 3.2 引用频率最高的应用案例

| 应用 | 至少引用次数 | 主要角色 |
|------|-----------|---------|
| Yelp | 20+ | 正面案例为主（Dedicated Search、Filter Strip、Parallel Architecture）+负面案例（Pop-up Alert Legion、Ignoring System Status） |
| Amazon | 15+ | Crippled Refinement（负面）+Partial Match移动网站（正面）+Carousel（正面）+Browse（混合） |
| Kayak | 12+ | Scrolling Calendar（正面）+分离Sort/Filter按钮（负面）+Bing地图集成失败（负面） |
| Facebook | 10+ | Swiss-Army-Knife Navigation标杆（正面）+Updates（正面） |
| Google Calendar/Contacts/Maps | 20+ | Android参考实现（正负混合） |
| TripAdvisor | 8+ | Parallel Architecture混乱（最详尽负面案例）+Pogosticking+Useless Controls |
| eBay | 8+ | Refinement Page黄金标准（正面）+Inline Error Message（正面） |
| Chase / USAA | 10+ | Login Accelerator + Bill Pay流程 + 各种银行模式 |

### 3.3 自引网络（Nudelman前作及个人发表）

| 作品 | 至少引用次数 | 被引用章节 |
|------|-----------|----------|
| 《Designing Search》（2011） | 8+ | 第7、8、9、12、13章 |
| "Mobile Auto-Suggest on Steroids: Tap-Ahead Design Pattern"（Smashing Magazine, 2011.4） | 2 | 第7章 |
| "Storyboarding iPad Transitions"（Boxes and Arrows, 2011.1） | 1 | 第4章 |
| DesignCaffeine咨询案例 | 多次 | 全书（eBay移动应用早期经历、25人可用性测试数据等） |

## L### 四、跨章节主题索引

### 4.1 "沉浸式体验"（Immersive Experience）主题

从第2章（Flatland+半透明菜单）→第8章（半透明Filter Strip）→第13章（Swiss-Army-Knife Navigation+Lights Out模式）→第14章（Content as Navigation+C-Swipe）。核心演进路线：去除非必需视觉元素→导航后退→内容上前→传感器驱动的直接交互。

### 4.2 "零结果管理"全生命周期

第7章（Auto-Suggest预防零结果）→第8章（过滤选项缺少项目计数导致零结果）→第9章（三恢复策略：Did You Mean?→Partial Match→Local Results）→第10章（Slider with Histogram通过库存可视化防止零结果区间选择）。全生命周期覆盖：预防→检测→恢复→根因消除。

### 4.3 "安全vs便捷"的张力

第11章（双因素认证+Voice Recognition）→第12章（Login Accelerator + NFC安全/隐私+Evildoer设计）。核心洞察：高安全性不必然等于繁琐——"The future is already here—it's just not evenly distributed"。

### 4.4 "按钮怀疑论"（Button Skepticism）

从第2章（Tap Anywhere→按钮不需要显式标识）→第10至11章（Stepper+Slider替代文本输入）→第13章（手势替代按钮导航）→第14章（"buttons are a hack"→Content as Navigation+C-Swipe）。最终指向：终极界面是无按钮界面——内容即交互。

### 4.5 "移动优先"（Mobile First）演进

从第3章（碎片化=device-native设计）→第4章（RITE便签纸原型法）→第7章（移动专属Auto-Suggest数据库）→第8章（GPS距离过滤不可在桌面复制）→第12章（Dedicated Pages Wizard Flow为"Mobile First"模式）→第13章（瑞士军刀导航=为小屏幕原生的导航方案）。移动不是桌面的缩小版——移动是桌面的进化版。

## L### 五、未完成/开放性议题

1. **代码实现：** "There is no code in this book"（Introduction）——网站 androiddesignbook.com 提供配套代码示例和迷你应用。
2. **Fragments框架深度：** 第14章仅提供概述，完整Fragments开发指南指向官方文档 developer.android.com/training/basics/fragments/index.html。
3. **平板全景：** "tablets are a huge area of mobile technology—these devices deserve their own separate book"（第14章）——平板话题远未穷尽。
4. **游戏设计模式：** 多次引用游戏（Angry Birds、Major Mayhem、Infinity Blade、N.O.V.A.）但未系统化游戏特有的设计模式——仅从中提取适用于"严肃"应用的部分。
5. **跨应用集成：** Integration（13.7）是"最后疆界"——本章仅提出问题（统一收件箱、个人仪表盘）但未提供成熟的实现方案——这是全书最大的未完成议程。
6. **专利悬而未决：** Pull to Refresh（Twitter专利）、Scroll to Search（可能Apple专利）、Tap-Ahead（归属未定）——这些专利可能在未来影响相关模式的法律可行性。
7. **C-Swipe验证：** "Much testing with a broad range of people is needed to confirm this"（14.6）——全书最具雄心的实验模式尚未经过大规模用户验证。

## L### 六、全书论证方法分类

| 论证方法 | 典型示例 | 价值 |
|---------|---------|------|
| Before/After对比 | AutoTrader三版本迭代（第1章）、Amazon移动端vs桌面端（第8章） | 最直观的设计决策可视化 |
| 跨平台对比 | Android vs iOS vs Windows Modern UI（贯穿Part I） | 建立Android设计DNA的独特性 |
| 反模式→模式结构 | 每章先暴露错误再提供正确方案 | 建立明确的价值判断框架 |
| 实证引用 | 25人可用性测试（"30%用户将验证页误认为确认页"）、eBay的"several billion dollars" | 商业数据增强设计建议的说服力 |
| 文学/文化类比 | Iron Man战衣、蘑菇笑话、Robinson Crusoe、瑞士军刀 | 降低抽象概念的认知门槛 |
| 自我披露 | eBay移动团队前成员、"Nudelman's Law"的自命名幽默 | 构建实践者权威（非纯粹学术权威） |

---

*本索引覆盖全书14章 + Introduction + Foreword中的所有58项模式、12项反模式、10项实验性模式、约100+应用案例引用、约30+外部权威引用、约10+贯穿性隐喻、5项跨章节核心主题。*
