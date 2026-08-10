# Ch09 分析报告：The State of the Art（当代技艺状况）

## 一、章节定位与功能（L2798–L3157）

全书的技术"现实检查"章：讨论数字排印时代的字符集规模、字体格式、多维字体、齐行技术、屏幕与打印、系统维护。功能：把前八章的古典原则"翻译"到 PostScript/TrueType/OpenType/Unicode 的当代技术语境，同时坚持"技艺高于工具"。

## 二、结构分析

- **9.1 十万字符的字母表（L2798–L2854）**：拉丁字母的"真实规模"（约 600+ 字符）；Unicode 与字符编码史。
- **9.2 字体的实质（L2856–L2925）**：金属 vs 数字；位图字体、PostScript、TrueType、Multiple Master、GX、TrueType Open、OpenType；Bézier 样条。
- **9.3 多维字体（L2934–L3015）**：
  - 9.3.1 字形（glyphs）与字符（characters）的区分（L2936）
  - 9.3.2 手选、随机与程序化的变化（L2967）
- **9.4 齐行方法（L3016–L3035）**：
  - 9.4.1 用最好的齐行引擎（L3018）
- **9.5 像素、打样与印刷（L3037–L3104）**：
  - 9.5.1 若文本将在屏幕上阅读（L3039）
  - 9.5.2 在每一阶段检查字型（L3067）
  - 9.5.3 跟到印刷厂（L3078）
- **9.6 维护系统（L3106–L3157）**：
  - 9.6.1 咨询祖先（L3106）
  - 9.6.2 关照低技术端（L3123）

## 三、内容分析

1. **字母表真实规模**：拉丁字母非 26 个，而是"接近 600 个且随时可增"（L2801）；Gutenberg 用 290 个 sort 排 42 行圣经（L2812）；ASCII 128 字符"连西班牙语/法语/德语工作字符集都装不下"（L2816–L2818）；"如此字符集长期被认为够用，说明 20 世纪中叶美国文明的技术中心主义之狭隘"（L2819）；Unicode 从 8 位到 16 位（L2835–L2836），96,382 字符（L2843）。
2. **字体格式**：PostScript（1982）与 TrueType（1992）的本质区别——hinting 方式与贝塞尔样条阶数（L2866–L2870）；cubic vs quadratic spline（L2878–L2887）；Multiple Master（L2899–L2902）；GX 与 TrueType Open（L2910–L2914）；OpenType（L2915–L2925）。
3. **字形 vs 字符**：Unicode 列"文本符号"而非"排印形态"（L2936–L2939）；字符集（character set）与字形调色板（glyph palette）之别（L2943）；早期冲头雕刻师常为一字刻多形（L2947–L2951）；Sophia 与 Zapfino 为"多维"特例（L2952–L2956）。
4. **齐行**：齐行引擎是"文本排印的心脏"（L3018 附近）；微缩放（microjustification）与压缩字体并用的现代方法（L3024–L3030）。
5. **屏幕与打印**：屏幕监视器上的字体低分辨率对策（L3039–L3066）；打样与印刷阶段的质量控制（L3067–L3104）；"文本与四色图同印时，黑色会向调机员最后调色妥协"（L3101）。
6. **系统维护**：排印"像诗歌绘画一样不受进步影响"（L3112–L3115）；"今天数字排印在某些方面仍落后于文艺复兴排版师与中世纪抄写员"（L3118）；低技术端（铅笔、稿纸、参考书）最需升级（L3131–L3132）；"字体像钢琴需要调音，像文本需要编辑"（L3151–L3155）。

## 四、逻辑梳理

从"字符集规模"（宏观编码）→"字体格式"（微观轮廓）→"字形-字符语义"（概念层）→"齐行"（算法层）→"像素/印刷"（输出层）→"系统维护"（生态层）。论证落点：技术不断换代，但"决定标准的是干活的人，不是配方或品牌"（L2863）。

## 五、材料使用方式

- 技术史料：ASCII/Latin-1/ISO 8859（L2815–L2827）；Unicode 版本史（L2837–L2843）；PostScript 1982、TrueType 1992（L2866–L2867）；Paul de Casteljau 与 Pierre Bézier（L2870）；OpenType 协议（L2915）。
- 字体实例：Adobe Jenson 的 MM 可缩放（L2905–L2908）；Sophia 的多字形（L2952–L2956）；Mrs Eaves 的连字库（L2976–L2979）。
- 社会批判：ASCII=NATO 冷战"我们—他们"心态的纪念物（L2828）。

## 六、论辩与阐述方法

1. 技术中立论：格式之争"真正重要的不是格式，而是手工技艺、常识与细节"（L2862）。
2. 历史连续论：Gutenberg 的多字形/字符区分早于 Unicode（L2946）；Unicode"相对新，但其编目的资源大多古老"（L2853）。
3. 文化批判：ASCII 的文化狭隘（L2819）与"NATO 冷战纪念物"（L2828）。
4. 比喻论证：字体=乐器（钢琴调音，L3151–L3157）；字形=舞蹈（L3148）。

## 七、语言文风摘录（附行号）

- "It is often said that the Latin alphabet consists of 26 letters, the Greek of 24 and the Arabic of 28."（L2799）
- "The extended ASCII character set is the alphabet not of the real world … but of NATO: a technological memento of the them-and-us mentality that thrived in the Cold War."（L2828）
- "In metal and digital founding alike, the standard is set by the human who does the work, not by the recipe or by the brand name of the tools."（L2863）
- "Typography at its best is sometimes as good, and at its worst is just as bad, as it ever was."（L3115）
- "The notes are fixed but they can be endlessly rearranged, into meaningful music or meaningless noise."（L3150）

## 八、实体清单（六类）

**人物**：Paul de Casteljau、Pierre Bézier（L2870）；Ottmar Mergenthaler（L6103 参见）；Hermann Zapf（L116、L190–192 参见）；Matthew Carter（L2952）；Zuzana Ličko（L2976）；Just van Rossum（L190）；Erik van Blokland（L190）；Peter Karow（L6201 参见）；John Warnock（L346 参见）。
**著作/作品**：Adobe Jenson（L2905）；Sophia（L2952）；Zapfino（L2956）；Mrs Eaves（L2976）；42 行圣经（L2812）。
**概念**：ASCII（L2815）；ISO 8859/Latin-1（L2824）；Unicode（L2837–L2843）；bitmap（L2864）；PostScript（L2866）；TrueType（L2867）；Bézier spline（L2870–L2887）；Multiple Master（L2899）；OpenType（L2915）；glyph/character（L2936–L2943）；glyph palette（L2943）；justification engine（L3018）；hinting（L2868）；resolution（L3066 附近）。
**机构**：Adobe Systems（L2915）；Microsoft（L2915）；ISO 日内瓦（L2824）；Unicode Consortium（L6759 参见）；NATO（L2828）；Greek Font Society（L4656，参见）。
**地点**：Geneva（L2824）；Geneva（ISO，同上）；Mountain View（L6920，参见）。
**事件**：1982 PostScript 问世（L2866）；1992 TrueType（L2867）；1990s OpenType 协议（L2915）；2003 Unicode 4.0.0（L2843）。

## 九、与前后章关联

- **与前**：字符集规模问题承接第6章新拼写法（L1902–L1970）；二维印刷史承接第7章 7.3。
- **与后**：字体格式与字形/字符区分直接服务第10章"打磨字体"（字符集、sidebearing、kerning、hinting，L3159–L3334）；Unicode 字符清单在附录 B（L4869 起）逐条给出。
