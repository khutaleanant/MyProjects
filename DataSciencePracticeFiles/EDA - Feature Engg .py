# EDA - Feature Engg - Creating new features
# Summing, Averaging or the fiinding the Median of the certain features can
# help reveal trends or patterns that are not immediately obvious

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Sales_Data.csv")

DATA1=DataFrame.groupby("Region")["Sales_Amount"].agg(["sum","mean","median"])

print("Multipal Aggregations For Sales_Amount by Region")
print(DATA1)

# The DataFrame.groupby() in pandas is used for gourping data in DataFrame based on one or more columns.
# It allows users to split data into groups,apply aggregation or transformation functions to
# each group and the combined the results back into DataFrame or series.
# This is a key feature of pandas for performing group-wise operations.