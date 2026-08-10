# NN_专项报告与实体总索引：《Atomic Design》Brad Frost

---

# 上部：专项报告

## 专项报告一：全书类比系统分析

### 1.1 类比总览

《Atomic Design》可能是设计方法论著作中使用类比密度最高的文本之一。全书使用了超过15种独立的类比，来自至少7个不同的知识域。以下是对全书类比系统的完整梳理。

### 1.2 类比清单（按出现顺序）

L### 1. 化学类比（Ch2核心）
- 源域：原子→分子→有机体（高中化学）
- 目标域：HTML标签→UI小组件→界面段落（界面设计）
- 功能：方法论建构——为五阶段模型提供认知框架
- 映射精度：高——在Atoms/Molecules/Organisms三个层面有精确的结构对应
- 适用边界：Frost在Templates阶段自觉放弃——"朋友们，是时候告别我们的化学类比了"
- 延伸使用：氢气的可燃性vs氦气的惰性（原子属性决定应用后果）；H₂O vs H₂O₂（相同原子组成但不同属性）

L### 2. 科幻跳伞服类比（Ch1）
- 源域：科幻电影中未来人类全都穿同一种跳伞服
- 目标域：所有网站使用同一个前端框架（Bootstrap）导致外观趋同
- 功能：批判现成框架
- 映射精度：低——表面类比，主要是为了制造幽默效果
- 插图：Melissa Frost绘制的"在未来，每个人都穿得一样"配图

L### 3. Ron Popeil烤肉机类比（Ch1）
- 源域："设好就忘"（set-it-and-forget-it）的Ron Popeil旋转烤肉机
- 目标域：大规模的全站重设计——"造完忘了，三年后再来一次"
- 功能：批判"项目化"心态
- 映射精度：低——贬义性的幽默类比

L### 4. JavaScript / Mustache 双关（Ch3）
- 源域：八字胡的实物形象
- 目标域：Mustache模板语言的`{{}}`语法
- 功能：纯幽默/记忆辅助
- 映射精度：极低——仅基于视觉相似性

L### 5. 俄罗斯套娃类比（Ch3核心）
- 源域：Matryoshka dolls——精美雕刻的空心木制娃娃，从小到大嵌套
- 目标域：Pattern Lab中的模式包含关系——原子被包含在分子中，分子被包含在有机体中
- 功能：技术概念引入——在大量代码片段到来之前建立直观的心理模型
- 映射精度：中——很好地表达了"嵌套包含"，但未覆盖"修改自动传播"的DRY利益
- 配图：S. Faric在Flickr上的俄罗斯套娃实物摄影

L### 6. 乐高类比（Ch4核心——来自Wolfram Nagel）
- 源域：两种乐高搭建方法——(a)直接倒出零件然后翻找；(b)先按类型和颜色分类整理
- 目标域：两种数字项目方法——(a)直接开始建网站；(b)先创建模式库的组件系统
- 功能：论证设计系统的效率价值——"organized inventory produces better, faster work"
- 映射精度：高——作为日常物品与专业实践的类比，具有极强的可理解性和共情力
- 配图：来自Nagel原书的三张乐高搭建对比插图

L### 7. 减法石雕类比（Ch4）
- 源域：雕塑家从一块巨石开始，粗凿→细雕→细节→定期退后审视→完成
- 目标域：数字设计的迭代过程——从低保真探索到高保真完成的逐步构建
- 功能：定义"好的迭代"的特征——逐步增加保真度，定期审视全局
- 映射精度：中高——准确描绘了"迭代"的时间维度和精度递进
- Frost的限定："Unlike sculpture we have the power of undo!"

L### 8. 预制厨师类比（Ch4）
- 源域：餐厅的预制厨师——切蔬菜、腌制肉类、准备沙拉，为正式烹饪做准备
- 目标域：前端开发者在项目第一天的代码准备——设置环境、标记基本模板和模式
- 功能：为"开发者在设计阶段就开始写代码"提供正当性辩护
- 映射精度：中——准确表达了"准备工作的专业价值"，但没有覆盖准备与主厨（设计）之间的实时交互

L### 9. "鼻子=脸"类比（Ch4客户反馈引用）
- 源域：通过展示一个人的鼻子来评价整张脸有多美
- 目标域：通过element collages来评价整个网站的设计
- 功能：承认低保真探索的认知局限——在某些节点上，人们需要看到"整张脸"
- 映射精度：低——主要用于表达客户的合理诉求，非方法论类比

