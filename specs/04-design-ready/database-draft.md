# Database Draft

資料庫草案只能根據已確認資料需求產生。每個欄位追溯至需求 ID。

## 資料表清單

| Table ID | Table Name | 用途 | 關聯需求 |
| --- | --- | --- | --- |
| TBL-001 | employees | 員工基本資料 | DR-009、ROLE-001 ~ ROLE-003 |
| TBL-002 | departments | 部門資料 | DR-009、BR-009 |
| TBL-003 | leave_requests | 請假申請主表 | DR-001 ~ DR-005 |
| TBL-004 | review_records | 審核紀錄 | DR-006、DR-007 |
| TBL-005 | leave_balances | 假期餘額 | DR-008 |
| TBL-006 | manager_delegates | 代理主管設定 | DR-010 |

---

## TBL-001：employees

- **Related Requirements**: DR-009、ENT-001
- **Purpose**: 儲存員工基本資料、角色與主要部門

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| name | VARCHAR(100) | Yes | — | — | DR-011 |
| role | ENUM('employee','manager','hr') | Yes | 'employee' | 可複合，建議以 role flags 或 junction table 處理多角色 | ROLE-001 ~ ROLE-003 |
| primary_department_id | UUID | Yes | — | FK → departments.id | DR-009、BR-009 |
| seniority_months | INTEGER | Yes | 0 | 月資，用於計算特休天數 | BR-004 |
| created_at | TIMESTAMPTZ | Yes | now() | — | — |
| updated_at | TIMESTAMPTZ | Yes | now() | — | — |

### Indexes

| Index Name | Columns | Unique | Purpose |
| --- | --- | --- | --- |
| IDX_employees_department | primary_department_id | No | 依部門查詢員工 |

---

## TBL-002：departments

- **Related Requirements**: DR-009、BR-009、ENT-002
- **Purpose**: 儲存部門資訊與負責主管

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| name | VARCHAR(100) | Yes | — | — | DR-011 |
| manager_id | UUID | Yes | — | FK → employees.id | BR-009 |
| created_at | TIMESTAMPTZ | Yes | now() | — | — |

---

## TBL-003：leave_requests

- **Related Requirements**: DR-001 ~ DR-005、WR-001 ~ WR-005、ENT-003
- **Purpose**: 儲存請假申請主表，包含申請內容與狀態

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| employee_id | UUID | Yes | — | FK → employees.id | FR-001 |
| leave_type | ENUM('annual','sick','personal','bereavement') | Yes | — | — | DR-003 |
| start_date | DATE | Yes | — | 不得晚於 end_date | DR-001 |
| end_date | DATE | Yes | — | 不得早於 start_date | DR-002 |
| duration_days | NUMERIC(4,1) | Yes | — | 最小 0.5，不得為負數 | BR-008 |
| reason | TEXT | Yes | — | 必填 | DR-004 |
| attachment_url | TEXT | No | NULL | 病假 duration > 3 時必填 | DR-005、BR-007 |
| status | ENUM('pending_review','approved','rejected','cancelled') | Yes | 'pending_review' | 狀態機見 WR-001 ~ WR-005 | WR-001 |
| created_at | TIMESTAMPTZ | Yes | now() | — | DR-011 |
| updated_at | TIMESTAMPTZ | Yes | now() | — | — |

### Indexes

| Index Name | Columns | Unique | Purpose |
| --- | --- | --- | --- |
| IDX_lr_employee | employee_id | No | 查詢特定員工申請 |
| IDX_lr_status | status | No | 過濾待審核申請（催審 Scheduler） |
| IDX_lr_created_at | created_at | No | 催審時間計算 |

### Relationships

| From | To | Cardinality | Rule |
| --- | --- | --- | --- |
| leave_requests.employee_id | employees.id | Many-to-One | 一位員工可有多筆申請 |

---

## TBL-004：review_records

- **Related Requirements**: DR-006、DR-007、ENT-004
- **Purpose**: 儲存主管對請假申請的審核動作與結果

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| leave_request_id | UUID | Yes | — | FK → leave_requests.id，Unique | FR-003 |
| reviewer_id | UUID | Yes | — | FK → employees.id（可為代理主管） | DR-007 |
| decision | ENUM('approved','rejected') | Yes | — | — | FR-003 |
| rejection_reason | TEXT | No | NULL | decision = rejected 時必填 | DR-006、BR-005 |
| reviewed_at | TIMESTAMPTZ | Yes | now() | — | DR-007 |

### Relationships

| From | To | Cardinality | Rule |
| --- | --- | --- | --- |
| review_records.leave_request_id | leave_requests.id | One-to-One | 一筆申請對應一筆審核紀錄 |
| review_records.reviewer_id | employees.id | Many-to-One | — |

---

## TBL-005：leave_balances

- **Related Requirements**: DR-008、BR-001 ~ BR-004、BR-011、ENT-005
- **Purpose**: 記錄各員工各假別年度假期餘額

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| employee_id | UUID | Yes | — | FK → employees.id | DR-008 |
| leave_type | ENUM('annual','sick','personal','bereavement') | Yes | — | — | DR-008 |
| year | INTEGER | Yes | — | 年度 | DR-008 |
| total_days | NUMERIC(4,1) | Yes | — | 年度總配額 | BR-001 ~ BR-004 |
| used_days | NUMERIC(4,1) | Yes | 0 | 已使用天數 | DR-008 |
| remaining_days | NUMERIC(4,1) | Yes | — | 計算欄位：total_days - used_days，≥ 0 | BR-011 |

### Indexes

| Index Name | Columns | Unique | Purpose |
| --- | --- | --- | --- |
| IDX_lb_employee_type_year | employee_id, leave_type, year | Yes | 確保每位員工每年每假別只有一筆 |

---

## TBL-006：manager_delegates

- **Related Requirements**: DR-010、FR-008、BR-010、BR-013、BR-015、ENT-006
- **Purpose**: 儲存主管的代理主管設定

| Column | Type | Required | Default | Rule | Related Requirement |
| --- | --- | --- | --- | --- | --- |
| id | UUID | Yes | gen_random_uuid() | PK | — |
| manager_id | UUID | Yes | — | FK → employees.id | DR-010 |
| delegate_id | UUID | Yes | — | FK → employees.id；不可等於 manager_id | BR-015、DR-010 |
| start_date | DATE | Yes | — | 不得晚於 end_date | DR-010 |
| end_date | DATE | Yes | — | 不得早於 start_date | DR-010 |
| created_at | TIMESTAMPTZ | Yes | now() | — | — |

### Indexes

| Index Name | Columns | Unique | Purpose |
| --- | --- | --- | --- |
| IDX_md_manager_active | manager_id, end_date | No | 查詢某主管的現行代理設定 |

### Relationships

| From | To | Cardinality | Rule |
| --- | --- | --- | --- |
| manager_delegates.manager_id | employees.id | Many-to-One | 主管可有多組歷史代理設定 |
| manager_delegates.delegate_id | employees.id | Many-to-One | — |
