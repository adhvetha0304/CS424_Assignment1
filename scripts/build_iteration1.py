
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_FILE = ROOT / "assignment2" / "visualization" / "iteration1.html"

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["observation_id"] = int(row["observation_id"])
    row["people_count"] = int(row["people_count"])
    row["session_id"] = int(row["session_id"])

# Each observation receives its own display row.
# This prevents records with the same occupancy and activity
# from completely covering one another.
activity_order = list(dict.fromkeys(
    row["main_activity"] for row in rows
))

spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Iteration 1: Individual Shared-Space Observations",
    "width": 750,
    "height": {"step": 18},
    "data": {"values": rows},
    "params": [
        {
            "name": "selectedSpace",
            "value": "All Spaces",
            "bind": {
                "input": "select",
                "options": [
                    "All Spaces",
                    "Study Lounge 1",
                    "Study Lounge 2",
                    "Gym",
                    "Common Area"
                ],
                "name": "Space: "
            }
        }
    ],
    "transform": [
        {
            "filter": "selectedSpace === 'All Spaces' || "
                      "datum.space === selectedSpace"
        }
    ],
    "mark": {
        "type": "circle",
        "size": 110,
        "opacity": 0.85
    },
    "encoding": {
        "x": {
            "field": "people_count",
            "type": "quantitative",
            "title": "People Observed",
            "scale": {"domain": [0, 15]}
        },
        "y": {
            "field": "observation_id",
            "type": "ordinal",
            "title": "Observation ID",
            "sort": "ascending"
        },
        "color": {
            "field": "noise_level",
            "type": "nominal",
            "title": "Noise Level",
            "scale": {
                "domain": ["Quiet", "Moderate", "Loud"],
                "range": ["steelblue", "orange", "crimson"]
            }
        },
        "tooltip": [
            {"field": "observation_id", "title": "Observation"},
            {"field": "space", "title": "Space"},
            {"field": "session_id", "title": "Session"},
            {"field": "date", "title": "Date"},
            {"field": "time", "title": "Time"},
            {"field": "people_count", "title": "People"},
            {"field": "main_activity", "title": "Activity"},
            {"field": "noise_level", "title": "Noise"},
            {"field": "context_notes", "title": "Context"}
        ]
    }
}

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iteration 1 - Shared Spaces</title>
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
</head>
<body>
<h2>Shared Spaces: Individual Observation Explorer</h2>
<p>Each observation occupies a separate row. Filter by space
and hover over a point to inspect its recorded context.</p>
<div id="vis"></div>
<script>
const spec = __SPEC__;
vegaEmbed("#vis", spec, {actions: false})
    .catch(error => console.error(error));
</script>
</body>
</html>"""

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(
    html.replace("__SPEC__", json.dumps(spec)),
    encoding="utf-8"
)

print(f"Generated {OUTPUT_FILE}")
print(f"Included {len(rows)} observations.")
