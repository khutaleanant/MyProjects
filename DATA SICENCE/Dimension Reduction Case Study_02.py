# Wrapper method (Recursive Feature Elimination)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import classification_report, accuracy_score

# Load the Wisconsin Breast Cancer Dataset
data = load_breast_cancer()

# Convert Dataset to pandas dataframe
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a logistic Regression Model
model = LogisticRegression(max_iter=10000)

# Apply RFE to select top ten features
rfe = RFE(model, n_features_to_select=10)
rfe.fit(X_train_scaled, y_train)

# Get selected feature names and their ranking
feature_ranking = pd.DataFrame({
    "Feature": X.columns,
    "Selected": rfe.support_,
    "Ranking": rfe.ranking_
})

# Display selected features
print("Selected Features:")
print(feature_ranking[feature_ranking["Selected"] == True])

# Visualize feature rankings
plt.figure(figsize=(12, 8))
plt.barh(feature_ranking["Feature"], feature_ranking["Ranking"], color='skyblue')
plt.xlabel("Ranking (1 = Selected)")
plt.title("Feature Ranking using RFE")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Train model on selected features
X_train_rfe = rfe.transform(X_train_scaled)
X_test_rfe = rfe.transform(X_test_scaled)

model.fit(X_train_rfe, y_train)
y_pred = model.predict(X_test_rfe)

# Evaluate model
print("\nModel Evaluation:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
