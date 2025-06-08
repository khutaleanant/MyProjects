# 📘 Decision Tree Algorithm (Simple Explanation)

# A Decision Tree is a machine learning method used to make predictions.

# It works like a flowchart:
# - Each question (node) checks one feature (like Age or BMI).
# - Each answer (branch) leads to the next question.
# - At the end (leaf), it gives the final result (like Yes or No for diabetes).

# How it builds the tree:
# - It finds the best questions to split the data.
# - It keeps splitting until:
#   - It can’t improve the result,
#   - Or the tree becomes too deep.

# Useful for:
# - Classification (e.g., predicting if someone has diabetes: Yes/No)
# - Regression (e.g., predicting a number like house price)


# Decision Tree Classifier for Diabetes Prediction

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\Diabetes_Prediction_Dataset.csv")

# Check for missing values
print("Missing Values:\n", DataFrame.isnull().sum())

# Display first 10 records
print("\nSample Data:\n", DataFrame.head(10))

# Encode categorical variables
le = LabelEncoder()
for column in DataFrame.columns:
    if DataFrame[column].dtype == 'object':
        DataFrame[column] = le.fit_transform(DataFrame[column])

# Display column names and types
print("\nEncoded Columns and Types:\n", DataFrame.dtypes)

# Define features and target
X = DataFrame.drop('diabetes', axis=1)
y = DataFrame['diabetes']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)

# Predict on test data
y_pred = dt_model.predict(X_test)

# Evaluate the model
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(dt_model, filled=True, feature_names=X.columns.tolist(), class_names=['No', 'Yes'])
plt.title("Decision Tree for Diabetes Prediction")
plt.show()
