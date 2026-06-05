import re
from pathlib import Path

STEPS = [
    ("00-inputs", "Step 0: Inputs"),
    ("01-discovery", "Step 1: Discovery"),
    ("02-requirements", "Step 2: Requirements"),
    ("03-analysis", "Step 3: Analysis"),
    ("04-design-ready", "Step 4: Design Ready"),
    ("05-versions", "Step 5: Versions"),
]

_PLACEHOLDER_VALUES = frozenset({
    "tbd", "", "pending", "draft", "open", "todo", "未評估", "yes", "no",
})
_ID_PATTERN = re.compile(r'^[A-Z]+-\d+$')
_VERSION_TBD = re.compile(r'^\d+\.\d+\.\d+\s*/\s*TBD$')
_TABLE_SEP = re.compile(r'^\|[\s\-:]+(\|[\s\-:]+)*\|$')
_LABEL_TBD = re.compile(r'^.+[:：]\s*TBD$')
_LABEL_ID = re.compile(r'^.+[:：]\s*[A-Z]+-\d+$')
_USER_STORY_TBD = re.compile(
    r'^As a TBD,?\s*I want TBD,?\s*so that TBD\.?$', re.IGNORECASE
)

_BOILERPLATE = frozenset({
    "本文件只記錄可直接從來源取得的事實，不記錄推測。",
    "本文件只彙整已確認需求。未確認內容不得放入本文件。",
    "本文件只能根據已確認需求產生。",
    "正式功能需求只能記錄已確認內容。",
    "假設是暫時性前提，不是已確認需求。假設被確認後，才可以轉入正式需求文件。",
    "不確定、矛盾、缺漏或需要確認的內容必須記錄於此。未回答問題不得寫入正式需求。",
    "Use case 必須追溯至已確認需求。",
    "API 草案只能對應已確認需求。",
    "資料庫草案只能根據已確認資料需求產生。",
    "在此貼上使用者口頭需求、訪談紀錄、會議摘要或其他原始描述。",
    "尚未確認。",
    "對話中的 Q&A 草稿暫存區。每筆回答在收到後立即寫入，正式處理進 `open-questions.md` 與 `decision-log.md` 後應清除對應項目。",
    "此檔案不屬於正式需求文件，不得被下游 prompt 引用為需求來源。",
})


def _has_substantive_content(filepath: Path) -> bool:
    """Return True when the file contains real data beyond template placeholders."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return False

    past_separator = False

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            past_separator = False
            continue

        if stripped.startswith("#"):
            past_separator = False
            continue

        if _TABLE_SEP.match(stripped):
            past_separator = True
            continue

        # Table row
        if stripped.startswith("|") and stripped.endswith("|"):
            if past_separator:
                cells = [c.strip() for c in stripped.split("|")[1:-1]]
                real_count = sum(
                    1 for cell in cells
                    if (cell.lower() not in _PLACEHOLDER_VALUES
                        and not _ID_PATTERN.match(cell)
                        and not _VERSION_TBD.match(cell)
                        and not _USER_STORY_TBD.match(cell))
                )
                if real_count >= 2:
                    return True
            continue

        # Non-table line
        past_separator = False
        if stripped.startswith(">"):
            continue
        content = stripped.lstrip("-* ").strip()
        if (content
                and content not in _BOILERPLATE
                and content.lower() != "tbd"
                and not _LABEL_TBD.match(content)
                and not _LABEL_ID.match(content)):
            return True

    return False


def swm_status_tool(project_path: str) -> str:
    specs_dir = Path(project_path) / "specs"
    lines = ["# SpecWingman Workflow Status", ""]

    for dir_name, label in STEPS:
        step_dir = specs_dir / dir_name
        if not step_dir.exists():
            lines.append(f"⬜ {label} (directory missing)")
            continue

        files = sorted(f for f in step_dir.iterdir() if f.is_file())
        if not files:
            lines.append(f"⬜ {label} (no files)")
            continue

        file_status = {f: _has_substantive_content(f) for f in files}
        content_count = sum(1 for v in file_status.values() if v)

        if content_count > 0:
            lines.append(f"✅ {label} ({content_count}/{len(files)} with content)")
        else:
            lines.append(f"🔄 {label} ({len(files)} files, all template)")

        for f in files:
            marker = "✅" if file_status[f] else "·"
            lines.append(f"  {marker} {f.name}")

    return "\n".join(lines)
