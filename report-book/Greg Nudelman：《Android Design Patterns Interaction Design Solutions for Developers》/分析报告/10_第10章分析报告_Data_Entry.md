# 10_第10章分析报告：Data Entry

## L### 一、章节定位与功能

第10章是全书模式密度最高的章节（9个模式），处理移动端最棘手的交互问题之一——数据输入。该章以Luke Wroblewski的《Web Form Design》作为理论基础，但不求详尽（"you could write an entire book specifically on this subject"），而是聚焦于Android表单中"最常被搞砸的方面"。9个模式覆盖了从离散值选择（Slider、Stepper、Drop Down、Multiple Select）、连续时间范围输入（Scrolling Calendar、Date and Time Wheel）到文本输入（Free-Form Text Input and Extract、Textbox with Input Mask、Textbox with Atomic Entities）的完整数据输入谱系。该章也包含全书最多的实验性模式建议（Slider with Histogram、Slider Based on Inventory Counts、Dual Combo Wheels）。

## L### 二、结构分析

- **10.1 Slider** — 单滑块（Zillow）vs 双滑块（Trulia）。实验变体：Slider with Histogram + Slider Based on Inventory Counts。
- **10.2 Stepper** — Kayak的房间/人数选择器。增强版Peapod→Pet Shop自定义Stepper（可点击中心文本直接输入大数字）。
- **10.3 Scrolling Calendar** — Kayak的连续滚动日历（超越桌面端的移动优先创新）。
- **10.4 Date and Time Wheel** — Google Calendar参考实现+Wheelie模式（ICS新增滑动）+ Picket Informant复合滚轮+Dual Combo Wheels实验模式。
- **10.5 Drop Down** — Trulia/Zillow的标准下拉+Calendar的文本+头像组合下拉。
- **10.6 Multiple Select** — Contacts分组多选+Photo Gallery多选+Pet Shop带操作栏的多选。
- **10.7 Free-Form Text Input and Extract** — Contacts标准文本输入+横屏Extract模式（全屏文本框）。
- **10.8 Textbox with Input Mask** — 隐式掩码（键盘类型变更）+显式掩码（Kayak日期格式）。静态行内掩码实验模式+禁用键盘键反模式。
- **10.9 Textbox with Atomic Entities** — Calendar邀请人输入（自动补全+红色方框标识未识别实体）。

## L### 三、内容分析（核心论题+关键论点案例）

**核心论题1：双滑块在不显示数值范围时几乎无用。** L### Trulia的双滑块和Zillow的两个单滑块都使用了无信息量的"$0"和"No Maximum"——"Imagine how useful these sliders would be if they actually said from the beginning that the range was from $476,000 to $3,234,700"。解决方案：(1)显示全集的真实最小/最大值；(2)将数字显示在滑块上方而非下方（手指不会遮挡）；(3)使用离散位置而非连续滑块（精确调整困难，尤其在移动中——"Nudelman's Law: It is hard to adjust continuous sliders precisely while being bumped around in the metro or a taxi"）。

**核心论题2：Slider with Histogram（带直方图的滑块）是实验性但在实践中强大的模式。** L### 50-100像素的直方图叠加在滑块上方，展示每段价格区间内的库存量。大条形=大库存→用户几乎不会意外选择"零结果区间"。Slider Based on Inventory Counts将滑块间隔按库存数而非绝对价格等分——确保每个位置都有足够的商品。"This is a safe, useful, and resourceful assumption."

**核心论题3：Peapod的Stepper定制是"偶然的可发现性"的案例。** L### 标准Android Stepper只有+/-按钮（数量0-5）。Peapod增强了中心文本字段可点击→弹出数字键盘光箱→可直接输入99。但增强的Stepper看起来与标准Stepper"一模一样"→可发现性极低。Pet Shop解决方案：自定义Stepper增加虚线轮廓和中间数字框→清晰表明可直接编辑。

