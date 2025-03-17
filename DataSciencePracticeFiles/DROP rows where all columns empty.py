# Drop all Rows where the all column data is empty or NA

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame.dropna(axis= 0,how="all",inplace=True)

DataFrame.to_csv("Drop All Empty Row.csv")

