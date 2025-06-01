import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data for 5 salespeople
data = {
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales_Made': [10000, 15000, 20000, 12000, 8000],  # sales in dollars
}

# Create a DataFrame
df = pd.DataFrame(data)

# Commission rate
commission_rate = 0.05  # 5%

# Calculate the commission for each salesperson
df['Commission'] = df['Sales_Made'] * commission_rate

# Calculate Total Earnings by adding Sales Made and Commission
df['Total_Earning'] = df['Sales_Made'] + df['Commission']

# Round Total Earnings to 2 decimal places
df['Total_Earning'] = df['Total_Earning'].round(2)

# Display the data
print(df)

# 1. Descriptive statistics for Sales_Made, Commission, and Total_Earning
print("\nDescriptive Statistics:")
print(df[['Sales_Made', 'Commission', 'Total_Earning']].describe())

# 2. Distribution of Sales Made and Commission
plt.figure(figsize=(12, 6))

# Plot Sales_Made and Commission distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Sales_Made'], bins=10, kde=True, color='blue')
plt.title('Distribution of Sales Made')

plt.subplot(1, 2, 2)
sns.histplot(df['Commission'], bins=10, kde=True, color='green')
plt.title('Distribution of Commission')

plt.tight_layout()
plt.show()

# 3. Correlation Analysis
correlation_matrix = df[['Sales_Made', 'Commission', 'Total_Earning']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot the correlation heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 4. Sales vs Commission Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Sales_Made'], y=df['Commission'], hue=df['Salesperson'], palette='Set2', s=100)
plt.title('Sales vs Commission')
plt.xlabel('Sales Made ($)')
plt.ylabel('Commission ($)')
plt.show()

# 5. Sales-to-Commission Ratio
df['Sales_to_Commission_Ratio'] = df['Sales_Made'] / df['Commission']
print("\nSales to Commission Ratio:")
print(df[['Salesperson', 'Sales_to_Commission_Ratio']])

# 6. Top Performers by Sales and Earnings
top_sales = df.sort_values(by='Sales_Made', ascending=False).head(3)
top_earners = df.sort_values(by='Total_Earning', ascending=False).head(3)

print("\nTop 3 Performers by Sales:")
print(top_sales[['Salesperson', 'Sales_Made']])

print("\nTop 3 Performers by Total Earnings:")
print(top_earners[['Salesperson', 'Total_Earning']])