L### 10. 瀑布/装配线类比（散布全书）
- 源域：物理制造的线性流水线（Henry Ford的装配线；建筑中的顺序工序）
- 目标域：数字项目中的"UX→视觉→前端→后端→上线"线性流程
- 功能：批判——物理世界的合理逻辑不适用于数字世界（像素很便宜，错误成本低）
- 映射精度：中——表达了线性结构，但物理制造的复杂性与数字设计的迭代性不完全对称

L### 11. "美酒vs新车"类比（Ch5）
- 源域：新车——开出停车场即刻贬值；美酒——随时间越陈越香
- 目标域：无维护的设计系统（贬值）vs持续维护的设计系统（增值）
- 功能：使"维护的价值"从抽象概念转化为可感知的日常经验
- 映射精度：低——高度简化的价值曲线类比
- 配图：Sabin Paul Croce和Ray Larabie在Flickr上的美酒和汽车照片

L### 12. 生物类比（Ch5）
- 源域：动物需要进食，植物需要水和阳光
- 目标域：设计系统需要持续关注和照顾
- 功能：自然化"维护"的概念——它不是额外的负担，而是任何活的东西的基本需求
- 映射精度：极低——泛化的生命类比，主要用于情感号召

L### 13. 博物馆/考古类比（Ch5——Nathan Curtis概念延伸）
- 源域：考古发掘或博物馆中的"制品"——静态、已完成、不会变化
- 目标域：风格指南如果只作为"制品"交付——它将像博物馆文物一样，被观看但不被使用
- 功能：建立"制品↔产品"的核心区分
- 映射精度：中——准确表达了静态vs动态的区分

L### 14. 西部片类比（Ch5）
- 源域：西部片结尾——英雄"骑着马奔向落日"
- 目标域：客户服务业的项目交付心态——交完包裹就潇洒离开
- 功能：幽默批判项目制的短视
- 映射精度：低——纯修辞性类比

L### 15. 婴儿与洗澡水（Ch5）
- 源域：不要把孩子连同洗澡水一起倒掉（英语谚语）
- 目标域：重建设计系统时不要全盘舍弃——按钮/表单/标签等基本模式将依然存在
- 功能：鼓励在设计系统演进中保持"保守中的进步"

### 1.3 类比使用模式总结

L### 高频使用类比的知识域排名
1. 日常物品/生活经验：俄罗斯套娃、乐高、美酒、汽车、预制厨师、科幻片、西部片、烤肉机——8个
2. 艺术与手工：石雕、画家（Chimero的比喻）、博物馆/考古——3个
3. 自然科学：化学（原子/分子/有机体）、生物学——2个
4. 工业制造：装配线/瀑布——1个
5. 语言学/文字游戏：八字胡（Mustache双关）——1个

**结论**：Frost的策略是"从日常出发，抵达专业"。绝大多数类比来自普通读者（非设计师/非开发者）也能完全理解的日常生活域——这使得本书具有了对跨专业读者的强大"翻译"能力。

---

## 专项报告二：全书修辞策略系统分析

### 2.1 核心修辞装置

L### 1. 反讽开场（Irony Opening）
- 实例：Ch1以"很久很久以前，有一种叫'书'的东西"开始——而作者正在写的正是一本书
- 功能：元叙事式的自我反讽建立亲和力，同时为"批判页面隐喻"的主题做铺垫

L### 2. 童话反转（Fairy-tale Subversion）
- 实例：Ch5以"And they lived happily ever after. Right? Not quite."开始
- 功能：通过构建过度美好的预期然后击碎，制造幽默并植入"上线不是终点"的核心信息

L### 3. 自传式自我暴露（Autobiographical Self-disclosure）
- 实例：Ch2的高中化学回忆（越战老兵+壮观胡子的Rae先生）；Ch4的"我从未上过一节计算机科学课"和"我被要求规范化数据库"
- 功能：将作者从"方法论权威"降格为"与读者同行的实践者"，建立平等的读者关系

L### 4. 预判性缓冲（Anticipatory Buffer）
- 实例："By now you may be wondering why we're talking about atomic theory, and maybe you're even a bit angry at me"；"If you're not a developer, don't freak out!"；"Whew. If you've made it this far, congratulations!"
- 功能：在认知负荷或怀疑峰值处插入缓冲语言，调节读者情绪

