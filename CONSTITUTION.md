# ReqForge Constitution

本文件定義 ReqForge 專案中 AI、PM、開發者與其他協作者共同遵守的需求工作原則。

## Workflow Step vs Artifact Layer

`prompts/` 中的編號代表 workflow step，也就是 AI 執行工作的建議順序。

`specs/` 中的編號代表 artifact layer，也就是文件成熟度、責任邊界與用途。

prompt 編號與 specs 資料夾編號不要求一對一對應。單一 prompt 可以讀取或更新多個 artifact layers，但必須明確列出 input files、output files 與 rules。

若某個 prompt 會回填較早階段的文件，例如釐清問題後更新 discovery、requirements 或 decision log，該 prompt 必須明確說明這是 backfill clarification，而不是產生新的未確認需求。

## 1. 不得自行腦補需求

AI 只能整理、歸納與轉換已提供的資訊。若資訊不足，不得把推測內容寫成已確認需求。

## 2. 不確定內容必須進入 open questions

所有不明確、矛盾、缺漏或需要利害關係人確認的內容，必須記錄於：

`specs/01-discovery/open-questions.md`

每個問題應包含：

- 問題編號
- 相關來源
- 影響範圍
- 建議詢問對象
- 狀態

## 3. 假設必須明確標記

任何暫時性推測、工作假設或為了繼續分析而建立的前提，必須記錄於：

`specs/01-discovery/assumptions.md`

假設不得直接升級為正式需求。假設只有在被確認後，才可以轉入 `specs/02-requirements/`。

## 4. 正式需求只接受已確認內容

`specs/02-requirements/` 中的內容必須是已確認需求。每個需求都應包含：

- 需求編號
- 需求描述
- 來源
- 狀態
- 驗收或判斷方式

## 5. 設計文件只能根據已確認需求產生

`specs/04-design-ready/` 中的文件不得引用未確認需求、未確認假設或未回答問題作為設計依據。

若設計所需資訊不足，應新增 open question，而不是補上設計細節。

## 6. 可追溯性優先

每個需求、規則、資料欄位、流程與權限都應盡量標記來源。來源可以是：

- 使用者描述
- 會議紀錄
- 文件檔名與頁碼
- 表格名稱與列號
- 訪談對象
- 已確認決策

## 7. 文件格式

所有文件必須使用 Markdown。表格、清單、標題與程式碼區塊應保持一致格式，方便版本控制與審查。

## 8. 需求編號規範

需求編號格式如下：

- `FR-001`：功能需求
- `BR-001`：商業規則
- `DR-001`：資料需求
- `WR-001`：流程需求
- `PR-001`：權限需求
- `NFR-001`：非功能需求

編號一旦發布不得重複使用。若需求被移除，應在 changelog 或 decision log 中記錄。