**核心论题4：Kayak的Scrolling Calendar是"移动端超越桌面端"的设计典范。** L### 连续七列滚动日历利用了"星期几从不变动"的事实（而月份天数变化多端）。"I consider the Kayak mobile app implementation more usable even than its desktop website——an impressive accomplishment!" 但横屏时光箱位于屏幕正中央→需要松开平板才能操作——这是人体工程学的失败。

**核心论题5：Date and Time Wheel的"Robinson Crusoe"困境。** L### 完全自由=完全责任。"entering dates and times like this is like playing Robinson Crusoe on a deserted island and having to make your shoes from scratch...For most people, too much control is just as bad as too little." 解决方案：Pocket Informant的复合滚轮（日期+小时+分钟+星期）→将三个独立滚轮合并为一个，显著减少点击。"Think of this...as a Robinson Crusoe who works remotely from his island on his MacBook Pro, ordering his Nike flip-flops from Zappos—all while sipping a frosty margarita."

**核心论题6：Android 4.0的多行文本字段是"Done按钮消失"的反模式。** L### 单行字段↔Next/Done按钮→推进到下一字段或提交表单。多行字段→Enter键替代Done→键盘始终不消失→用户只能通过硬件返回按钮或点击屏幕空白处关闭键盘→可发现性极低。更糟的是：横屏"Done"转移到下一字段，竖屏"Done"提交表单——"diametrically opposite functions"。解决方案：键盘应在用户点击任何其他表单字段时立即折叠，不论字段类型。

## L### 四、逻辑梳理（论证链条+因果转折）

**主论证链：** 移动数据输入难（手指大+屏幕小+环境乱）→ 9个模式提供替代键盘输入的方案 → 离散值选择（Slider/Stepper/Drop Down）→ 时间范围输入（Calendar/Wheel）→ 文本输入（Free-Form/Mask/Atomic Entities）。

**关键因果转折：**
- 线性价格滑块→容易产生零结果（如"$45.50 to $46.10"）→ 离散位置滑块+直方图/库存计数→彻底消除零结果风险。
- 标准Stepper仅适合0-5 → Peapod的"中心点击编辑"增强→但可发现性低→Pet Shop的自定义虚线+数字框视觉提示。
- Calendar的Done按钮在横竖屏功能相反→这是一个"消失的Done按钮"导致用户被困在键盘视图中的反模式。

**Fitts's Law的反复应用：** 大设备上更难精确调整小控件→"the larger the device, the harder it seems to adjust the slider precisely"→建议平板使用离散位置滑块而非连续滑块→并将控件放在边缘（优化拇指操作）。

## L### 五、材料使用方式

1. **Trulia vs Zillow截图对比（Figure 10.1-10.2）：** 双滑块vs两个单滑块的视觉对比。
2. **Kayak横屏截图（Figure 10.6, 10.13, 10.14）：** 连续滑块显示范围问题+日历光箱居中问题+静默吞掉日期错误。
3. **Peapod截图（Figure 10.8-10.9）：** Stepper的智能增强+可发现性低。
4. **Kayak Scrolling Calendar截图（Figure 10.12）：** 移动端超越桌面端的典范。
5. **Google Calendar多屏截图（Figure 10.15-10.16, 10.25）：** Date and Time Wheel参考实现+错误处理反模式。
6. **Pocket Informant iPhone截图（Figure 10.20）：** 复合滚轮的iOS参考。
7. **Contacts多屏截图（Figure 10.30-10.32, 10.34, 10.38-10.40）：** 多选+文本输入+键盘问题。

## L### 六、论辩与阐述方法

1. **Robinson Crusoe隐喻：** 完全自由=完全责任→帮助读者理解"为什么太多自由度也会有害"。
2. **"Nudelman's Law"的幽默自创：** 对菲茨定律的移动适配版本——"hard to adjust continuous sliders precisely while being bumped around in the metro"——以半幽默的自命名法分享原创观察。
3. **Clint Eastwood / Western致敬：** "For a Few Dollars More"——以电影标题指代价格区间的微小变化。
4. **Fitts's Law的频繁引用：** 作为人体工程学限制的科学解释。

