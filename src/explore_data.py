import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "cleaned_network_traffic.csv"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH, low_memory=False)
df.columns = df.columns.str.strip()

# Count each traffic label
label_counts = df["Label"].value_counts()

print("Network Traffic Label Counts")
print("=" * 35)
print(label_counts)

# Plot the label distribution
plt.figure(figsize=(10, 6))
label_counts.plot(kind="bar")
plt.title("Distribution of Network Traffic Labels")
plt.xlabel("Traffic Label")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

output_path = REPORTS_DIR / "traffic_label_distribution.png"
plt.savefig(output_path)
plt.show()

print("\nChart saved to:", output_path)
