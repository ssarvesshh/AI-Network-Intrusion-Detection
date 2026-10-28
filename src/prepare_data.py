import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "cleaned_network_traffic.csv"

df = pd.read_csv(DATA_PATH, low_memory=False)
df.columns = df.columns.str.strip()

# Convert labels into two classes: Benign and Attack
df["Label"] = df["Label"].astype(str).str.strip()
df["Target"] = (df["Label"].str.upper() != "BENIGN").astype(int)

# Keep numeric features only
X = df.drop(columns=["Label", "Target"])
X = X.select_dtypes(include=["number"])

# Replace invalid values and remove unusable rows
X = X.replace([float("inf"), float("-inf")], float("nan"))
valid_rows = X.notna().all(axis=1)
X = X.loc[valid_rows]
y = df.loc[valid_rows, "Target"]

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Data preparation successful!")
print("Number of input features:", X.shape[1])
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("\nTraining class distribution:")
print(y_train.value_counts().rename(index={0: "Benign", 1: "Attack"}))

# Save prepared datasets
X_train.to_csv(PROJECT_DIR / "data" / "X_train.csv", index=False)
X_test.to_csv(PROJECT_DIR / "data" / "X_test.csv", index=False)
y_train.to_csv(PROJECT_DIR / "data" / "y_train.csv", index=False)
y_test.to_csv(PROJECT_DIR / "data" / "y_test.csv", index=False)

print("\nTraining and testing files saved in data/")
