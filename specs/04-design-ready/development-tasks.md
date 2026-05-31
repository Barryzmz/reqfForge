# Development Tasks

每個任務追溯至需求 ID。未能追溯至需求的任務不得列入。

## 任務清單

| Task ID | 任務 | 類型 | 關聯需求 | 依賴 | 狀態 |
| --- | --- | --- | --- | --- | --- |
| TASK-001 | 建立資料庫 Schema（6 張資料表） | Backend / DB | DR-001 ~ DR-011 | — | Todo |
| TASK-002 | 實作員工認證與角色權限 Middleware | Backend | PR-001 ~ PR-007 | TASK-001 | Todo |
| TASK-003 | 實作 POST /api/leaves（申請送出，含所有驗證） | Backend | FR-001、FR-002、BR-007 ~ BR-012 | TASK-001、TASK-002 | Todo |
| TASK-004 | 實作 GET /api/leaves（員工查詢自身紀錄） | Backend | PR-002 | TASK-001、TASK-002 | Todo |
| TASK-005 | 實作 PATCH /api/leaves/:id/cancel（取消申請） | Backend | FR-007、WR-005 | TASK-001、TASK-002 | Todo |
| TASK-006 | 實作 POST /api/leaves/:id/review（主管審核） | Backend | FR-003、BR-005、BR-009、BR-010 | TASK-001、TASK-002 | Todo |
| TASK-007 | 實作 GET /api/hr/leaves（HR 全員查詢） | Backend | FR-005、PR-006 | TASK-001、TASK-002 | Todo |
| TASK-008 | 實作 GET /api/hr/leaves/export（Excel 報表匯出） | Backend | FR-006、DR-011 | TASK-001、TASK-002 | Todo |
| TASK-009 | 實作 POST /api/delegates 與 GET /api/delegates/me | Backend | FR-008、BR-015、DR-010 | TASK-001、TASK-002 | Todo |
| TASK-010 | 實作 GET /api/leave-balances/me（假期餘額查詢） | Backend | DR-008、BR-001 ~ BR-004 | TASK-001、TASK-002 | Todo |
| TASK-011 | 實作催審 Scheduler（定期掃描超時待審申請） | Backend | FR-004、BR-006、WR-004 | TASK-001 | Todo |
| TASK-012 | 實作 Email 通知發送（催審） | Backend | FR-004、BR-006 / DEC-002 | TASK-011 | Todo |
| TASK-013 | 實作系統內通知儲存與發送（催審） | Backend | FR-004、BR-006 / DEC-002 | TASK-011 | Todo |
| TASK-014 | 實作代理期間結束後待審申請回歸邏輯 | Backend | BR-013、DR-010 | TASK-001、TASK-011 | Todo |
| TASK-015 | 實作假期餘額年度初始化邏輯（依假別規則） | Backend | BR-001 ~ BR-004 | TASK-001 | Todo |
| TASK-016 | 前端：請假申請頁（PAGE-001，含條件性診斷書上傳） | Frontend | FR-001、FR-002、BR-007、BR-008 | TASK-003 | Todo |
| TASK-017 | 前端：我的請假紀錄頁（PAGE-002，含取消按鈕） | Frontend | FR-007、PR-002 | TASK-004、TASK-005 | Todo |
| TASK-018 | 前端：主管待審核頁（PAGE-003，含審核表單） | Frontend | FR-003、BR-005 | TASK-006 | Todo |
| TASK-019 | 前端：代理主管設定頁（PAGE-004） | Frontend | FR-008 | TASK-009 | Todo |
| TASK-020 | 前端：HR 全員假期紀錄頁（PAGE-005） | Frontend | FR-005 | TASK-007 | Todo |
| TASK-021 | 前端：HR 報表匯出頁（PAGE-006） | Frontend | FR-006 | TASK-008 | Todo |
| TASK-022 | 前端：假期餘額查詢頁（PAGE-007） | Frontend | DR-008 | TASK-010 | Todo |
| TASK-023 | 撰寫後端 API 單元測試（TC-001 ~ TC-027 相關案例） | Testing | 全部 FR、BR | TASK-003 ~ TASK-014 | Todo |
| TASK-024 | 撰寫 E2E 測試（主要流程：申請 → 審核 → 催審） | Testing | FR-001、FR-003、FR-004 | TASK-016 ~ TASK-018 | Todo |

## 任務依賴關係說明

```
TASK-001（DB Schema）
    └── TASK-002（Auth Middleware）
            ├── TASK-003（POST /api/leaves）── TASK-016（前端申請頁）
            ├── TASK-004（GET /api/leaves）── TASK-017（我的紀錄頁）
            ├── TASK-005（PATCH cancel）────── TASK-017
            ├── TASK-006（POST review）─────── TASK-018（主管審核頁）
            ├── TASK-007（HR GET leaves）───── TASK-020（HR 紀錄頁）
            ├── TASK-008（HR export）───────── TASK-021（HR 匯出頁）
            ├── TASK-009（delegates）───────── TASK-019（代理設定頁）
            └── TASK-010（balances）─────────── TASK-022（餘額查詢頁）

TASK-011（Scheduler）
    ├── TASK-012（Email 通知）
    ├── TASK-013（系統通知）
    └── TASK-014（代理到期回歸）

TASK-015（假期餘額初始化）── 獨立，需在系統上線前完成
```

## 未解決事項（影響 TASK-012、TASK-013）

| QD ID | 問題 | 影響任務 |
| --- | --- | --- |
| QD-002 | Scheduler 執行頻率 | TASK-011 |
| QD-003 | 系統內通知的儲存與讀取機制 | TASK-013 |