L### 5. 十诫式格式化（Decalogue Formatting）
- 实例：Ch5的十个"Make it..."原则；Ch4界面审计的五步法；Ch2五阶段末尾的五条总结
- 功能：提供记忆结构（编号+重复句法），赋予宣言式权威

L### 6. 微型叙事嵌入（Embedded Micro-narrative）
- 实例："Death to the waterfall"（400+词微型小说）；"Frost的健康保险公司网站"（70词个人轶事）
- 功能：将抽象论证锚定于具体的、身体的经验，使读者能够"经历"而非仅仅"理解"论点

L### 7. 行业警句引用（Industry Aphorism Quotation）
- 实例：几乎每一个主要论点都附带一个行业人物的警句式引用
- 功能：权威背书+概念凝练+不同声音的对话性

### 2.2 读者关系建构

Frost的修辞策略中最显著的特征是他与读者的关系建构：
- 始终使用第一人称"I"和第二人称"you"——在一个容易沦为非人格化技术手册的主题中始终保持了对话性
- 使用"we"在第一和第二人称之间切换——当讨论行业问题时用"we"（"我们都在这个多设备宇宙中挣扎"）将读者拉入同行共同体
- 自嘲作为去权威化的修辞工具——当Frost说"我不是PHP巫师"、"我在高中美术室度过而非计算机科学教室"时，他是在宣告：不需要成为专家也能理解和实践原子设计

---

## 专项报告三：全书叙事结构分析

### 3.1 宏观叙事弧线

《Atomic Design》可以解读为一个"英雄之旅"（Hero's Journey）的叙事结构应用于方法论写作：

L### 序幕：平凡世界中的召唤
Foreword + Ch1前半："我们日常面临着页面隐喻的暴政"——现状的描述

L### 拒绝召唤→跨越门槛
Ch1后半："但模块化的精神正在各处渗透"——变革力量的觉醒

L### 导师与试炼
Ch2（方法论） + Ch3（工具）——获得"原子设计"的魔法剑（方法论）和"Pattern Lab"的盾牌（工具）

L### 接近最深洞穴→磨难
Ch4前半："Death to the waterfall"——直面行业最深的黑暗（瀑布流程）并在其中受苦

L### 奖励→返回之路
Ch4后半："Bring it on home"——完成项目，携带新的智慧和系统归来

L### 复活→带着灵药返回
Ch5："Make it last" + "Go forth and be atomic"——设计系统被重新定义为"活的产品"，方法论被交付给全世界

### 3.2 情感的节奏控制

全书的情感曲线呈现出有意识的波动设计：
- Ch1：幽默（高能量）→温和批判（中能量）
- Ch2：个人回忆（温暖）→方法论建构（理性）→诗意升华（Frank Chimero引用）
- Ch3：技术解释（低情感/高认知负荷）
- Ch4："Death to the waterfall"（高情感/悲剧叙事）→迭代论述（中能量）→"Bring it on home"（喜悦/庆祝）
- Ch5：反转幽默（"Not quite"的惊讶）→严肃宣言（十诫）→鼓舞号召（"Go forth"的高情感终章）

这种情感波动使得阅读体验不会因为600+行的连续论述而变得单调——它模拟了真实项目的情绪起伏：希望→困惑→学会工具→遭遇现实→克服困难→庆祝→新的挑战→终局决心。

---

## 专项报告四：全书引文系统分析

### 4.1 引文使用统计

全书引用约30+位行业人物的言论，引文总数超过45处。以下是最频繁被引用的人物排名：

L### Nathan Curtis — 设计系统理论家（4次以上引用，集中在Ch5）
- 核心概念：(1)"设计系统是有资金的产品vs风格指南是制品" (2)"把风格指南交付当作高潮是错误的叙事"

L### Mark Boulton — 网页设计师/内容理论家（4次以上引用，分布在Ch2和Ch4）
- 核心概念：(1)内容结构vs内容本身的区分 (2)"设计过程怪异而复杂，因为人怪异而复杂"

L### Dan Mall — 设计师/Frost的合作者（4次以上引用，集中在Ch4）
- 核心概念：(1)"我们像卖画一样卖网站" (2)element collages (3)"把'在浏览器中设计'改为'在浏览器中决策'"

