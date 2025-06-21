## Non-Linear Regression using Random Forest on Energy Efficiency Dataset
# Non-linear regression is a type of supervised learning algorithm used in machine learning where the relationship between the input variables (features) 
# and the output variable (target) cannot be modeled accurately using a straight line (i.e., it's not linear).
# Instead, non-linear functions (like polynomials, exponentials, logarithmic functions, etc.) are used to model complex, curved relationships in the data.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
DataFrame=pd.read_csv("C://Data Science Programs Practice//Energy Efficiency Dataset.csv")

# Features and targets
X=DataFrame[["X1","X2","X3","X4","X5","X6","X7","X8"]]
y1=DataFrame["Y1"]  # Heating Load
y2=DataFrame["Y2"]  # Cooling Load

# Split the Data into training and testing sets
X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
_,_,y2_train,y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)

# Non-Linear Regression Model
model_y1 = RandomForestRegressor(n_estimators=100, random_state=42)
model_y1.fit(X_train, y1_train)

model_y2 = RandomForestRegressor(n_estimators=100, random_state=42)
model_y2.fit(X_train, y2_train)

# Predict
y1_pred = model_y1.predict(X_test)
y2_pred = model_y2.predict(X_test)

# Evaluate the model
print("Heating Load (Y1) Evaluation:")
print("Mean Squared Error:", mean_squared_error(y1_test, y1_pred))
print("R^2 Score:", r2_score(y1_test, y1_pred))
print("\nCooling Load (Y2) Evaluation:")
print("Mean Squared Error:", mean_squared_error(y2_test, y2_pred))
print("R^2 Score:", r2_score(y2_test, y2_pred))

# Visualize the results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y1_test, y=y1_pred)
plt.plot([y1_test.min(), y1_test.max()], [y1_test.min(), y1_test.max()], 'r--')
plt.title('Heating Load (Y1) Prediction')
plt.xlabel('Actual Y1')
plt.ylabel('Predicted Y1')

plt.subplot(1, 2, 2)
sns.scatterplot(x=y2_test, y=y2_pred)
plt.plot([y2_test.min(), y2_test.max()], [y2_test.min(), y2_test.max()], 'r--')
plt.title('Cooling Load (Y2) Prediction')
plt.xlabel('Actual Y2')
plt.ylabel('Predicted Y2')

plt.tight_layout()
plt.show()
