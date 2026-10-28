from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "Wednesday-workingHours.pcap_ISCX.csv"

print("Loading dataset from:", DATA_PATH)

df = pd.read_csv(DATA_PATH, low_memory=False)

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nFirst 5 rows:")
print(df.head())