L### Stephen Hay — 网页设计师（2次引用，Ch1）
- 核心概念："展示完全烘焙的Photoshop合成图是展示网站绝对不会看起来像什么的最有效方式"

L### Dave Rupert — 前端开发者（1次核心引用+多次提及，Ch1）
- 核心概念："tiny Bootstraps for every client"

L### Anna Debenham — 作者（2次引用，Ch1和Ch5）
- 核心概念：(1)风格指南的教育功能 (2)公共风格指南的招聘价值

L### Karen McGrane — 内容策略师（1次引用，Ch1）
- 核心概念：模块化内容的未来愿景

L### Jina Bolton / Salesforce — 设计师（3次以上引用，Ch3和Ch5）
- 核心概念：设计系统制作者与使用者的反馈循环

L### Frank Chimero — 设计师/作者（1次引用，Ch2）
- 核心概念：画家比喻——部分与整体之间的舞步

### 4.2 引文功能类型

L### 1. 权威背书型
由知名行业人物提供的支持性引文，增强论点的可信度。
L### 2. 概念定义型
由行业人物提供的术语或概念的精确表述（如Nathan Curtis的"系统vs制品"）。
L### 3. 叙事启动型
用于启动一个章节或重要段落的引文（如Mark Boulton对"人很怪异"的引用开启了Ch4整个"人的问题"板块）。
L### 4. 过渡桥接型
在两个主题之间提供过渡的引文（如Dennis Crowley的"最难的是建造建造产品的机器"连接了风格指南的益处和挑战）。
L### 5. 警句收束型
极短的警句用于收束一个讨论段（如Jason Santa Maria的"Ideas are meant to be ugly"）。

---

## 专项报告五：全书视觉修辞分析

### 5.1 图像使用统计与分类

全书包含约60+张图像（含插图、截屏、信息图、照片），分为以下类别：

L### 信息图/示意图（约15张）
- 原子设计五阶段全景图
- HTML元素周期表（Josh Duck）
- 化学方程式示意图
- 模式结构-内容对比图
- 瀑布vs迭代协作流程对比图
- Trent Walton的迭代流程图
- 设备进化三连图（过去-现在-未来）
- Lonely Planet Rizzo圣杯架构图
- Canonical Vanilla决策树图
- Phase2 Technology的模板桥接图
- 制作者vs使用者关系频谱图
- "风格指南折断"对比图

L### 截屏（约25张）
- Pattern Lab界面截图（默认仪表盘、文件夹结构、代码视图、lineage视图、文档/注解视图）
- 商业网站截图（Gap产品网格、Time Inc.首页模板和页面、United.com按钮集合）
- 设计工具/框架截图（Bootstrap组件、Salesforce Lightning代码视图、Material Design组件文档）
- 风格指南截图（Yelp首页、Intuit Harmony平台切换、Shopify风格指南首页、Styleguides.io汇总页）
- ish.视口工具三尺寸截图

L### 照片/实物图（约10张）
- 俄罗斯套娃（S. Faric on Flickr）
- 乐高搭建对比（来自Wolfram Nagel的书）
- 石雕过程（Mike Beauregard on Flickr）
- 预制厨师工作照
- 美酒（Sabin Paul Croce on Flickr）
- 汽车（Ray Larabie on Flickr）
- 20-second gut test工作坊现场照

L### 原创插图（约5张）
- Melissa Frost的"科幻跳伞服"插图
- 高中学化学的回忆插图（非直接化学课本内容）
- 各种设备集合的图示
- "Death to the waterfall"中的瀑布流程示意图

L### 设计探索制品（约10张）
- Style tiles示例
- Element collages示例
- 低保真HTML线框
- Display patterns手势草图
- 电子表格内容规划
- Dan Mall的header视觉探索
- Frost的header HTML灰度原型
- 最终header实现

### 5.2 图像-文本关系模式

L### 模式1：概念双码化
将抽象概念同时以文字定义和视觉图示呈现——如原子设计的五阶段全景图同时展示五个嵌套的同心层级。

L### 模式2：并置对比
将"之前/之后"或"对/错"并排展示——如United.com的按钮集合并排显示37种不一致的按钮样式来暴露问题。

