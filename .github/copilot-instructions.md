# ReqForge — Copilot Instructions

This repository uses the ReqForge structured requirements workflow. Read `CONSTITUTION.md` for all core rules — it is the highest authority.

## Core Rule

**Never assume requirements.** Only record what is explicitly stated in source documents. Mark unknowns as Open Questions or Assumptions — never write them as confirmed requirements.

## Skills

ReqForge uses a skills-based workflow. Each skill has a dedicated file under `.github/skills/<skill-name>/SKILL.md`.

When the user invokes a skill (e.g., `rf.discover`, `run rf.discover`, `run step 1`), read the corresponding SKILL.md in full and execute all its instructions:

| Skill | SKILL.md | Trigger examples |
|-------|----------|-----------------|
| `rf.discover` | `.github/skills/rf.discover/SKILL.md` | "rf.discover", "run step 1", "初步探索" |
| `rf.extract` | `.github/skills/rf.extract/SKILL.md` | "rf.extract", "run step 2", "提取需求" |
| `rf.clarify` | `.github/skills/rf.clarify/SKILL.md` | "rf.clarify", "run step 3", "釐清需求" |
| `rf.analyze` | `.github/skills/rf.analyze/SKILL.md` | "rf.analyze", "run step 4", "分析需求" |
| `rf.spec` | `.github/skills/rf.spec/SKILL.md` | "rf.spec", "run step 5", "生成規格" |
| `rf.design` | `.github/skills/rf.design/SKILL.md` | "rf.design", "run step 6", "生成設計" |
| `rf.log` | `.github/skills/rf.log/SKILL.md` | "rf.log", "run step 7", "更新版本" |
| `rf.status` | `.github/skills/rf.status/SKILL.md` | "rf.status", "status", "進度" |
| `rf.next` | `.github/skills/rf.next/SKILL.md` | "rf.next", "next", "下一步" |
| `rf.help` | `.github/skills/rf.help/SKILL.md` | "rf.help", "help", "指令列表" |
