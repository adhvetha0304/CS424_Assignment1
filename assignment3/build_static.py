
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT = ROOT / "assignment3" / "visualization" / "static.html"

with INPUT.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["observation_id"] = int(row["observation_id"])
    row["people_count"] = int(row["people_count"])
    row["session_id"] = int(row["session_id"])

spaces = [
    "Study Lounge 1",
    "Study Lounge 2",
    "Gym",
    "Common Area",
]

sessions = list(range(1, 8))

assert len(rows) == 28
assert len({
    (row["session_id"], row["space"]) for row in rows
}) == 28

session_labels = [
    next(
        row["session_label"]
        for row in rows
        if row["session_id"] == session
    )
    for session in sessions
]

spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Overview: Occupancy by Session and Space",
    "width": 680,
    "height": 230,
    "data": {"values": rows},
    "layer": [
        {
            "mark": {
                "type": "rect",
                "stroke": "white",
                "strokeWidth": 1,
                "interactive": False
            },
            "encoding": {
                "x": {
                    "field": "session_label",
                    "type": "ordinal",
                    "title": "Observation Session",
                    "sort": session_labels,
                    "axis": {
                        "labelAngle": -35,
                        "labelLimit": 160
                    }
                },
                "y": {
                    "field": "space",
                    "type": "nominal",
                    "title": "Space",
                    "sort": spaces
                },
                "color": {
                    "field": "people_count",
                    "type": "quantitative",
                    "title": "People Observed",
                    "scale": {"scheme": "blues"}
                }
            }
        },
        {
            "mark": {
                "type": "text",
                "fontSize": 14,
                "interactive": False
            },
            "encoding": {
                "x": {
                    "field": "session_label",
                    "type": "ordinal",
                    "sort": session_labels
                },
                "y": {
                    "field": "space",
                    "type": "nominal",
                    "sort": spaces
                },
                "text": {
                    "field": "people_count",
                    "type": "quantitative",
                    "format": "d"
                },
                "color": {
                    "condition": {
                        "test": "datum.people_count >= 12",
                        "value": "white"
                    },
                    "value": "black"
                }
            }
        }
    ]
}

page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Shared Spaces - Static Condition</title>

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 30px;
    color: #222;
}
h1 {
    margin-bottom: 12px;
}
.description {
    margin-bottom: 25px;
    color: #555;
}
#vis {
    margin-bottom: 25px;
}
table {
    border-collapse: collapse;
    font-size: 13px;
}
th, td {
    border: 1px solid #ccc;
    padding: 9px;
    text-align: left;
}
th {
    background: #f2f2f2;
    white-space: nowrap;
}
tbody tr:nth-child(even) {
    background: #f8f8f8;
}
</style>
</head>

<body>
<h1>Shared Spaces: Coordinated Observation Explorer</h1>

<p class="description">
This version shows occupancy across seven observation sessions.
The heatmap shows the number of people in each space and session.
Use the reference table below to check noise levels and other
observation details. Sessions are ordered observations, not
equally spaced time intervals.
</p>

<div id="vis"></div>

<h2>Observation Reference Table</h2>
<table>
<thead>
<tr>
<th>Session</th>
<th>Space</th>
<th>People</th>
<th>Noise Level</th>
<th>Activity</th>
<th>Date</th>
<th>Time</th>
<th>Context</th>
</tr>
</thead>
<tbody>
"""

fields = [
    "session_id",
    "space",
    "people_count",
    "noise_level",
    "main_activity",
    "date",
    "time",
    "context_notes",
]

for row in sorted(
    rows,
    key=lambda r: (
        spaces.index(r["space"]),
        r["session_id"]
    )
):
    page += "<tr>"
    for field in fields:
        page += (
            "<td>"
            + html.escape(str(row[field]))
            + "</td>"
        )
    page += "</tr>"

page += """
</tbody>
</table>

<script>
const spec = __SPEC__;

vegaEmbed("#vis", spec, {
    actions: false,
    tooltip: false
}).catch(error => {
    console.error(error);
    document.getElementById("vis").textContent =
        "The visualization could not be loaded.";
});
</script>

</body>
</html>
"""

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(
    page.replace("__SPEC__", json.dumps(spec)),
    encoding="utf-8"
)

print(f"Generated {OUTPUT}")
print(f"Included {len(rows)} observations.")