L### 模式3：结构展示
展示代码片段或文件夹结构来证明技术论断——如Pattern Lab的atoms/molecules/organisms文件夹树状视图证明了"五阶段模型在工具中是可操作的"。

L### 模式4：叙事插图
在长篇叙事段落中插入相关图像，打破纯文字的单调——如"Death to the waterfall"叙事之后紧跟瀑布流程示意图。

L### 模式5：类比可视化
将类比中的源域以实物照片呈现——如俄罗斯套娃的实物照片使得"嵌套包含"的抽象概念在读者心中建立了一个视觉锚点。

---

# 下部：全书实体总索引

## 索引A：人物实体（按姓氏字母序）

本索引收录全书被引用、提及或作为案例来源的所有人物。格式：姓名 — 身份/组织 — 主要出现章节 — 核心引用/贡献。

L### Bolton, Jina — 设计师, Salesforce — Ch3, Ch5 — "The Design System informs our Product Design"；公共风格指南作为招聘工具的亲历者
L### Boulton, Mark — 网页设计师/内容理论家 — Ch2, Ch4 — 内容结构vs内容本身的区分；"人怪异所以过程怪异"
L### Brook, Jennifer — UX设计师 — Ch4 — TechCrunch的display patterns手势草图
L### Chimero, Frank — 设计师/作者,《The Shape of Design》 — Ch2 — 画家比喻："a dance of switching contexts"
L### Clarke, Andy — 网页设计师 — Ch1 — "design atmosphere"概念
L### Clark, Josh — 设计师/Frost合作者 — Foreword — 与Dan Mall共同撰写前言
L### Crossman, Jeff — 设计师, GE — Ch2 — 原子设计术语在GE的本地化
L### Crowley, Dennis — 企业家 — Ch1 — "最难的是建造建造产品的机器"
L### Curtis, Nathan — 设计系统理论家 — Ch5 — "系统是有资金的产品vs风格指南是制品"
L### Debenham, Anna — 作者,《Front-End Style Guides》 — Ch1, Ch5 — 风格指南的教育功能；公共风格指南的招聘价值
L### Duck, Josh — 网页开发者 — Ch2 — HTML元素周期表的创建者
L### Frost, Brad — 本书作者 — 全书 — 原子设计方法论的创建者；Pattern Lab的联合创建者
L### Frost, Melissa — 插画师 — Ch1 — "科幻跳伞服"及各章插图的创作者
L### Harned, Brett — 项目经理 — Ch1 — Agile vs. agile的区分
L### Hay, Stephen — 网页设计师 — Ch1 — "presenting fully baked Photoshop comps is the most effective way to show your clients what their website will never look like"
L### Holgado, Federico — Lead UX Developer, MailChimp — Ch1 — MailChimp模式库复用的经验
L### Lee, Kate Kiefer — 语音与语调专家 — Ch1 — "voice stays the same but tone changes"
L### Lovely, Evan — 技术专家, Phase2 Technology — Ch3, Ch5 — Pattern Lab + Drupal + Twig桥接方案
L### Mall, Dan — 设计师/Frost合作者 — Ch1, Ch4 — "deciding in the browser"；element collages的创建者；TechCrunch视觉探索
L### Marcotte, Ethan — 网页设计师 — Ch1 — Responsive Web Design创始人
L### McGrane, Karen — 内容策略师 — Ch1 — 模块化内容的未来愿景
L### Muenzenmeyer, Brian — 开发者, Pattern Lab联合维护者 — Ch3 — Pattern Lab的共同创建者之一
L### Nagel, Wolfram — 作者,《Multiscreen UX Design》 — Ch4 — 乐高类比（两种搭建方法对比）
L### Olsen, Dave — 开发者, Pattern Lab联合维护者 — Ch3 — Pattern Lab的共同创建者之一
L### Persson, Inayaili de León — Canonical网页团队 — Ch5 — Vanilla框架的模式治理决策树
L### Rupert, Dave — 前端开发者, Paravel — Ch1 — "tiny Bootstraps for every client"
L### Santa Maria, Jason — 设计师/作者 — Ch4 — "Ideas are meant to be ugly"
L### Schleifer, Alex — 设计负责人, Airbnb — Ch5 — "最大的生存威胁是忽视"
L### Sivitz, Micah — Shyp公司 — Ch5 — 设计系统的Slack+GitHub沟通自动化
L### Somers, Marcelo — 网络开发者 — Ch3, Ch5 — "Chasing the Holy Grail"文章；版本化CSS/JS策略
L### Spool, Jared — UX研究者 — Ch1 — "Magic Escalator of Acquired Knowledge"概念
L### Walton, Trent — 设计师, Paravel — Ch4 — 迭代设计流程图的创作者
L### Warren, Samantha — 设计师 — Ch1, Ch4 — Style Tiles的创建者
L### Berners-Lee, Tim — 万维网发明者 — Ch1 — 页面隐喻的历史根源

