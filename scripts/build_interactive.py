import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_FILE = ROOT / "assignment2" / "visualization" / "alternative_c.html"

# Reading the processed observations
with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Converting numeric values for the visualization
for row in rows:
    row["observation_id"] = int(row["observation_id"])
    row["people_count"] = int(row["people_count"])
    row["session_id"] = int(row["session_id"])

activity_order = [
    "None",
    "Studying/Working",
    "Exercising",
    "Recreation",
    "Mixed",
    "Reading",
    "Event/Social"
]

spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Occupancy, Activity, and Noise in Shared Spaces",
    "width": 750,
    "height": 350,
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
        "size": 120,
        "opacity": 0.8
    },
    "encoding": {
        "x": {
            "field": "people_count",
            "type": "quantitative",
            "title": "People Observed",
            "scale": {"domain": [0, 15]}
        },
        "y": {
            "field": "main_activity",
            "type": "nominal",
            "title": "Main Activity",
            "sort": activity_order
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
<title>Shared Spaces - Observation Explorer</title>
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
</head>
<body>
<h2>Shared Spaces: Observation Explorer</h2>
<p>Filter by space and hover over an observation to examine its context.</p>
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