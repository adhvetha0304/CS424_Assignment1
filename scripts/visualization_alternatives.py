import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
OUTPUT_DIR = ROOT / "assignment2" / "figures" / "alternatives"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Reading the processed dataset
df = pd.read_csv(INPUT_FILE, keep_default_na=False)

spaces = [
    "Study Lounge 1",
    "Study Lounge 2",
    "Gym",
    "Common Area",
]

fig, ax = plt.subplots(figsize=(10, 5))

for i, space in enumerate(spaces):
    counts = df.loc[
        df["space"] == space, "people_count"
    ].sort_values()

    minimum = counts.min()
    maximum = counts.max()
    median = counts.median()

    # Showing the observed range
    ax.plot(
        [minimum, maximum],
        [i, i],
        color="gray",
        linewidth=2,
        alpha=0.6,
        zorder=1
    )

    # Separating repeated observations vertically
    repeated = {}

    for count in counts:
        occurrence = repeated.get(count, 0)
        repeated[count] = occurrence + 1

        offsets = [0, -0.12, 0.12, -0.24, 0.24, -0.36, 0.36]

        ax.scatter(
            count,
            i + offsets[occurrence],
            color="steelblue",
            s=65,
            alpha=0.85,
            zorder=3
        )

    # Adding the median as a separate mark
    ax.scatter(
        median,
        i,
        marker="D",
        color="darkorange",
        s=100,
        edgecolor="black",
        linewidth=0.5,
        zorder=4
    )

ax.set_yticks(range(len(spaces)))
ax.set_yticklabels(spaces)
ax.invert_yaxis()

ax.set_xlabel("People Observed")
ax.set_title("Occupancy Distribution by Shared Space")
ax.set_xlim(-0.5, 15)
ax.set_xticks(range(0, 15, 2))
ax.grid(axis="x", alpha=0.25)

# Explaining the visual marks
from matplotlib.lines import Line2D

legend_items = [
    Line2D([0], [0], marker="o", linestyle="None",
           color="steelblue", label="Observation"),
    Line2D([0], [0], marker="D", linestyle="None",
           color="darkorange", markeredgecolor="black",
           label="Median"),
    Line2D([0], [0], color="gray", linewidth=2,
           label="Observed range")
]

ax.legend(
    handles=legend_items,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.14),
    ncol=3,
    frameon=False
)

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "alternative_a_distribution.png",
    dpi=200
)
plt.close()

print("Saved alternative_a_distribution.png")