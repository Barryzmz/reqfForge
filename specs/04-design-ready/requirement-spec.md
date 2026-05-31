# Requirement Specification

## Metadata

- **Project**: 員工請假管理系統
- **Version**: 1.0.0-draft
- **Date**: 2026-05-31
- **Sources**: SRC-001（PM 初次訪談紀錄）、SRC-002（特休年資對照表，以驗證情境假設代入）

---

## Scope

### In Scope

- 員工線上申請請假（特休、病假、事假、喪假）
- 主管線上審核請假申請（同意 / 拒絕）
- 系統自動催審提醒（超過 3 天未審核）
- HR 查看全員假期紀錄
- HR 匯出 Excel 格式假期報表
- 員工取消「待審核」狀態的申請
- 主管設定代理主管（含代理期間管理）
- 假期餘額追蹤（各假別剩餘天數）
- 申請日期重疊與餘額不足的驗證

### Out of Scope

- 薪資計算或薪資單產出
- 排班或工時管理
- 系統管理員角色與後台管理功能（來源未提及）

### 未解決事項（不影響主流程，列入下版）

- Q-008：員工申請時是否即時顯示剩餘假期天數（Open）

---

## User Roles

| Role ID | 角色 | 說明 |
| --- | --- | --- |
| ROLE-001 | 員工（Employee） | 發起請假申請、取消待審核申請、查看自身假期紀錄 |
| ROLE-002 | 主管（Manager） | 審核管轄員工的請假申請、設定代理主管 |
| ROLE-003 | HR | 查看全員假期紀錄、匯出假期報表 |

---

## Requirements

### Functional Requirements

| ID | 需求摘要 | Actor | Priority | Source | Acceptance Criteria | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | 員工可填寫請假申請（開始日期、結束日期、假別、原因），最小單位 0.5 天，送出後狀態為「待審核」 | Employee | High | SRC-001 / FACT-005、013 / Q-009 | AC-001、AC-002、AC-003 | Confirmed |
| FR-002 | 員工申請病假超過 3 天需上傳診斷書，3 天以內不強制 | Employee | High | SRC-001 / FACT-014 / Q-001 / DEC-001 | AC-004、AC-005、AC-006 | Confirmed |
| FR-003 | 主管可同意或拒絕管轄員工的請假申請；拒絕需填寫原因 | Manager | High | SRC-001 / FACT-006、015、016 / Q-003、004 | AC-007、AC-008、AC-009 | Confirmed |
| FR-004 | 申請送出超過 3 天未審核，系統向主管發送系統內通知與 Email | System | High | SRC-001 / FACT-017 / Q-002 / DEC-002 | AC-010 | Confirmed |
| FR-005 | HR 可查看所有員工的請假申請紀錄 | HR | High | SRC-001 / FACT-007 | AC-011 | Confirmed |
| FR-006 | HR 可匯出 Excel 格式假期報表（指定欄位） | HR | Medium | SRC-001 / FACT-018 / Q-005 / DEC-005 | AC-012 | Confirmed |
| FR-007 | 員工可取消「待審核」狀態的申請；已審核申請不可取消 | Employee | Medium | Q-010 / DEC-009 | AC-013、AC-014 | Confirmed |
| FR-008 | 主管可設定代理人與代理期間；代理期間代理人擁有對等審核權限 | Manager | Medium | Q-004 / DEC-004 | AC-015、AC-016 | Confirmed |

---

### Business Rules

