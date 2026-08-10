# Ch06 分析报告：Street signs and Breadcrumbs（路标与面包屑）

## 章节定位与功能（行号范围）

第六章（L1277-1800），副题"DESIGNING NAVIGATION（导航设计）"（L1279）。属第二部"Things You Need to Get Right（你必须做对的事）"。功能：全书的导航专论——从"人在真实空间如何寻路"类比出 Web 导航的本质、要素、惯例，给出可执行的导航设计清单与"后备箱测试（trunk test）"。是全书写得最详尽的一章。

## 结构分析

- 引子：Talking Heads《Once in a Lifetime》"How did I get here?!"（L1281-1283）
- 事实宣告：找不到路就不会用网站（L1285-1289）
- 商城场景：在 Sears 找电锯的流程图（L1291-1343）
- Web Navigation 101：浏览/搜索两种寻路与流程图（L1343-1374）
- "浏览的不可承受之轻"：Web 空间的三大缺失（尺度/方向/位置感）（L1374-1412）
- 导航被忽视的用途（L1414-1424）
- Web 导航惯例总览（L1426-1448）
- 持久导航五要素：Site ID、Sections、Utilities、Home、Search（L1450-1587）
- 次级/三级导航问题（L1588-1628）
- 页面名（Page names）（L1630-1676）
- "You are here"指示（L1678-1703）
- 面包屑（Breadcrumbs）（L1705-1728）
- 标签（Tabs）（L1730-1755）
- 后备箱测试（trunk test）（L1757-1799）

## 内容分析

**行为基础**：寻路=决定"自己找 vs 问人"（对应 Web 上"浏览 vs 搜索"，L1321-1343）；Jakob Nielsen 将用户分为"搜索主导（search-dominant）"与"链接主导（link-dominant）"（L1348-1350）。流程都以"找到就停/找不到就失望离开"收尾（L1366）。

**Web 空间的三大缺失**：① 无尺度感（不知网站多大，L1378-1382，故已访问链接变色有用 L1384）；② 无方向感（只有层级意义上的上下，L1386）；③ 无位置感（点击即传送，无法靠身体记忆抄近道，L1388-1400）。Home 页因此像"北极星"（L1402），书签与 Back 键是替代记忆（L1400）。"Web 导航"一词存在的理由正是"你在 Web 上天生是迷路的"（L1406-1408），"导航不是网站的一个功能，导航就是网站本身——没有它，就没有'那里'"（L1410）。

**被忽视的三大用途**：导航告诉你"这里有什么"（揭示内容，L1420）、"怎么用"（隐含的操作指南，L1422）、"建站的人行不行"（信心来源，L1424）。

**持久导航（persistent navigation）**：每页都出现、位置外观稳定（L1452-1459），包含 Site ID、Sections、Utilities、Home、Search 五要素（L1461-1466）。例外是表单页——尽量精简以免分散填写注意力（L1469-1475）。
- **Site ID**：如同建筑门上的名字，但 Web 是"传送"，所以每页都要看到（L1479）；位置在左上（L1485-1487）；要么最醒目、要么"框住"整页（L1505-1507）。
- **Sections**：站点层级顶层的栏目链接（L1523）。
- **Utilities**：帮使用站点或了解出版者的链接（登录、帮助、购物车、关于我们等，L1535-1539），只放四五个最常用的，其余进页脚（L1550）。
- **Home 链接**：像"重置键"或"出狱卡"，永远可见（L1552-1558）。
- **Search**：公式=一个框+一个按钮+词"Search"或放大镜图标（L1564-1570）；忌花哨措辞（用 Search 不用 Find/Quick Find，L1572）、忌多余说明（L1574）、忌过早给限定选项（L1576-1586）。

**低层导航**：设计者常只做好前两层，第三层起开始"临场发挥"（L1616）。原因：多层导航难设计、没时间、觉得不重要、拿不到示例内容（L1618-1624）。作者断言用户花在低层页面的时间与顶层一样多，且事后嫁接一致导航几乎不可能（L1626），故"在争论配色之前，先做出所有层级的示例页"（L1628）。

**页面名**：每页必须有名（L1650）、名要在正确位置（框住本页内容，L1656）、名要醒目（L1662）、名要与所点击的文字匹配（"隐式社会契约"，L1664-1670）。

**"You are here"**：用加粗、变色、反白、箭头等突出当前位置（L1685-1697）；最常见的错误是太含蓄——"设计师觉得像拇指一样扎眼时，可能还要再醒目一倍"（L1703）。

**面包屑**：置于页面顶部、用">"作分隔、最后一项加粗且不是链接（L1724-1728），来自汉塞尔与格蕾特的典故（L1712-1714）。

