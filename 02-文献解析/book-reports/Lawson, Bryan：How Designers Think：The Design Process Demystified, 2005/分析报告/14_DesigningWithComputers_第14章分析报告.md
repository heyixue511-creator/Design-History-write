# 14 第14章分析報告：Designing with Computers（與計算機共同設計）

## 一、章節定位與功能

### L001 在全書結構中的位置
本章是全書的終章（第14章之後直接為BIBLIOGRAPHY（L3171）與Index（L3465），源文件無後記章節），承擔雙重功能：既是對計算機輔助設計這一新興領域的全面介紹，也是對全書所有主題在「人機關係」這一新語境中的重新審視。它將第1章的「設計作為技能」、第6章的約束模型、第8章的信息加工理論和第13章的群體合作主題整合進一個關於人機合作的綜合性討論。

### L002 核心功能
1. **歷史功能**：記錄CAD從1960年代到1980年代末的發展歷程
2. **分類功能**：將計算機在設計中的角色分為四類——管理、信息處理、解決方案評估、解決方案生成
3. **預測功能**：基於第五代計算機和人工智能的發展趨勢，推測未來的設計實踐
4. **反思功能**：在全書結尾提供方法論反思和未來研究方向

## 二、結構分析

### L003 章節內部結構
本章包含十二個主要段落（源文件自L2719至L3077共有12個`##`小節；原報告稱「九個」與所列12項不符，已更正）：
1. **Why use computers in design at all?**（為什麼要在設計中使用計算機？）
2. **An historical perspective**（歷史視角）
3. **Computers as machines**（計算機作為機器）
4. **The information revolution**（信息革命）
5. **The computer in the design office**（設計事務所中的計算機）——四種角色
6. **Early attempts at solution generation**（早期解決方案生成嘗試）
7. **Early solution evaluation ideas**（早期解決方案評估想法）
8. **Ad hoc or integrated systems?**（即時系統還是集成系統？）
9. **Computer models**（計算機模型）
10. **The problem of the interface**（界面問題）
11. **The metaphor of the interface**（界面隱喻）
12. **Designer and computer**（設計師與計算機）

## 三、內容分析（核心論題＋關鍵論點案例）

### L005 核心論題
**計算機不應被理解為設計過程的自動化替代者，而應被理解為具有特定優勢和劣勢的「合作夥伴」。** 關鍵問題不是計算機是否能夠設計（它們不能，至少在設計的完整意義上不能），而是人類設計師和計算機如何能夠形成一種生產性的共生關係——一種利用各自優勢並彌補各自局限的關係。

### L006 關鍵論點與案例

**論點1：計算機在設計中的四種角色（Lawson, 1981）**
- **管理角色**：支持事務所運營（電子郵件、日記、工資單、文字處理）——不直接影響設計過程
- **信息處理角色**：保存和複製數據（圖紙、文檔）——自動化繪圖和文檔生產
- **解決方案評估角色**：對設計提案進行建模並生成評估輸出——三維建模軟件
- **解決方案生成角色**：實際建議部分或全部設計解決方案——最具爭議性但最有潛力

**論點2：早期解決方案生成的局限**
- **Boyd Auger的BAID1程序**：使用隨機生成和標準測試來排列住宅佈局——滿足隱私、日光和日照的蘇格蘭建築法規
- **Whitehead & Eldars (1964)的程序**：根據最小化人流距離來規劃建築佈局——以醫院手術室套間為例
- **三個主要批評**：
  （1）不保證最優解——Cross (1977)證明人類設計師能夠產生比程序更好的解決方案（雖然人類的平均表現低於計算機）
  （2）輸入數據的虛假精確性——建築物使用模式的預測遠不如程序所要求的那樣精確
  （3）程序只處理了一個約束子集（人流），而忽略了所有其他約束——"The crux of this difficulty is that the computer has removed just one set of internal client/user generated set of constraints"

**論點3：ABACUS的解決方案評估方法——人機角色的逆轉**
- **SPACES程序套件**：從時間表數據生成氣泡圖——用戶可以交互式地移動和重塑氣泡
- **GOAL和PARTIAL程序**：提供多種性能反饋（流通效率、資本成本、能源消耗）
- **Robert Aish (1977)的實驗**：幼兒園校長（無建築設計或計算機經驗）使用這些程序設計了80人幼兒園——其他教師評判這些設計更令人滿意地解釋了用戶需求
- 關鍵逆轉：計算機不再主導過程；人類設計師主導，計算機提供反饋

**論點4：即時系統vs.集成系統**
- **即時（ad hoc）方法**：為特定評估研究運行單獨的程序——每個程序需要自己的數據輸入
- **集成方法**：首先向計算機全面描述設計，然後運行任意程序——一次描述，多次使用
- 集成方法的優勢：計算機接管測量和計算的角色——"each individual evaluation study makes virtually no demands on the designer other than initiating the appropriate program"
- **GABLE項目**（謝菲爾德大學，Lawson指導）：通過「閱讀」建築平面圖來自動構建建築模型——計算機自動構建每個內部空間的模型和外部皮膚

