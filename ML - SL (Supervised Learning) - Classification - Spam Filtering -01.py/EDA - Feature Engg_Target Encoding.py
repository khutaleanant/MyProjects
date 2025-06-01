import pandas as pd

DataFram=pd.read_csv("C:\Data Science Programs Practice\Sales_Data.csv")

# Perform target encoding on "Product_Category" Column.
# Calculate mean of "Sales_Amount" for each "Product_Category"

DATA1=DataFram.groupby("Product_Category")["Sales_Amount"].mean()
# Map the encoding back to "Product_Category" column

DataFram["Product_Category_Encoded"]=DataFram["Product_Category"].map(DATA1)

DataFram.to_csv("Product Category Data_01.csv",index=False)

# Target Encoding >> Using target variable to encode categorical variables which can be
# usefull for high-cardinality features.

