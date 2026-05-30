# ReqForge

ReqForge 是一個需求規格工作流專案，用來協助 PM、開發者與 AI 協作者，將使用者口頭需求、會議紀錄、PPT、Excel、Word、PDF 等資料，整理、釐清並產出正式需求規格文件。

本專案的核心目標不是快速產生文件，而是建立一個可追溯、可審核、可逐步確認的需求整理流程。所有正式需求必須能回到來源、確認狀態與決策紀錄。

## Workflow Steps 與 Artifact Layers

`prompts/` 代表 workflow steps，也就是 AI 執行需求整理工作的步驟。prompt 編號用來表示建議執行順序，不代表一定要一對一對應 `specs/` 資料夾編號。

`specs/` 代表 artifact layers，也就是文件的成熟度與用途。資料夾編號描述文件從原始輸入、探索、需求、分析、規格草稿、設計交付到版本紀錄的演進層次。

因此，某些 prompt 可能會讀取或回填多個 artifact layers。例如 `prompts/03-clarify-requirements.prompt.md` 是 backfill clarification step：第一階段只提出釐清問題；使用者回答後，第二階段才回填 `specs/01-discovery/`、`specs/02-requirements/` 與 `specs/05-versions/decision-log.md`。

`specs/04-design-ready/requirement-spec.md` 是進入設計交付前的 confirmed-requirements-only draft。它只整理已確認需求與可追溯分析，不代表已產出 API、資料庫、前端頁面或開發任務等設計文件。

## 工作流

1. 01 read inputs
   - Prompt: `prompts/01-read-inputs.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/00-inputs/`
   - Output: `specs/01-discovery/`
   - 放置原始輸入摘要或使用者描述。
   - 不在此階段判斷需求正確性。

2. 02 extract requirements
   - Prompt: `prompts/02-extract-requirements.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/01-discovery/`
   - Output: `specs/02-requirements/`
   - 從已確認事實萃取正式需求。
   - 不確定內容必須回寫 `open-questions.md`。
   - 推測性內容必須回寫 `assumptions.md`。

3. 03 clarify requirements
   - Prompt: `prompts/03-clarify-requirements.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/01-discovery/`, `specs/02-requirements/`
   - Output: `specs/01-discovery/open-questions.md`, `specs/01-discovery/assumptions.md`, `specs/02-requirements/`, `specs/05-versions/decision-log.md`
   - Backfill clarification：先提出問題，不修改文件；使用者回答後，才回填 discovery、requirements 與 decision log。

4. 04 analyze requirements
   - Prompt: `prompts/04-analyze-requirements.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/01-discovery/`, `specs/02-requirements/`
   - Output: `specs/03-analysis/`
   - 根據已確認需求建立 use cases、user stories、acceptance criteria、domain model、state transitions 與 edge cases。

5. 05 generate spec
   - Prompt: `prompts/05-generate-spec.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/01-discovery/`, `specs/02-requirements/`, `specs/03-analysis/`, `templates/requirement-spec-template.md`
   - Output: `specs/04-design-ready/requirement-spec.md`
   - 產出進入 design-ready 前的 confirmed-requirements-only draft。
   - 使用 `FR`、`BR`、`DR`、`WR`、`PR`、`NFR` 等編號。

6. 06 generate design-ready documents
   - Prompt: `prompts/06-generate-design-ready.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/04-design-ready/requirement-spec.md`, `templates/`
   - Output: `specs/04-design-ready/`
   - 產出可交付給設計、前端、後端、測試與專案管理使用的文件。
   - 設計文件只能根據已確認需求產生。

7. 07 update versions
   - Prompt: `prompts/07-update-versions.prompt.md`
   - Input: `CONSTITUTION.md`, `specs/01-discovery/`, `specs/02-requirements/`, `specs/03-analysis/`, `specs/04-design-ready/`
   - Output: `specs/05-versions/changelog.md`, `specs/05-versions/decision-log.md`
   - 維護 changelog 與 decision log。

## 需求編號

| 類型 | 前綴 | 說明 |
| --- | --- | --- |
| Functional Requirement | `FR` | 功能需求 |
| Business Rule | `BR` | 商業規則 |
| Data Requirement | `DR` | 資料需求 |
| Workflow Requirement | `WR` | 流程需求 |
| Permission Requirement | `PR` | 權限需求 |
| Non-functional Requirement | `NFR` | 非功能需求 |

範例：`FR-001`、`BR-001`、`DR-001`、`WR-001`、`PR-001`、`NFR-001`。

## AI 使用原則

- AI 不得自行腦補需求。
- 不確定的需求必須寫入 `specs/01-discovery/open-questions.md`。
- 假設必須寫入 `specs/01-discovery/assumptions.md`。
- 已確認需求才可以寫入正式需求文件。
- 設計文件只能根據已確認需求產生。
- 所有需求都要盡量可追溯來源。
- 文件全部使用 Markdown。

詳細原則請見 `CONSTITUTION.md`。
