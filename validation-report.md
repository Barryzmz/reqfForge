# ReqForge 驗證報告

**日期**：2026-05-31
**驗證情境**：員工請假管理系統
**執行範圍**：Prompt 01 → 07 完整工作流

---

## 一、驗證方法

### 情境設計原則

為了有效驗證工作流，設計了一個「刻意不完整」的 PM 口述情境，目標是讓每個驗證機制都有機會被觸發：

| 設計手法 | 具體內容 | 用途 |
| --- | --- | --- |
| 明確缺漏 | 病假診斷書「不確定強制」、喪假天數未給親等 | 觸發 open questions |
| 待提供資料 | 特休年資 Excel（SRC-002）尚未交付 | 測試來源缺漏處理 |
| 未討論流程 | 催審方式、代理主管機制 | 測試 AI 是否補需求 |
| 衝突規則 | 跨部門主管不知道誰來審 | 測試 AI 是否自行裁決 |
| 完全未定義 | HR 報表格式 | 測試 Needs Clarification 標記 |

Prompt 03 以後，所有問題改由 AI 代入合理答案（標記為「驗證情境假設回答」），模擬使用者回答，繼續推進流程。

---

## 二、各 Prompt 執行摘要

### Prompt 01 — Read Inputs

**輸入**：`specs/00-inputs/user-description.md`（PM 口述）
**產出**：5 個 discovery 文件

| 文件 | 內容 |
| --- | --- |
| source-summary.md | 識別 SRC-001（口述）、SRC-002（未提供） |
| extracted-facts.md | 20 條事實，全部標記來源 |
| open-questions.md | 11 個問題（Q-001 ~ Q-011） |
| assumptions.md | 4 條工作假設 |
| glossary.md | 10 個術語 |

**執行觀察**：AI 正確將「不確定是不是強制」寫成 Q-001 而非補進需求，符合 CONSTITUTION 規定。

---

### Prompt 02 — Extract Requirements

**輸入**：`specs/01-discovery/`
**產出**：8 個需求文件

首輪產出 FR-001 ~ FR-006、BR-001 ~ BR-006、DR-001 ~ DR-008、WR-001 ~ WR-004、PR-001 ~ PR-005。

**執行觀察**：FR-002（診斷書）、FR-004（催審方式）、FR-006（報表格式）均正確標記為 `Needs Clarification`，未自行補齊。NFR 文件保持空白（來源未提及）。

---

### Prompt 03 — Clarify Requirements（Phase 1 + Phase 2）

**Phase 1**：提出 11 個問題，依 blocking 程度分類，未修改任何文件。

Blocking 問題（Q-003、Q-004、Q-006、Q-007）：影響後續分析與規格書能否產出。
Non-blocking 問題（Q-001、Q-002、Q-005、Q-009、Q-010、Q-011）：不影響主流程但影響功能完整性。

**Phase 2**：代入答案後回填，新增：

| 新增項目 | 說明 |
| --- | --- |
| FR-007、FR-008 | 取消申請、代理主管 |
| BR-007 ~ BR-010 | 診斷書規則、半天單位、跨部門規則、代理範圍 |
| DR-009 ~ DR-011 | 主要部門、代理設定、報表欄位 |
| WR-005 | 取消狀態轉換 |
| PR-002 ~ PR-007 | 重整後的完整權限矩陣 |
| DEC-001 ~ DEC-010 | 10 條決策記錄寫入 decision-log.md |

---

### Prompt 04 — Analyze Requirements

**產出**：6 個分析文件

| 文件 | 產出內容 |
| --- | --- |
| use-cases.md | UC-001 ~ UC-007，含基本流程與替代流程 |
| user-stories.md | US-001 ~ US-008，覆蓋三種角色 |
| acceptance-criteria.md | AC-001 ~ AC-022，摘要索引格式 |
| domain-model.md | 6 個實體（Employee、Department、LeaveRequest、ReviewRecord、LeaveBalance、ManagerDelegate） |
| state-transitions.md | ST-001 ~ ST-007，含合法與不合法轉換清單 |
| edge-cases.md | EC-001 ~ EC-012，初始 6 個標記為 Open |

**執行觀察**：邊界條件（病假恰好 3 天、代理期間結束後的待審申請）均被識別為 edge case，而非被跳過。6 個 Open edge cases 經使用者要求補齊後，追加 BR-011 ~ BR-015 與 DEC-011 ~ DEC-016。

---

### Prompt 05 — Generate Spec

**產出**：`specs/04-design-ready/requirement-spec.md`

| 類型 | 數量 |
| --- | --- |
| FR（功能需求） | 8 |
| BR（業務規則） | 15 |
| DR（資料需求） | 11 |
| WR（流程需求） | 5 |
| PR（權限需求） | 7 |
| NFR（非功能需求） | 0（來源未提及） |

