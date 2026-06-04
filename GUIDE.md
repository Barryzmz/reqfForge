# SpecWingman 使用指南

SpecWingman 是一套結構化需求規格工作流程工具，協助 PM、開發者與 AI 協作者將非正式的輸入（口語描述、會議記錄、PDF、Excel 等），轉化為可追溯、可審計的正式需求規格文件。

---

## 核心原則

在開始使用前，請先理解最重要的一條規則：

> **禁止腦補** — 只記錄來源中明確提供的資訊。遇到不確定的地方，標記為「待確認問題」或「假設」，而非自行填補。

更多原則詳見 [CONSTITUTION.md](CONSTITUTION.md)。

---

## 目錄結構

```
specwingman/
├── .claude/
│   └── commands/     # Slash commands（/swm.help、/swm.status 等）
├── prompts/          # 7 個 AI 工作流程步驟的提示詞
├── specs/            # 所有產出文件（6 個階段）
│   ├── 00-inputs/    # 原始輸入資料
│   ├── 01-discovery/ # 初步探索產出
│   ├── 02-requirements/ # 正式需求
│   ├── 03-analysis/  # 分析文件
│   ├── 04-design-ready/ # 設計與開發文件
│   └── 05-versions/  # 版本與決策紀錄
├── templates/        # 可重用的 Markdown 範本
├── CONSTITUTION.md   # 核心原則與規則
└── GUIDE.md          # 本文件
```

---

## Slash Commands

在 Claude Code 中，每個步驟都有對應的 slash command，直接輸入即可執行：

| 指令 | 用途 |
|------|------|
| `/swm.help` | 列出所有指令 |
| `/swm.status` | 掃描 specs/ 顯示各步驟完成狀態 |
| `/swm.next` | 自動判斷目前進度並執行下一步 |
| `/swm.discover` | 步驟 1：讀取輸入 → 初步探索 |
| `/swm.extract` | 步驟 2：提取正式需求 |
| `/swm.clarify` | 步驟 3：啟動需求釐清 Q&A |
| `/swm.analyze` | 步驟 4：分析需求 |
| `/swm.spec` | 步驟 5：生成需求規格書 |
| `/swm.design` | 步驟 6：生成設計文件 |
| `/swm.log` | 步驟 7：更新版本紀錄 |

> **注意：** `/swm.clarify` 用於啟動提問流程。回答問題時直接在對話中回覆即可，不需再輸入指令。

---

## 跨 LLM 使用

SpecWingman 支援三種 AI 工具，核心 workflow（`prompts/`、`specs/`、`CONSTITUTION.md`）完全共用。

### Skills 架構（參考 spec-kit）

每個工作流步驟都有對應的 **Skill 檔案**，放在 `.github/skills/<skill-name>/SKILL.md`。
這是跨工具的通用格式 — Copilot、Codex CLI 都能直接讀取並執行。

```
.github/skills/
├── swm.discover/SKILL.md
├── swm.extract/SKILL.md
├── swm.clarify/SKILL.md
├── swm.analyze/SKILL.md
├── swm.spec/SKILL.md
├── swm.design/SKILL.md
├── swm.log/SKILL.md
├── swm.status/SKILL.md
├── swm.next/SKILL.md
└── swm.help/SKILL.md
```

### 各工具呼叫方式

| 工具 | 呼叫格式 | 設定檔 |
|------|---------|--------|
| **Claude Code** | `/swm.discover`、`/swm.next` 等 slash commands | `.claude/commands/` |
| **GitHub Copilot** | `swm.discover`、`run swm.discover`、`run step 1` | `.github/copilot-instructions.md` + `.github/skills/` |
| **OpenAI Codex CLI** | `swm.discover`、`run step 1` | `AGENTS.md` + `.github/skills/` |
| **其他 LLM** | 直接貼上對應的 `prompts/*.prompt.md` 內容 | — |

**注意：** `/swm.*` 格式的 slash commands 僅 Claude Code 支援。其他工具使用 skill 名稱（不帶斜線）觸發相同流程，結果與輸出格式完全一致。

---

## 完整工作流程

共 7 個步驟，每個步驟有對應的提示詞檔案（`prompts/0X-*.prompt.md`）與 slash command。

### 步驟 0：準備輸入資料

將需求來源放入 `specs/00-inputs/`：

- 將 PM 口頭描述、會議記錄、需求文件等整理並寫入 `specs/00-inputs/user-description.md`
- 若有多份來源（PDF、Excel、口述），分別標記來源 ID（S01、S02…）

---

### 步驟 1：讀取輸入 → 初步探索

**指令：** `/swm.discover`

**提示詞：** [prompts/01-read-inputs.prompt.md](prompts/01-read-inputs.prompt.md)

**輸入：** `CONSTITUTION.md` + `specs/00-inputs/`

**產出（`specs/01-discovery/`）：**

| 檔案 | 內容 |
|------|------|
| `source-summary.md` | 所有來源清單與 ID |
| `extracted-facts.md` | 直接來自來源的事實（不推論）|
| `open-questions.md` | 需要釐清的問題 |
| `assumptions.md` | 工作假設（使用前必須確認）|
| `glossary.md` | 術語定義 |

**注意：** 本步驟只做事實提取，不推論需求。

---

### 步驟 2：提取需求 → 正式需求

**指令：** `/swm.extract`

**提示詞：** [prompts/02-extract-requirements.prompt.md](prompts/02-extract-requirements.prompt.md)

**輸入：** `CONSTITUTION.md` + `specs/01-discovery/`

**產出（`specs/02-requirements/`）：**

