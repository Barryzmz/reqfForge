from pathlib import Path

from tools.utils import _read_file, _read_dir, validate_project_path


def swm_discover_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "01-read-inputs.prompt.md")
    inputs = _read_dir(root / "specs" / "00-inputs")

    return f"""# SpecWingman Step 1: Discovery Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Input Files
{inputs}

## Next Step
Process the above and call `swm_write_discovery` with these parameters:
- source_summary: content for specs/01-discovery/source-summary.md
- extracted_facts: content for specs/01-discovery/extracted-facts.md
- open_questions: content for specs/01-discovery/open-questions.md
- assumptions: content for specs/01-discovery/assumptions.md
- glossary: content for specs/01-discovery/glossary.md
"""


def swm_write_discovery_tool(
    project_path: str,
    source_summary: str,
    extracted_facts: str,
    open_questions: str,
    assumptions: str,
    glossary: str,
) -> str:
    root = validate_project_path(project_path)
    output_dir = root / "specs" / "01-discovery"
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "source-summary.md": source_summary,
        "extracted-facts.md": extracted_facts,
        "open-questions.md": open_questions,
        "assumptions.md": assumptions,
        "glossary.md": glossary,
    }

    for filename, content in files.items():
        (output_dir / filename).write_text(content, encoding="utf-8")

    written = [f"specs/01-discovery/{f}" for f in files]
    return "Step 1 complete. Written:\n" + "\n".join(f"  · {p}" for p in written)
