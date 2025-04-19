#
import pandas as pd

DataFrame = pd.read_excel("C:/Data Science Programs Practice/HR Data.xlsx")

print(DataFrame.head())
print(DataFrame.tail())
print(DataFrame.columns)
print(DataFrame.dtypes)

DataFrame.to_excel("HR_DATA_WITH_STARTROW.xlsx", index=False,startrow=7)

# startrow=7:- This tells pandas to start writing the Data from row 8 (because excel's rows are 1-indexed and pandas using 0-indexed) in the excel file.
# Therefore row 7 in pandas corresponds to row 8 in excel.
# index=False:- This tells pandas not to write the index column to the excel file.