# dropna(axis=0,how="any") -- Drop rows with any missing values

import pandas as pd

DataFrame1=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")
DataFrame1.dropna(axis=0,how="any",inplace=True)
DataFrame1.to_csv("Drop Rows which NA.csv")

# dropna(axis=1,how="any") -- Drop column with any missing values # don't use the inplace=True

DataFrame2=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")
DATA=DataFrame2.dropna(axis=1,how="any")
DATA.to_csv("Drop Columns which NA.csv")