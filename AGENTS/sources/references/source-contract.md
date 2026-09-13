# 来源登记契约

执行数据任务时以 `01-基础文献/references.md` 保存逐条登记，复用已确认的等价索引也可，但字段含义不变。原文 MD 沿用 books、papers 子目录。使用 Markdown 表格或条目，不编写生成程序，不另建根级 sources 目录。

| 字段 | 要求 |
| --- | --- |
| ref_id | 稳定文献编号；优先沿用现行清单编号，不按处理批次重排 |
| bibliography_entry | 清单原条目；格式整理采用用户指定的 GB/T 7714—2015，不捏造缺失元数据 |
| bibliography_locator | 清单真实路径、版本及条目定位；未找到则 null 并标明待对齐 |
| work_id / edition_id | 可确认时标识著作与版本；同著作不同译本不自动当独立证据 |
| md_sources | 文件列表，每项有仓库相对路径、SHA-256、完整性状态及与原著的对应说明 |
| pdf_status | local_unavailable / accessible / unknown；不可访问不代表不存在 |
| pdf_locator | 仅使用实际确认的定位；缺失为 null，不写示例路径 |
| match_status | confirmed / candidate / ambiguous / missing_md |
| issues | 缺损、版本、卷册、重复和待核的具体问题 |

原文拆成多个 MD 时同一 ref_id 关联多个路径，不冒充多篇独立文献。
登记文件和 MD 版本变化后，下游记录按来源版本复核。
登记所有清单条目，包括缺源条目；清单之外的 MD 单列待对齐，不纳入已确认覆盖率。
