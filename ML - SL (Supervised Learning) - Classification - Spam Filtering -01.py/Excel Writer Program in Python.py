# Using this program, we can read the "Complete Data" sheet from an Excel file and write it to a new Excel file.
import pandas as pd

# Read the "Complete Data" sheet from the Excel file
DataFrame = pd.read_excel("C:/Data Science Programs Practice/HR Data.xlsx",sheet_name="Complete Data")

# Write the data to a new excel file
with pd.ExcelWriter("OutputFile.xlsx") as writer:
    # Write the sheet or DataFrame to the output file under the sheet name "Complete Data"
    DataFrame.to_excel(writer, sheet_name="Complete Data", index=False)