**論點5：Fitts List——人機能力對比**
- 計算機的特徵：快速、精確、一致、可靠、不知疲倦、不厭倦
- 人類的特徵：靈活、富有想像力、擅長歸納推理、能夠做出平衡的綜合判斷
- 人類的劣勢：緩慢、易出錯、不一致、會厭倦、會感覺不適
- 計算機的劣勢：僵化、缺乏想像力、編程繁瑣、可能無預警地災難性失敗
- 設計系統的目標：結合二者的優勢

**論點6：界面隱喻——架起人機鴻溝**
- Van Norman (1986)的四個條件：隱喻的物理任務必須接近程序輔助的任務；用戶應已具備物理任務的專業知識；隱喻應該能夠貫穿整個程序；隱喻應能在沒有物理對應物的情況下被延伸
- 建築繪圖系統：依賴傳統繪圖板的隱喻（圖層、T尺、三角板）
- 圖形設計：依賴繪畫的隱喻（顏料盒、畫筆、噴槍）
- 工程設計：依賴零件裝配的隱喻
- 所有這些現有隱喻都不完全適合建築設計的三維模型需求
- **樂觀的展望**：伴隨計算機長大的一代可能不需要物理隱喻——"youngsters who have grown up using computers as toys find the ideas of computer models and transformation quite natural without the need of physical metaphors"

## 四、邏輯梳理（論證鏈條＋因果轉折）

### L007 主要論證鏈條

```
為什麼要在設計中使用計算機？（問題提出）
    ↓
懷疑態度（Cross的批評）vs.樂觀態度（Negroponte的願景）
    ↓ （歷史視角）
計算機從第一代到第五代的演變
    ↓ （技術分析）
並行處理、VLSI、聲明式語言→新的可能性
    ↓ （角色分類）
四種角色：管理→信息處理→評估→生成
    ↓ （經驗回顧）
早期生成嘗試的失敗：程序主導，人類被動
    ↓ （逆轉）
ABACUS方法：人類主導，計算機提供反饋
    ↓ （技術挑戰）
即時vs.集成系統、幾何建模、界面設計
    ↓ （人機關係）
Fitts List→設計最優的人機合作
    ↓ （開放性結論）
計算機不會替代設計師，但將改變設計過程
```

## 五、材料使用方式

### L009 材料類型與策略
1. **技術史敘事**：計算機從第一代到第五代的演變——清晰的技術教育
2. **CAD系統案例研究**：BAID1、Whitehead & Eldars、SPACES、GOAL、GABLE——詳細的功能描述和批判性評估
3. **心理學理論**：Fitts的人類績效理論——為人機角色分配提供框架
4. **自我引用**：Lawson自身在GABLE項目的工作——建立作者在該領域的專業權威
5. **未來學論述**：Negroponte、第五代計算機項目——引入思辨性維度

## 六、論辯與闡述方法

### L010 主要論辯策略
1. **技術教育**：以非專業讀者能理解的方式解釋計算機硬件和軟件——從晶體管到VLSI，從FORTRAN到PROLOG
2. **平衡呈現**：公平地展示Cross的批評（計算機本質上有害於設計過程）和Negroponte的願景（人機共生），然後提出自己的中間立場
3. **案例分析**：對特定CAD系統的詳細描述和批判——既展示成就也揭示局限
4. **角色框架**：四種角色的分類為討論提供了清晰的結構

## 七、語言文風（原文摘錄＋L###）

### L011 原文摘錄

> "The change from thinking about machine design to thinking about systems design is not a gradual evolution but a discontinuity." —— W. T. Singleton（章首引文）

> "In 1968 one could read all existing literature in English on the subject of 'artificial intelligence' within one month. Now it takes about six months." —— Nicholas Negroponte (1975)（章首引文，信息爆炸的生動度量）

> "my interest is simply to preface and encourage a machine intelligence that stimulates a design for the good life and will allow for a full set of self-improving methods. We are talking about a symbiosis that is a cohabitation of two intelligent species." —— Nicholas Negroponte (1970)（L013，技術樂觀主義的極致表達）

> "The reality that lies behind the dramatist's simple image and the advertiser's hype is much more prosaic."（L013）【校对修正：此句實際出自源文件L2473（第13章，討論設計的社會性與群體工作），不屬第14章，特此更正出處】

> "Whilst computer aided design remains shrouded by so many unanswered questions there seems little doubt that work will continue."（L020）

## 八、實體清單（六類每類≥3＋L###）

