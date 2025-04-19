# Using the folliwng code, we can create an Excel file with a custom index label and handle missing values.
import pandas as pd

DataFrame=pd.read_excel("C:/Data Science Programs Practice/HR Data.xlsx") # by defualt it reads the first sheet only if you are not specifying the sheet name.
DataFrame.to_excel("HR_DATA_WITH_Index_Label.xlsx",index=True,index_label="ROW ID",na_rep="N/A")
