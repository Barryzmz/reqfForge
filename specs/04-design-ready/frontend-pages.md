# Frontend Pages

每個頁面追溯至需求 ID。角色存取規則依 `specs/02-requirements/permission-requirements.md`。

## 頁面清單

| Page ID | 頁面名稱 | 主要角色 | 目的 | 關聯需求 |
| --- | --- | --- | --- | --- |
| PAGE-001 | 請假申請頁 | Employee | 填寫並送出請假申請 | FR-001、FR-002、BR-007、BR-008、BR-011、BR-012 |
| PAGE-002 | 我的請假紀錄頁 | Employee | 查看自身申請清單、取消待審核申請 | FR-007、PR-002、WR-005 |
| PAGE-003 | 主管待審核頁 | Manager | 查看待審核申請清單並進行審核 | FR-003、BR-005、BR-009、BR-010、WR-002、WR-003 |
| PAGE-004 | 代理主管設定頁 | Manager | 設定代理人與代理期間 | FR-008、BR-015、DR-010 |
| PAGE-005 | HR 全員假期紀錄頁 | HR | 查看所有員工請假申請 | FR-005、PR-006 |
| PAGE-006 | HR 報表匯出頁 | HR | 匯出 Excel 假期報表 | FR-006、DR-011、PR-007 |
| PAGE-007 | 假期餘額查詢頁 | Employee | 查看自身各假別剩餘天數 | DR-008、BR-001 ~ BR-004 |

---

## PAGE-001：請假申請頁

- **Route**: /leave/apply
- **Permission**: Employee（已登入）
- **Related Requirements**: FR-001、FR-002、BR-007、BR-008、BR-011、BR-012

### Main Actions

- 填寫假別（特休 / 病假 / 事假 / 喪假）
- 填寫開始日期、結束日期（日曆元件，支援半天選擇，最小單位 0.5 天）
- 填寫請假原因（文字欄位）
- 病假且天數 > 3 時顯示診斷書上傳欄位（條件性顯示）
- 喪假需額外選擇親等（依 BR-003 對照表枚舉）
- 送出前前端驗證：必填欄位、日期合法性、附件條件

### Required Data

- 員工自身假期餘額（API-010，用於前端顯示剩餘天數）
- 員工現有申請清單（用於日期重疊前端提示）

### Validation（前端）

| 規則 | 提示訊息 | 關聯需求 |
| --- | --- | --- |
| 必填欄位不得為空 | 請填寫所有必填欄位 | FR-001 |
| 結束日期不得早於開始日期 | 結束日期不可早於開始日期 | DR-001、DR-002 |
| 病假 > 3 天需上傳診斷書 | 病假超過 3 天需附上診斷書 | BR-007 |
| 申請天數不得超過餘額 | 假期餘額不足（剩餘 N 天） | BR-011 |
| 日期不得與現有申請重疊 | 申請日期與現有申請重疊 | BR-012 |

---

## PAGE-002：我的請假紀錄頁

- **Route**: /leave/my-records
- **Permission**: Employee（已登入）
- **Related Requirements**: FR-007、PR-002、WR-005

### Main Actions

- 列出自身所有請假申請（依日期排序）
- 顯示各申請的狀態（待審核 / 已核准 / 已拒絕 / 已取消）
- 「待審核」狀態的申請提供「取消申請」按鈕
- 點選申請可查看詳情（含拒絕原因）

### Required Data

- 自身請假申請清單（API-002）

---

## PAGE-003：主管待審核頁

- **Route**: /manager/review
- **Permission**: Manager（已登入）；代理主管於代理期間內可存取
- **Related Requirements**: FR-003、BR-005、PR-004、PR-005、WR-002、WR-003

### Main Actions

- 列出所有屬於管轄員工且狀態為「待審核」的申請
- 點選申請查看詳情（申請人、假別、日期、原因、附件）
- 執行「同意」或「拒絕」
- 拒絕時強制填寫拒絕原因

### Required Data

- 管轄員工的待審核申請清單（API-005 查詢前置）

### Validation（前端）

| 規則 | 提示訊息 | 關聯需求 |
| --- | --- | --- |
| 拒絕需填寫原因 | 請填寫拒絕原因 | BR-005 |

---

## PAGE-004：代理主管設定頁

- **Route**: /manager/delegate
- **Permission**: Manager（已登入）
- **Related Requirements**: FR-008、BR-015、DR-010

### Main Actions

- 查看目前的代理設定（若有）
- 指定代理人（從員工清單選擇）
- 設定代理起始日與結束日
- 儲存代理設定

### Validation（前端）

| 規則 | 提示訊息 | 關聯需求 |
| --- | --- | --- |
| 代理人不可為自己 | 代理人不可設定為自己 | BR-015 |
| 結束日期不得早於起始日期 | 代理結束日不可早於起始日 | DR-010 |

### Required Data

- 員工清單（用於選擇代理人）
- 現有代理設定（API-009）

---

## PAGE-005：HR 全員假期紀錄頁

- **Route**: /hr/leave-records
- **Permission**: HR（已登入）
- **Related Requirements**: FR-005、PR-006

### Main Actions

- 列出所有員工的請假申請紀錄
- 支援依員工姓名、部門、假別、狀態篩選（篩選欄位依報表欄位為基礎）
- 點選申請查看詳情

### Required Data

- 全員請假申請（API-006）

---

## PAGE-006：HR 報表匯出頁

- **Route**: /hr/export
- **Permission**: HR（已登入）
- **Related Requirements**: FR-006、DR-011、PR-007

### Main Actions

- 提供匯出按鈕
- 點擊後下載 Excel 報表（含 DR-011 定義的 8 個欄位）

### Required Data

- 觸發 API-007 下載

---

## PAGE-007：假期餘額查詢頁

- **Route**: /leave/balances
- **Permission**: Employee（已登入）
- **Related Requirements**: DR-008、BR-001 ~ BR-004

### Main Actions

- 顯示自身各假別的年度總配額與剩餘天數
- 分假別顯示（特休、病假、事假）

> 備註：喪假通常不預先配額，依申請時親等計算，此頁是否顯示喪假餘額尚未明確，視實作決定。

### Required Data

- 自身假期餘額（API-010）
