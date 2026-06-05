from pathlib import Path

from tools.utils import _read_file, _read_dir, validate_project_path


def swm_spec_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "05-generate-spec.prompt.md")
    template = _read_file(root / "templates" / "requirement-spec-template.md")
    discovery = _read_dir(root / "specs" / "01-discovery")
    requirements = _read_dir(root / "specs" / "02-requirements")
    analysis = _read_dir(root / "specs" / "03-analysis")

    return f"""# SpecWingman Step 5: Generate Requirement Spec Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Requirement Spec Template
{template}

## Discovery Files (specs/01-discovery/)
{discovery}

## Requirements Files (specs/02-requirements/)
{requirements}

## Analysis Files (specs/03-analysis/)
{analysis}

## Next Step
Process the above and call `swm_write_spec` with:
- requirement_spec: full content for specs/04-design-ready/requirement-spec.md
"""


def swm_write_spec_tool(project_path: str, requirement_spec: str) -> str:
    root = validate_project_path(project_path)
    output_dir = root / "specs" / "04-design-ready"
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "requirement-spec.md").write_text(requirement_spec, encoding="utf-8")

    return "Step 5 complete. Written:\n  · specs/04-design-ready/requirement-spec.md"
