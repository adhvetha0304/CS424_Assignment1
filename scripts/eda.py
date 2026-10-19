import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_DIR = ROOT / "assignment2" / "figures" / "eda"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Reading the processed data
df = pd.read_csv(INPUT_FILE, keep_default_na=False)

spaces = [
    "Study Lounge 1",
    "Study Lounge 2",
    "Gym",
    "Common Area",
]

fig, ax = plt.subplots(figsize=(9, 5))

# Plotting each observation and separating overlapping points
for i, space in enumerate(spaces):
    counts = df.loc[
        df["space"] == space, "people_count"
    ].sort_values()

    repeated = {}

    for count in counts:
        occurrence = repeated.get(count, 0)
        repeated[count] = occurrence + 1

        offsets = [-0.12, 0, 0.12, -0.24, 0.24, -0.36, 0.36]

        ax.scatter(
        i + offsets[occurrence],
        count,
        s=65,
        color="steelblue",
        alpha=0.8
        )

ax.set_xticks(range(len(spaces)))
ax.set_xticklabels(spaces)

ax.set_xlabel("Shared Space")
ax.set_ylabel("People Observed")
ax.set_title("Observed Occupancy Across Shared Spaces")
ax.set_ylim(bottom=-0.5)
ax.grid(axis="y", alpha=0.25)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "occupancy_by_space.png",
    dpi=200
)

plt.close()

print("Saved occupancy_by_space.png")

# Checking the distribution numerically
print(
    df.groupby("space")["people_count"].agg(
        ["count", "min", "median", "mean", "max"]
    )
)

# Comparing occupancy across observation sessions
session_data = df.pivot(
    index="session_id",
    columns="space",
    values="people_count"
).reindex(columns=spaces)

session_labels = (
    df.drop_duplicates("session_id")
    .set_index("session_id")
    .loc[session_data.index, "session_label"]
)

fig, ax = plt.subplots(figsize=(10, 6))

heatmap = ax.imshow(
    session_data.to_numpy(),
    cmap="YlGnBu",
    aspect="auto",
    vmin=0
)

# Adding the actual people counts inside each cell
for i in range(len(session_data)):
    for j in range(len(spaces)):
        value = int(session_data.iloc[i, j])

        ax.text(
            j,
            i,
            str(value),
            ha="center",
            va="center",
            color="white" if value >= 8 else "black"
        )

ax.set_xticks(range(len(spaces)))
ax.set_xticklabels(spaces)

ax.set_yticks(range(len(session_labels)))
ax.set_yticklabels(session_labels)

ax.set_title("Observed Occupancy by Session and Space")
ax.set_xlabel("Shared Space")
ax.set_ylabel("Observation Session")

fig.colorbar(heatmap, ax=ax, label="People Observed")

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "occupancy_by_session.png",
    dpi=200
)
plt.close()

print("Saved occupancy_by_session.png")