---
description: 列出所有 ReqForge 可用的 skills 與對應用途
---

# rf-help — ReqForge 指令速查表

列出所有可用的 ReqForge skills。

## 執行

輸出以下速查表：

---

## ReqForge Skills 列表

| Skill | 用途 |
|-------|------|
| `rf-help` | 列出所有 skills（本頁）|
| `rf-status` | 掃描 specs/ 顯示各步驟完成狀態 |
| `rf-next` | 自動判斷目前進度，執行下一個未完成步驟 |
| `rf-discover` | 步驟 1：讀取 00-inputs，產出初步探索文件（01-discovery/）|
| `rf-extract` | 步驟 2：從探索結果提取正式需求（02-requirements/）|
| `rf-clarify` | 步驟 3：互動式 Q&A，釐清需求並回填文件 |
| `rf-analyze` | 步驟 4：分析需求，產出使用案例、領域模型等（03-analysis/）|
| `rf-spec` | 步驟 5：整合所有需求，生成需求規格書（requirement-spec.md）|
| `rf-design` | 步驟 6：生成 API、DB、前端、測試、開發任務文件（04-design-ready/）|
| `rf-log` | 步驟 7：更新 changelog 與 decision-log（05-versions/）|

## 呼叫方式

| 工具 | 呼叫格式 |
|------|---------|
| Claude Code | `/rf-discover`、`/rf-next` 等 slash commands |
| GitHub Copilot | `rf-discover`、`run rf-discover`、`run step 1` |
| Codex CLI | `rf-discover`、`run step 1` |

## 建議流程

```
rf-discover → rf-extract → rf-clarify → rf-analyze → rf-spec → rf-design → rf-log
```

不確定從哪裡開始？執行 `rf-status` 或 `rf-next`。
