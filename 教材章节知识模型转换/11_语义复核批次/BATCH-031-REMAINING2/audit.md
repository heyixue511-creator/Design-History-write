# BATCH-031-REMAINING2 语义复核审计

- 批次：BATCH-031-REMAINING2
- 状态：complete（12/12）
- 方向：设计史奠基文本与剩余资产（室内设计史/世界设计史卷二/俄国先锋/设计认知/广告批判/Eames/Gray/冷战设计/全球设计史方法）

## 本批来源与映射

| source_id | 文献 | 映射（section:grade） | 体裁/等级约束 |
|---|---|---|---|
| B0223 | Pile & Gura《A History of Interior Design》4th ed. | C.0:C / 2.5:C / 11.1:C | 室内设计通史 |
| B0433 | Margolin《World History of Design》Vol.2 (1900-1945) | C.0:A / 3.4:C / 8.3:C | 世界设计史卷二 |
| B0095 | Dabrowski《Revolution: Russian Avant-Garde 1912-1930》(MoMA馆刊) | 3.4:C / 3.7:C | 展览文章→限C |
| B0088 | Cooke《Architectural Drawings of the Russian Avant-Garde》 | 3.4:C / 3.7:C | 展览图录→限C |
| B0271 | Lawson《How Designers Think》 | C.0:B / 0.1:C / 13.4:C | 设计认知经典 |
| B0308 | Polanyi《The Tacit Dimension》 | C.0:B / 0.1:C / 16.5:C | 默会认知经典 |
| B0430 | Packard《The Hidden Persuaders》 | 9.1:B / 9.1:C / 13.2:C | 消费批判经典 |
| B0335 | Kirkham《Charles and Ray Eames》 | 7.3:B / 9.3:B / 14.1:C | Eames学术专著 |
| B0354 | Pevsner《Pioneers of Modern Design》 | C.0:A / 2.7:C / 11.1:C | 现代设计史奠基 |
| B0004 | Adam《Eileen Gray: Architect, Designer》 | 9.3:B / 5.1:C / 11.1:C | 人物传记 |
| P0044 | Golec 书评（V&A《Cold War Modern》三卷） | 8.3:B / 9.1:C | 书评→限B |
| P0016 | Čapková 书评（Kirkham/Weber《History of Design》） | C.0:B / 3.7:C | 书评→限B |

合计：12 来源 / 32 映射行（A2 / B8 / C22）——全部 V2。

## 关键决策

1. **B0354 Pevsner 定为 C.0 A**：现代设计史奠基文本——'从莫里斯到格罗皮乌斯是一个历史单元'叙事范式（Pevsner范式），与 Giedion/Hitchcock-Johnson 构成正统谱系，同时也是女性主义/后殖民/后现代史学的批判对象。
2. **B0433 Margolin 卷二定为 C.0 A**：与卷三（B0288）同级——马格林世界史体系独立条目，承担 1900-1945 全球多中心设计史实证。
3. **B0263（Fallan 重条）去重跳过**：与已复核 B0152（同书《Design History: Understanding Theory and Method》）重复，按惯例不入批。
4. **等级约束执行**：展览文章/图录（B0095/B0088）限 C；书评（P0044/P0016）限 B；传记（B0004）按 9.3 B 处理。
5. **P0044 文件名含拼接**（'...Posters of the Cold War'）——实际为 Golec 书评评 V&A 三卷本（含《Posters of the Cold War》），非多书拼接，按单一来源处理。

## 聚合与矩阵结果

- 聚合索引：2358 映射行 / 378/589 来源（64.18%）/ 121 小节；A697 B940 C666 D18 X37；全部 V2
- CH99 C.0：79 → 85（+B0354 A、B0433 A、B0271 B、B0308 B、P0016 B、B0223 C）
- CH03：3.4 +2（B0433/B0088）、3.7 +2（B0095/B0088）
- CH09：9.1 +2（B0430）、9.3 +2（B0335/B0004）
- CH11：11.1 +3（B0223/B0004/B0354）
- CH02：2.7 → 56（+B0354）
- CH05 5.1 +1（B0004）、CH07 7.3 +1（B0335）、CH08 8.3 +2（B0433/P0044）、CH13 13.2 +1（B0430）/13.4 +1（B0271）、CH14 14.1 +1（B0335）、CH16 16.5 +1（B0308）、CH00 0.1 +2（B0271/B0308）

## 待办（不阻塞本批）

- CH03 矩阵使用旧版结构缓存（本次 BATCH-031 由 _agg_ch03_structure.py 实时读取批次后重建，已含本批新增；CH06/CH08 结构缓存未重算——本批无 6.x/8.x 新增小节结构变化，8.3 仅追加来源已生效）
- 剩余未复核约 211 来源（含中文书 B0466/B0484/B0490/B0496/B0502 等编码待解析条目）
