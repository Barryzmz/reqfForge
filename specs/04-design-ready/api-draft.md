# API Draft

API 草案只能對應已確認需求。每個端點都追溯至需求 ID。

## API 清單

| API ID | Method | Path | 用途 | 關聯需求 |
| --- | --- | --- | --- | --- |
| API-001 | POST | /api/leaves | 員工送出請假申請 | FR-001、FR-002、BR-007、BR-008、BR-011、BR-012 |
| API-002 | GET | /api/leaves | 員工查看自身請假紀錄 | FR-005（員工視角）、PR-002 |
| API-003 | GET | /api/leaves/:id | 查看單筆請假申請詳情 | PR-002、PR-004 |
| API-004 | PATCH | /api/leaves/:id/cancel | 員工取消待審核申請 | FR-007、WR-005、PR-003 |
| API-005 | POST | /api/leaves/:id/review | 主管審核請假申請 | FR-003、BR-005、BR-009、BR-010、WR-002、WR-003 |
| API-006 | GET | /api/hr/leaves | HR 查看全員請假紀錄 | FR-005、PR-006 |
| API-007 | GET | /api/hr/leaves/export | HR 匯出 Excel 報表 | FR-006、DR-011、PR-007 |
| API-008 | POST | /api/delegates | 主管設定代理主管 | FR-008、BR-010、BR-015、DR-010 |
| API-009 | GET | /api/delegates/me | 主管查看自己的代理設定 | FR-008、DR-010 |
| API-010 | GET | /api/leave-balances/me | 員工查看自身假期餘額 | DR-008、BR-001 ~ BR-004 |

---

## API-001：送出請假申請

- **Related Requirements**: FR-001、FR-002、BR-007、BR-008、BR-011、BR-012
- **Method**: POST
- **Path**: /api/leaves
- **Auth Required**: Yes（Employee）

### Request

```json
{
  "leave_type": "sick",
  "start_date": "2026-06-01",
  "end_date": "2026-06-03",
  "duration_days": 2.5,
  "reason": "就醫",
  "attachment_url": "https://..."
}
```

> `leave_type` 枚舉：annual（特休）/ sick（病假）/ personal（事假）/ bereavement（喪假）
> `duration_days` 最小單位 0.5（BR-008）
> `attachment_url` 僅在 sick leave 且 duration_days > 3 時為必填（BR-007）

### Response

```json
{
  "id": "lr-001",
  "status": "pending_review",
  "created_at": "2026-06-01T09:00:00Z"
}
```

### Errors

| Status | Code | Message | Condition | Related Requirement |
| --- | --- | --- | --- | --- |
| 400 | MISSING_FIELD | 必填欄位缺漏 | 任一必填欄位為空 | FR-001 |
| 400 | ATTACHMENT_REQUIRED | 病假超過 3 天需附診斷書 | sick leave，duration > 3，無附件 | FR-002、BR-007 |
| 400 | INSUFFICIENT_BALANCE | 假期餘額不足 | 申請天數超過剩餘餘額 | BR-011 |
| 400 | DATE_OVERLAP | 申請日期與現有申請重疊 | 日期與已有申請衝突 | BR-012 |
| 400 | INVALID_DATE_RANGE | 結束日期早於開始日期 | end_date < start_date | DR-001、DR-002 |
| 400 | UNSUPPORTED_BEREAVEMENT_RELATION | 親等不在支援範圍 | 喪假申請，親等不在對照表 | BR-014 |

---

## API-002：查看自身請假紀錄

- **Related Requirements**: PR-002
- **Method**: GET
- **Path**: /api/leaves
- **Auth Required**: Yes（Employee）

### Response

```json
{
  "data": [
    {
      "id": "lr-001",
      "leave_type": "sick",
      "start_date": "2026-06-01",
      "end_date": "2026-06-03",
      "duration_days": 2.5,
      "status": "pending_review",
      "created_at": "2026-06-01T09:00:00Z"
    }
  ]
}
```

> 僅回傳當前登入員工自身的申請紀錄（PR-002）

---

## API-003：查看單筆請假申請

- **Related Requirements**: PR-002、PR-004
- **Method**: GET
- **Path**: /api/leaves/:id
- **Auth Required**: Yes（Employee 只可查自己；Manager 只可查管轄員工）

### Response

```json
{
  "id": "lr-001",
  "applicant": { "id": "emp-001", "name": "王小明" },
  "leave_type": "sick",
  "start_date": "2026-06-01",
  "end_date": "2026-06-03",
  "duration_days": 2.5,
  "reason": "就醫",
  "attachment_url": "https://...",
  "status": "pending_review",
  "review_record": null,
  "created_at": "2026-06-01T09:00:00Z"
}
```

### Errors

