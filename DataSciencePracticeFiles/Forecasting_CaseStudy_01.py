import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Dataframe=pd.read_csv("C:\Data Science Programs Practice\Company Workforce Forcasating - Empolyee Attrition.csv")

# Basic overview
print("Shape of the DataFrame:", Dataframe.shape)
print("DataTypes of the DataFrame:\n", Dataframe.dtypes)
print("Missing Values in the DataFrame:\n", Dataframe.isnull().sum())
print("Statistical Summary of the DataFrame:\n", Dataframe.describe(include='all'))

# Check missing values
plt.figure(figsize=(10, 6))
sns.heatmap(Dataframe.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Outlier detection
numrical_cols = Dataframe.select_dtypes(include="number").columns

plt.figure(figsize=(15, 10))
for i, col in enumerate(numrical_cols[:6],1):   #Show first 6 rows for clarity
    plt.subplot(3, 3, i)
    sns.boxplot(x=Dataframe[col])
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# Trend example (monthly income vs years at company)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years at Company', y='Monthly Income', data=Dataframe, hue='Job Level')
plt.title('Monthly Income vs Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Monthly Income')
plt.legend(title='Job Level')
plt.show()

# Seasonality example (Attrition vs Job Role)
plt.figure(figsize=(12, 6))
sns.countplot(x='Job Role', hue='Attrition', data=Dataframe)
plt.title('Attrition by Job Role')
plt.xticks(rotation=45)
plt.xlabel('Job Role')
plt.ylabel('Count')
plt.legend(title='Attrition', loc='upper right')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 10))
correlation_matrix = Dataframe[numrical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

# Attrition by Categorical Fetures
cat_fetures = ['Gender', 'Marital Status', 'Overtime', 'Work-Life Balance']

for col in cat_fetures:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=col, hue='Attrition', data=Dataframe)
    plt.title(f'Attrition by {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.legend(title='Attrition', loc='upper right')
    plt.show()




