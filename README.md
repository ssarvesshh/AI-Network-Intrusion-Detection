# AI-Powered Network Intrusion Detection System

## 1. Project Overview

This project uses machine learning to classify network traffic records as
Benign or Attack. It uses a Random Forest classifier trained on the
CIC-IDS2017 Wednesday working-hours dataset.

The project includes data cleaning, exploratory analysis, model training,
evaluation, feature-importance visualization, and a Streamlit dashboard.

**Important:** This is an educational, offline demonstration. It does not
monitor live network traffic or guarantee that a prediction is correct.

## 2. Objectives

- Load and clean network traffic data.
- Explore traffic labels and distributions.
- Prepare numerical features for machine learning.
- Train a Random Forest classification model.
- Evaluate model performance on held-out test data.
- Visualize important features and model predictions.
- Provide an interactive CSV-analysis dashboard.

## 3. Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Visual Studio Code

## 4. Project Structure

```text
AI-Network-Intrusion-Detection/
├── app.py
├── data/
│   ├── Wednesday-workingHours.pcap_ISCX.csv
│   ├── cleaned_network_traffic.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
├── models/
│   └── intrusion_detection_model.joblib
├── notebooks/
├── reports/
│   ├── traffic_label_distribution.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
├── src/
│   ├── load_dataset.py
│   ├── explore_data.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── feature_importance.py
│   └── predict_traffic.py
└── README.md
```

## 5. Workflow

1. Load the original CSV dataset.
2. Clean column names and remove duplicate or incomplete records.
3. Explore the distribution of network traffic labels.
4. Convert labels into Benign and Attack classes.
5. Select numerical features and split the data into training and testing sets.
6. Train a Random Forest classifier.
7. Evaluate the classifier using accuracy, precision, recall, F1-score,
   and a confusion matrix.
8. Visualize feature importance.
9. Run a sample prediction.
10. Use the Streamlit dashboard to analyze compatible CSV files.

## 6. Setup

Install Python 3.12 or another compatible Python version.

Activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages if needed:

```powershell
uv pip install numpy pandas matplotlib seaborn scikit-learn jupyter joblib streamlit
```

## 7. Running the Project

Run these commands from the project root, in order:

```powershell
python src/load_dataset.py
python src/explore_data.py
python src/prepare_data.py
python src/train_model.py
python src/evaluate_model.py
python src/feature_importance.py
python src/predict_traffic.py
python -m streamlit run app.py
```

The Streamlit dashboard normally opens at http://localhost:8501.

## 8. Evaluation

The evaluation script reports accuracy, precision, recall, and F1-score.
It also creates a confusion matrix.

The feature-importance script ranks the numerical features used by the
Random Forest model.

Record the actual results printed by your scripts before reporting
performance in a presentation. Do not assume a particular accuracy.

## 9. Limitations

- The model is trained on a particular public dataset.
- Its performance on other networks or newer attack types may differ.
- Dataset bias and class imbalance can affect results.
- Predictions are not proof of malicious activity.
- The dashboard analyzes uploaded CSV records; it does not capture packets
  or automatically block network connections.

## 10. Future Improvements

- Add more datasets and evaluate generalization.
- Improve handling of class imbalance.
- Compare Random Forest with other classifiers.
- Add better validation and input-column checks.
- Explore live traffic collection in a controlled lab environment.
- Improve dashboard charts and reporting.

## 11. Dataset

CIC-IDS2017, published by the Canadian Institute for Cybersecurity:
https://www.unb.ca/cic/datasets/ids-2017.html

Follow the dataset's applicable terms and citation requirements when
redistributing data or publishing results.

## 12. Conclusion

This project demonstrates an end-to-end machine-learning workflow for
network traffic classification, from data preparation and model training
to evaluation and interactive visualization.
