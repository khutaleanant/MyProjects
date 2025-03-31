# The goal of Missing Data Analysis is to understand the pattern and extent of missing values and to decide how to handle them appropriately.

#Methods for Identifying Missing Data:
# 1) NaN (Not a Number): Typically used in pandas to represent missing values.

# 2) Null or None: In some databases, missing data is represented as NULL or None.

import pandas as pd

# Example dataset
data = {
    'Age': [25, 30, 35, None, 40, 45, None, 50],
    'Salary': [50000, 60000, 70000, 80000, None, 90000, 100000, None],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# Check for missing data in each column
missing_data = df.isnull().sum()

# Check the percentage of missing data in each column
missing_percentage = (df.isnull().sum() / df.shape[0]) * 100

print("Missing Data Count:\n", missing_data)
print("\nMissing Data Percentage:\n", missing_percentage)
