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

# Exploring activity, noise level, and occupancy
from matplotlib.lines import Line2D

noise_colors = {
    "Quiet": "steelblue",
    "Moderate": "orange",
    "Loud": "crimson",
}

activity_order = [
    "None",
    "Studying/Working",
    "Exercising",
    "Recreation",
    "Mixed",
    "Reading",
    "Event/Social",
]

fig, axes = plt.subplots(
    2, 2,
    figsize=(13, 9),
    sharey=True
)

for ax, space in zip(axes.flat, spaces):
    subset = df[df["space"] == space]

    activities = [
        activity for activity in activity_order
        if activity in subset["main_activity"].values
    ]

    repeated = {}

    for _, row in subset.iterrows():
        activity = row["main_activity"]
        count = row["people_count"]

        x = activities.index(activity)

        # Separating observations with the same activity and count
        key = (activity, count)
        occurrence = repeated.get(key, 0)
        repeated[key] = occurrence + 1

        offsets = [0, -0.12, 0.12, -0.24, 0.24, -0.36, 0.36]

        ax.scatter(
            x + offsets[occurrence],
            count,
            color=noise_colors[row["noise_level"]],
            s=75,
            alpha=0.85
        )

    ax.set_xticks(range(len(activities)))
    ax.set_xticklabels(activities, rotation=35, ha="right")
    ax.set_title(space)
    ax.grid(axis="y", alpha=0.2)

# Using one consistent scale covering all observed counts
for ax in axes.flat:
    ax.set_ylim(-0.5, 15)

fig.suptitle(
    "Observed Occupancy by Activity and Noise Level",
    fontsize=15
)

fig.supylabel("People Observed")
fig.supxlabel("Main Activity")

legend_items = [
    Line2D(
        [0], [0],
        marker="o",
        linestyle="None",
        color=color,
        markersize=9,
        label=level
    )
    for level, color in noise_colors.items()
]

fig.legend(
    handles=legend_items,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.94),
    ncol=3
)

plt.tight_layout(rect=[0, 0.03, 1, 0.9])

plt.savefig(
    OUTPUT_DIR / "occupancy_activity_noise.png",
    dpi=200
)

plt.close()

print("Saved occupancy_activity_noise.png")