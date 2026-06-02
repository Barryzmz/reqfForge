---
description: 掃描 specs/ 目前狀態，自動判斷並執行下一個未完成的工作流步驟
---

# rf-next — 自動判斷並執行下一步

掃描 `specs/` 目前狀態，找出第一個未完成的步驟，告知用戶並直接執行。

## 判斷邏輯

依序檢查每個步驟，找到第一個「未開始」或「進行中」的步驟：

**步驟 1（rf-discover）已完成的條件：**
`specs/01-discovery/` 中的 source-summary.md、extracted-facts.md、open-questions.md、assumptions.md、glossary.md 都有超過 1 筆非 TBD 的實質內容。

**步驟 2（rf-extract）已完成的條件：**
`specs/02-requirements/functional-requirements.md` 有至少 1 筆 FR-### 項目，其他需求檔案有實質內容。

**步驟 3（rf-clarify）已完成的條件：**
`specs/01-discovery/open-questions.md` 中沒有狀態為 `Open` 或 `Awaiting Answer` 的問題。

**步驟 4（rf-analyze）已完成的條件：**
`specs/03-analysis/` 中的 use-cases.md、user-stories.md、acceptance-criteria.md、domain-model.md、state-transitions.md、edge-cases.md 都有實質內容。

**步驟 5（rf-spec）已完成的條件：**
`specs/04-design-ready/requirement-spec.md` 有實質的需求規格內容（非空表格）。

**步驟 6（rf-design）已完成的條件：**
`specs/04-design-ready/` 中的 api-draft.md、database-draft.md、frontend-pages.md、test-cases.md、development-tasks.md 都有超過 1 筆非 TBD 的實質內容。

**步驟 7（rf-log）已完成的條件：**
`specs/05-versions/changelog.md` 和 `decision-log.md` 都有實質的版本紀錄。

## 執行步驟

1. 讀取上述各步驟的關鍵檔案，判斷完成狀態
2. 找出第一個未完成的步驟
3. 輸出簡短報告：

```
目前進度：步驟 X 已完成，步驟 Y 尚未完成。

即將執行：rf-[step-name]（步驟 Y — [步驟說明]）
```

4. 立即執行該步驟對應的完整指示：

| 下一步 | 執行內容 |
|--------|---------|
| 步驟 1 | 讀取並執行 `.github/skills/rf-discover/SKILL.md` |
| 步驟 2 | 讀取並執行 `.github/skills/rf-extract/SKILL.md` |
| 步驟 3 | 讀取並執行 `.github/skills/rf-clarify/SKILL.md` |
| 步驟 4 | 讀取並執行 `.github/skills/rf-analyze/SKILL.md` |
| 步驟 5 | 讀取並執行 `.github/skills/rf-spec/SKILL.md` |
| 步驟 6 | 讀取並執行 `.github/skills/rf-design/SKILL.md` |
| 步驟 7 | 讀取並執行 `.github/skills/rf-log/SKILL.md` |

5. 若所有步驟皆完成，輸出：

```
所有步驟已完成。如有需求變更，請執行 rf-clarify 重新進入釐清流程，或 rf-log 更新版本紀錄。
```
