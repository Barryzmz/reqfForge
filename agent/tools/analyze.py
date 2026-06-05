from pathlib import Path

from tools.utils import _read_file, _read_dir, validate_project_path


def swm_analyze_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "04-analyze-requirements.prompt.md")
    discovery = _read_dir(root / "specs" / "01-discovery")
    requirements = _read_dir(root / "specs" / "02-requirements")

    return f"""# SpecWingman Step 4: Analyze Requirements Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Discovery Files (specs/01-discovery/)
{discovery}

## Requirements Files (specs/02-requirements/)
{requirements}

## Next Step
Process the above and call `swm_write_analyze` with these parameters:
- use_cases: content for specs/03-analysis/use-cases.md
- user_stories: content for specs/03-analysis/user-stories.md
- acceptance_criteria: content for specs/03-analysis/acceptance-criteria.md
- domain_model: content for specs/03-analysis/domain-model.md
- state_transitions: content for specs/03-analysis/state-transitions.md
- edge_cases: content for specs/03-analysis/edge-cases.md
"""


def swm_write_analyze_tool(
    project_path: str,
    use_cases: str,
    user_stories: str,
    acceptance_criteria: str,
    domain_model: str,
    state_transitions: str,
    edge_cases: str,
) -> str:
    root = validate_project_path(project_path)
    output_dir = root / "specs" / "03-analysis"
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "use-cases.md": use_cases,
        "user-stories.md": user_stories,
        "acceptance-criteria.md": acceptance_criteria,
        "domain-model.md": domain_model,
        "state-transitions.md": state_transitions,
        "edge-cases.md": edge_cases,
    }

    for filename, content in files.items():
        (output_dir / filename).write_text(content, encoding="utf-8")

    written = [f"specs/03-analysis/{f}" for f in files]
    return "Step 4 complete. Written:\n" + "\n".join(f"  · {p}" for p in written)
