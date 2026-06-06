<p align="center">
  <img src="assets/banner.svg" alt="SpecWingman Banner" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0.0-008fd3?style=flat-square" alt="version 3.0.0" />
  <img src="https://img.shields.io/badge/specs-traceable-6f42c1?style=flat-square" alt="traceable specs" />
  <img src="https://img.shields.io/badge/MCP-supported-2ea44f?style=flat-square" alt="MCP supported" />
  <img src="https://img.shields.io/badge/no-guesswork-f97316?style=flat-square" alt="no guesswork" />
  <img src="https://img.shields.io/badge/license-MIT-008fd3?style=flat-square" alt="MIT license" />
</p>

# SpecWingman

SpecWingman 是一個需求規格工作流專案，用來協助 PM、開發者與 AI 協作者，將使用者口頭需求、會議紀錄、PPT、Excel、Word、PDF 等資料，整理、釐清並產出正式需求規格文件。

本專案的核心目標不是快速產生文件，而是建立一個可追溯、可審核、可逐步確認的需求整理流程。所有正式需求必須能回到來源、確認狀態與決策紀錄。

支援 **Claude Code**（slash commands + MCP）、**GitHub Copilot**、**OpenAI Codex CLI** 與其他 MCP 客戶端，核心 workflow 完全共用。詳見 [GUIDE.md](GUIDE.md)。

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
   - 從已確認事實萃取正式需求，不只是文字整理。
   - 輸出必須可驗收、可追蹤，並能轉換成後續分析、規格書與測試案例。
   - Functional requirements 必須包含 actor、trigger、preconditions 與 acceptance criteria，並優先使用 Given / When / Then 格式。
   - Business rules、workflow requirements 與 permission requirements 必須包含可驗證描述。
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
   - 使用時機：使用者回答釐清問題後、requirements 被更新後、requirement-spec 產出後、design-ready 文件產出後，或任何需求決策有變更時。
   - 需求決策不可只存在對話紀錄，必須記錄到 `specs/05-versions/decision-log.md`。
   - 文件新增、修改、移除或重新產出時，必須記錄到 `specs/05-versions/changelog.md`。

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
- AI 不得因為業界常見做法或一般系統常見流程，就把功能寫成已確認需求。
- 常見做法只能標示為 Suggested Practice、Assumption 或 Open Question；除非來源或使用者明確確認，否則不得進入正式需求。
- 不確定的需求必須寫入 `specs/01-discovery/open-questions.md`。
- 假設必須寫入 `specs/01-discovery/assumptions.md`。
- 已確認需求才可以寫入正式需求文件。
- AI 必須區分 Confirmed Requirement、Suggested Practice、Assumption 與 Open Question。
- 若模型傾向補齊常見流程，仍必須優先保守處理；不確定時應提出問題，而不是補需求。
- 設計文件只能根據已確認需求產生。
- 所有需求都要盡量可追溯來源。
- 文件全部使用 Markdown。

詳細原則請見 `CONSTITUTION.md`。

## MCP Server

`agent/` 目錄提供 Python MCP Server，讓支援 MCP 的 AI 工具以程式化方式執行整個 workflow。每個步驟拆為 `swm_*_context`（讀取上下文）與 `swm_write_*`（寫入產出）兩個工具，另有 `swm_status`（進度檢查）與 `swm_next`（自動推進 orchestrator）。

```bash
cd agent && pip install -e .
python agent/server.py
```

詳見 [GUIDE.md](GUIDE.md) 的「MCP Server」章節。