### L012 一、人物與學者
| 實體 | 身份 | 關鍵貢獻 |
|------|------|----------|
| Nicholas Negroponte | MIT教授 | The Architecture Machine, Soft Architecture Machines |
| Nigel Cross | 設計研究者 | The Automated Architect——對CAD的批判 |
| Tom Maver | CAD先驅 | ABACUS單元（Strathclyde大學） |
| Boyd Auger | 建築師/CAD研究者 | BAID1程序 |
| Robert Aish | CAD研究者 | 用戶參與CAD實驗 |
| John Lansdown | CAD研究者 | 即時vs.集成系統的區分 |
| Paul Fitts | 心理學家 | Fitts List——人機能力對比 |
| W. T. Singleton | 人因工程學家 | Man-Machine Systems |
| Donald Hoey | CAD研究者 | 基於知識的建築批評系統 |
| Mark Van Norman | CAD研究者 | 界面隱喻理論 |
| Alan Turing | 計算機先驅 | 人工智能的哲學基礎 |

### L013 二、機構與組織
| 實體 | 性質 |
|------|------|
| ABACUS (Strathclyde University) | CAD研究單元 |
| GABLE (Sheffield University) | CAD研究單元 |
| MIT (Massachusetts Institute of Technology) | 研究型大學 |
| Building Research Establishment | 建築研究機構 |
| Oxford Regional Hospital Board (OXSYS) | 醫療建築CAD |
| Government Property Services Agency (CEDAR) | 政府建築CAD |

### L014 三、概念與術語
| 實體 | 定義 |
|------|------|
| four roles of CAD | 管理/信息處理/解決方案評估/解決方案生成 |
| ad hoc vs. integrated systems | 即時系統vs.集成系統 |
| declarative vs. procedural languages | 聲明式vs.程序式語言（PROLOG/LISP vs. FORTRAN/BASIC） |
| expert systems | 專家系統——基於知識庫和推理引擎 |
| Fitts List | 人機能力對比清單 |
| interface metaphor | 界面隱喻——架起人機互動的心理橋樑 |
| parallel processing | 並行處理——第五代計算機的核心特徵 |
| VLSI (Very Large Scale Integration) | 超大規模集成電路 |
| solution generation role | 解決方案生成角色——最具爭議性的CAD角色 |
| solution evaluation role | 解決方案評估角色——當前最成功的CAD角色 |
| fifth generation computer | 第五代計算機——理解自然語言和圖形的知識處理機 |
| number trap | 數字陷阱——CAD可能強化的設計陷阱 |

### L015 四、著作與文獻
| 實體 | 作者 | 年份 |
|------|------|------|
| The Architecture Machine | Nicholas Negroponte | 1970 |
| Soft Architecture Machines | Nicholas Negroponte | 1975 |
| The Automated Architect | Nigel Cross | 1977 |
| The Architect and the Computer | Boyd Auger | 1972 |
| Man-Machine Systems | W. T. Singleton | 1974 |
| Human Performance | Fitts & Posner | 1967 |
| Expert Systems: their Impact on the Construction Industry | John Lansdown | 1982 |

### L016 五、案例與設計作品
| 實體 | 類型 | CAD角色 |
|------|------|----------|
| Isla Dino佈局（BAID1） | 計算機生成 | 解決方案生成 |
| 醫院手術室套間（Whitehead & Eldars） | 計算機生成 | 解決方案生成 |
| 80人幼兒園（Aish的實驗） | 人機合作 | 解決方案評估+用戶參與 |
| GABLE學生項目（購物中心、網球中心、電影院） | 人機合作 | 集成系統——視覺評估 |
| El Lissitzky風格建築批評（Hoey的專家系統） | 計算機生成 | 知識基礎——建築批評 |

### L017 六、實驗與研究
| 實體 | 研究者 | 年份 |
|------|--------|------|
| 用戶參與CAD實驗（幼兒園設計） | Robert Aish | 1977 |
| ISAAC：從平面圖自動解釋空間 | Lawson & Riley | 1982 |
| RODIN：三維屋頂形式建模 | Riley & Lawson | 1982 |
| 基於知識的建築批評系統 | Donald Hoey | 1987 |
| 繪圖協調失敗研究 | Crawshaw (BRE) | 1976 |

## 九、與前後章關聯

### L018 與前章（第13章）的關聯
- 第13章討論了人類群體合作——第14章將合作的概念擴展到人機之間
- 第13章的角色概念（領導者、小丑、律師）在第14章被轉化為人機角色分配的問題
- Fitts List（第14章）提供了對人類和機器能力的系統性對比——這為理解第13章中人類獨特的群體動力學提供了對照

### L019 全書結尾的關聯【校对修正：原標題為「與後記『Only Connect』的關聯」，但源文件無後記章節，已改寫】
- 本章以開放性問題結束——"Whether the apparent advantages of computer aided design will materialise or remain a mirage is as yet unclear"（源文件L3118）
- 全書在第14章末（L3168）以「Perhaps we should hope never fully to understand the way designers think…」的反思性陳述收束，並直接進入BIBLIOGRAPHY（L3171）
- 本章對第五代計算機和人工智能的討論為全書結尾對設計研究未來方向的展望提供了具體的技術語境
