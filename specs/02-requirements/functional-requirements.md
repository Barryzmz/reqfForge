# Functional Requirements

正式功能需求只能記錄已確認內容。

---

## FR-001

| Field | Value |
| --- | --- |
| ID | FR-001 |
| Title | 員工發起請假申請 |
| Description | 員工可以在系統中填寫請假申請，包含開始日期、結束日期、假別與原因；最小申請單位為 0.5 天 |
| Actor | 員工（Employee） |
| Trigger | 員工選擇申請請假 |
| Preconditions | 員工已登入系統 |
| Source | SRC-001 / FACT-005 / FACT-013 / Q-009 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 員工已登入系統
When 員工填寫開始日期、結束日期、假別、原因並送出申請
Then 系統應建立一筆請假申請紀錄
And 申請狀態應為「待審核」
```

```gherkin
Given 員工填寫請假申請
When 員工未填寫必填欄位（開始日期、結束日期、假別、原因之一）
Then 系統應拒絕送出並提示缺漏欄位
```

```gherkin
Given 員工選擇申請天數
When 員工填寫日期範圍
Then 系統應支援以 0.5 天為最小單位的申請（例如半天假）
```

---

## FR-002

| Field | Value |
| --- | --- |
| ID | FR-002 |
| Title | 病假申請診斷書條件性上傳 |
| Description | 員工申請病假時，若請假天數超過 3 天，系統應要求上傳診斷書；3 天以內不強制 |
| Actor | 員工（Employee） |
| Trigger | 員工選擇假別為病假並送出申請 |
| Preconditions | 員工已登入系統、假別選擇為病假 |
| Source | SRC-001 / FACT-014 / Q-001 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 員工申請病假
When 請假天數超過 3 天且員工未上傳診斷書
Then 系統應拒絕送出並提示需上傳診斷書
```

```gherkin
Given 員工申請病假
When 請假天數為 3 天以內
Then 系統應允許不上傳診斷書直接送出申請
```

```gherkin
Given 員工申請病假且請假天數超過 3 天
When 員工上傳診斷書
Then 系統應儲存附件並與申請單關聯，允許送出申請
```

---

## FR-003

| Field | Value |
| --- | --- |
| ID | FR-003 |
| Title | 主管審核請假申請 |
| Description | 主管可以在系統中對員工的請假申請執行同意或拒絕；拒絕時需填寫原因；審核範圍為主管管轄員工（含代理期間擴展範圍） |
| Actor | 主管（Manager） |
| Trigger | 主管查看待審核的請假申請 |
| Preconditions | 主管已登入系統；存在狀態為「待審核」的請假申請屬於主管管轄員工 |
| Source | SRC-001 / FACT-006 / FACT-015 / FACT-016 / Q-003 / Q-004 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 主管查看一筆狀態為「待審核」的請假申請
When 主管選擇同意
Then 系統應將申請狀態更新為「已核准」
And 系統應記錄審核時間與審核人
```

```gherkin
Given 主管查看一筆狀態為「待審核」的請假申請
When 主管選擇拒絕並填寫拒絕原因
Then 系統應將申請狀態更新為「已拒絕」
And 系統應記錄拒絕原因、審核時間與審核人
```

```gherkin
Given 主管選擇拒絕
When 主管未填寫拒絕原因
Then 系統應拒絕送出並提示需填寫拒絕原因
```

---

## FR-004

| Field | Value |
| --- | --- |
| ID | FR-004 |
| Title | 系統催審提醒 |
| Description | 當請假申請送出後超過 3 天主管尚未審核，系統應同時透過系統內通知與 Email 發送催審提醒給負責審核的主管 |
| Actor | 系統（System） |
| Trigger | 請假申請送出後經過 3 天，申請狀態仍為「待審核」 |
| Preconditions | 請假申請狀態為「待審核」 |
| Source | SRC-001 / FACT-017 / Q-002 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 一筆請假申請狀態為「待審核」
When 申請送出後已超過 3 天
Then 系統應對負責審核的主管發送系統內通知
And 系統應同時發送 Email 通知給該主管
```

---

## FR-005

| Field | Value |
| --- | --- |
| ID | FR-005 |
| Title | HR 查看全員假期紀錄 |
| Description | HR 可以在系統中查看所有員工的假期申請紀錄 |
| Actor | HR |
| Trigger | HR 進入假期紀錄查詢頁面 |
| Preconditions | HR 已登入系統 |
| Source | SRC-001 / FACT-007 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given HR 已登入系統
When HR 查看假期紀錄
Then 系統應顯示所有員工的請假申請紀錄
```

---

## FR-006

| Field | Value |
| --- | --- |
| ID | FR-006 |
| Title | HR 匯出假期報表 |
| Description | HR 可以從系統匯出 Excel 格式的假期報表，欄位包含：員工姓名、部門、假別、開始日期、結束日期、天數、狀態、申請日期 |
| Actor | HR |
| Trigger | HR 選擇匯出報表 |
| Preconditions | HR 已登入系統 |
| Source | SRC-001 / FACT-018 / Q-005 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given HR 已登入系統
When HR 選擇匯出報表
Then 系統應產出 Excel 格式的報表檔案
And 報表欄位應包含：員工姓名、部門、假別、開始日期、結束日期、天數、狀態、申請日期
```

---

## FR-007

| Field | Value |
| --- | --- |
| ID | FR-007 |
| Title | 員工取消待審核的請假申請 |
| Description | 員工可以在申請狀態為「待審核」時取消自己的請假申請；不支援修改，需取消後重新申請 |
| Actor | 員工（Employee） |
| Trigger | 員工選擇取消一筆「待審核」狀態的申請 |
| Preconditions | 員工已登入系統；目標申請狀態為「待審核」 |
| Source | Q-010 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 員工查看一筆狀態為「待審核」的請假申請
When 員工選擇取消申請
Then 系統應將申請狀態更新為「已取消」
And 該申請不再出現於主管待審核清單中
```

```gherkin
Given 員工查看一筆狀態為「已核准」或「已拒絕」的請假申請
When 員工嘗試取消申請
Then 系統應拒絕操作並提示無法取消已審核的申請
```

---

## FR-008

| Field | Value |
| --- | --- |
| ID | FR-008 |
| Title | 主管指定代理主管 |
| Description | 主管可以在系統中指定代理人及代理期間；代理期間代理人可審核被代理主管管轄員工的請假申請 |
| Actor | 主管（Manager） |
| Trigger | 主管設定代理主管資訊 |
| Preconditions | 主管已登入系統 |
| Source | Q-004 |
| Status | Confirmed |

### Acceptance Criteria

```gherkin
Given 主管已登入系統
When 主管指定代理人並設定代理起訖日期
Then 系統應在代理期間內，允許代理人審核被代理主管管轄的員工請假申請
```

```gherkin
Given 代理期間已結束
When 代理人嘗試審核原被代理主管管轄員工的申請
Then 系統應拒絕操作並提示代理期間已結束
```