| ID | 規則 | 條件 | 預期結果 | Source | Status |
| --- | --- | --- | --- | --- | --- |
| BR-001 | 病假上限一年 30 天 | 員工申請病假時 | 超出上限則拒絕（見 BR-011） | SRC-001 / FACT-010 / ASM-001 | Confirmed |
| BR-002 | 事假上限一年 14 天 | 員工申請事假時 | 超出上限則拒絕（見 BR-011） | SRC-001 / FACT-011 / ASM-001 | Confirmed |
| BR-003 | 喪假依親等計算：父母/配偶 8 天；祖父母/子女/配偶父母 6 天；兄弟姊妹/配偶祖父母 3 天 | 員工申請喪假時 | 依親等給予對應天數；親等不在範圍則拒絕（見 BR-014） | SRC-001 / FACT-012 / Q-007 / DEC-007 | Confirmed |
| BR-004 | 特休依年資計算：6個月~1年3天；1~2年7天；2~3年10天；3~5年14天；5~10年15天；10年以上每年+1天上限30天 | 員工申請特休時 | 依年資給予對應天數 | SRC-001 / FACT-009 / Q-006 / DEC-006 | Confirmed |
| BR-005 | 主管拒絕申請時必須填寫拒絕原因 | 主管執行拒絕動作 | 未填寫原因時系統拒絕提交 | SRC-001 / FACT-016 | Confirmed |
| BR-006 | 申請送出後超過 3 天未審核，系統觸發催審（系統通知 + Email） | 申請為「待審核」且超過 3 天 | 主管收到催審通知；申請狀態不變 | SRC-001 / FACT-017 / Q-002 / DEC-002 | Confirmed |
| BR-007 | 病假申請超過 3 天須附診斷書，3 天以內不強制 | 員工申請病假 | 超過 3 天未附診斷書時系統拒絕提交 | SRC-001 / FACT-014 / Q-001 / DEC-001 | Confirmed |
| BR-008 | 請假最小申請單位為 0.5 天 | 員工填寫請假日期 | 系統支援 0.5 天為最小單位 | Q-009 / DEC-008 | Confirmed |
| BR-009 | 跨部門員工的申請由主要部門主管審核 | 員工屬於多個部門 | 僅主要部門主管可審核 | SRC-001 / FACT-019 / Q-003 / DEC-003 | Confirmed |
| BR-010 | 代理主管的審核範圍限定於被代理主管管轄員工；代理期間結束後自動失效 | 代理主管代為審核 | 代理期間外嘗試審核時系統拒絕 | Q-004 / DEC-004 | Confirmed |
| BR-011 | 申請天數超過假期餘額時系統拒絕送出並提示剩餘天數 | 員工送出申請時 | 超過餘額或餘額為 0 均拒絕 | EC-001、EC-009 / DEC-011 | Confirmed |
| BR-012 | 申請日期與現有申請重疊時系統拒絕送出並提示衝突 | 員工送出申請時 | 重疊申請被拒絕 | EC-007 / DEC-014 | Confirmed |
| BR-013 | 代理期間結束時仍有未審核申請，回歸被代理主管的待審核清單 | 代理期間到期時 | 申請不遺失，責任回歸原主管 | EC-005 / DEC-013 | Confirmed |
| BR-014 | 申請喪假親等不在對照表範圍內時系統拒絕並提示聯繫 HR | 員工申請喪假時 | 非支援親等被拒絕 | EC-010 / DEC-015 | Confirmed |
| BR-015 | 主管不可將自己設定為代理人 | 主管設定代理主管時 | 系統拒絕自我代理設定 | EC-012 / DEC-016 | Confirmed |

---

### Data Requirements

| ID | 資料需求 | 實體 / 欄位 | 格式或限制 | Source | Status |
| --- | --- | --- | --- | --- | --- |
| DR-001 | 請假申請需記錄開始日期 | LeaveRequest.開始日期 | 日期格式，不得晚於結束日期 | SRC-001 / FACT-013 | Confirmed |
| DR-002 | 請假申請需記錄結束日期 | LeaveRequest.結束日期 | 日期格式，不得早於開始日期 | SRC-001 / FACT-013 | Confirmed |
| DR-003 | 請假申請需記錄假別 | LeaveRequest.假別 | 枚舉：特休 / 病假 / 事假 / 喪假 | SRC-001 / FACT-008、013 | Confirmed |
| DR-004 | 請假申請需記錄原因（必填） | LeaveRequest.原因 | 文字欄位 | SRC-001 / FACT-013 | Confirmed |
| DR-005 | 病假超過 3 天需儲存診斷書附件 | LeaveRequest.附件 | 檔案（格式與大小限制尚未確認） | SRC-001 / FACT-014 / Q-001 | Confirmed |
| DR-006 | 拒絕申請需記錄拒絕原因（拒絕時必填） | ReviewRecord.拒絕原因 | 文字欄位 | SRC-001 / FACT-016 | Confirmed |
| DR-007 | 審核需記錄審核時間與審核人 | ReviewRecord.審核時間、審核人 | 時間戳記、人員參照 | SRC-001 / FACT-015、016 | Confirmed |
| DR-008 | 需記錄各員工各假別的假期餘額，最小單位 0.5 天，不得為負數 | LeaveBalance.員工、假別、剩餘天數、年度 | 數值，≥ 0，單位 0.5 天 | SRC-001 / FACT-010、011 / Q-009 | Confirmed |
| DR-009 | 員工需標記主要部門 | Employee.主要部門 | 部門參照 | Q-003 / DEC-003 | Confirmed |
| DR-010 | 代理主管設定需記錄代理人、代理起訖日期 | ManagerDelegate.主管、代理人、起始日、結束日 | 結束日不得早於起始日；代理人不可為自己 | Q-004 / DEC-004、DEC-016 | Confirmed |
| DR-011 | 假期報表欄位：員工姓名、部門、假別、開始日期、結束日期、天數、狀態、申請日期 | 報表匯出欄位 | Excel 格式 | Q-005 / DEC-005 | Confirmed |

