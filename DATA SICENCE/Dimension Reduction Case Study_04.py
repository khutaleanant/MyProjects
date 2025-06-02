# Filter Method (Chi-Squered Test)

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Scale features to [0,1] Range(Chi-squared requires non-negative values)
scaler=MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Apply Chi-squared test to select top 10 features
chi2_selector = SelectKBest(score_func=chi2, k=10)
X_kbest = chi2_selector.fit_transform(X_scaled, y)

# Get the selected feature names and scores
selected_mask=chi2_selector.get_support()
selected_features= X.columns[selected_mask]
feature_scores=chi2_selector.scores_[selected_mask]

# Create a Dataframe of selected features and their scores
chi2_results=pd.DataFrame({"Feature":selected_features,"Chi2 Score":feature_scores})
print(f"Selected Features(Chi-Squared):{chi2_results}")

# Save selected features and scores to CSV file
chi2_results.to_csv("Selected_Features_Chi2.csv",index=False)

# Split the selected Features into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X_kbest,y,test_size=0.3,random_state=42)

# Train and Evaluate a model
model=LogisticRegression(max_iter=10000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("\n Classification Report:\n",classification_report(y_test,y_pred))
print("Accuracy Score:",accuracy_score(y_test,y_pred))

# Plot Chi-Squared Scores
plt.figure(figsize=(12,12))
plt.barh(chi2_results["Feature"],chi2_results["Chi2 Score"])
plt.title("Top Ten Features By Chi-Squared Score")
plt.tight_layout()
plt.show()