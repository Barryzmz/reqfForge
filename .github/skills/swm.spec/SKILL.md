---
description: 步驟 5：整合所有已確認需求，生成需求規格書（requirement-spec.md）
---

# swm.spec — 步驟 5：生成需求規格書

對應 `prompts/05-generate-spec.prompt.md`。

## Pre-flight 檢查

執行前，讀取以下檔案：
- `specs/03-analysis/use-cases.md`、`user-stories.md`、`acceptance-criteria.md`（確認有實質內容）
- `specs/01-discovery/open-questions.md`（確認無 Open / Awaiting Answer 問題）

若 specs/03-analysis/ 檔案無實質內容，停止並提示：「請先執行 swm.analyze 完成步驟 4。」

若 open-questions.md 仍有未回答問題，停止並提示：「open-questions.md 有 N 個未回答問題，必須先執行 swm.clarify 完成釐清，才能生成規格書。需求規格書只接受已確認內容。」

## 執行

讀取並完整遵循 `prompts/05-generate-spec.prompt.md` 的所有指示。

輸入：
- `CONSTITUTION.md`
- `specs/01-discovery/`（全部）
- `specs/02-requirements/`（全部）
- `specs/03-analysis/`（全部）
- `templates/requirement-spec-template.md`

產出：
- `specs/04-design-ready/requirement-spec.md`

## Post-execution

完成後提醒用戶：
> 步驟 5 完成。需求規格書是後續設計的唯一依據。建議執行 `swm.log` 更新版本紀錄，或執行 `swm.design` 生成設計文件（步驟 6）。
