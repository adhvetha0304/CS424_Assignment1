
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_FILE = ROOT / "assignment3" / "visualization" / "interactive.html"

with INPUT_FILE.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["observation_id"] = int(row["observation_id"])
    row["people_count"] = int(row["people_count"])
    row["session_id"] = int(row["session_id"])

spaces = [
    "Study Lounge 1",
    "Study Lounge 2",
    "Gym",
    "Common Area"
]

sessions = list(range(1, 8))

assert len(rows) == 28
assert len({
    (row["session_id"], row["space"]) for row in rows
}) == 28
assert {
    (row["session_id"], row["space"]) for row in rows
} == {
    (session, space)
    for session in sessions
    for space in spaces
}

session_labels = [
    next(
        row["session_label"]
        for row in rows
        if row["session_id"] == session
    )
    for session in sessions
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

highlight_params = [
    {
        "name": "highlightActive",
        "value": False
    },
    {
        "name": "highlightedSessions",
        "value": []
    }
]

opacity = {
    "condition": {
        "test": (
            "!highlightActive || "
            "indexof(highlightedSessions, datum.session_id) >= 0"
        ),
        "value": 1
    },
    "value": 0.12
}

spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Overview: Occupancy by Session and Space",
    "width": 680,
    "height": 230,
    "data": {"values": rows},
    "params": highlight_params,
    "layer": [
        {
            "params": [selection],
            "mark": {
                "type": "rect"
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
                    "scale": {
                        "scheme": "blues"
                    }
                },
                "opacity": opacity,
                "stroke": {
                    "condition": {
                        "param": "selectedObservation",
                        "empty": False,
                        "value": "#d97706"
                    },
                    "value": "white"
                },
                "strokeWidth": {
                    "condition": {
                        "param": "selectedObservation",
                        "empty": False,
                        "value": 3
                    },
                    "value": 1
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
                        "test": (
                            "datum.people_count >= 12 && "
                            "(!highlightActive || "
                            "indexof(highlightedSessions, datum.session_id) >= 0)"
                        ),
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

<title>Shared Spaces - Interactive Condition</title>

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
    line-height: 1.5;
}

.noise-controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
}

.noise-controls select,
.noise-controls button {
    padding: 8px;
    font-family: Arial, sans-serif;
    font-size: 14px;
}

.noise-controls button {
    cursor: pointer;
}

#highlight-status {
    margin-bottom: 20px;
    color: #444;
    font-size: 14px;
}

#vis {
    margin-bottom: 25px;
    max-width: 100%;
    overflow-x: auto;
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
</style>
</head>

<body>

<h1>Shared Spaces: Coordinated Observation Explorer</h1>

<p class="description">
Choose a space and noise level to highlight matching observation
sessions across all four spaces. Click a heatmap cell to inspect
its details, or double-click to clear the cell selection.
Sessions are ordered observations, not equally spaced time intervals.
</p>

<div class="noise-controls">
    <label for="noise-space">Reference space:</label>

    <select id="noise-space">
        <option value="">Choose a space</option>
        <option value="Study Lounge 1">Study Lounge 1</option>
        <option value="Study Lounge 2">Study Lounge 2</option>
        <option value="Gym">Gym</option>
        <option value="Common Area">Common Area</option>
    </select>

    <label for="noise-level">Noise level:</label>

    <select id="noise-level">
        <option value="">Choose a noise level</option>
        <option value="Quiet">Quiet</option>
        <option value="Moderate">Moderate</option>
        <option value="Loud">Loud</option>
    </select>

    <button id="clear-highlight" type="button">
        Clear Highlight
    </button>
</div>

<p id="highlight-status" aria-live="polite">
    No noise highlight applied.
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
const spaceSelect = document.getElementById("noise-space");
const noiseSelect = document.getElementById("noise-level");
const clearButton = document.getElementById("clear-highlight");
const highlightStatus = document.getElementById("highlight-status");

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

vegaEmbed("#vis", spec, {actions: false, tooltip: false})
    .then(result => {
        const view = result.view;

        async function updateHighlight() {
            const chosenSpace = spaceSelect.value;
            const chosenNoise = noiseSelect.value;

            if (!chosenSpace || !chosenNoise) {
                view.signal("highlightActive", false);
                view.signal("highlightedSessions", []);
                await view.runAsync();

                highlightStatus.textContent =
                    "No noise highlight applied.";
                return;
            }

            const matchingSessions = observations
                .filter(row =>
                    row.space === chosenSpace &&
                    row.noise_level === chosenNoise
                )
                .map(row => row.session_id)
                .sort((a, b) => a - b);

            view.signal("highlightedSessions", matchingSessions);
            view.signal("highlightActive", true);
            await view.runAsync();

            if (matchingSessions.length === 0) {
                highlightStatus.textContent =
                    "No sessions match: " +
                    chosenSpace + " / " + chosenNoise + ".";
            } else {
                highlightStatus.textContent =
                    "Matching sessions: " +
                    matchingSessions.map(id => "S" + id).join(", ") +
                    " (" + chosenSpace + " / " + chosenNoise + ").";
            }
        }

        spaceSelect.addEventListener("change", updateHighlight);
        noiseSelect.addEventListener("change", updateHighlight);

        clearButton.addEventListener("click", () => {
            spaceSelect.value = "";
            noiseSelect.value = "";
            updateHighlight();
        });

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
            "The visualization could not be loaded. " +
            "Check the browser console.";
    });
</script>

</body>
</html>
"""

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE.write_text(
    page.replace("__SPEC__", json.dumps(spec))
        .replace("__DATA__", json.dumps(rows)),
    encoding="utf-8"
)

print(f"Generated {OUTPUT_FILE}")
print(f"Included {len(rows)} observations.")
