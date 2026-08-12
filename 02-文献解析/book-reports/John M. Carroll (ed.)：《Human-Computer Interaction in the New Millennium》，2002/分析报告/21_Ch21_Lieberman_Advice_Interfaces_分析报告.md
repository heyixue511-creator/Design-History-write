# Ch21 分析报告：Interfaces That Give and Take Advice

**作者**：Henry Lieberman（MIT Media Lab）
**所属 Part**：Part V — Media and Information
**在书中位置**：第475–486页

---

## 一、章节定位与功能
### L001
Ch21提出"建议型界面"（Advice-Based Interfaces）作为HCI的新范式——取代"要么全自动代理（AI agents），要么全手动操作"的二元对立。界面应既能给出建议（give advice），也能接受建议（take advice）——让用户和系统形成持续的"建议对话"。

## 二、结构分析
- 21.1 Introduction + 21.2 Examples（Letizia: Web浏览器给出建议; Mondrian: 图形编辑器接受建议）
- 21.3 Advice-Based Interfaces in AI and HCI（灵活规划/资源受限推理/Anytime算法/Critics/编程示范/上下文敏感）
- 21.4 Future of Advice-Oriented Interfaces（互联网应用/物理界面/语音手势界面/视觉传达设计建议/学习工具建议）
- 21.5 Conclusion

## 三、内容分析
### L002 核心论题
完全自动化的智能代理（"全能的代理做一切"）面临不可逾越的知识工程瓶颈——而"建议型界面"通过在"自动"和"手动"之间建立中间地带（系统建议+人类决策）提供了一条更实用的路径。

### L003 关键论点
1. **Letizia**（给出建议的Web浏览器）：在用户浏览时，Letizia在后台分析行为并推荐相关链接——建议是"被动的"（不打断用户），由用户决定是否采纳。
2. **Mondrian**（接受建议的图形编辑器）：用户通过"编程示范"（Programming by Example）向系统"教授"操作——系统从用户的演示中推断规则并泛化。
3. "Advice as a Tool for Helping People Learn" ——建议型界面不仅是效率工具，也是学习工具——用户通过评估和调整建议来深化对领域的理解。

### L004 原文摘录
> "Why is almost every kind of input by a human to a computer referred to as a 'command'?"（源文件 L12418）
> "I propose that a key idea in achieving this will be the development of computer interfaces based on the idea of advice."（源文件 L12423）【校对修正：原两处引文措辞与源文件不符，已替换为原文】

### L005 关键实体
- **人物**：Henry Lieberman
- **系统**：Letizia（Web浏览建议代理）; Mondrian（图形编辑示范学习系统）
- **概念**：Advice-Based Interfaces, Programming by Example, Anytime Algorithms, Critics, Resource-Limited Reasoning, Give Advice vs Take Advice

## 九、关联
- **Ch22 (Terveen/Hill/推荐系统)**：Ch21的"建议"= Ch22的"推荐"在概念层面的统一——都试图在"自动"和"手动"之间建立中间地带
- **Ch11 (Shneiderman/创造力)**：Genex的"Relate"（咨询同行/导师）可以被解释为"接受人类建议"——Ch21将其扩展到"接受系统建议"
- **Ch19 (多模态)**：多模态界面的"互消歧"机制是一种建议型交互——系统在不确定时提供候选解释
