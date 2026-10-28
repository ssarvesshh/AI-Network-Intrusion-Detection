from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_PATH = PROJECT_DIR / "models" / "intrusion_detection_model.joblib"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

print("Loading trained model...")
model = load(MODEL_PATH)

X_train = pd.read_csv(DATA_DIR / "X_train.csv", nrows=1)
feature_names = X_train.columns

importance = pd.Series(
    model.feature_importances_,
    index=feature_names
).sort_values(ascending=False)

top_features = importance.head(15)

print("\nTop 15 Important Features:")
print(top_features)

plt.figure(figsize=(10, 7))
top_features.sort_values().plot(kind="barh")
plt.title("Top 15 Important Network Traffic Features")
plt.xlabel("Importance Score")
plt.ylabel("Network Feature")
plt.tight_layout()

chart_path = REPORTS_DIR / "feature_importance.png"
plt.savefig(chart_path)
plt.show()

print("\nChart saved to:", chart_path)
