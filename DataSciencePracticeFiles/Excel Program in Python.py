# Update the excel file with the missing data representation.
import pandas as pd

DataFrame = pd.read_excel("C:/Data Science Programs Practice/HR Data.xlsx",sheet_name="Terminated")

DataFrame.to_excel("HR_DATA_WITH_NA_REPRESENTATION.xlsx",index=False,na_rep="MISSING DATA")

