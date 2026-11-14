import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assignment3"
PRACTICE_DATA = BASE / "study" / "practice_data.csv"

with PRACTICE_DATA.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

assert len(rows) == 12, f"Expected 12 practice observations, got {len(rows)}"
assert len({(r["session_id"], r["space"]) for r in rows}) == 12

for condition in ("static", "interactive"):
    source_path = BASE / f"build_{condition}.py"
    source = source_path.read_text(encoding="utf-8")

    old_input = (
        '"data" / "processed" / "shared_spaces_processed.csv"'
    )
    new_input = '"assignment3" / "study" / "practice_data.csv"'

    old_output = f'"{condition}.html"'
    new_output = f'"practice_{condition}.html"'

    changes = [
        (old_input, new_input),
        (old_output, new_output),
        ("sessions = list(range(1, 8))", "sessions = list(range(1, 4))"),
        ("== 28", "== 12"),
    ]

    for old, new in changes:
        assert old in source, f"Missing expected text in {source_path}: {old}"
        source = source.replace(old, new)

    exec(
        compile(source, str(source_path), "exec"),
        {"__file__": str(source_path), "__name__": "__main__"}
    )

    output = BASE / "visualization" / f"practice_{condition}.html"
    page = output.read_text(encoding="utf-8")

    banner = (
        '<div style="background:#fff3cd;color:#553c00;'
        'border:1px solid #e0bd63;padding:12px 16px;'
        'margin:15px;font-family:Arial,sans-serif;">'
        '<strong>PRACTICE ONLY — SYNTHETIC DATA.</strong> '
        'These 12 fictional observations are not part of the main study.'
        '</div>'
    )

    page, count = re.subn(
        r"(<body\b[^>]*>)",
        lambda match: match.group(1) + "\n" + banner,
        page,
        count=1,
        flags=re.IGNORECASE,
    )
    assert count == 1, f"Could not find HTML body in {output}"

    page = page.replace("28 observations", "12 practice observations")
    output.write_text(page, encoding="utf-8")
    print(f"Created {output.relative_to(ROOT)}")

print("Original study generators and pages were not modified.")