---

### Workflow Requirements

| ID | 流程需求 | From State | Action | To State | Actor | Source | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WR-001 | 員工送出申請後，狀態設為「待審核」 | （初始） | 員工送出申請 | 待審核 | Employee | SRC-001 / FACT-005 | Confirmed |
| WR-002 | 主管同意後，狀態更新為「已核准」 | 待審核 | 主管同意 | 已核准 | Manager | SRC-001 / FACT-015 | Confirmed |
| WR-003 | 主管拒絕（含填寫原因）後，狀態更新為「已拒絕」 | 待審核 | 主管拒絕 | 已拒絕 | Manager | SRC-001 / FACT-015、016 | Confirmed |
| WR-004 | 超過 3 天未審核，系統發催審通知；申請狀態不變 | 待審核 | 系統觸發催審 | 待審核 | System | SRC-001 / FACT-017 / Q-002 | Confirmed |
| WR-005 | 員工取消「待審核」申請後，狀態更新為「已取消」 | 待審核 | 員工取消 | 已取消 | Employee | Q-010 / DEC-009 | Confirmed |

**不合法轉換（系統應拒絕）：**

| 起始狀態 | 嘗試動作 | 系統行為 |
| --- | --- | --- |
| 已核准 / 已拒絕 | 員工取消 | 拒絕，提示無法取消已審核申請 |
| 已取消 | 主管審核 | 拒絕，申請已取消 |

---

### Permission Requirements

| ID | 角色 | 可執行動作 | 限制範圍 | Source | Status |
| --- | --- | --- | --- | --- | --- |
| PR-001 | Employee | 建立請假申請 | 僅可為自己申請 | SRC-001 / FACT-005 | Confirmed |
| PR-002 | Employee | 查看自身請假申請紀錄 | 禁止查看其他員工的紀錄 | Q-011 / DEC-010 | Confirmed |
| PR-003 | Employee | 取消「待審核」狀態的申請 | 僅限「待審核」狀態 | Q-010 / DEC-009 | Confirmed |
| PR-004 | Manager | 審核管轄員工的請假申請（同意或拒絕） | 僅限管轄員工（跨部門以主要部門為準）；含代理期間擴展範圍 | SRC-001 / FACT-006 / Q-003、004 | Confirmed |
| PR-005 | 代理主管 | 於代理期間內審核被代理主管管轄員工的申請 | 代理期間限定；代理期間結束後自動失效 | Q-004 / DEC-004 | Confirmed |
| PR-006 | HR | 查看所有員工的請假申請紀錄 | — | SRC-001 / FACT-007 | Confirmed |
| PR-007 | HR | 匯出 Excel 格式假期報表 | — | SRC-001 / FACT-018 / Q-005 | Confirmed |

---

### Non-functional Requirements

本版本無已確認的非功能需求。來源（SRC-001）未提及效能、安全性、可用性等需求，待後續釐清後補充。

---

## Domain Model Summary

| 實體 | 主要屬性 | 關聯需求 |
| --- | --- | --- |
| Employee | ID、姓名、主要部門、角色、年資 | FR-001、PR-001 ~ PR-003、DR-009 |
| Department | ID、名稱、主管 | BR-009、DR-009 |
| LeaveRequest | ID、申請員工、假別、開始日期、結束日期、天數、原因、附件、狀態、申請時間 | FR-001 ~ FR-003、FR-007、WR-001 ~ WR-005 |
| ReviewRecord | ID、關聯申請、審核人、審核結果、拒絕原因、審核時間 | FR-003、DR-006、DR-007 |
| LeaveBalance | 員工、假別、剩餘天數、年度 | BR-001 ~ BR-004、BR-011、DR-008 |
| ManagerDelegate | 被代理主管、代理人、代理起始日、代理結束日 | FR-008、BR-010、BR-013、BR-015、DR-010 |

完整實體關係定義請見 `specs/03-analysis/domain-model.md`。

---

## State Transitions Summary

LeaveRequest 狀態：**待審核 → 已核准 / 已拒絕 / 已取消**

