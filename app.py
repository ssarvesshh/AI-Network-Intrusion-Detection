from pathlib import Path

import pandas as pd
import streamlit as st
from joblib import load

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "intrusion_detection_model.joblib"

st.set_page_config(
    page_title="AI Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Network Intrusion Detection System")
st.write(
    "Analyze network traffic records using a machine-learning model "
    "trained to distinguish benign traffic from potential attacks."
)

if not MODEL_PATH.exists():
    st.error("Trained model not found. Run src/train_model.py first.")
    st.stop()

@st.cache_resource
def load_model(path):
    return load(path)

model = load_model(MODEL_PATH)
expected_features = list(model.feature_names_in_)

st.sidebar.header("Project Information")
st.sidebar.write("Model: Random Forest")
st.sidebar.write("Task: Binary traffic classification")
st.sidebar.info(
    "This is a demonstration using uploaded CSV records. "
    "It does not monitor live network traffic."
)

st.subheader("Analyze Network Traffic")
uploaded_file = st.file_uploader(
    "Upload a network traffic CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file, low_memory=False)
        data.columns = data.columns.str.strip()

        st.write("Uploaded dataset preview")
        st.dataframe(data.head(10), use_container_width=True)

        # Match the columns used during model training.
        features = data.reindex(columns=expected_features)

        for column in expected_features:
            features[column] = pd.to_numeric(
                features[column], errors="coerce"
            )

        features = features.replace([float("inf"), float("-inf")], float("nan"))

        valid_rows = features.notna().all(axis=1)
        invalid_count = int((~valid_rows).sum())

        if invalid_count:
            st.warning(
                f"{invalid_count} rows contain missing or invalid "
                "required features and will be skipped."
            )

        valid_features = features.loc[valid_rows]

        if valid_features.empty:
            st.error(
                "No usable rows found. Check that the uploaded CSV "
                "contains the same network feature columns as the training data."
            )
            st.stop()

        max_rows = 5000
        if len(valid_features) > max_rows:
            st.warning(
                f"Only the first {max_rows} valid rows will be analyzed "
                "to keep the dashboard responsive."
            )
            valid_features = valid_features.head(max_rows)

        if st.button("Analyze Traffic", type="primary"):
            predictions = model.predict(valid_features)

            results = data.loc[valid_features.index].copy()
            results["AI Prediction"] = [
                "Attack" if value == 1 else "Benign"
                for value in predictions
            ]

            benign_count = int((predictions == 0).sum())
            attack_count = int((predictions == 1).sum())

            st.subheader("Prediction Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("Records analyzed", len(predictions))
            col2.metric("Benign predictions", benign_count)
            col3.metric("Attack predictions", attack_count)

            st.write("Prediction results")
            st.dataframe(results, use_container_width=True)

            st.download_button(
                "Download Prediction Results",
                data=results.to_csv(index=False).encode("utf-8"),
                file_name="intrusion_detection_predictions.csv",
                mime="text/csv"
            )

            st.caption(
                "Predictions are model estimates, not proof that traffic "
                "is safe or malicious. Validate results before taking action."
            )

    except Exception as error:
        st.error(f"Could not analyze this file: {error}")

else:
    st.info("Upload a CSV file to begin analyzing network traffic.")
    st.write("The uploaded file must contain the numeric feature columns "
             "used to train this model.")

st.divider()
st.caption("Educational machine-learning project | Random Forest classifier")
