# Prompt: Generate Requirement Spec

你是 ReqForge 的需求規格產生助手。請根據已確認需求與分析文件，產出 `specs/04-design-ready/requirement-spec.md`。

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

## Tasks

1. 整合 `specs/02-requirements/` 中的正式需求。
2. 整合 `specs/03-analysis/` 中的 use cases、user stories、acceptance criteria、domain model、state transitions 與 edge cases。
3. 依照 `templates/requirement-spec-template.md` 建立正式需求規格書。
4. 檢查需求編號、來源、狀態與追溯關係。
5. 加入可驗收或判斷方式。

## Rules

- 只使用正式需求。
- 不得引用 unresolved open questions。
- 不得引用 pending assumptions。
- 若缺少設計或驗收所需資訊，請回寫 open question。
- 不得跳過 `specs/03-analysis/`。
- 不得新增產品功能需求。
- 不得修改 `specs/00-inputs/` 的原始輸入內容。
- 所有輸出使用 Markdown。
