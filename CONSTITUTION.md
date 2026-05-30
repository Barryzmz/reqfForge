# ReqForge Constitution

本文件定義 ReqForge 專案中 AI、PM、開發者與其他協作者共同遵守的需求工作原則。

## Workflow Step vs Artifact Layer

`prompts/` 中的編號代表 workflow step，也就是 AI 執行工作的建議順序。

`specs/` 中的編號代表 artifact layer，也就是文件成熟度、責任邊界與用途。

prompt 編號與 specs 資料夾編號不要求一對一對應。單一 prompt 可以讀取或更新多個 artifact layers，但必須明確列出 input files、output files 與 rules。

若某個 prompt 會回填較早階段的文件，例如釐清問題後更新 discovery、requirements 或 decision log，該 prompt 必須明確說明這是 backfill clarification，而不是產生新的未確認需求。

## 1. 不得自行腦補需求

AI 只能整理、歸納與轉換已提供的資訊。若資訊不足，不得把推測內容寫成已確認需求。

## 2. 禁止常識補完

AI 不得因為某功能是業界常見做法、一般系統常見流程或模型認為合理，就將其寫成已確認需求。

例如 Email 通知、附件上傳、審核歷程、權限控管、匯出報表、狀態追蹤等常見能力，只有在來源文件、`specs/00-inputs/user-description.md` 或使用者釐清回答明確確認時，才可以進入正式需求。

常見做法可以作為 Suggested Practice、Assumption 或 Open Question 記錄，但不得直接進入 `specs/02-requirements/` 或任何正式需求文件。

## 3. 區分確認需求、建議做法、假設與待釐清問題

AI 必須明確區分下列狀態：

- Confirmed Requirement：有來源文件、使用者描述或使用者釐清回答明確支持的需求。
- Suggested Practice：AI 基於經驗提出的建議做法，尚未被確認，不得寫成正式需求。
- Assumption：為了暫時推進分析而建立的假設，必須明確標示，且不得直接升級為正式需求。
- Open Question：需要使用者、PM 或利害關係人回答後才能判斷的問題。

即使 AI 模型傾向補齊常見業務流程，也必須優先保守處理。若不確定，應提出問題或標示假設，而不是補上需求。

## 4. 不確定內容必須進入 open questions

所有不明確、矛盾、缺漏或需要利害關係人確認的內容，必須記錄於：

`specs/01-discovery/open-questions.md`

每個問題應包含：

- 問題編號
- 相關來源
- 影響範圍
- 建議詢問對象
- 狀態

## 5. 假設必須明確標記

任何暫時性推測、工作假設或為了繼續分析而建立的前提，必須記錄於：

`specs/01-discovery/assumptions.md`

假設不得直接升級為正式需求。假設只有在被確認後，才可以轉入 `specs/02-requirements/`。

## 6. 正式需求只接受已確認內容

`specs/02-requirements/` 中的內容必須是已確認需求。每個需求都應包含：

- 需求編號
- 需求描述
- 來源
- 狀態
- 驗收或判斷方式

## 7. 設計文件只能根據已確認需求產生

`specs/04-design-ready/` 中的文件不得引用未確認需求、未確認假設或未回答問題作為設計依據。

若設計所需資訊不足，應新增 open question，而不是補上設計細節。

## 8. 可追溯性優先

每個需求、規則、資料欄位、流程與權限都應盡量標記來源。來源可以是：

- 使用者描述
- 會議紀錄
- 文件檔名與頁碼
- 表格名稱與列號
- 訪談對象
- 已確認決策

## 9. 文件格式

所有文件必須使用 Markdown。表格、清單、標題與程式碼區塊應保持一致格式，方便版本控制與審查。

## 10. 需求編號規範

需求編號格式如下：

- `FR-001`：功能需求
- `BR-001`：商業規則
- `DR-001`：資料需求
- `WR-001`：流程需求
- `PR-001`：權限需求
- `NFR-001`：非功能需求

編號一旦發布不得重複使用。若需求被移除，應在 changelog 或 decision log 中記錄。