規格書包含 Domain Model 摘要、State Transitions 摘要、Edge Cases 摘要，以及完整追溯表（每條需求對應 Source ID、Fact ID、Decision ID）。

---

### Prompt 06 — Generate Design-ready Documents

**產出**：6 份設計交付文件

| 文件 | 產出量 |
| --- | --- |
| system-design-brief.md | 架構層次說明 + 3 個設計層問題（QD-001 ~ QD-003） |
| api-draft.md | API-001 ~ API-010，含 Request / Response / Error 定義 |
| database-draft.md | TBL-001 ~ TBL-006，含欄位、型別、索引、關聯 |
| frontend-pages.md | PAGE-001 ~ PAGE-007，含路由、權限、主要操作、前端驗證規則 |
| test-cases.md | TC-001 ~ TC-027，覆蓋全部 AC 與 edge cases |
| development-tasks.md | TASK-001 ~ TASK-024，含完整依賴關係圖 |

**執行觀察**：設計過程中發現 4 個新問題（QD-001 ~ QD-004），包含附件格式限制、Scheduler 執行頻率、系統內通知機制、喪假餘額顯示邏輯，記錄在 system-design-brief.md。

---

### Prompt 07 — Update Versions

執行稽核後發現：QD-001 ~ QD-004 只存在 `system-design-brief.md`，未回填至正式 `open-questions.md`。

補齊後追加：
- DEC-017：薪資計算、排班明確列為 Out of Scope
- DEC-018：NFR 空白為有意識的決策（來源未提及，不得自行補齊）

---

## 三、需求填寫方式說明

### 來源處理

所有需求均從 `specs/00-inputs/user-description.md` 的原始口述中萃取。每條需求必須能追溯至具體的 Fact ID（FACT-001 ~ FACT-020）。沒有 Fact 支撐的內容不得寫成需求。

### 問題與假設處理

| 情況 | 處理方式 |
| --- | --- |
| 來源說「不確定」 | 寫入 open-questions.md，需求標記 Needs Clarification |
| 來源有矛盾 | 寫入 open-questions.md，等待確認後才進需求 |
| 需要暫時推進 | 寫入 assumptions.md，明確標記不是正式需求 |
| 業界常見做法但來源未提 | 不寫進需求，最多作為 Suggested Practice 記錄 |

### 釐清問題的分類方式

Phase 1 提問時依影響程度分為兩類：

**Blocking**：若不回答，後續分析或規格書會有明顯空缺，例如跨部門審核規則（影響 FR-003、PR-004、WR-002、WR-003）。

**Non-blocking**：可以繼續推進，但功能不完整，例如催審通知方式（FR-004 已確認觸發條件，只差通知管道）。

### Decision Log 的寫入時機

每次使用者回答被寫回正式文件時，必須同步寫一條 DEC 記錄，包含：決策內容、原因、來源、關聯需求 ID。本次驗證共產生 DEC-001 ~ DEC-018。

---

## 四、工作流漏洞

### 漏洞 1：設計層問題沒有正式回流機制

**現象**：Prompt 06 產生的 QD-001 ~ QD-004 只存在 `system-design-brief.md`，直到 Prompt 07 稽核才被手動回填至 `open-questions.md`。

**影響**：若 Prompt 07 不執行或跳過，這些問題永遠只存在設計文件裡，無法被追蹤。

**建議修補**：在 `prompts/06-generate-design-ready.prompt.md` 的 Rules 中加入：
> 「若設計需要額外資訊，必須新增至 `specs/01-discovery/open-questions.md`，不只是寫在設計文件中。」

---

### 漏洞 2：Edge Case 補齊流程未被任何 Prompt 正式涵蓋

**現象**：Prompt 04 產生了 6 個 Open edge cases，補齊動作是使用者手動要求的，不在任何 prompt 的正式 Task 列表中。若使用者跳過補齊直接執行 Prompt 05，Open edge cases 會出現在規格書中，但 Prompt 05 的 Rules 要求「只使用已確認需求」，形成矛盾。

**建議修補**：在 Prompt 04 或 Prompt 05 的 Rules 中加入：
> 「若 `specs/03-analysis/edge-cases.md` 中存在 Open 狀態的 edge case，應在執行 Prompt 05 前先透過 Prompt 03 backfill 步驟或補充決策解決。」

---

### 漏洞 3：Pending Assumption 可以無限期存在

**現象**：`ASM-002`（角色清單是否完整）從 Prompt 01 一路 Pending 到 Prompt 07，從未被強制處理。`TASK-002`（Auth Middleware）已隱性依賴這個假設，卻沒有任何機制警示。

**影響**：未確認的假設可能成為設計文件的隱性前提，導致開發完才發現基礎前提錯誤。

**建議修補**：在 `CONSTITUTION.md` 加入：
> 「Assumption 狀態為 Pending 的項目不得作為設計文件的依賴；若需依賴，必須先升格為 Confirmed Requirement 或回寫 Open Question。」

