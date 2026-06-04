# swm.design — 步驟 6：生成設計文件

對應 `prompts/06-generate-design-ready.prompt.md`。

## Pre-flight 檢查

執行前，讀取 `specs/04-design-ready/requirement-spec.md`：
- 若檔案不存在或只有空表格，停止並提示：「請先執行 /swm.spec 完成步驟 5，才能生成設計文件。設計文件只能根據已確認的需求規格書產生。」
- 若有實質內容，繼續執行。

## 執行

讀取並完整遵循 `prompts/06-generate-design-ready.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/04-design-ready/requirement-spec.md`
- `templates/api-draft-template.md`
- `templates/database-draft-template.md`
- `templates/test-case-template.md`
- `templates/development-tasks-template.md`

產出（`specs/04-design-ready/`）：
- `system-design-brief.md`
- `api-draft.md`
- `database-draft.md`
- `frontend-pages.md`
- `test-cases.md`（TC-###）
- `development-tasks.md`（TASK-###）

## Post-execution

完成後提醒用戶：
> 步驟 6 完成。開發就緒文件已生成。建議執行 `/swm.log` 更新版本紀錄，完成完整的審計軌跡。
