# 07_实体与关系网络

## 目录用途

本目录建立教材涉及的人物、机构、企业、学校、展览、对象、出版物及传播关系网络。实体网络服务于跨章对象去重（同一实体在不同章节出现时只计一份P0）与教材叙事组织（人物谱系、制度链条、传播路径）。

## 实体类型

| 类型 | 说明 | 示例 |
|---|---|---|
| person | 人物（设计师、理论家、组织者、行动者） | Henry Dreyfuss、杭间 |
| institution | 机构（协会、委员会、政府部门） | SID、CoID、MITI |
| enterprise | 企业 | AEG、Braun、商务印书馆 |
| school | 学校／教育机构 | 包豪斯、乌尔姆、北京美术学校 |
| exhibition | 展览／博览会 | 1851年博览会、1925年巴黎博览会、MoMA Good Design展 |
| object | 对象（产品、图像、档案、建筑） | 红蓝椅、月份牌、Joe/Josephine百分位图 |
| publication | 出版物（期刊、书籍、宣言） | 《De Stijl》期刊、Fortune 1934、未来主义宣言 |

## 关系类型

| 类型 | 含义 | 证据要求 |
|---|---|---|
| founded／co-founded | 创建／共同创建 | 需机构档案或行动者文本（标注单方自述） |
| directed／taught／studied | 领导／任教／求学 | 学校档案或行动者自述 |
| designed／produced | 设计／生产 | 对象证据（图版、档案、实物） |
| exhibited／displayed | 展出／陈列 | 展览目录或档案 |
| published | 出版 | 版权页、书目记录 |
| commissioned | 委托 | 合同、企业记录 |
| influenced／transmitted | 影响／传播 | 必须有接触、课程、出版、委托等中介证据；风格相似≠影响 |
| shared_object | 共享对象（去重组） | 同一档案／对象／文本跨来源出现 |

## 规则

1. **去重锚点**：同一实体全库只计一个ID（跨章节共享）；共享对象组见各章去重总表。
2. **因果克制**：influenced／transmitted 关系必须有可追踪中介；无中介时降级为 shared_object 或相似性标注。
3. **行动者自述**：person 的行为（如 Dreyfuss"帮助组织"SID）须在 relation 的 note 中标注单方自述属性。
4. **文件组织**：每章一个 JSON（`CH00_实体网络.json` … `CH99_实体网络.json`），含 `entities` 与 `relations` 两个数组；全库索引可另建 `实体总表.csv`。

## 生成与核验

- 首批实体网络从各章矩阵 A 级来源与来源卡 `original_spot_checks` 提取（V2）。
- 关系升级为因果须返回 P0 档案核验；当前全部关系为 V2 导航级。