完整狀態機與不合法轉換定義請見 `specs/03-analysis/state-transitions.md`。

---

## Edge Cases Summary

| Edge Case ID | 情境 | 處理方式 |
| --- | --- | --- |
| EC-001 / EC-009 | 申請天數超過餘額或餘額為 0 | 拒絕送出，提示剩餘天數（BR-011） |
| EC-002 | 病假恰好 3 天 | 視為「3 天以內」，不需診斷書（BR-007） |
| EC-003 | 病假 3.5 天 | 超過 3 天，需診斷書（BR-007） |
| EC-004 | 主管請假且未設代理 | 申請維持待審核，催審機制自然觸發（BR-006） |
| EC-005 | 代理到期有殘留待審申請 | 回歸被代理主管待審清單（BR-013） |
| EC-006 | 跨部門員工，主要部門主管在代理期間 | 由代理主管審核（BR-009、BR-010） |
| EC-007 | 申請日期與現有申請重疊 | 拒絕送出，提示重疊（BR-012） |
| EC-008 | 結束日期早於開始日期 | 拒絕送出，提示日期錯誤（DR-001、DR-002） |
| EC-010 | 喪假親等不在對照表 | 拒絕送出，提示聯繫 HR（BR-014） |
| EC-011 | 代理結束日早於起始日 | 拒絕儲存，提示日期錯誤（DR-010） |
| EC-012 | 主管自我代理 | 系統拒絕（BR-015） |

完整 edge case 定義請見 `specs/03-analysis/edge-cases.md`。

---

## Traceability

| Requirement ID | Source ID | Fact ID | Decision ID |
| --- | --- | --- | --- |
| FR-001 | SRC-001 | FACT-005、FACT-013 | DEC-008 |
| FR-002 | SRC-001 | FACT-014 | DEC-001 |
| FR-003 | SRC-001 | FACT-006、FACT-015、FACT-016 | DEC-003、DEC-004 |
| FR-004 | SRC-001 | FACT-017 | DEC-002 |
| FR-005 | SRC-001 | FACT-007 | — |
| FR-006 | SRC-001 | FACT-018 | DEC-005 |
| FR-007 | — | — | DEC-009 |
| FR-008 | — | FACT-020 | DEC-004 |
| BR-001 | SRC-001 | FACT-010 | — |
| BR-002 | SRC-001 | FACT-011 | — |
| BR-003 | SRC-001 | FACT-012 | DEC-007 |
| BR-004 | SRC-001 | FACT-009 | DEC-006 |
| BR-005 | SRC-001 | FACT-016 | — |
| BR-006 | SRC-001 | FACT-017 | DEC-002 |
| BR-007 | SRC-001 | FACT-014 | DEC-001 |
| BR-008 | — | — | DEC-008 |
| BR-009 | SRC-001 | FACT-019 | DEC-003 |
| BR-010 | — | FACT-020 | DEC-004 |
| BR-011 | — | FACT-010、FACT-011 | DEC-011 |
| BR-012 | — | — | DEC-014 |
| BR-013 | — | FACT-020 | DEC-013 |
| BR-014 | SRC-001 | FACT-012 | DEC-015 |
| BR-015 | — | — | DEC-016 |
| DR-001 ~ DR-004 | SRC-001 | FACT-013 | — |
| DR-005 | SRC-001 | FACT-014 | DEC-001 |
| DR-006 ~ DR-007 | SRC-001 | FACT-015、FACT-016 | — |
| DR-008 | SRC-001 | FACT-010、FACT-011 | DEC-008 |
| DR-009 | SRC-001 | FACT-019 | DEC-003 |
| DR-010 | — | FACT-020 | DEC-004、DEC-016 |
| DR-011 | SRC-001 | FACT-018 | DEC-005 |
| WR-001 | SRC-001 | FACT-005 | — |
| WR-002 | SRC-001 | FACT-015 | — |
| WR-003 | SRC-001 | FACT-015、FACT-016 | — |
| WR-004 | SRC-001 | FACT-017 | DEC-002 |
| WR-005 | — | — | DEC-009 |
| PR-001 | SRC-001 | FACT-005 | — |
| PR-002 | — | — | DEC-010 |
| PR-003 | — | — | DEC-009 |
| PR-004 | SRC-001 | FACT-006 | DEC-003、DEC-004 |
| PR-005 | — | FACT-020 | DEC-004 |
| PR-006 | SRC-001 | FACT-007 | — |
| PR-007 | SRC-001 | FACT-018 | DEC-005 |
