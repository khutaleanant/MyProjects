# Filtering Groups based on conditions
# User can filter groups based on certain conditions using the filter() method.

import pandas as pd

DataFram=pd.read_csv("C:\Data Science Programs Practice\Sales_Data.csv")

# Filter groups where sum of "Sales_Amount" is greater than 4000

DATA1=DataFram.groupby("Region").filter(lambda x:x["Sales_Amount"].sum()>4000)

DATA1.to_csv("Sales Greater that 4000.csv")