## 索引B：组织/公司实体（按字母序）

L### Airbnb — 共享住宿平台 — Ch5 — "忽视是最大威胁"的理念来源
L### Bootstrap (Twitter) — 前端框架 — Ch1, Ch3 — 讨论现成框架时的核心参照物
L### Canonical / Vanilla — Ubuntu母公司 — Ch5 — 模式治理决策树
L### CERN — 欧洲核子研究组织 — Ch1 — 万维网诞生地
L### Dalhousie University — 大学 — Ch1 — 写作风格指南案例
L### Entertainment Weekly — 媒体 — Foreword, Ch4 — Style tiles + Element collages项目
L### Foundation (Zurb) — 前端框架 — Ch1 — 与Bootstrap并列的框架
L### Gap — 服装零售商 — Ch2 — 电商产品网格有机体案例
L### GE (General Electric) — 跨国企业 — Ch2 — 原子设计术语本地化
L### GitHub — 代码托管平台 — Ch1, Ch5 — 代码风格指南案例；设计系统问题追踪
L### Google / Material Design — 科技公司 — Ch1, Ch5 — 设计语言；changelog；组件文档
L### Instagram — 社交平台 — Ch2 — 原子设计非web应用的证明案例
L### Intuit / Harmony — 财务软件 — Ch5 — 跨平台设计系统案例
L### Lonely Planet / Rizzo — 旅行指南 — Ch3, Ch5 — 圣杯设计系统先驱
L### MailChimp — 邮件营销 — Ch1 — 语音和语调指南；模式库复用
L### NPR / COPE — 广播电台 — Ch1 — 模块化内容平台
L### Paravel — 网页工作室 — Ch1, Ch4 — Microsoft首页重设计；迭代流程图
L### Phase2 Technology — 技术公司 — Ch3, Ch5 — Pattern Lab + Drupal + Twig桥接
L### Pittsburgh Community Food Bank — 公益 — Ch4 — 低保真线框案例
L### Salesforce / Lightning — CRM平台 — Ch3, Ch5 — 商业设计系统标杆
L### Shyp — 物流科技 — Ch5 — 设计系统沟通自动化案例
L### Starbucks — 咖啡连锁 — Ch1 — 模式命名案例（Blocks Three-Up）
L### TechCrunch — 技术媒体 — Foreword, Ch4 — 核心重设计项目
L### The Economist — 新闻媒体 — Ch1 — 写作风格指南案例
L### Time Inc. — 媒体集团 — Ch2, Ch3 — 首页模板和页面案例；Pattern Lab贯穿案例
L### United.com — 航空公司 — Ch4 — 界面审计反面案例
L### U.S. Federal Government — 政府 — Ch5 — 巨型分散组织设计系统
L### West Virginia University — 大学 — Ch1 — 品牌身份指南案例
L### Yelp — 消费者评论 — Ch1, Ch5 — 风格指南首页设计案例

## 索引C：技术/工具实体（按类别）

L### 模式库与设计系统工具
L### Pattern Lab — Frost的开源工具 — Ch3, Ch4, Ch5
L### Bootstrap — Twitter前端框架 — Ch1
L### Foundation — Zurb前端框架 — Ch1
L### Salesforce Lightning Design System — 商业设计系统 — Ch3, Ch5
L### Lonely Planet Rizzo — 圣杯系统 — Ch3, Ch5
L### Canonical Vanilla Framework — CSS框架 — Ch5
L### Intuit Harmony — 跨平台设计系统 — Ch5
L### U.S. Draft Web Digital Standards — 公共设计系统 — Ch5

