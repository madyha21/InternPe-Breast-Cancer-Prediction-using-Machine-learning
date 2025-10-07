# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the Breast Cancer Diagnostic dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
columns = [
    "id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se", "concavity_se",
    "concave points_se", "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst",
    "area_worst", "smoothness_worst", "compactness_worst", "concavity_worst", "concave points_worst",
    "symmetry_worst", "fractal_dimension_worst"
]

data = pd.read_csv(url, header=None, names=columns)

# Encode the target variable
label_encoder = LabelEncoder()
data["diagnosis"] = label_encoder.fit_transform(data["diagnosis"])

# Split the dataset into features (X) and target variable (y)
X = data.drop(['id', 'diagnosis'], axis=1)
y = data['diagnosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a SVM classifier
model = SVC()
model.fit(X_train, y_train)

# Streamlit app
st.title("Breast Cancer Prediction System")

# Sidebar for user input features
st.sidebar.header("User Input Features")
user_input = {}

for column in X.columns:
    value = st.sidebar.slider(f"{column}:", float(X[column].min()), float(X[column].max()), float(X[column].mean()))
    user_input[column] = value

user_input_df = pd.DataFrame([user_input])  # Convert to DataFrame

# Predict the diagnosis
prediction = model.predict(user_input_df)

# Display prediction
st.subheader("Prediction")
diagnosis_label = "Malignant" if prediction[0] == 1 else "Benign"
st.write(f"The diagnosis is {diagnosis_label}.")

# Display model evaluation metrics
st.subheader("Model Evaluation Metrics")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

st.write(f"Accuracy: {accuracy:.2f}")
st.write("Classification Report:")
st.text(classification_rep)
