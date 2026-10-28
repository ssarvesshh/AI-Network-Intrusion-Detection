import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "Wednesday-workingHours.pcap_ISCX.csv"

print("Loading dataset...")
df = pd.read_csv(DATA_PATH, low_memory=False)

print("Original shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Remove duplicate rows
df = df.drop_duplicates()

# Replace infinite values and handle missing values
df = df.replace([float("inf"), float("-inf")], float("nan"))
df = df.dropna()

print("Shape after cleaning:", df.shape)
print("Missing values remaining:", int(df.isna().sum().sum()))
print("\nTraffic labels:")
print(df["Label"].value_counts())

# Save the cleaned dataset
OUTPUT_PATH = PROJECT_DIR / "data" / "cleaned_network_traffic.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved to:", OUTPUT_PATH)
