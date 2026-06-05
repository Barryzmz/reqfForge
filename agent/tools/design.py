from pathlib import Path

from tools.utils import _read_file, validate_project_path


def swm_design_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "06-generate-design-ready.prompt.md")
    requirement_spec = _read_file(root / "specs" / "04-design-ready" / "requirement-spec.md")
    tpl_api = _read_file(root / "templates" / "api-draft-template.md")
    tpl_db = _read_file(root / "templates" / "database-draft-template.md")
    tpl_tasks = _read_file(root / "templates" / "development-tasks-template.md")
    tpl_tests = _read_file(root / "templates" / "test-case-template.md")

    return f"""# SpecWingman Step 6: Generate Design-ready Documents Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Requirement Spec (specs/04-design-ready/requirement-spec.md)
{requirement_spec}

## Template: API Draft
{tpl_api}

## Template: Database Draft
{tpl_db}

## Template: Development Tasks
{tpl_tasks}

## Template: Test Cases
{tpl_tests}

## Next Step
Process the above and call `swm_write_design` with these parameters:
- system_design_brief: content for specs/04-design-ready/system-design-brief.md
- api_draft: content for specs/04-design-ready/api-draft.md
- database_draft: content for specs/04-design-ready/database-draft.md
- frontend_pages: content for specs/04-design-ready/frontend-pages.md
- test_cases: content for specs/04-design-ready/test-cases.md
- development_tasks: content for specs/04-design-ready/development-tasks.md
"""


def swm_write_design_tool(
    project_path: str,
    system_design_brief: str,
    api_draft: str,
    database_draft: str,
    frontend_pages: str,
    test_cases: str,
    development_tasks: str,
) -> str:
    root = validate_project_path(project_path)
    output_dir = root / "specs" / "04-design-ready"
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "system-design-brief.md": system_design_brief,
        "api-draft.md": api_draft,
        "database-draft.md": database_draft,
        "frontend-pages.md": frontend_pages,
        "test-cases.md": test_cases,
        "development-tasks.md": development_tasks,
    }

    for filename, content in files.items():
        (output_dir / filename).write_text(content, encoding="utf-8")

    written = [f"specs/04-design-ready/{f}" for f in files]
    return "Step 6 complete. Written:\n" + "\n".join(f"  · {p}" for p in written)
