# ReqForge — Agent Instructions

ReqForge 是一套結構化需求規格工作流程，協助將非正式輸入（口頭描述、會議記錄、PDF、Excel）轉化為可追溯、可審計的正式需求規格文件。

## Core Rules

執行任何步驟前，先讀取 `CONSTITUTION.md` — 這是所有工作的最高原則。

最重要的規則：
- **禁止腦補** — 只記錄來源中明確提供的資訊
- **區分狀態** — Confirmed Requirement / Suggested Practice / Assumption / Open Question 必須明確區分
- **不確定內容** 必須進入 `specs/01-discovery/open-questions.md`，不得寫成正式需求

## File Structure

```
.github/skills/      # Skills（每個工作流步驟的完整指示）
specs/
├── 00-inputs/       # 原始輸入（user-description.md）
├── 01-discovery/    # 步驟 1 產出
├── 02-requirements/ # 步驟 2 產出
├── 03-analysis/     # 步驟 4 產出
├── 04-design-ready/ # 步驟 5-6 產出
└── 05-versions/     # 步驟 7 產出（changelog / decision-log）
prompts/             # 各步驟的詳細執行指示（由 SKILL.md 引用）
```

## Skills

ReqForge 使用 skills 架構。每個步驟對應 `.github/skills/<skill-name>/SKILL.md`。

使用者提到以下關鍵字時，讀取對應的 SKILL.md 並**完整**執行其所有指示：

| Skill | SKILL.md | 觸發關鍵字 |
|-------|----------|-----------|
| `rf-discover` | `.github/skills/rf-discover/SKILL.md` | discover / step 1 / 初步探索 |
| `rf-extract` | `.github/skills/rf-extract/SKILL.md` | extract / step 2 / 提取需求 |
| `rf-clarify` | `.github/skills/rf-clarify/SKILL.md` | clarify / step 3 / 釐清需求 |
| `rf-analyze` | `.github/skills/rf-analyze/SKILL.md` | analyze / step 4 / 分析需求 |
| `rf-spec` | `.github/skills/rf-spec/SKILL.md` | spec / step 5 / 生成規格 |
| `rf-design` | `.github/skills/rf-design/SKILL.md` | design / step 6 / 生成設計 |
| `rf-log` | `.github/skills/rf-log/SKILL.md` | log / step 7 / 更新版本 |
| `rf-status` | `.github/skills/rf-status/SKILL.md` | status / 進度 / 哪個步驟 |
| `rf-next` | `.github/skills/rf-next/SKILL.md` | next / 下一步 / 接下來做什麼 |
| `rf-help` | `.github/skills/rf-help/SKILL.md` | help / 指令列表 |