L### 模板语言与数据格式
L### Mustache — 逻辑无关模板语言 — Ch3, Ch5
L### Twig — PHP模板引擎 — Ch3, Ch5
L### Handlebars / Underscore / Jade / Nunjucks — 其他模板语言 — Ch5
L### JSON — 数据交换格式 — Ch3
L### YAML / Markdown — 数据/文档格式 — Ch3

L### 设计工具
L### Photoshop — 图像编辑 — Ch1, Ch4
L### Sketch — 矢量设计 — Ch1, Ch4
L### After Effects — 动效工具 — Ch4
L### Balsamiq — 线框工具 — Ch4

L### 前端技术
L### HTML / CSS / JavaScript — web标准三层 — Ch2, Ch3
L### SCSS (Sassy CSS) — CSS预处理器 — Ch3
L### OOCSS / SMACSS / BEM — CSS方法论 — Ch1
L### Container Queries — 前瞻CSS特性 — Ch3

L### 后端/CMS
L### PHP / Node.js — Pattern Lab引擎 — Ch3
L### Drupal — CMS — Ch3, Ch5
L### WordPress — CMS — Ch3
L### MySQL — 数据库 — Ch3

L### 协作与治理工具
L### Git / GitHub — 版本控制 — Ch3, Ch5
L### Slack / Yammer / HipChat — 团队沟通 — Ch5
L### JIRA / GitHub Issues — 问题追踪 — Ch5
L### Sass Deprecate — Salesforce的模式弃用工具 — Ch5
L### Component Libraries Drupal Module — Phase2的桥接组件 — Ch5

L### 测试与审查工具
L### ish. — Frost的视口测试工具 — Ch3
L### CSS Stats / Stylify Me — 风格审查工具 — Ch4
L### QuickTime — 屏幕录制工具 — Ch4

L### 设计与展示工具
L### Google Slides / PowerPoint / Keynote — 演示工具 — Ch4
L### Evernote Web Clipper — 网页截取 — Ch4
L### CodePen — 在线代码片段 — Ch4

L### 早期组件库
L### YUI (Yahoo User Interface Library) — Ch1
L### jQuery UI — Ch1

## 索引D：概念/方法论实体（按主题）

L### 核心方法论
L### Atomic Design — 五阶段方法论 — Ch2, 全书
L### Atoms / Molecules / Organisms / Templates / Pages — 五阶段 — Ch2
L### Mental Model（心智模型） — 对原子设计的本质定性 — Ch2
L### Modularity（模块化） — 全书基础概念 — Ch1, 全书

L### 风格指南与模式库
L### Style Guide（风格指南） — 六大类 — Ch1
L### Pattern Library（模式库） — 同front-end style guide/UI library — Ch1, Ch3
L### Brand Identity Guidelines — 品牌身份 — Ch1
L### Design Language Guidelines — 设计语言 — Ch1
L### Voice and Tone Guidelines — 语音与语调 — Ch1
L### Writing Style Guides — 写作指南 — Ch1
L### Code Style Guides — 代码指南 — Ch1

L### 工作流与流程
L### Interface Inventory（界面审计） — 五步法 — Ch4
L### 20-Second Gut Test — 审美偏好快测 — Ch4
L### Waterfall Process（瀑布流程） — 批判对象 — Ch4
L### Iterative Process（迭代流程） — 替代方案 — Ch4
L### Front-end Prep Chef（前端预制厨师） — 角色类比 — Ch4
L### Make-Show-Official（做-展示-正式化） — 三步策略 — Ch5

L### 设计探索工具
L### Style Tiles — Samantha Warren — Ch1, Ch4
L### Element Collages — Dan Mall — Ch1, Ch4
L### Content & Display Patterns — 低保真UX方法 — Ch4
L### Design Atmosphere — Andy Clarke — Ch1

L### 设计系统治理
L### Design System as Product（系统即产品） — Nathan Curtis — Ch5
L### Holy Grail（圣杯） — 同步理想 — Ch3, Ch5
L### Governance（治理） — 变更管理 — Ch5
L### Design System Makers vs. Users — 角色二分 — Ch5
L### Friendly Friction（友善摩擦） — 系统思维 — Ch5
L### Pattern Deprecation（模式弃用） — 生命周期管理 — Ch5
L### Design System Evangelism（系统传播） — 内部推广 — Ch5
L### Templating Language Bridge — 技术桥接 — Ch5

