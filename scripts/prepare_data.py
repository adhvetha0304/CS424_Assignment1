import pandas as pd
from pathlib import Path

# File paths
ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "shared_spaces.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "shared_spaces_processed.csv"
