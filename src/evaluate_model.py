import pandas as pd
from pathlib import Path
from joblib import load
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_PATH = PROJECT_DIR / "models" / "intrusion_detection_model.joblib"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

print("Loading model and test data...")
model = load(MODEL_PATH)
X_test = pd.read_csv(DATA_DIR / "X_test.csv", low_memory=False)
y_test = pd.read_csv(DATA_DIR / "y_test.csv").iloc[:, 0]

print("Testing model...")
y_pred = model.predict(X_test)

print("\nModel Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(
    y_test, y_pred,
    labels=[0, 1],
    target_names=["Benign", "Attack"],
    zero_division=0
))

cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Benign", "Attack"]
)
display.plot()
plt.title("Intrusion Detection - Confusion Matrix")
plt.tight_layout()

chart_path = REPORTS_DIR / "confusion_matrix.png"
plt.savefig(chart_path)
plt.show()

print("\nConfusion matrix saved to:", chart_path)