L### 计算机科学原则
L### DRY (Don't Repeat Yourself) — Ch3
L### Single Responsibility Principle — Ch2
L### Separation of Concerns — Ch1
L### Object-Oriented Programming — Ch1

L### 设计原则
L### Responsive Web Design — Ethan Marcotte — Ch1
L### Future-Friendly — The Future-Friendly Manifesto — Ch1
L### Mobile-First — Ch4
L### Progressive Enhancement — Ch4

L### 内容策略
L### COPE (Create Once, Publish Everywhere) — NPR — Ch1
L### Content Structure vs. Final Content — Mark Boulton — Ch2

L### 命名与分类
L### Context-Agnostic Naming — 语境无关命名 — Ch5
L### Contextual Documentation — 语境相关文档 — Ch5
L### Pattern Lineage（模式谱系） — 自动上下文 — Ch3, Ch5

L### UI变体管理
L### Pseudo-Patterns（伪模式） — Pattern Lab机制 — Ch3
L### Template Variations（模板变体） — 极端案例测试 — Ch2
L### Page-Level Data Override — 页面级数据覆盖 — Ch3

L### 行业概念
L### Magic Escalator of Acquired Knowledge — Jared Spool — Ch1
L### Special Snowflake Syndrome — Brad Frost自创 — Ch1
L### Agile vs. agile — Brett Harned — Ch1
L### "Deciding in the Browser" — Dan Mall — Ch4
L### "Tiny Bootstraps" — Dave Rupert — Ch1

## 索引E：项目/案例实体（按章节）

L### Ch1
L### TechCrunch Redesign — 多章节主线项目
L### Microsoft Homepage (Paravel) — "tiny Bootstraps"来源
L### NPR COPE Platform — 模块内容先驱
L### MailChimp Voice and Tone — 语音语调标杆
L### Google Material Design — 设计语言标杆
L### West Virginia University Brand Guidelines — 品牌指南
L### The Economist Writing Style Guide — 写作指南
L### GitHub Code Style Guide — 代码指南
L### Yelp Style Guide — 风格指南设计

L### Ch2
L### Time Inc. Homepage — 模板/页面阶段案例
L### Instagram Native App — 非web应用五阶段分析
L### Gap E-commerce — 产品网格有机体案例

L### Ch3
L### Time Inc. Website (Pattern Lab实现) — 全章贯穿案例
L### Salesforce Lightning Design System — 代码视图案例
L### Lonely Planet Rizzo — 圣杯代码视图案例
L### Phase2 Technology (Pattern Lab + Drupal) — 模板桥接案例

L### Ch4
L### TechCrunch Header Design Journey — 从概念到完成的完整旅程
L### Entertainment Weekly — Style tiles + Element collages
L### Pittsburgh Community Food Bank — 低保真线框
L### About.com Health Conditions — 电子表格内容规划
L### United.com — 界面审计负面案例

L### Ch5
L### Lonely Planet Rizzo — 圣杯架构
L### Salesforce Lightning — 设计系统治理
L### Canonical Vanilla — 模式治理决策树
L### Phase2 Technology — Technical圣杯实现
L### U.S. Draft Web Digital Standards — 巨型分散组织案例
L### Intuit Harmony — 跨平台设计系统
L### Shyp — 沟通自动化

## 索引F：文献/资源实体（按类型）

L### 书籍
L### Ethan Marcotte, Responsive Web Design (A Book Apart, 2011)
L### Frank Chimero, The Shape of Design
L### Anna Debenham, Front-End Style Guides
L### Wolfram Nagel, Multiscreen UX Design
L### Brad Frost, Atomic Design (本书)

L### 宣言/标准
L### The Future-Friendly Manifesto (2011)

L### 网站/资源
L### Styleguides.io — 公共风格指南汇总
L### This Is Responsive — Frost的响应式模式展示
L### Josh Duck's Periodic Table of HTML Elements
L### Pattern Lab Documentation

L### 网络文章
L### Marcelo Somers, "Chasing the Holy Grail"
L### Nicole Sullivan, OOCSS / Media Object

L### 播客
L### StylesGuide Podcast — Frost & Anna Debenham主持

---

*报告生成日期：2026年8月4日*
*覆盖范围：《Atomic Design》全书（Foreword + Ch1-Ch5 + Resources）*
*总报告文件数：7份（00_整体分析报告 + 01~05_分章报告 + NN_专项报告与实体总索引）*
