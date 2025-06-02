# Fixing or correcting inconsistance numrical values

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for Gender Correction.csv")

DataFrame["Annual Income ($)"]="$"+DataFrame["Annual Income ($)"].astype(str)

# DataFrame.to_csv("Corrected Dataset for Numbers_02.csv")

# Replace the $ symbol with Rs. symoble at the beginning of the "Annual Income ($)"

DataFrame["Annual Income ($)"]=DataFrame["Annual Income ($)"].replace({r"^\$":"Rs."},regex=True)

DataFrame.to_csv("Corrected Dataset for Numbers_03.csv")
