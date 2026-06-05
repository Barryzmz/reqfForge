from pathlib import Path
from typing import Optional

from tools.utils import _read_file, _read_dir, validate_project_path


def swm_clarify_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "03-clarify-requirements.prompt.md")
    discovery = _read_dir(root / "specs" / "01-discovery")
    requirements = _read_dir(root / "specs" / "02-requirements")
    decision_log = _read_file(root / "specs" / "05-versions" / "decision-log.md")

    answer_draft_path = root / "specs" / "01-discovery" / "answer-draft.md"
    answer_draft_content = answer_draft_path.read_text(encoding="utf-8").strip() if answer_draft_path.exists() else ""
    is_phase2 = bool(answer_draft_content)

    answer_draft_section = (
        f"\n## User Answers (specs/01-discovery/answer-draft.md)\n\n{answer_draft_content}\n"
        if is_phase2 else ""
    )
    phase_instruction = (
        "**You are in Phase 2.** User answers are provided above. "
        "Perform the full backfill and call `swm_write_clarify` with all fields. "
        "Pass answer_draft=\"\" to clear the draft file after processing."
        if is_phase2 else
        "**You are in Phase 1.** Generate clarification questions and call `swm_write_clarify` "
        "with only open_questions. Do not modify any other files yet."
    )

    return f"""# SpecWingman Step 3: Clarify Requirements Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Discovery Files (specs/01-discovery/)
{discovery}

## Requirements Files (specs/02-requirements/)
{requirements}

## Decision Log (specs/05-versions/decision-log.md)
{decision_log}
{answer_draft_section}
## Phase Instructions

{phase_instruction}

### swm_write_clarify parameters
- open_questions: updated content for specs/01-discovery/open-questions.md (required)
- answer_draft: pass "" to clear after Phase 2 processing; omit in Phase 1 (optional)
- assumptions: updated content for specs/01-discovery/assumptions.md (Phase 2 only)
- decision_log: full updated content for specs/05-versions/decision-log.md (Phase 2 only)

To backfill requirements files after Phase 2, call `swm_write_extract` with updated content.
"""


def swm_write_clarify_tool(
    project_path: str,
    open_questions: str,
    answer_draft: Optional[str] = None,
    assumptions: Optional[str] = None,
    decision_log: Optional[str] = None,
) -> str:
    root = validate_project_path(project_path)
    discovery_dir = root / "specs" / "01-discovery"
    discovery_dir.mkdir(parents=True, exist_ok=True)

    written = []

    (discovery_dir / "open-questions.md").write_text(open_questions, encoding="utf-8")
    written.append("specs/01-discovery/open-questions.md")

    if answer_draft is not None:
        (discovery_dir / "answer-draft.md").write_text(answer_draft, encoding="utf-8")
        written.append("specs/01-discovery/answer-draft.md")

    if assumptions is not None:
        (discovery_dir / "assumptions.md").write_text(assumptions, encoding="utf-8")
        written.append("specs/01-discovery/assumptions.md")

    if decision_log is not None:
        versions_dir = root / "specs" / "05-versions"
        versions_dir.mkdir(parents=True, exist_ok=True)
        (versions_dir / "decision-log.md").write_text(decision_log, encoding="utf-8")
        written.append("specs/05-versions/decision-log.md")

    return "Step 3 written:\n" + "\n".join(f"  · {p}" for p in written)
