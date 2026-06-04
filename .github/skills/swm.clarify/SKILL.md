---
description: 步驟 3：互動式 Q&A，釐清未確認需求並回填文件
---

# swm.clarify — 步驟 3：釐清需求（互動式 Q&A）

對應 `prompts/03-clarify-requirements.prompt.md`。

## Pre-flight 檢查

執行前，讀取 `specs/02-requirements/functional-requirements.md`：
- 若無任何 FR-### 項目，停止並提示：「請先執行 swm.extract 完成步驟 2，再執行 swm.clarify。」
- 若有實質需求內容，繼續執行。

## 執行

讀取並完整遵循 `prompts/03-clarify-requirements.prompt.md` 的所有指示，包含三個 phase：

**Phase 0（Session 繼續檢查）：**
讀取 `specs/01-discovery/open-questions.md`，若有狀態為 `Awaiting Answer` 的問題，優先重新提問這些問題，而非產生新問題。

**Phase 1（提問）：**
將問題寫入 `specs/01-discovery/open-questions.md`（狀態 `Awaiting Answer`）後，再向用戶提問。

**Phase 2（回填）：**
收到用戶回答後，立即將每個回答寫入 `specs/01-discovery/answer-draft.md`，再依序更新：
- `specs/01-discovery/open-questions.md`（狀態改為 `Answered`）
- `specs/01-discovery/assumptions.md`
- `specs/02-requirements/`（對應需求文件）
- `specs/05-versions/decision-log.md`

## Post-execution

完成後提醒用戶：
> 步驟 3 完成。建議執行 `swm.log` 更新版本紀錄，或執行 `swm.analyze` 進入步驟 4。
