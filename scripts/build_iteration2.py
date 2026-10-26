import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_FILE = ROOT / "assignment2" / "visualization" / "iteration2.html"

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["observation_id"] = int(row["observation_id"])
    row["people_count"] = int(row["people_count"])
    row["session_id"] = int(row["session_id"])

assert len(rows) == 28
assert len({(row["session_id"], row["space"]) for row in rows}) == 28

spaces = [
    "Study Lounge 1",
    "Study Lounge 2",
    "Gym",
    "Common Area"
]

session_labels = [
    next(
        row["session_label"]
        for row in rows
        if row["session_id"] == i
    )
    for i in range(1, 8)
]

selection = {
    "name": "selectedObservation",
    "select": {
        "type": "point",
        "fields": ["observation_id"],
        "on": "click",
        "clear": "dblclick"
    }
}

spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Overview: Occupancy by Session and Space",
    "width": 680,
    "height": 230,
    "data": {"values": rows},
    "layer": [
        {
            "params": [selection],
            "mark": {
                "type": "rect",
                "stroke": "white",
                "strokeWidth": 1
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
                },
                "opacity": {
                    "condition": {
                        "param": "selectedObservation",
                        "value": 1
                    },
                    "value": 0.55
                },
                "tooltip": [
                    {
                        "field": "observation_id",
                        "title": "Observation"
                    },
                    {
                        "field": "space",
                        "title": "Space"
                    },
                    {
                        "field": "session_label",
                        "title": "Session"
                    },
                    {
                        "field": "people_count",
                        "title": "People"
                    }
                ]
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

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iteration 2 - Coordinated Shared-Space Views</title>

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

#details {
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 20px;
    max-width: 650px;
    background: #fafafa;
}

#details p {
    margin: 8px 0;
    line-height: 1.5;
}

#details strong {
    display: inline-block;
    min-width: 145px;
}

#vis {
    margin-bottom: 25px;
}
</style>
</head>

<body>

<h1>Shared Spaces: Coordinated Observation Explorer</h1>

<p class="description">
Click a heatmap cell to inspect an observation.
Double-click a cell to clear the selection.
Sessions are ordered observations, not equally spaced time intervals.
</p>

<div id="vis"></div>

<h2>Selected Observation Details</h2>

<div id="details">
Click a heatmap cell to inspect an observation.
</div>

<script>
const spec = __SPEC__;
const observations = __DATA__;

const details = document.getElementById("details");

function showDetails(row) {
    details.replaceChildren();

    if (!row) {
        details.textContent =
            "Click a heatmap cell to inspect an observation.";
        return;
    }

    const fields = [
        ["Observation", row.observation_id],
        ["Space", row.space],
        ["Session", row.session_id],
        ["Date", row.date],
        ["Time", row.time],
        ["People Observed", row.people_count],
        ["Activity", row.main_activity],
        ["Noise Level", row.noise_level],
        ["Context", row.context_notes]
    ];

    for (const [label, value] of fields) {
        const paragraph = document.createElement("p");
        const strong = document.createElement("strong");

        strong.textContent = label + ": ";

        paragraph.appendChild(strong);
        paragraph.appendChild(
            document.createTextNode(String(value ?? ""))
        );

        details.appendChild(paragraph);
    }
}

vegaEmbed("#vis", spec, {actions: false})
    .then(result => {
        const view = result.view;

        view.addSignalListener(
            "selectedObservation_tuple",
            (name, value) => {
                if (
                    !value ||
                    !Array.isArray(value.fields) ||
                    !Array.isArray(value.values)
                ) {
                    showDetails(null);
                    return;
                }

                const index = value.fields.findIndex(
                    field => field.field === "observation_id"
                );

                if (index === -1) {
                    showDetails(null);
                    return;
                }

                const id = Number(value.values[index]);

                const row = observations.find(
                    observation => observation.observation_id === id
                );

                showDetails(row || null);
            }
        );
    })
    .catch(error => {
        console.error(error);
        details.textContent =
            "The visualization could not be loaded. Check the browser console.";
    });
</script>

</body>
</html>"""

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE.write_text(
    html.replace("__SPEC__", json.dumps(spec))
        .replace("__DATA__", json.dumps(rows)),
    encoding="utf-8"
)

print(f"Generated {OUTPUT_FILE}")
print(f"Included {len(rows)} observations.")