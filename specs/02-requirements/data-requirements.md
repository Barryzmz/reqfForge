# Data Requirements

| ID | 資料需求 | 資料欄位或實體 | 格式或限制 | 來源 | 狀態 |
| --- | --- | --- | --- | --- | --- |
| DR-001 | 請假申請需記錄開始日期 | 請假申請（LeaveRequest）.開始日期 | 日期格式，不得晚於結束日期 | SRC-001 / FACT-013 | Confirmed |
| DR-002 | 請假申請需記錄結束日期 | 請假申請（LeaveRequest）.結束日期 | 日期格式，不得早於開始日期 | SRC-001 / FACT-013 | Confirmed |
| DR-003 | 請假申請需記錄假別 | 請假申請（LeaveRequest）.假別 | 枚舉：特休、病假、事假、喪假 | SRC-001 / FACT-008 / FACT-013 | Confirmed |
| DR-004 | 請假申請需記錄申請原因 | 請假申請（LeaveRequest）.原因 | 文字欄位，必填 | SRC-001 / FACT-013 | Confirmed |
| DR-005 | 病假申請超過 3 天需儲存診斷書附件 | 請假申請（LeaveRequest）.附件 | 檔案，格式與大小限制尚未確認 | SRC-001 / FACT-014 / Q-001 | Confirmed（附件格式限制尚未確認） |
| DR-006 | 主管拒絕申請時需記錄拒絕原因 | 審核紀錄（ReviewRecord）.拒絕原因 | 文字欄位，拒絕時必填 | SRC-001 / FACT-016 | Confirmed |
| DR-007 | 審核需記錄審核時間與審核人 | 審核紀錄（ReviewRecord）.審核時間、審核人 | 時間戳記、人員參照 | SRC-001 / FACT-015 / FACT-016 | Confirmed |
| DR-008 | 需記錄各員工各假別的剩餘天數（假期餘額），最小單位 0.5 天 | 假期餘額（LeaveBalance）.員工、假別、剩餘天數 | 數值，最小單位 0.5，不得為負數 | SRC-001 / FACT-010 / FACT-011 / Q-009 | Confirmed |
| DR-009 | 需記錄員工主要部門資訊 | 員工（Employee）.主要部門 | 部門參照，跨部門員工需明確標記主要部門 | Q-003 | Confirmed |
| DR-010 | 需記錄代理主管設定（代理人、代理起訖日期） | 代理設定（ManagerDelegate）.主管、代理人、代理起始日、代理結束日 | 日期範圍，代理結束日不得早於代理起始日 | Q-004 | Confirmed |
| DR-011 | 假期報表需包含指定欄位 | 報表匯出欄位：員工姓名、部門、假別、開始日期、結束日期、天數、狀態、申請日期 | Excel 格式 | Q-005 | Confirmed |
