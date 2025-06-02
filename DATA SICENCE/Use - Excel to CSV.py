import pandas as pd


# DataFrame=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",sheet_name="Complete Data")
# DataFrame2=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",sheet_name=1)
DataFrame=pd.read_excel("C:\Data Science Programs Practice\HR Data.xlsx",sheet_name=None)

# DataFrame.to_csv("Excel to CSV_06.csv")

with open("DATA FROM EXCEL.txt","w",encoding="utf-8") as file:
    file.write(DataFrame.to_string())
