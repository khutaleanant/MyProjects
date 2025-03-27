# EDA - Indentify and Handle Outliers (Boxplot and IQR) are common methods for detecting Outliers in Numerical Data.
# Outliers = are data points that deviate significatly from the rest of the
# data in the dataset. This values are unusually high or low compared to the other
# observations and can often distort statistical analyses such as MEAN,STD DEV, and REGG analysis.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

# Plot Boxplot to identify outliers in numeric column

sns.boxplot(x=DataFrame["Salary"])
plt.show()

# Identifying Outliers using IQR

Q1=DataFrame["Salary"].quantile(0.25)
Q3=DataFrame["Salary"].quantile(0.75)

IQR=Q3-Q1

Lower_Bound=Q1-1.5*IQR
Upper_Bound=Q3+1.5*IQR

# filter out the Outliers

DataFrame_Outliers_Removed=DataFrame[(DataFrame["Salary"]>=Lower_Bound)&(DataFrame["Salary"]<=Upper_Bound)]

# Print details about Outliers

Outliers=DataFrame[(DataFrame["Salary"]<Lower_Bound)|(DataFrame["Salary"]>Upper_Bound)]

print(f"Number of Outliers ={Outliers.shape[0]}")
print(f"Outliers Removed ={DataFrame.shape[0]-DataFrame_Outliers_Removed.shape[0]}")
print(f"Original Dataset Size ={DataFrame.shape[0]} Rows")
print(f"Dataset Size After Removing Outliers ={DataFrame_Outliers_Removed.shape[0]} Rows")

# Optionally show the Outliers data if needed

print(Outliers)