# Drop all Rows where the all column data is empty or NA

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Fortune_1000.csv")

DataFrame.dropna(how="all",inplace=True)

DataFrame.to_csv("Drop All Empty Row4.csv",index=False)
