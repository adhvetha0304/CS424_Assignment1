import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "shared_spaces.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"

df = pd.read_csv(INPUT_FILE, keep_default_na=False)

# Checking that the expected columns are present
required_columns = [
    "observation_id",
    "date",
    "day_of_week",
    "time",
    "time_period",
    "space",
    "space_type",
    "people_count",
    "noise_level",
    "main_activity",
    "context_notes",
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

# Checking the important fields before processing
if not df["observation_id"].is_unique:
    raise ValueError("observation_id should be unique.")

if df["people_count"].eq("").any():
    raise ValueError("people_count contains missing values.")

if df["noise_level"].eq("").any():
    raise ValueError("noise_level contains missing values.")

# Making sure numeric fields are stored as numbers
df["observation_id"] = pd.to_numeric(
    df["observation_id"],
    errors="raise"
).astype(int)

df["people_count"] = pd.to_numeric(
    df["people_count"],
    errors="raise"
).astype(int)

if (df["people_count"] < 0).any():
    raise ValueError("people_count cannot be negative.")

# Removing extra spaces from text fields
categorical_columns = [
    "day_of_week",
    "time",
    "time_period",
    "space",
    "space_type",
    "noise_level",
    "main_activity",
]

for column in categorical_columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )

# Setting the date format consistently
df["date"] = pd.to_datetime(
    df["date"],
    errors="raise"
).dt.strftime("%Y-%m-%d")

# Checking the activity values for empty and non-empty spaces
empty_spaces = df["people_count"] == 0

if not (
    df.loc[empty_spaces, "main_activity"] == "None"
).all():
    raise ValueError(
        "An empty-space observation does not have None as its activity."
    )

if (
    df.loc[~empty_spaces, "main_activity"]
    .isin(["", "None"])
).any():
    raise ValueError(
        "A non-empty observation is missing its activity."
    )

# Adding an ID for each observation session
session_order = [
    ("2026-09-27", "6-9 PM"),
    ("2026-09-28", "5 PM"),
    ("2026-09-29", "6 AM"),
    ("2026-09-29", "3 PM"),
    ("2026-10-01", "6 PM"),
    ("2026-10-01", "9 PM"),
    ("2026-10-03", "5:50 PM"),
]

session_map = {
    (date, time): index + 1
    for index, (date, time) in enumerate(session_order)
}

df["session_id"] = [
    session_map.get((date, time))
    for date, time in zip(df["date"], df["time"])
]

if df["session_id"].isna().any():
    raise ValueError(
        "An observation could not be assigned to a session."
    )

df["session_id"] = df["session_id"].astype(int)

# Checking that every session contains all four spaces
session_counts = df.groupby("session_id").size()
session_spaces = df.groupby("session_id")["space"].nunique()

if not (session_counts == 4).all():
    raise ValueError(
        "Every observation session should contain four observations."
    )

if not (session_spaces == 4).all():
    raise ValueError(
        "Every observation session should contain all four spaces."
    )

# Adding a readable label for each session
df["session_label"] = (
    "S"
    + df["session_id"].astype(str)
    + ": "
    + df["date"]
    + " "
    + df["time"]
)

# Saving the processed dataset
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Processed {len(df)} observations.")
print(f"Saved processed data to: {OUTPUT_FILE}")
