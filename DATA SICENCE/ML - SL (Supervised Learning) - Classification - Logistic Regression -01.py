# 📘 Logistic Regression for Diabetes Prediction
# ---------------------------------------------------
# Logistic Regression is a supervised machine learning algorithm used for binary classification tasks.
# It predicts the probability that a data point belongs to a particular class (e.g., "Diabetes: Yes or No").
# In this example, we will use a real-world diabetes prediction dataset to:
# - Load and clean the data
# - Encode categorical values
# - Train a logistic regression model
# - Evaluate its performance
# - Visualize results with a confusion matrix

# 🔧 Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 📥 Step 1: Load the dataset
df = pd.read_csv("C:\\Data Science Programs Practice\\Diabetes_Prediction_Dataset.csv")

# 🧹 Step 2: Check and handle missing values
print("Missing Values:\n", df.isnull().sum())

# 🔁 Step 3: Encode categorical columns to numeric (e.g., Gender, Smoking)
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# 🎯 Step 4: Define input features (X) and target variable (y)
X = df.drop('diabetes', axis=1)  # Features
y = df['diabetes']               # Target

# ✂️ Step 5: Split the dataset into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🤖 Step 6: Train the Logistic Regression model
model = LogisticRegression(max_iter=1000)  # max_iter increased to ensure convergence
model.fit(X_train, y_train)

# 🔍 Step 7: Make predictions on the test data
y_pred = model.predict(X_test)

# 📊 Step 8: Evaluate the model
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# 📉 Step 9: Visualize the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Logistic Regression")
plt.tight_layout()
plt.show()