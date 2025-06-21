import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Polynomial Regression Sample Dataset.csv")

# Extract features and target
X = DataFrame[["x"]].values
y = DataFrame["y"].values

# Create polynomial features (Change the degree as needed)
degree = 2  # You can try 3,4,etc.
poly= PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Predict
y_pred = model.predict(X_poly)

# Predict for the visualization
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_plot_poly = poly.transform(X_plot)
y_plot = model.predict(X_plot_poly)

# Print output
print(f"\nPolynomial Regression (Degree {degree})")
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")   # Includes terms for x^0, x^1, x^2, ...
print("\nPredicted Values for Training Data:")
for i in range(len(X)):
    print(f"x =: {X[i][0]:.2f}, Actual: {y[i]:.2f}, Predicted: {y_pred[i]:.2f}")

# Calculate R-squared
r2 = r2_score(y, y_pred)
print(f"R-squared: {r2:.4f}")

# Plotting the results
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X_plot, y_plot, color='red', label=f'Polynomial Regression (Degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Polynomial Regression Fit")
plt.legend()
plt.grid(True)
plt.show()
