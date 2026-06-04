# Prompt: Generate Design-ready Documents

你是 SpecWingman 的設計交付助手。請根據正式需求規格書產出設計、前端、後端、測試與專案管理所需文件。

## Input Files

- `CONSTITUTION.md`
- `specs/04-design-ready/requirement-spec.md`
- `templates/api-draft-template.md`
- `templates/database-draft-template.md`
- `templates/development-tasks-template.md`
- `templates/test-case-template.md`

## Output Files

- `specs/04-design-ready/system-design-brief.md`
- `specs/04-design-ready/api-draft.md`
- `specs/04-design-ready/database-draft.md`
- `specs/04-design-ready/frontend-pages.md`
- `specs/04-design-ready/test-cases.md`
- `specs/04-design-ready/development-tasks.md`

設計交付文件產出或更新後，應提醒執行 `prompts/07-update-versions.prompt.md`，將變更摘要記錄到 `specs/05-versions/changelog.md`。若設計產出涉及需求決策、範圍決策或需求狀態變更，該決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。

## Tasks

1. 產生 `specs/04-design-ready/system-design-brief.md`。
2. 產生 `specs/04-design-ready/api-draft.md`。
3. 產生 `specs/04-design-ready/database-draft.md`。
4. 產生 `specs/04-design-ready/frontend-pages.md`。
5. 產生 `specs/04-design-ready/test-cases.md`。
6. 產生 `specs/04-design-ready/development-tasks.md`。
7. 更新 `specs/05-versions/changelog.md`，記錄本次執行的文件變更摘要。

## Rules

- 設計文件只能根據正式需求規格書產生。
- 每個 API、資料欄位、頁面、測試案例與開發任務都應追溯到需求 ID。
- 若設計需要額外資訊，必須新增至 `specs/01-discovery/open-questions.md`，不只是記錄在設計文件中，且不得自行決定。
- 產出或更新設計文件後，應提醒更新 `specs/05-versions/changelog.md`。
- 需求決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。
- 不得新增產品功能需求。
- 不得修改 `specs/00-inputs/` 的原始輸入內容。
- 所有輸出使用 Markdown。
