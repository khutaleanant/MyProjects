# Exploratory Data Analysis (EDA) Practice - Range Calculation for the perticular column

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for EDA - RANGE.csv")

print(DataFrame.head())
print(DataFrame.dtypes)

AGE_Range="Age"
Work_Exp_Range="Work Experience"

DATA1=DataFrame["Age"].max()-DataFrame["Age"].min()
DATA2=DataFrame["Work Experience"].max()-DataFrame["Work Experience"].min()

print(f"The range of the column {AGE_Range} is {DATA1}")
print(f"The range of the column {Work_Exp_Range} is {DATA2}")


