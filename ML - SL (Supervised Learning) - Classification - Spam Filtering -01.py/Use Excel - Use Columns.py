# the usecols parameter in pandas read_excel(allow user to select specific columns to read from an excel file insted of loading entire dataset)

import pandas as pd

# using column names
# DataFrame=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",usecols=["Country","Ethnicity"])

# using column indices(0-based)
DataFrame=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",usecols=[0,2,3])

DataFrame.to_excel("Excel to CSV 03.xlsx")
