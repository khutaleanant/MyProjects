# The pd.to_datetime() function ensure the that the date values are consistent
# and correctly interpreted reardless of the format in the original CSV  file.
# The Output will be in datetime64 format,which is more useful for analysis. 

import pandas as pd

DataFrame=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",sheet_name="Complete Data")

# Standardizing date columns
# Convert date column to a uniform datetime format

# For Single column format
DataFrame["Terminated on"]=pd.to_datetime(DataFrame["Terminated on"])

# For Multipal colum forma

for col in ["Terminated on", "Hired on"]:
    DataFrame[col] = pd.to_datetime(DataFrame[col])

DataFrame.to_csv("HR DATA with NEW Date Format_02.csv")


