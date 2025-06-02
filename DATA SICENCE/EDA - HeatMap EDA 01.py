import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample banking data (Correlation between variables)
data = {
    'Loan_Amount': [10000, 15000, 20000, 25000, 30000],
    'Interest_Rate': [5.5, 6.0, 5.8, 6.2, 5.7],
    'Customer_Age': [35, 42, 29, 50, 38],
    'Credit_Score': [700, 650, 720, 680, 690],
    'Loan_Approval_Status': [1, 0, 1, 0, 1]  # 1 = Approved, 0 = Denied
}

df = pd.DataFrame(data)

# Compute correlation matrix
correlation_matrix = df.corr()

# Plot hplt.show()eatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap - Banking Data')
# 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample ecommerce data (Performance of products by category)
data = {
    'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing'],
    'Price': [500, 40, 700, 1200, 50],
    'Sales': [200, 400, 150, 100, 450],
    'Ratings': [4.5, 3.9, 4.7, 4.2, 3.8],
    'Stock_Level': [20, 100, 5, 2, 80]
}

df = pd.DataFrame(data)

# Calculate correlation between numeric features (excluding 'Product_Category')
corr_matrix = df[['Price', 'Sales', 'Ratings', 'Stock_Level']].corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlation Heatmap - Ecommerce Data')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample educational data (Student performance factors)
data = {
    'Study_Hours': [10, 15, 8, 12, 20],
    'Attendance': [85, 90, 75, 80, 95],
    'Grades': [88, 92, 78, 80, 95],
    'Extra_Activities': [5, 3, 6, 4, 2]
}

df = pd.DataFrame(data)

# Calculate correlation between numeric features
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Correlation Heatmap - Educational Data')
plt.show()