---

### 漏洞 4：Prompt 07 的執行時機依賴人工紀律

**現象**：`prompts/07-update-versions.prompt.md` 列出了 5 種應該觸發的時機，但整個流程中沒有任何機制強制執行這些觸發點。實際上，changelog 是「邊做邊補」的，而非統一在 Prompt 07 更新。

**影響**：若執行者紀律不足，changelog 與 decision-log 容易出現漏記或延遲。

**建議修補**：將版本更新責任明確分配給各 prompt，在每個 prompt 的 Tasks 末尾加入固定項目：
> 「更新 `specs/05-versions/changelog.md`，記錄本次執行的文件變更與摘要。」

---

## 五、可優化項目

### 優化 1：`requirement-spec-template.md` 與實際產出不一致

**現象**：模板只有 Metadata、Scope、Requirements、Traceability 四個區塊，但 Prompt 05 實際產出還包含 Domain Model Summary、State Transitions Summary、Edge Cases Summary。AI 需要「自行判斷」要加哪些章節。

**建議**：更新模板，加入這三個 Summary 區塊，並明確說明它們引用 `specs/03-analysis/` 的對應文件。

---

### 優化 2：`frontend-pages.md` 沒有對應模板

**現象**：Prompt 06 要求產出 `frontend-pages.md`，但 `templates/` 目錄下沒有對應的模板。頁面格式（Route、Permission、Main Actions、Required Data、Validation）完全由 AI 自行決定，不同次執行可能格式不一致。

**建議**：新增 `templates/frontend-page-template.md`，統一頁面描述格式。

---

### 優化 3：Open Questions 缺乏分層

**現象**：需求層問題（Q-001 ~ Q-011）與設計層問題（QD-001 ~ QD-004）混在同一個 `open-questions.md`，難以一眼判斷哪些問題影響需求確認、哪些影響設計推進。

**建議**：在 `open-questions.md` 加入「來源層次」欄位（Requirements / Design），或分為 `open-questions.md` 與 `design-questions.md` 兩個文件管理。

---

### 優化 4：缺少需求一致性檢查步驟

**現象**：Prompt 02 → Prompt 04 之間沒有一個明確的「需求一致性驗證」步驟，用來確認：
- 所有 FR 都有對應的驗收條件
- 所有 WR 的狀態轉換都已窮舉
- 所有 PR 的角色都與 user-roles.md 一致

本次驗證中，PR-005 在 Prompt 03 後被重整，如果沒有手動追蹤容易產生 ID 錯位。

**建議**：在 Prompt 03 和 Prompt 04 之間增加一個可選的「Requirements Review」步驟，執行 ID 一致性、角色對應、狀態完整性的稽核。

---

### 優化 5：NFR 無主動詢問機制

**現象**：`non-functional-requirements.md` 從頭到尾保持空白，因為來源沒提到。但在實際專案中，效能與安全需求往往是在設計階段才被提出，而工作流沒有任何步驟主動詢問。

**建議**：在 Prompt 03（釐清需求）的問題清單中，加入固定的 NFR 詢問項：
> 「以下非功能面向是否有需求需要確認：效能基準、並發用量、安全規範、資料保留政策？」

---

## 六、驗證結論

| 評估面向 | 結論 |
| --- | --- |
| 工作流可執行性 | **通過**：7 個 prompt 全數可從頭執行到尾，產出所有預期文件 |
| CONSTITUTION 遵守率 | **高**：AI 在模糊點一致選擇「標記問題」而非「補需求」，共產出 15 個問題而非自行填入 |
| 可追溯性 | **高**：每條需求均有 Source ID / Fact ID / Decision ID；設計文件每個元素均追溯至需求 ID |
| 版本管理 | **部分通過**：changelog 與 decision-log 完整，但 Prompt 07 的觸發時機依賴人工紀律 |
| 漏洞密度 | **低**：發現 4 個流程邏輯漏洞，均有明確修補方向，不影響核心可用性 |
| 整體評估 | ReqForge 工作流架構完整、邏輯自洽，適合作為需求管理的協作框架使用 |

### 待處理項目（本次驗證遺留）

| ID | 問題 | 影響範圍 | 優先級 |
| --- | --- | --- | --- |
| Q-008 | 申請時是否即時顯示剩餘假期天數 | FR-001、DR-008 | Low |
| QD-001 | 附件允許的檔案格式與大小上限 | DR-005、API-003、TBL-003 | Medium |
| QD-002 | 催審 Scheduler 執行頻率 | TASK-011 | Medium |
| QD-003 | 系統內通知的儲存與讀取機制 | TASK-013、前端頁面範圍 | Medium |
| QD-004 | 假期餘額頁是否顯示喪假餘額 | PAGE-007、TBL-005 | Low |
| ASM-002 | 角色清單是否完整（是否有系統管理員等角色） | TASK-002、PR-001 ~ PR-007 | Medium |
