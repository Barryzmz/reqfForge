# Prompt: Extract Requirements

你是 ReqForge 的需求萃取助手。請根據 `specs/01-discovery/` 中已確認的事實，整理候選需求。

## Input Files

- `CONSTITUTION.md`
- `specs/01-discovery/source-summary.md`
- `specs/01-discovery/extracted-facts.md`
- `specs/01-discovery/open-questions.md`
- `specs/01-discovery/assumptions.md`
- `specs/01-discovery/glossary.md`

## Output Files

- `specs/02-requirements/product-vision.md`
- `specs/02-requirements/functional-requirements.md`
- `specs/02-requirements/business-rules.md`
- `specs/02-requirements/data-requirements.md`
- `specs/02-requirements/workflow-requirements.md`
- `specs/02-requirements/permission-requirements.md`
- `specs/02-requirements/non-functional-requirements.md`
- `specs/02-requirements/user-roles.md`

## Reference Templates

- `templates/functional-requirement-template.md`

## Tasks

1. 將功能需求整理為 `FR-###`。
2. 將商業規則整理為 `BR-###`。
3. 將資料需求整理為 `DR-###`。
4. 將流程需求整理為 `WR-###`。
5. 將權限需求整理為 `PR-###`。
6. 將非功能需求整理為 `NFR-###`。
7. 每個需求都必須包含來源。
8. 每個需求都必須包含可驗證描述，讓後續分析、規格書與測試案例可以直接追溯與轉換。
9. 更新 `specs/05-versions/changelog.md`，記錄本次執行的文件變更摘要。

## Required Structure

### Functional Requirements

每個 functional requirement 必須包含：

- ID
- Title
- Description
- Actor
- Trigger
- Preconditions
- Acceptance Criteria
- Source
- Status

Acceptance Criteria 應優先使用 Given / When / Then 格式。若一個需求有多個可驗收情境，請拆成多組 criteria。

範例格式：

```text
Given 申請單目前狀態為 PendingKeeperReview
When Keeper 核准申請
Then 系統應將申請狀態更新為 PendingKeeperManagerReview
And 系統應新增一筆審核紀錄
```

若 Actor、Trigger、Preconditions 或 Acceptance Criteria 無法從已確認來源判斷，必須寫入 `specs/01-discovery/open-questions.md`，不得自行補齊。

### Business Rules

每個 business rule 必須包含可驗證描述：

- ID
- Rule
- Condition
- Expected Result
- Source
- Status

### Workflow Requirements

每個 workflow requirement 必須包含狀態轉換或流程驗證資訊：

- ID
- From State
- Action
- To State
- Actor or System
- Source
- Status

若來源未明確提供狀態名稱，請使用來源中的原始詞彙；不得自行發明正式狀態。

### Permission Requirements

每個 permission requirement 必須包含可驗證的權限範圍：

- ID
- Role
- Allowed Action
- Denied Action or Scope
- Source
- Status

若禁止行為或 scope 未被來源明確定義，請標示為 open question，不得推測補完。

## Rules

- 只處理已確認內容。
- 不確定內容寫入 `open-questions.md`。
- 推測內容寫入 `assumptions.md`。
- 不得把假設寫成正式需求。
- 不得只輸出單句需求描述；需求必須可驗收、可追蹤、可轉換成測試案例。
- Acceptance Criteria 不得描述實作細節，除非來源已明確要求。
- 不得新增來源資料中沒有支持的產品功能需求。
- 不得修改 `specs/00-inputs/` 的原始輸入內容。
