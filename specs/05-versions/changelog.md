# Changelog

| Version / Date | Changed Files | Summary | Reason | Related Prompt Step |
| --- | --- | --- | --- | --- |
| 0.1.0 / 2026-05-31 | specs/00-inputs/user-description.md | 填入員工請假管理系統驗證情境原始描述 | 初始驗證情境輸入 | 00-inputs |
| 0.2.0 / 2026-05-31 | specs/01-discovery/ | 完成 source-summary、extracted-facts、open-questions、assumptions、glossary | Prompt 01 執行完畢 | 01-read-inputs |
| 0.3.0 / 2026-05-31 | specs/02-requirements/ | 完成 product-vision、functional-requirements（FR-001~006）、business-rules（BR-001~006）、data-requirements（DR-001~008）、workflow-requirements（WR-001~004）、permission-requirements（PR-001~005）、non-functional-requirements、user-roles | Prompt 02 執行完畢 | 02-extract-requirements |
| 0.4.0 / 2026-05-31 | specs/01-discovery/open-questions.md、specs/01-discovery/assumptions.md、specs/02-requirements/（全部）、specs/05-versions/decision-log.md | 釐清 Q-001~011，回填需求文件；新增 FR-007、FR-008、BR-007~010、DR-009~011、WR-005、PR-002~003重整；記錄 DEC-001~010 | Prompt 03 Phase 2 執行完畢 | 03-clarify-requirements |
| 0.5.0 / 2026-05-31 | specs/03-analysis/use-cases.md、specs/03-analysis/user-stories.md、specs/03-analysis/acceptance-criteria.md、specs/03-analysis/domain-model.md、specs/03-analysis/state-transitions.md、specs/03-analysis/edge-cases.md | 完成全部分析文件：UC-001~007、US-001~008、AC-001~022、6 個實體 domain model、7 個狀態轉換、12 個 edge cases | Prompt 04 執行完畢 | 04-analyze-requirements |
| 0.5.1 / 2026-05-31 | specs/03-analysis/edge-cases.md、specs/02-requirements/business-rules.md、specs/05-versions/decision-log.md | 補齊 6 個 Open edge cases（EC-001、004、005、007、009、010、012）；新增 BR-011~015；記錄 DEC-011~016 | Edge case 缺口補足，保持需求可追溯 | 04-analyze-requirements（補充） |
| 1.0.0 / 2026-05-31 | specs/04-design-ready/requirement-spec.md | 產出完整需求規格書，涵蓋 FR-001~008、BR-001~015、DR-001~011、WR-001~005、PR-001~007；含 Domain Model 摘要、State Transitions 摘要、Edge Cases 摘要與完整追溯表 | Prompt 05 執行完畢 | 05-generate-spec |
| 1.1.0 / 2026-05-31 | specs/04-design-ready/system-design-brief.md、api-draft.md、database-draft.md、frontend-pages.md、test-cases.md、development-tasks.md | 產出全部 6 份設計交付文件：API-001~010、TBL-001~006、PAGE-001~007、TC-001~027、TASK-001~024；發現 3 個設計層 open questions（QD-001~003） | Prompt 06 執行完畢 | 06-generate-design-ready |
| 1.1.1 / 2026-05-31 | specs/01-discovery/open-questions.md | 將設計階段發現的 QD-001~004 正式寫入 open-questions.md | Prompt 07 稽核：發現設計層問題僅存在 system-design-brief.md，未回填至正式問題追蹤文件 | 07-update-versions |
| 1.1.2 / 2026-05-31 | specs/05-versions/changelog.md、specs/05-versions/decision-log.md | 完成 Prompt 07 版本稽核：確認 DEC-001~016 完整記錄、Q-001~011 全部 Answered（除 Q-008）、QD-001~004 已正式追蹤；無遺漏決策 | Prompt 07 執行完畢，完成驗證情境完整工作流收尾 | 07-update-versions |
