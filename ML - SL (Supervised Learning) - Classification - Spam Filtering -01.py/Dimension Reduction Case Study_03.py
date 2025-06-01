# Embedded Method (Lasso Regression)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LassoCV, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Load the Dataset
data = load_breast_cancer()

# Convert to Pandas DataFrame
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data (Lasso is sensitive to scale)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# LassoCV (Lasso with Cross-Validation to find best alpha)
lasso = LassoCV(cv=5, max_iter=1000, random_state=42)
lasso.fit(X_train_scaled, y_train)

# Get selected features (Non-Zero Coefficients)
coef = pd.Series(lasso.coef_, index=X.columns)
selected_features = coef[coef != 0]
print("Selected Features (Lasso):")
print(selected_features)

# Save selected features to CSV file
selected_features.to_csv("selected_features_Lasso.csv", header=["Coefficient"])

# Evaluate on test set using only selected features
X_train_selected = X_train_scaled[:, coef != 0]
X_test_selected = X_test_scaled[:, coef != 0]

# Train a simple logistic regression model on selected features
model = LogisticRegression(max_iter=1000)
model.fit(X_train_selected, y_train)

# Corrected prediction line
y_pred = model.predict(X_test_selected)

# Model evaluation
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Visualize selected feature coefficients
plt.figure(figsize=(12, 10))
selected_features.sort_values().plot(kind="barh")
plt.title("Lasso Selected Features and Coefficients")
plt.xlabel("Coefficient Value")
plt.tight_layout()
plt.savefig("Lasso_Features_Importance.png")
plt.show()