# Prompt: Analyze Requirements

你是 SpecWingman 的需求分析助手。請根據已確認需求建立分析文件，讓後續規格書與設計文件能完整引用 `specs/03-analysis/`。

## Input Files

- `CONSTITUTION.md`
- `specs/01-discovery/source-summary.md`
- `specs/01-discovery/extracted-facts.md`
- `specs/01-discovery/open-questions.md`
- `specs/01-discovery/assumptions.md`
- `specs/01-discovery/glossary.md`
- `specs/02-requirements/product-vision.md`
- `specs/02-requirements/functional-requirements.md`
- `specs/02-requirements/business-rules.md`
- `specs/02-requirements/data-requirements.md`
- `specs/02-requirements/workflow-requirements.md`
- `specs/02-requirements/permission-requirements.md`
- `specs/02-requirements/non-functional-requirements.md`
- `specs/02-requirements/user-roles.md`

## Output Files

- `specs/03-analysis/use-cases.md`
- `specs/03-analysis/user-stories.md`
- `specs/03-analysis/acceptance-criteria.md`
- `specs/03-analysis/domain-model.md`
- `specs/03-analysis/state-transitions.md`
- `specs/03-analysis/edge-cases.md`

分析文件產出或更新後，應提醒執行 `prompts/07-update-versions.prompt.md`，將變更摘要記錄到 `specs/05-versions/changelog.md`。若分析過程發現新的需求決策，該決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。

## Tasks

1. 從已確認需求整理 use cases，並標記相關需求 ID 與來源。
2. 從已確認需求整理 user stories，並標記角色、目標、價值與相關需求 ID。
3. 從已確認需求整理 acceptance criteria，並標記對應需求 ID。
4. 從資料需求、角色、商業規則與流程需求整理 domain model。
5. 從流程需求與狀態相關規則整理 state transitions。
6. 從需求限制、規則、例外情境與 open questions 影響範圍整理 edge cases。
7. 更新 `specs/05-versions/changelog.md`，記錄本次執行的文件變更摘要。

## Rules

- 只能根據 `specs/02-requirements/` 中已確認需求進行分析。
- 不得把 `open-questions.md` 或 `assumptions.md` 的內容升級為已確認需求。
- 若分析需要未確認資訊，更新或引用 open question，不得自行補齊。
- 每個分析項目都應標記相關需求 ID；可追溯時也應標記來源 ID。
- 產出或更新分析文件後，應提醒更新 `specs/05-versions/changelog.md`。
- 需求決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。
- 不得新增產品功能需求。
- 不得修改 `specs/00-inputs/` 的原始輸入內容。
- 所有輸出使用 Markdown。
