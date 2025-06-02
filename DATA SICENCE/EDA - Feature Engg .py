# EDA - Feature Engg - Creating new features
# Summing, Averaging or the fiinding the Median of the certain features can
# help reveal trends or patterns that are not immediately obvious

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Sales_Data.csv")

DATA1=DataFrame.groupby("Region")["Sales_Amount"].agg(["sum","mean","median","count","min","max","quantile","first","last","std"])

print("Multipal Aggregations For Sales_Amount by Region")
print(DATA1)

DATA1.to_csv("Multipal Aggregations For Sales_Amount by Region.csv")

# Plotting the Bar Chart for Total Sales by Region
plt.figure(figsize=(10, 6))
sns.barplot(x=DATA1.index, y=DATA1["sum"], palette="viridis")
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting the Pie Chart for Sales Distribution by Region
plt.figure(figsize=(8, 8))
sales_sum = DATA1["sum"]
plt.pie(sales_sum, labels=sales_sum.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3", len(sales_sum)))
plt.title('Sales Distribution by Region')
plt.show()

# The DataFrame.groupby() in pandas is used for gourping data in DataFrame based on one or more columns.
# It allows users to split data into groups,apply aggregation or transformation functions to
# each group and the combined the results back into DataFrame or series.
# This is a key feature of pandas for performing group-wise operations.