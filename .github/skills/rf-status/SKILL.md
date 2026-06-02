---
description: 掃描 specs/ 各資料夾，顯示 ReqForge 工作流每個步驟的完成狀態
---

# rf-status — ReqForge 工作流進度檢查

掃描 `specs/` 各資料夾的實際內容，判斷每個步驟的完成狀態，輸出一張進度表。

## 判斷規則

- **✅ 完成**：關鍵檔案存在，且有超過 1 筆非 TBD 的實質內容
- **🔄 進行中**：檔案存在，但部分欄位仍為 TBD，或有 Open 狀態的 open questions 尚未回答
- **⬜ 未開始**：檔案不存在，或只有表頭/template 說明文字，無任何實質資料列

## 執行步驟

依序讀取下列檔案，判斷每個步驟的狀態：

**步驟 0 — 準備輸入**
- `specs/00-inputs/user-description.md`：是否有真實的專案描述？

**步驟 1 — 讀取輸入 → 初步探索**
- `specs/01-discovery/source-summary.md`：是否有來源清單？
- `specs/01-discovery/extracted-facts.md`：是否有提取出的事實？
- `specs/01-discovery/glossary.md`：是否有術語定義？
- `specs/01-discovery/assumptions.md`：是否有假設記錄？
- `specs/01-discovery/open-questions.md`：是否有問題列表？

**步驟 2 — 提取需求 → 正式需求**
- `specs/02-requirements/functional-requirements.md`：是否有 FR-### 項目？
- `specs/02-requirements/product-vision.md`：是否有願景描述？
- `specs/02-requirements/business-rules.md`：是否有 BR-### 項目？
- `specs/02-requirements/user-roles.md`：是否有角色定義？
- 其餘 `specs/02-requirements/` 檔案是否有實質內容？

**步驟 3 — 釐清需求 → 確認問題**
- `specs/01-discovery/open-questions.md`：是否所有問題都已回答（狀態非 Open）？
- `specs/01-discovery/answer-draft.md`：是否有回答草稿？
- `specs/05-versions/decision-log.md`：是否有 DEC-### 決策紀錄？

**步驟 4 — 分析需求 → 分析文件**
- `specs/03-analysis/use-cases.md`：是否有使用案例？
- `specs/03-analysis/user-stories.md`：是否有使用者故事？
- `specs/03-analysis/acceptance-criteria.md`：是否有驗收標準？
- `specs/03-analysis/domain-model.md`：是否有領域模型？
- `specs/03-analysis/state-transitions.md`：是否有狀態轉換？
- `specs/03-analysis/edge-cases.md`：是否有邊界案例？

**步驟 5 — 生成規格 → 需求規格書**
- `specs/04-design-ready/requirement-spec.md`：是否有完整的需求規格？

**步驟 6 — 生成設計文件 → 開發就緒**
- `specs/04-design-ready/system-design-brief.md`：是否有系統架構？
- `specs/04-design-ready/api-draft.md`：是否有 API 端點（非 TBD）？
- `specs/04-design-ready/database-draft.md`：是否有 Schema（非 TBD）？
- `specs/04-design-ready/frontend-pages.md`：是否有頁面規劃？
- `specs/04-design-ready/test-cases.md`：是否有 TC-### 測試案例？
- `specs/04-design-ready/development-tasks.md`：是否有 TASK-### 開發任務？

**步驟 7 — 更新版本 → 變更紀錄**
- `specs/05-versions/changelog.md`：是否有版本紀錄？
- `specs/05-versions/decision-log.md`：是否有 DEC-### 決策紀錄？

## 輸出格式

```
## ReqForge 工作流進度

| 步驟 | 名稱 | 狀態 | 備註 |
|------|------|------|------|
| 步驟 0 | 準備輸入 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 1 | 初步探索 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 2 | 提取需求 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 3 | 釐清需求 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 4 | 分析需求 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 5 | 需求規格書 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 6 | 設計文件 | ✅ / 🔄 / ⬜ | 簡短說明 |
| 步驟 7 | 版本紀錄 | ✅ / 🔄 / ⬜ | 簡短說明 |

**目前位置：** 步驟 X — [步驟名稱]

**建議下一步：** [具體行動]

**待解決問題（如有）：**
- open-questions.md 中仍有 N 個 Open 問題
- 哪些假設仍為 Pending 狀態
```
