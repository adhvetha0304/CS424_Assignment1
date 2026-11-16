import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "study" / "results.csv"
OUT = ROOT / "analysis"
OUT.mkdir(exist_ok=True)

with INPUT.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

assert len(rows) == 40, "Expected 40 task records"
assert len({r["participant_id"] for r in rows}) == 10

for r in rows:
    r["time_seconds"] = float(r["time_seconds"])
    r["accuracy"] = int(r["accuracy"])
    r["timed_out"] = int(r["timed_out"])

def summarize(group):
    return {
        "n": len(group),
        "mean": mean(r["time_seconds"] for r in group),
        "median": median(r["time_seconds"] for r in group),
        "accuracy": mean(r["accuracy"] for r in group) * 100,
        "timeouts": sum(r["timed_out"] for r in group),
    }

groups = defaultdict(list)
participants = defaultdict(dict)

for r in rows:
    groups[r["condition"]].append(r)
    groups[(r["condition"], r["task_type"])].append(r)
    groups[(r["condition_order"], r["condition"])].append(r)
    participants[r["participant_id"]].setdefault(
        r["condition"], []
    ).append(r["time_seconds"])

lines = ["ASSIGNMENT 3 - STUDY RESULTS", "=" * 40]
lines.append(f"Participants: {len(participants)}")
lines.append(f"Tasks: {len(rows)}")
lines.append("")

for condition in ("Static", "Interactive"):
    s = summarize(groups[condition])
    lines.append(
        f"{condition}: n={s['n']}, mean={s['mean']:.2f}s, "
        f"median={s['median']:.2f}s, "
        f"accuracy={s['accuracy']:.1f}%, "
        f"timeouts={s['timeouts']}"
    )

lines.append("\nBY TASK TYPE")
for task in ("A", "B"):
    for condition in ("Static", "Interactive"):
        s = summarize(groups[(condition, task)])
        lines.append(
            f"Task {task}, {condition}: "
            f"n={s['n']}, mean={s['mean']:.2f}s, "
            f"median={s['median']:.2f}s"
        )

lines.append("\nBY PRESENTATION ORDER")
for order in ("Static-Interactive", "Interactive-Static"):
    for condition in ("Static", "Interactive"):
        s = summarize(groups[(order, condition)])
        lines.append(
            f"{order}, {condition}: "
            f"n={s['n']}, mean={s['mean']:.2f}s"
        )

lines.append("\nPAIRED PARTICIPANT AVERAGES")
diffs = []
for pid in sorted(participants):
    static = mean(participants[pid]["Static"])
    interactive = mean(participants[pid]["Interactive"])
    diff = static - interactive
    diffs.append(diff)
    lines.append(
        f"{pid}: static={static:.2f}s, "
        f"interactive={interactive:.2f}s, "
        f"static-minus-interactive={diff:+.2f}s"
    )

lines.append(
    f"\nMean paired difference: {mean(diffs):+.2f}s"
)
lines.append(
    f"Participants faster with interactive: "
    f"{sum(d > 0 for d in diffs)}/10"
)

report = "\n".join(lines) + "\n"
(OUT / "summary.txt").write_text(report, encoding="utf-8")
print(report)

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib not installed; numerical analysis is saved.")
    print("Charts can be generated after installing matplotlib.")
else:
    conditions = ["Static", "Interactive"]
    values = [summarize(groups[c])["mean"] for c in conditions]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(conditions, values, color=["#F6A0AC", "#A1C3E7"])
    ax.set_ylabel("Mean completion time (seconds)")
    ax.set_title("Average Task Completion Time")
    ax.set_ylim(0, max(values) * 1.25)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.5,
            f"{value:.2f}s",
            ha="center"
        )
    for bar in ax.patches:
        bar.set_edgecolor("#4F5568")
        bar.set_linewidth(1.0)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#E8EAF0", linewidth=0.7)
    fig.tight_layout()
    fig.savefig(OUT / "condition_times.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    task_types = ["A", "B"]
    x = range(len(task_types))
    width = 0.35

    for offset, condition, color in [
        (-width / 2, "Static", "#F6A0AC"),
        (width / 2, "Interactive", "#A1C3E7"),
    ]:
        values = [
            summarize(groups[(condition, task)])["mean"]
            for task in task_types
        ]
        ax.bar(
            [i + offset for i in x],
            values,
            width,
            label=condition,
            color=color,
        )

    ax.set_xticks(list(x), ["Task A", "Task B"])
    ax.set_ylabel("Mean completion time (seconds)")
    ax.set_title("Completion Time by Task Type")
    ax.legend()
    for bar in ax.patches:
        bar.set_edgecolor("#4F5568")
        bar.set_linewidth(1.0)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#E8EAF0", linewidth=0.7)
    fig.tight_layout()
    fig.savefig(OUT / "task_type_times.png", dpi=180)
    plt.close(fig)

    print("Charts saved:")
    print(" - assignment3/analysis/condition_times.png")
    print(" - assignment3/analysis/task_type_times.png")

# Required accuracy comparison chart
if "plt" in globals():
    fig, ax = plt.subplots(figsize=(7, 4.5))

    conditions = ["Static", "Interactive"]
    accuracies = [
        summarize(groups[c])["accuracy"]
        for c in conditions
    ]

    bars = ax.bar(
        conditions,
        accuracies,
        color=["#F6A0AC", "#A1C3E7"]
    )

    ax.set_ylim(0, 110)
    ax.set_ylabel("Task accuracy (%)")
    ax.set_title("Task Accuracy by Visualization Condition")

    for bar, value in zip(bars, accuracies):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 2,
            f"{value:.0f}%",
            ha="center"
        )

    for bar in ax.patches:
        bar.set_edgecolor("#4F5568")
        bar.set_linewidth(1.0)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#E8EAF0", linewidth=0.7)
    fig.tight_layout()
    fig.savefig(
        OUT / "condition_accuracy.png",
        dpi=180
    )
    plt.close(fig)

    print("Saved assignment3/analysis/condition_accuracy.png")


# Paired completion times by participant
if "plt" in globals():
    ids = sorted(participants)
    static_times = [
        mean(participants[pid]["Static"]) for pid in ids
    ]
    interactive_times = [
        mean(participants[pid]["Interactive"]) for pid in ids
    ]

    fig, ax = plt.subplots(figsize=(9, 4.8))
    x = list(range(len(ids)))

    for i, (s, t) in enumerate(zip(static_times, interactive_times)):
        ax.plot([i, i], [s, t], color="#CDD1DC", linewidth=1.5, zorder=1)

    ax.scatter(
        x, static_times, color="#F6A0AC",
        edgecolors="#4F5568", s=65, label="Static", zorder=3
    )
    ax.scatter(
        x, interactive_times, color="#A1C3E7",
        edgecolors="#4F5568", s=65, label="Interactive", zorder=3
    )

    ax.set_xticks(x, ids)
    ax.set_ylabel("Mean completion time (seconds)")
    ax.set_title("Completion Time by Participant")
    ax.set_ylim(bottom=0)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#E8EAF0", linewidth=0.7)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "participant_times.png", dpi=180)
    plt.close(fig)

    print("Saved assignment3/analysis/participant_times.png")
