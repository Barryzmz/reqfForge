---
description: 步驟 1：讀取 specs/00-inputs/ 中的所有輸入，產出初步探索文件（01-discovery/）
---

# rf-discover — 步驟 1：讀取輸入 → 初步探索

對應 `prompts/01-read-inputs.prompt.md`。

## Pre-flight 檢查

執行前，先讀取 `specs/00-inputs/user-description.md`：
- 若檔案不存在或內容為空白，停止並提示：「請先在 specs/00-inputs/user-description.md 填入需求來源描述，再執行 rf-discover。」
- 若有實質內容，繼續執行。

## 執行

讀取並完整遵循 `prompts/01-read-inputs.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/00-inputs/user-description.md`（及 00-inputs/ 中的所有其他來源）

產出（`specs/01-discovery/`）：
- `source-summary.md`
- `extracted-facts.md`
- `open-questions.md`
- `assumptions.md`
- `glossary.md`

## Post-execution

完成後提醒用戶：
> 步驟 1 完成。建議執行 `rf-log` 更新版本紀錄，或直接執行 `rf-extract` 進入步驟 2。
