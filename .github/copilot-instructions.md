# SpecWingman — Copilot Instructions

This repository uses the SpecWingman structured requirements workflow. Read `CONSTITUTION.md` for all core rules — it is the highest authority.

## Core Rule

**Never assume requirements.** Only record what is explicitly stated in source documents. Mark unknowns as Open Questions or Assumptions — never write them as confirmed requirements.

## Skills

SpecWingman uses a skills-based workflow. Each skill has a dedicated file under `.github/skills/<skill-name>/SKILL.md`.

When the user invokes a skill (e.g., `swm.discover`, `run swm.discover`, `run step 1`), read the corresponding SKILL.md in full and execute all its instructions:

| Skill | SKILL.md | Trigger examples |
|-------|----------|-----------------|
| `swm.discover` | `.github/skills/swm.discover/SKILL.md` | "swm.discover", "run step 1", "初步探索" |
| `swm.extract` | `.github/skills/swm.extract/SKILL.md` | "swm.extract", "run step 2", "提取需求" |
| `swm.clarify` | `.github/skills/swm.clarify/SKILL.md` | "swm.clarify", "run step 3", "釐清需求" |
| `swm.analyze` | `.github/skills/swm.analyze/SKILL.md` | "swm.analyze", "run step 4", "分析需求" |
| `swm.spec` | `.github/skills/swm.spec/SKILL.md` | "swm.spec", "run step 5", "生成規格" |
| `swm.design` | `.github/skills/swm.design/SKILL.md` | "swm.design", "run step 6", "生成設計" |
| `swm.log` | `.github/skills/swm.log/SKILL.md` | "swm.log", "run step 7", "更新版本" |
| `swm.status` | `.github/skills/swm.status/SKILL.md` | "swm.status", "status", "進度" |
| `swm.next` | `.github/skills/swm.next/SKILL.md` | "swm.next", "next", "下一步" |
| `swm.help` | `.github/skills/swm.help/SKILL.md` | "swm.help", "help", "指令列表" |
