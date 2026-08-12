# Ch12 分析报告：Interaction Spaces for Twenty-First-Century Computing

**作者**：Terry Winograd（斯坦福大学）
**所属 Part**：Part III — User Interface Software and Tools
**在书中位置**：第259–277页

---

## 一、章节定位与功能
### L001
Winograd提出"交互空间"（Interaction Spaces）作为21世纪计算的整合性架构模型——在设备/程序/现象之间建立松散的动态耦合，取代传统的"一个用户+一个计算机+一个应用"的刚性界面模型。

## 二、结构分析
- 12.1 Introduction + Scenario（斯坦福 iRoom 场景）
- 12.2 Architecture Models（设备-程序解耦 + 设备-现象解耦）
- 12.3 Robust Dynamic Configuration and Communication
- 12.4 Context-Based Interpretation
- 12.5 Action and Perception（三个例子：iRoom, Interactive Habitat, Classroom 2000）
- 12.6 Research Issues（以人为中心的交互/不完全信息的有效处理/可变质量保证响应/多人多设备/标准模型）
- 12.7 Conclusion

## 三、内容分析
### L002 核心论题
传统计算将设备、程序、界面三者固定绑定——未来需要"交互空间"范式：多种设备动态发现和配置、程序在空间层面运行、交互对物理环境和社会情境做出响应。

### L003 关键论点
1. "Decoupling Devices from Programs" —— 设备不是程序的附属品，而是可与任何程序动态关联。
2. "Decoupling Devices from Phenomena" —— 计算机与物理现象之间的映射应该是动态可配置的，而非硬编码。
3. "Context-Based Interpretation" —— 交互含义不仅取决于输入，还取决于周围环境的状态（谁在场、在做什么、之前的交互历史）。

### L004 原文摘录
> "Computing environments of the late twentieth century have been dominated by a standard desktop/laptop configuration."（源文件 L7154）
> "The problem in trying to support the programming of our interactive workspace scenario is not just one of writing more drivers and APIs."（源文件 L7234）【校对修正：原两处引文为改写，已替换为原文】

### L005 关键实体
- **人物**：Winograd; Phil Agre; Paul Dourish
- **系统**：Stanford iRoom, Interactive Habitat, Classroom 2000
- **概念**：Interaction Spaces, Device-Program Decoupling, Device-Phenomenon Decoupling, Context-Based Interpretation

## 九、关联
- **Ch10 (Myers)** 提供了Winograd愿景的工具历史背景
- **Ch25 (Streitz/Roomware)** 是"交互空间"在物理建筑层面的具体实现
- **Ch23 (Abowd/Ubicomp)** 的"上下文感知计算"直接承袭Winograd的Context-Based Interpretation