## L### 七、语言文风（原文摘录+L###）

**原文摘录1**（Calendar错误处理）：
> "Remember: Dates are tricky. In the United States, many people make a mistake of entering the wrong AM/PM marker for appointments that span the noon hour."

L### 分析：以文化特例（美国人的午间AM/PM混淆）揭示"日期输入错误"的普遍性→论证系统不应"吞掉"日期错误。

**原文摘录2**（键盘反模式）：
> "The Landscape Done button moves to the next field, whereas the Portrait Done button actually submits the form!" 

L### 分析：以感叹号强调横竖屏"Done"按钮执行相反功能的荒谬性——这是Android 4.0键盘行为中最令人困惑的设计缺陷。

**原文摘录3**（Nudelman's Law）：
> "You have permission to refer to this thereafter as Nudelman's Law if you want."

L### 分析：半幽默的"定律自命名"——将观察包装为可引用的"定律"，增强记忆点。

## L### 八、实体清单（六类，每类≥3项+L###）

### 8.1 核心人物实体

1. **Luke Wroblewski** — 《Web Form Design》作者。L### 输入掩码反模式分析的权威支持。
2. **Alan Cooper** — "pagination of the calendar is a paradigm as old as the Gregorian calendar"——批判翻页日历。
3. **Clint Eastwood** — 间接引用（"For a Few Dollars More"）。

### 8.2 核心概念/术语实体

1. **Nudelman's Law** — 移动中精确调整连续滑块极难。L### 菲茨定律的移动幽默版。
2. **Wheelie Mode（滚轮模式）** — Android 4.0新增的滑动调整Date/Time Wheel功能。L### iOS Picker的Android移植。
3. **Extract Mode（提取模式）** — 横屏时文本框放大为全屏编辑视图。L### Android特有功能。
4. **Atomic Entities（原子实体）** — 离散、不可再分的系统对象（如联系人、机场）。L### Textbox with Atomic Entities模式的理论基础。

### 8.3 核心应用/产品实体

1. **Trulia / Zillow** — Slider对比案例。
2. **Kayak** — Scrolling Calendar标杆+Stepper正面案例+连续滑块问题。
3. **Peapod** — Stepper增强（可发现性低）。
4. **Google Calendar / Contacts** — Date/Time Wheel参考+Drop Down+多选+文本输入。
5. **Pocket Informant（iPhone）** — 复合滚轮概念。
6. **Alarm Clock Xtreme** — Android Picker widget演示。

### 8.5 核心模式/反模式实体

1. **10.1 Slider**
2. **10.2 Stepper**
3. **10.3 Scrolling Calendar**
4. **10.4 Date and Time Wheel**
5. **10.5 Drop Down**
6. **10.6 Multiple Select**
7. **10.7 Free-Form Text Input and Extract**
8. **10.8 Textbox with Input Mask**
9. **10.9 Textbox with Atomic Entities**
10. **Slider with Histogram（实验模式）**
11. **Slider Based on Inventory Counts（实验模式）**
12. **Dual Combo Wheels（实验模式）**

## L### 九、与前后章关联

**与第8章的关系：** Slider with Histogram（10.1）→ 8.3 Filter Strip的配套数据输入组件。

**与第9章的关系：** 不显示库存范围的滑块导致零结果→ 第9章的零结果恢复策略为输入错误提供安全网。

**与第11章的关系：** 第10章的单字段数据输入模式→第11章将这些模式组合成完整表单（表单布局、错误信息、提交策略、输入来自环境的传感器数据）。

**与第12章的关系：** Drop Down vs Dedicated Selection Page（12.2）的选择标准→第10章定义选择控制的通用方案→第12章在银行安全环境中重新评估。
