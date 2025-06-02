# Standerdizing catogerical data
# Replace lower case value to upper case and upper case vale in to the Lower case in perticular coulmns in CSV file.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for Gender Correction.csv")

#UpperCase
DataFrame["Profession"]=DataFrame["Profession"].str.upper()
DataFrame.to_csv("Corrected dataset_UpperCase.csv")

# LowerCase
DataFrame["Profession"]=DataFrame["Profession"].str.lower()
DataFrame.to_csv("Corrected dataset_LowerCase.csv")

