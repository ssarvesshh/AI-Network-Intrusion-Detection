import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_DIR = PROJECT_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

print("Loading training data...")
X_train = pd.read_csv(DATA_DIR / "X_train.csv", low_memory=False)
y_train = pd.read_csv(DATA_DIR / "y_train.csv").iloc[:, 0]

print("Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

model.fit(X_train, y_train)

model_path = MODEL_DIR / "intrusion_detection_model.joblib"
dump(model, model_path)

print("\nModel training completed successfully!")
print("Training records:", len(X_train))
print("Input features:", X_train.shape[1])
print("Saved model to:", model_path)