| Status | Code | Message | Condition | Related Requirement |
| --- | --- | --- | --- | --- |
| 403 | FORBIDDEN | 無權查看此申請 | Employee 查看他人申請；Manager 查看非管轄員工申請 | PR-002、PR-004 |
| 404 | NOT_FOUND | 申請不存在 | ID 無效 | — |

---

## API-004：取消請假申請

- **Related Requirements**: FR-007、WR-005、PR-003
- **Method**: PATCH
- **Path**: /api/leaves/:id/cancel
- **Auth Required**: Yes（Employee，僅限本人申請）

### Response

```json
{
  "id": "lr-001",
  "status": "cancelled"
}
```

### Errors

| Status | Code | Message | Condition | Related Requirement |
| --- | --- | --- | --- | --- |
| 400 | INVALID_STATE | 只有待審核的申請可以取消 | 申請狀態非 pending_review | FR-007、WR-005 |
| 403 | FORBIDDEN | 只能取消自己的申請 | 非申請人嘗試取消 | PR-003 |

---

## API-005：主管審核請假申請

- **Related Requirements**: FR-003、BR-005、WR-002、WR-003、PR-004、PR-005
- **Method**: POST
- **Path**: /api/leaves/:id/review
- **Auth Required**: Yes（Manager 或有效代理主管）

### Request

```json
{
  "decision": "approved",
  "rejection_reason": null
}
```

> `decision` 枚舉：approved / rejected
> `rejection_reason` 在 decision 為 rejected 時為必填（BR-005）

### Response

```json
{
  "id": "lr-001",
  "status": "approved",
  "reviewed_by": "mgr-001",
  "reviewed_at": "2026-06-04T10:00:00Z"
}
```

### Errors

| Status | Code | Message | Condition | Related Requirement |
| --- | --- | --- | --- | --- |
| 400 | REJECTION_REASON_REQUIRED | 拒絕時需填寫原因 | decision=rejected，rejection_reason 為空 | BR-005 |
| 403 | FORBIDDEN | 無審核權限 | 非管轄員工的申請；代理期間已結束 | PR-004、PR-005、BR-010 |
| 400 | INVALID_STATE | 申請狀態不可審核 | 申請非 pending_review 狀態 | WR-002、WR-003 |

---

## API-006：HR 查看全員請假紀錄

- **Related Requirements**: FR-005、PR-006
- **Method**: GET
- **Path**: /api/hr/leaves
- **Auth Required**: Yes（HR）

### Response

```json
{
  "data": [
    {
      "id": "lr-001",
      "applicant": { "id": "emp-001", "name": "王小明", "department": "工程部" },
      "leave_type": "sick",
      "start_date": "2026-06-01",
      "end_date": "2026-06-03",
      "duration_days": 2.5,
      "status": "approved",
      "created_at": "2026-06-01T09:00:00Z"
    }
  ]
}
```

---

## API-007：HR 匯出假期報表

- **Related Requirements**: FR-006、DR-011、PR-007
- **Method**: GET
- **Path**: /api/hr/leaves/export
- **Auth Required**: Yes（HR）

### Response

Excel 檔案下載（Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet）

欄位：員工姓名、部門、假別、開始日期、結束日期、天數、狀態、申請日期（DR-011）

---

## API-008：主管設定代理主管

- **Related Requirements**: FR-008、BR-010、BR-015、DR-010
- **Method**: POST
- **Path**: /api/delegates
- **Auth Required**: Yes（Manager）

### Request

```json
{
  "delegate_id": "emp-002",
  "start_date": "2026-06-10",
  "end_date": "2026-06-14"
}
```

### Errors

| Status | Code | Message | Condition | Related Requirement |
| --- | --- | --- | --- | --- |
| 400 | SELF_DELEGATE | 代理人不可為自己 | delegate_id = 自己的 ID | BR-015 |
| 400 | INVALID_DATE_RANGE | 結束日期早於起始日期 | end_date < start_date | DR-010 |

---

## API-009：查看代理設定

- **Related Requirements**: FR-008、DR-010
- **Method**: GET
- **Path**: /api/delegates/me
- **Auth Required**: Yes（Manager）

### Response

```json
{
  "delegate": { "id": "emp-002", "name": "李大華" },
  "start_date": "2026-06-10",
  "end_date": "2026-06-14",
  "is_active": false
}
```

---

## API-010：查看自身假期餘額

- **Related Requirements**: DR-008、BR-001 ~ BR-004
- **Method**: GET
- **Path**: /api/leave-balances/me
- **Auth Required**: Yes（Employee）

### Response

```json
{
  "balances": [
    { "leave_type": "annual", "remaining_days": 7.5, "year": 2026 },
    { "leave_type": "sick", "remaining_days": 28.0, "year": 2026 },
    { "leave_type": "personal", "remaining_days": 14.0, "year": 2026 }
  ]
}
```
