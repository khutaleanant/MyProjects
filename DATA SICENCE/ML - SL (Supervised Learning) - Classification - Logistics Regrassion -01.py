# Logistic Regression on Rain Prediction (Binary Classification)
# This code predicts whether it will rain tomorrow using logistic regression on the WeatherAUS dataset.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_curve, auc, precision_recall_curve
)
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\WeatherAUS.csv")

# Basic inspection
print("Shape: ", DataFrame.shape)
print("Missing Values:\n", DataFrame.isnull().sum().sort_values(ascending=False).head())

# Visualize target distribution
sns.countplot(x='RainTomorrow', data=DataFrame)
plt.title("RainTomorrow Class Distribution")
plt.show()

# Drop columns with many missing values or irrelevant features
DataFrame.drop(['Date', 'Location', 'Evaporation', 'Sunshine', 'Cloud9am', 'Cloud3pm'], axis=1, inplace=True)

# Fill missing values for numeric columns with median
for col in DataFrame.select_dtypes(include=['float64', 'int64']).columns:
    DataFrame[col] = DataFrame[col].fillna(DataFrame[col].median())

# Encode categorical columns using LabelEncoder
le = LabelEncoder()
for col in DataFrame.select_dtypes(include=['object']).columns:
    if col != 'RainTomorrow':  # Skip target column here
        DataFrame[col] = le.fit_transform(DataFrame[col])

# Encode target variable (ensure binary 0/1 format)
DataFrame['RainTomorrow'] = DataFrame['RainTomorrow'].map({'No': 0, 'Yes': 1})

# Drop any rows with NaN in the target column (just in case)
DataFrame.dropna(subset=['RainTomorrow'], inplace=True)

# Prepare input features (X) and target (y)
X = DataFrame.drop('RainTomorrow', axis=1)
y = DataFrame['RainTomorrow']

# Check target classes (for debugging)
print("Target class distribution:\n", y.value_counts())

# Split data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Predict classes and probabilities
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]  # Probability of class 1 (Rain)

# Evaluate model performance
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# -------------------------
# 📊 Post Modeling Visualizations
# -------------------------

# Confusion Matrix Visualization
plt.figure(figsize=(6, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d',
            cmap='Blues', xticklabels=['No Rain', 'Rain'], yticklabels=['No Rain', 'Rain'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, color='blue', label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.grid()
plt.show()

# Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_prob)

plt.figure(figsize=(6, 6))
plt.plot(recall, precision, color='green')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.grid()
plt.show()

# Feature Importance (Model Coefficients)
coeff_dataframe = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', key=abs, ascending=False)

plt.figure(figsize=(8, 10))
sns.barplot(x='Coefficient', y='Feature', data=coeff_dataframe, palette='viridis')
plt.title("Feature Importance (Logistic Regression Coefficients)")
plt.tight_layout()
plt.show()