from pathlib import Path

STEPS = [
    ("00-inputs", "Step 0: Inputs"),
    ("01-discovery", "Step 1: Discovery"),
    ("02-requirements", "Step 2: Requirements"),
    ("03-analysis", "Step 3: Analysis"),
    ("04-design-ready", "Step 4: Design Ready"),
    ("05-versions", "Step 5: Versions"),
]


def swm_status_tool(project_path: str) -> str:
    specs_dir = Path(project_path) / "specs"
    lines = ["# SpecWingman Workflow Status", ""]

    for dir_name, label in STEPS:
        step_dir = specs_dir / dir_name
        if not step_dir.exists():
            lines.append(f"✗ {label} (directory missing)")
            continue

        files = sorted(f for f in step_dir.iterdir() if f.is_file())
        if files:
            lines.append(f"✓ {label}")
            for f in files:
                lines.append(f"  · {f.name}")
        else:
            lines.append(f"○ {label} (no files yet)")

    return "\n".join(lines)
