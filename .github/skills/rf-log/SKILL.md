---
description: 步驟 7：更新 changelog 與 decision-log，維護完整的審計軌跡（可在任何步驟後執行）
---

# rf-log — 步驟 7：更新版本紀錄

對應 `prompts/07-update-versions.prompt.md`。

可在任何步驟完成後執行，用於維護完整的審計軌跡。

## Pre-flight 檢查

無（任何時間都可執行）。

## 執行

讀取並完整遵循 `prompts/07-update-versions.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/`（全部現有文件）
- `specs/05-versions/changelog.md`（現有紀錄）
- `specs/05-versions/decision-log.md`（現有紀錄）

產出（更新既有檔案）：
- `specs/05-versions/changelog.md`：新增本次變更摘要、受影響檔案、對應步驟
- `specs/05-versions/decision-log.md`：新增已確認決策（DEC-###）、決策理由、來源

**時間戳格式：** `YYYY-MM-DD HH:MM:SS +08:00`

## Post-execution

完成後告知用戶：
> 版本紀錄已更新。changelog 與 decision-log 保持完整的審計軌跡。
