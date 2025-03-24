# Fixing or correcting inconsistance numrical values

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for Gender Correction.csv")

# DataFrame["Annual Income ($)"]="$"+DataFrame["Annual Income ($)"].astype(str)

# DataFrame.to_csv("Corrected Dataset for Numbers.csv")

DataFrame["Annual Income ($)"]=DataFrame["Annual Income ($)"].replace({",":""},regex=True).astype(str)

DataFrame.to_csv("Corrected Dataset for Numbers_01.csv")

# print(DataFrame.dtypes)
