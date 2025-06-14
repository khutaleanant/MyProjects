#	Linear Regression is a supervised machine learning algorithm used for predicting a continuous target variable based on one or more input features. 
#   It models the relationship between the dependent variable (target) and one or more independent variables (features) by fitting a linear equation to the observed data. 
#	Mathematically, it assumes that the target variable y can be expressed as a linear combination of the input features X: 
#	y=β0+β1x1+β2x2+⋯+βnxn+ϵ
#	β0 is the intercept (bias term),
#	β1 ,β2,…,βn are the coefficients (weights) for each feature,
#	ϵ represents the error term (noise). 
#	The goal of linear regression is to learn the coefficients β that minimize the difference between the predicted values and the actual target values, often by minimizing the mean squared error.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# Load the dataset
url="http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg","cylinders","displacement","horsepower","weight","acceleration","model year","origin","car name"]
DataFrame=pd.read_csv(url,names=column_names,sep=r"\s+",na_values="?")

# Clean the data
DataFrame.dropna(inplace=True)
DataFrame.drop("car name",axis=1,inplace=True)

# Convert Data Types if needed
DataFrame["horsepower"] = DataFrame["horsepower"].astype(float)

# Exploratory Data Analysis (EDA) Visualizations
# Correlation HeatMap
plt.figure(figsize=(10, 10))
sns.heatmap(DataFrame.corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()

# Pairplot to see relationship
sns.pairplot(DataFrame[["mpg","horsepower","weight","acceleration","displacement"]])
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.show()

# Distribution of MPG
sns.histplot(data=DataFrame, x='mpg', kde=True, bins=20)
plt.title("Distribution of MPG")
plt.xlabel("Miles Per Gallon (MPG)")
plt.ylabel("Frequency")
plt.show()

# Feature and Target
X= DataFrame.drop("mpg", axis=1)
y = DataFrame["mpg"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared score :", r2_score(y_test, y_pred))

# Coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\n Model Coefficients:\n", coefficients)

# Visualization : Actual vs Predicted MPG
plt.figure(figsize=(10, 10))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--') # Reference line
plt.title("Actual vs Predicted MPG")
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.show()

# Residual Plot
residual= y_test - y_pred
plt.figure(figsize=(10, 10))
sns.histplot(residual, bins=30, kde=True)
plt.title("Residuals Distribution")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