**标签**：自明、难忽略、漂亮（L1736-1742）；有效标签须做出"当前标签在前的空间错觉"——不同色+与内容区相连（L1746-1748）。

**后备箱测试**：想象被蒙眼锁进后备箱扔进站内深处，睁眼须秒答：这是哪个站？我在哪页？站点主要栏目？这层的选项？我在全局何处？怎么搜索？（L1761-1773）做法：随机选页打印、伸长手臂眯眼看、快速圈出六要素（L1781-1797）。

## 逻辑梳理

从物理寻路（商城）→ 推导 Web 寻路（浏览/搜索）→ 指出 Web 空间缺失导致"天然迷路"→ 导航作为"补偿感/处所感"的系统 → 列出持久导航五要素与各层细节 → 用"后备箱测试"总验收。论证链中反复出现"环境缺失→用界面惯例补偿"的逻辑：无尺度感→面包屑/变色链接；无方向感→层级指示；无位置感→Site ID/页面名/You are here。

## 材料使用方式

- 音乐/电影引子：Talking Heads（L1281-1283）
- 虚构场景流程图：Sears 找电锯（含"问店员"分支，L1291-1343）；网站浏览/搜索流程图（L1368-1374）
- 真实站点：Williams-Sonoma（Site ID/Sections/Utilities/页面名标注图，L1443-1448）；University of Virginia、KAYAK、NASA 站标示例（L1513-1519）；South Park/Facebook"传送"示意（L1481-1483）
- 文学典故：汉塞尔与格蕾特（L1712-1714）；《教父》式叙事（未点名）
- 专家引用：Nielsen 的 search-dominant/link-dominant（L1348-1350）；Leonardo da Vinci 发明标签（戏说，L1732）
- 设计惯例：波士顿 vs 洛杉矶路牌对比（L1630-1646）

## 论辩与阐述方法

全章以"类比-拆解-清单-验收测试"组织。最突出的方法是把抽象的 Web 空间问题映射到物理空间（商城、路标、建筑名、博物馆），再用流程图把寻路过程可视化。验收环节（trunk test）用"体验性测试"替代抽象原则，体现本书"重经验验证"的方法观。多处用"我怀疑/我猜"表达个人推断（如 da Vinci 发明标签，L1732），区分事实与意见。

## 语言文风摘录（附行号）

- "People won't use your Web site if they can't find their way around it."（找不到路，就不会用你的站。L1287）
- "Navigation isn't just a feature of a Web site; it is the Web site…Without it, there's no there there."（导航不是功能，导航就是网站……没有它，就没有"那里"。L1410）
- "Navigation reveals content!"（导航揭示内容！L1420）
- "Why I love to drive in L.A."（为什么我爱在洛杉矶开车，L1630）
- "Just click your heels three times and say, 'There's no place like home.'"（敲三下鞋跟说"没有地方比得上家"，L1552，化用《绿野仙踪》）
- "It's so easy to forget that the Web experience is often more like being abducted than following a garden path."（L1775）

## 实体清单（六类，附行号证据）

**人物**：Jakob Nielsen（L1348-1350）；Leonardo da Vinci（L1732）；Talking Heads（L1283）；S. Z. "Cuddles" Sakall（脚注，L1341）
**著作/作品**：《Once in a Lifetime》（Talking Heads，L1283）；《绿野仙踪》（L1552 化用）；汉塞尔与格蕾特童话（L1712-1714）；Casablanca（脚注，L1339-1341）
**概念**：Web navigation（L1406-1408）；persistent/global navigation（L1452）；Site ID（L1479-1511）；Sections（L1523）；Utilities（L1535-1550）；page name（L1630-1676）；"You are here" indicator（L1678-1703）；Breadcrumbs（L1705-1728）；tabs（L1730-1755）；trunk test（L1757-1799）；search-dominant/link-dominant users（L1348-1350）；bookmarks（L1400）
**机构**：Williams-Sonoma（L1445）；University of Virginia（L1513）；KAYAK（L1519）；NASA（L1519）；Sears（L1293-1410）；South Park、Facebook（示例站，L1481-1483）
**地点**：Los Angeles（L1630-1646）；Boston（L1638-1644）；Budapest（脚注，L1341）；Kansas（L1477 化用《绿野仙踪》）
**事件**：无独立事件（案例均为站点导航示例）

## 与前后章关联

承第 1-5 章"别让我思考/扫描/无脑选择/删字"原则，将其工程化为导航系统；第 7 章把同一套原则用于首页（导航是首页的核心组件，L1827）。第 8 章"争论"与第 9 章"测试"则处理"怎么知道导航设计对了"——trunk test 正是可交给用户验证的雏形。
