---
description: 步驟 2：從 01-discovery/ 的探索結果提取正式需求，產出 02-requirements/
---

# swm.extract — 步驟 2：提取需求

對應 `prompts/02-extract-requirements.prompt.md`。

## Pre-flight 檢查

執行前，讀取 `specs/01-discovery/` 中的關鍵檔案（source-summary.md、extracted-facts.md、open-questions.md）：
- 若任一檔案不存在或只有表頭/空白內容，停止並提示：「請先執行 swm.discover 完成步驟 1，再執行 swm.extract。」
- 若有實質內容，繼續執行。

## 執行

讀取並完整遵循 `prompts/02-extract-requirements.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/01-discovery/`（全部檔案）

產出（`specs/02-requirements/`）：
- `product-vision.md`
- `functional-requirements.md`（FR-###）
- `business-rules.md`（BR-###）
- `data-requirements.md`（DR-###）
- `workflow-requirements.md`（WR-###）
- `permission-requirements.md`（PR-###）
- `non-functional-requirements.md`（NFR-###）
- `user-roles.md`

## Post-execution

完成後提醒用戶：
> 步驟 2 完成。建議執行 `swm.log` 更新版本紀錄，或執行 `swm.clarify` 進行需求釐清（步驟 3）。
