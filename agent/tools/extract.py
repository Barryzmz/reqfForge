from pathlib import Path


def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _read_dir(dir_path: Path) -> str:
    if not dir_path.exists():
        return "(no files found)"
    parts = []
    for f in sorted(dir_path.iterdir()):
        if f.is_file():
            parts.append(f"### {f.name}\n\n{f.read_text(encoding='utf-8')}")
    return "\n\n---\n\n".join(parts) if parts else "(no files found)"


def swm_extract_context_tool(project_path: str) -> str:
    root = Path(project_path)
    constitution = _read_file(root / "CONSTITUTION.md")
    prompt = _read_file(root / "prompts" / "02-extract-requirements.prompt.md")
    templates = _read_file(root / "templates" / "functional-requirement-template.md")
    discovery = _read_dir(root / "specs" / "01-discovery")

    return f"""# SpecWingman Step 2: Requirements Extraction Context

## Task Instructions
{prompt}

## CONSTITUTION (follow strictly)
{constitution}

## Reference Template
{templates}

## Discovery Files (specs/01-discovery/)
{discovery}

## Next Step
Process the above and call `swm_write_extract` with these parameters:
- product_vision: content for specs/02-requirements/product-vision.md
- functional_requirements: content for specs/02-requirements/functional-requirements.md
- business_rules: content for specs/02-requirements/business-rules.md
- data_requirements: content for specs/02-requirements/data-requirements.md
- workflow_requirements: content for specs/02-requirements/workflow-requirements.md
- permission_requirements: content for specs/02-requirements/permission-requirements.md
- non_functional_requirements: content for specs/02-requirements/non-functional-requirements.md
- user_roles: content for specs/02-requirements/user-roles.md
"""


def swm_write_extract_tool(
    project_path: str,
    product_vision: str,
    functional_requirements: str,
    business_rules: str,
    data_requirements: str,
    workflow_requirements: str,
    permission_requirements: str,
    non_functional_requirements: str,
    user_roles: str,
) -> str:
    output_dir = Path(project_path) / "specs" / "02-requirements"
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "product-vision.md": product_vision,
        "functional-requirements.md": functional_requirements,
        "business-rules.md": business_rules,
        "data-requirements.md": data_requirements,
        "workflow-requirements.md": workflow_requirements,
        "permission-requirements.md": permission_requirements,
        "non-functional-requirements.md": non_functional_requirements,
        "user-roles.md": user_roles,
    }

    for filename, content in files.items():
        (output_dir / filename).write_text(content, encoding="utf-8")

    written = [f"specs/02-requirements/{f}" for f in files]
    return "Step 2 complete. Written:\n" + "\n".join(f"  · {p}" for p in written)
