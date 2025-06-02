# Random Forest is a powerful ensemble learning algorithm used for 
# classification and regression tasks in supervised machine learning.
# It operates by constructing a "Forest" of decision trees during training and
# outputs the class that is the mode of the classes (Classification) or mean prediction (For Regression)
# of the individual trees.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,accuracy_score


# Load the dataset
Dataframe=pd.read_csv("C:\\Data Science Programs Practice\\Heart_Cleveland_Upload.csv")

# Preview Data and Columns
print("First Five Rows of the Selected Dataset")
print(Dataframe.head())
print("\nColumns in the dataset")
print(Dataframe.columns)

# Set the correct target column name
target_column="condition"

# Data Visualization
# Visualize target distribution
plt.figure(figsize=(12,12))
sns.countplot(x=target_column,data=Dataframe)
plt.title("Target Class Distribution")
plt.xlabel("Heart Condition")
plt.ylabel("Count")
plt.show()

# Visualize correlation heatmap between features
plt.figure(figsize=(12,12))
sns.heatmap(Dataframe.corr(),annot=True,fmt=".2f",cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# Visualize Distributions of selected features by target class
features_to_plot=["age","chol","thalach"]
for feature in features_to_plot:
    plt.figure(figsize=(12,12))
    sns.histplot(Dataframe,x=feature,hue=target_column,multiple="stack",kde=True)
    plt.title(f"Distribution of {feature} by heart condition")
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.show()

# Separate Features and Target
X=Dataframe.drop(columns=[target_column])
y=Dataframe[target_column]

# Spilt Dataset into train and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Initialize and Train random forest classifier (rfc)
rfc=RandomForestClassifier(n_estimators=100,random_state=42)
rfc.fit(X_train,y_train)

# Predict on test set and evaluate
y_pred=rfc.predict(X_test)
print(f"Acurracy on test set: {accuracy_score(y_test,y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test,y_pred))


 

