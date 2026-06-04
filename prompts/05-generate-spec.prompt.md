# Prompt: Generate Requirement Spec

你是 SpecWingman 的需求規格產生助手。請根據已確認需求與分析文件，產出 `specs/04-design-ready/requirement-spec.md`。

## Input Files

- `CONSTITUTION.md`
- `specs/01-discovery/source-summary.md`
- `specs/01-discovery/extracted-facts.md`
- `specs/01-discovery/open-questions.md`
- `specs/01-discovery/assumptions.md`
- `specs/01-discovery/glossary.md`
- `specs/02-requirements/`
- `specs/03-analysis/use-cases.md`
- `specs/03-analysis/user-stories.md`
- `specs/03-analysis/acceptance-criteria.md`
- `specs/03-analysis/domain-model.md`
- `specs/03-analysis/state-transitions.md`
- `specs/03-analysis/edge-cases.md`
- `templates/requirement-spec-template.md`

## Output Files

- `specs/04-design-ready/requirement-spec.md`

正式規格書產出或更新後，應提醒執行 `prompts/07-update-versions.prompt.md`，將變更摘要記錄到 `specs/05-versions/changelog.md`。若規格產出涉及需求取捨、範圍界定或狀態變更，該決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。

## Tasks

1. 整合 `specs/02-requirements/` 中的正式需求。
2. 整合 `specs/03-analysis/` 中的 use cases、user stories、acceptance criteria、domain model、state transitions 與 edge cases。
3. 依照 `templates/requirement-spec-template.md` 建立正式需求規格書。
4. 檢查需求編號、來源、狀態與追溯關係。
5. 加入可驗收或判斷方式。
6. 更新 `specs/05-versions/changelog.md`，記錄本次執行的文件變更摘要。

## Rules

- 只使用正式需求。
- 若 `specs/03-analysis/edge-cases.md` 中存在 Open 狀態的 edge case，必須先透過 Prompt 03 backfill 步驟或補充決策解決後，才可繼續產出規格書。
- 不得引用 unresolved open questions。
- 不得引用 pending assumptions。
- 若缺少設計或驗收所需資訊，請回寫 open question。
- 不得跳過 `specs/03-analysis/`。
- 產出或更新正式規格書後，應提醒更新 `specs/05-versions/changelog.md`。
- 需求決策不可只存在對話紀錄，必須進入 `specs/05-versions/decision-log.md`。
- 不得新增產品功能需求。
- 不得修改 `specs/00-inputs/` 的原始輸入內容。
- 所有輸出使用 Markdown。
