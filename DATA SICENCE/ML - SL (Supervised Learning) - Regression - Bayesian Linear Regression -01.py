# Bayesian Linear Regression on Yacht Hydrodynamics Dataset
# Bayesian Linear Regression is a supervised learning algorithm that applies the principles of Bayesian inference to the linear regression model. 
# Unlike traditional linear regression, which gives point estimates for model parameters (coefficients),
# Bayesian linear regression provides probability distributions over those parameters.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set Seaborn style
sns.set(style="whitegrid")

# Load the dataset
DataFrame = pd.read_csv("C://Data Science Programs Practice//Yacht Hydrodynamics Dataset.csv")

# Exploratory Data Analysis (EDA)
# Pairplot of Features and Target
sns.pairplot(DataFrame)
plt.suptitle("Pairplot of Yacht Hydrodynamics Dataset", y=1.02)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(DataFrame.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap of Yacht Hydrodynamics Dataset")
plt.show()

# Prepare Data for Modeling
X = DataFrame.drop("Rr", axis=1)  # Features
y = DataFrame["Rr"]  # Target variable
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit Bayesian Ridge Regression Model
model = BayesianRidge()
model.fit(X_train, y_train)
y_pred, y_std = model.predict(X_test, return_std=True)

# Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Coefficient Summary with Uncertainty
print("\nBayesian Regression Coefficients:")
for feature,coef,std in zip(X.columns,model.coef_,np.sqrt(np.diag(model.sigma_))):
    print(f"{feature:5s}:Coef= {coef:.4f} , {std:.4f}")

# Visualizations
# Predictions with Error Bars
plt.figure(figsize=(10, 6))
plt.errorbar(range(len(y_test)), y_pred, yerr=y_std, fmt='o', label='Predictions with Uncertainty', alpha=0.7)
plt.scatter(range(len(y_test)), y_test, color='red', label='True Values', alpha=0.5)
plt.title("Bayesian Ridge Regression Predictions with Uncertainty")
plt.xlabel("Sample Index")
plt.ylabel("Rr (Resistance)")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

# Predicted vs True Values Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Prediction')
plt.title("Predicted vs True Values")
plt.xlabel("True Resistance (Rr)")
plt.ylabel("Predicted Resistance (Rr)")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

# Residuals Plot
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=30, kde=True, color='purple', alpha=0.6)
plt.title("Residuals Distribution")
plt.xlabel("Residual (True - Predicted)")
plt.ylabel("Density")
plt.tight_layout()
plt.grid(True)
plt.show()