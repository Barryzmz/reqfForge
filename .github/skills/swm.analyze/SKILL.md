---
description: 步驟 4：分析已確認需求，產出使用案例、領域模型、狀態機等分析文件（03-analysis/）
---

# swm.analyze — 步驟 4：分析需求

對應 `prompts/04-analyze-requirements.prompt.md`。

## Pre-flight 檢查

執行前，讀取 `specs/02-requirements/functional-requirements.md` 和 `specs/01-discovery/open-questions.md`：
- 若 functional-requirements.md 無 FR-### 項目，停止並提示：「請先執行 swm.extract 完成步驟 2。」
- 若 open-questions.md 有狀態為 `Open` 或 `Awaiting Answer` 的問題，警示用戶：「open-questions.md 有未回答問題，建議先執行 swm.clarify 完成釐清，再進行分析。如確認繼續，分析結果可能不完整。」

## 執行

讀取並完整遵循 `prompts/04-analyze-requirements.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/01-discovery/`（全部）
- `specs/02-requirements/`（全部）

產出（`specs/03-analysis/`）：
- `use-cases.md`
- `user-stories.md`
- `acceptance-criteria.md`
- `domain-model.md`
- `state-transitions.md`
- `edge-cases.md`

## Post-execution

完成後提醒用戶：
> 步驟 4 完成。建議執行 `swm.log` 更新版本紀錄，或執行 `swm.spec` 生成需求規格書（步驟 5）。