| 檔案 | 需求 ID | 說明 |
|------|---------|------|
| `product-vision.md` | — | 產品願景 |
| `functional-requirements.md` | FR-### | 功能需求 |
| `business-rules.md` | BR-### | 業務規則 |
| `data-requirements.md` | DR-### | 資料需求 |
| `workflow-requirements.md` | WR-### | 流程需求 |
| `permission-requirements.md` | PR-### | 權限需求 |
| `non-functional-requirements.md` | NFR-### | 非功能需求 |
| `user-roles.md` | — | 使用者角色 |

---

### 步驟 3：釐清需求 → 確認問題

**指令：** `/swm.clarify`（啟動提問；回答問題時直接在對話中回覆即可）

**提示詞：** [prompts/03-clarify-requirements.prompt.md](prompts/03-clarify-requirements.prompt.md)

**輸入：** `CONSTITUTION.md` + `specs/01-discovery/` + `specs/02-requirements/`

**產出：**
- 更新 `open-questions.md`（標記已回答 / 新增問題）
- 更新 `assumptions.md`
- 更新 `decision-log.md`（記錄每個決策）

**流程：**
1. AI 列出待確認問題
2. 使用者回答問題
3. AI 回填需求文件並更新決策紀錄

---

### 步驟 4：分析需求 → 分析文件

**指令：** `/swm.analyze`

**提示詞：** [prompts/04-analyze-requirements.prompt.md](prompts/04-analyze-requirements.prompt.md)

**輸入：** `CONSTITUTION.md` + `specs/01-02/`

**產出（`specs/03-analysis/`）：**

| 檔案 | 說明 |
|------|------|
| `use-cases.md` | 使用案例圖與描述 |
| `user-stories.md` | 使用者故事 |
| `acceptance-criteria.md` | 每項需求的驗收標準 |
| `domain-model.md` | 實體關係與資料模型 |
| `state-transitions.md` | 狀態機圖 |
| `edge-cases.md` | 例外情境與邊界條件 |

---

### 步驟 5：生成規格 → 需求規格書

**指令：** `/swm.spec`

**提示詞：** [prompts/05-generate-spec.prompt.md](prompts/05-generate-spec.prompt.md)

**輸入：** `CONSTITUTION.md` + `specs/01-04/` + `templates/`

**產出：** `specs/04-design-ready/requirement-spec.md`

這是最終確認版需求規格，後續設計文件皆以此為唯一依據。

---

### 步驟 6：生成設計文件 → 開發就緒

**指令：** `/swm.design`

**提示詞：** [prompts/06-generate-design-ready.prompt.md](prompts/06-generate-design-ready.prompt.md)

**輸入：** `CONSTITUTION.md` + `requirement-spec.md` + `templates/`

**產出（`specs/04-design-ready/`）：**

| 檔案 | 說明 |
|------|------|
| `system-design-brief.md` | 系統架構概覽 |
| `api-draft.md` | REST API 端點規格 |
| `database-draft.md` | 資料庫 Schema |
| `frontend-pages.md` | UI 頁面規劃 |
| `test-cases.md` | 測試案例（TC-###）|
| `development-tasks.md` | 開發任務與 Sprint（TASK-###）|

---

### 步驟 7：更新版本 → 變更紀錄

**指令：** `/swm.log`

**提示詞：** [prompts/07-update-versions.prompt.md](prompts/07-update-versions.prompt.md)

**輸入：** `CONSTITUTION.md` + 所有 `specs/`

**產出（`specs/05-versions/`）：**

| 檔案 | 說明 |
|------|------|
| `changelog.md` | 文件版本變更歷史 |
| `decision-log.md` | 決策紀錄（DEC-###）含理由與來源 |

---

## 需求 ID 命名規則

| 前綴 | 類型 | 說明 |
|------|------|------|
| FR-### | 功能需求 | 系統「做什麼」|
| BR-### | 業務規則 | 約束與邏輯規則 |
| DR-### | 資料需求 | 資料模型、欄位定義 |
| WR-### | 流程需求 | 流程、狀態變化 |
| PR-### | 權限需求 | 存取控制規則 |
| NFR-### | 非功能需求 | 效能、安全性、可用性 |
| TC-### | 測試案例 | 測試情境 |
| TASK-### | 開發任務 | 開發工作項目 |
| DEC-### | 決策 | 已記錄的決策 |

---

## 快速開始範例

以下以「員工請假管理系統」為例：

```
1. 將 PM 口述需求寫入 specs/00-inputs/user-description.md
2. 執行 /swm.discover（初步探索，產出 01-discovery/）
3. 執行 /swm.extract（提取正式需求，產出 02-requirements/）
4. 執行 /swm.clarify（AI 提問），直接在對話中回答問題
5. 執行 /swm.analyze → /swm.spec → /swm.design
6. 每個步驟完成後執行 /swm.log 更新版本紀錄
7. 最終在 specs/04-design-ready/ 取得完整的開發就緒文件
```

不知道從哪裡開始？執行 `/swm.status` 查看進度，或 `/swm.next` 直接跳到下一步。

---

## 常見問題

**Q：AI 問了很多問題，我可以先跳過嗎？**
可以，但未解答的問題會在需求中保持「待確認」狀態，相關需求不會被寫入設計文件。

**Q：某個功能是「業界標準」，需要特別說明嗎？**
需要。SpecWingman 明確禁止以「業界慣例」補充需求，每項需求必須有明確的輸入來源。

**Q：我可以跳過某個步驟嗎？**
不建議。每個步驟的產出是下一步的輸入。跳過步驟可能導致設計文件缺乏追溯來源。

**Q：需求確認後想修改怎麼辦？**
執行 `/swm.clarify` 重新進入釐清流程，完成後執行 `/swm.log` 記錄變更原因，保持完整的審計軌跡。

---

## 相關文件

- [CONSTITUTION.md](CONSTITUTION.md) — 核心原則（必讀）
- [templates/](templates/) — 所有輸出格式範本
