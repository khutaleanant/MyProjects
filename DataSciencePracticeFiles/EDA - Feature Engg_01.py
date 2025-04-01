# EDA - Feature Engg
# Count of Quantity_Sold Transactions per Region

import pandas as pd

DataFram=pd.read_csv("C:\Data Science Programs Practice\Sales_Data.csv")

DATA1 = DataFram.groupby("Region")["Quantity_Sold"].count()
# print("\nCount of Quantity_Sold by Region")

# Reset the index to make 'Region' a column again
DATA1 = DATA1.reset_index()

print(DATA1)
DATA1.to_csv("OutPut01.csv",index=False)
