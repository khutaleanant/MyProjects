# If you only want ot drop rows where the specific column has missing data
## then you can pass the SUBSET arrgument

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

Data1=DataFrame.dropna(subset=["Dislikes","Category"]) # We can remove from Multipal columns

# Data1.to_csv("DROPNAFile.csv")

#You can resend the Index using the reset_index funtion

Data1.reset_index(drop=True,inplace=True)

Data1.to_csv("DropNaIndexSequesnce.csv")