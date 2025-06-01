# Writing the multiple sheets starting from the specified rows.

from itertools import tee
import pandas as pd
sheets=pd.read_excel("C:/Data Science Programs Practice/HR Data.xlsx",sheet_name=None)

# Write a new excel file with different start rows for each sheet.

with pd.ExcelWriter("HR_DATA_MULTIPLE_SHEET.xlsx") as writer:
    # Write the first sheet starting from row 5(Excel row 6)
    sheets["Terminated"].to_excel(writer,sheet_name="Terminated",index=False,startrow=5)

    # Write the second sheet starting from row 3(Excel row 4)
    sheets["Active"].to_excel(writer,sheet_name="Active",index=False,startrow=3)
