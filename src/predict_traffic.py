from pathlib import Path
import pandas as pd
from joblib import load

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_PATH = PROJECT_DIR / "models" / "intrusion_detection_model.joblib"

print("Loading trained intrusion detection model...")
model = load(MODEL_PATH)

X_test = pd.read_csv(DATA_DIR / "X_test.csv", nrows=1)

print("\nUsing one network traffic record for demonstration...")
prediction = model.predict(X_test)[0]

if prediction == 0:
    print("\nAI Prediction: BENIGN TRAFFIC")
    print("The model classified this record as normal traffic.")
else:
    print("\nAI Prediction: ATTACK TRAFFIC")
    print("The model classified this record as potentially malicious traffic.")

print("\nPrediction completed successfully.")
