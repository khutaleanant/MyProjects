import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor,plot_tree
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Insurance.csv")

# Features and Target
X=DataFrame[["age","sex","bmi","children","smoker","region"]]
y=DataFrame["charges"]

# One-hot encoding for categorical variables
X_encoded = pd.get_dummies(X,columns=["sex","smoker","region"],drop_first=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train Regression Tree model
reg_tree = DecisionTreeRegressor(random_state=42,max_depth=4)  # limit depth for clearer plot
reg_tree.fit(X_train,y_train)

# Make predictions
y_pred = reg_tree.predict(X_test)

# Evaluate the model
mse= mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared score: {r2:.2f}")

# Visualize the Regression Tree
plt.figure(figsize=(32, 16))
plot_tree(reg_tree, feature_names=list(X_encoded.columns), filled=True, rounded=True,fontsize=12,precision=2)
plt.title("Regression Tree", fontsize=18)
plt.tight_layout(pad=3.0)
plt.show()

# Visualize the predictions vs actual chagres
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6,color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", linewidth=2)
plt.title("Actual vs Predicted Insurance Charges")
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.grid(True)
plt.show()