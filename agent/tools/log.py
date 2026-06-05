from pathlib import Path

from tools.utils import _read_file, _read_dir, validate_project_path


def swm_log_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "07-update-versions.prompt.md")
    discovery = _read_dir(root / "specs" / "01-discovery")
    requirements = _read_dir(root / "specs" / "02-requirements")
    analysis = _read_dir(root / "specs" / "03-analysis")
    design_ready = _read_dir(root / "specs" / "04-design-ready")
    changelog = _read_file(root / "specs" / "05-versions" / "changelog.md")
    decision_log = _read_file(root / "specs" / "05-versions" / "decision-log.md")

    return f"""# SpecWingman Step 7: Update Versions Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Discovery Files (specs/01-discovery/)
{discovery}

## Requirements Files (specs/02-requirements/)
{requirements}

## Analysis Files (specs/03-analysis/)
{analysis}

## Design-ready Files (specs/04-design-ready/)
{design_ready}

## Current Changelog (specs/05-versions/changelog.md)
{changelog}

## Current Decision Log (specs/05-versions/decision-log.md)
{decision_log}

## Next Step
Process the above and call `swm_write_log` with:
- changelog: full updated content for specs/05-versions/changelog.md
- decision_log: full updated content for specs/05-versions/decision-log.md
"""


def swm_write_log_tool(project_path: str, changelog: str, decision_log: str) -> str:
    root = validate_project_path(project_path)
    versions_dir = root / "specs" / "05-versions"
    versions_dir.mkdir(parents=True, exist_ok=True)

    (versions_dir / "changelog.md").write_text(changelog, encoding="utf-8")
    (versions_dir / "decision-log.md").write_text(decision_log, encoding="utf-8")

    return "Step 7 complete. Written:\n  · specs/05-versions/changelog.md\n  · specs/05-versions/decision-log.md"
