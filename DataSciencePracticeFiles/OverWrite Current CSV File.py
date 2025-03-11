# Overwrite existing CSV file with new data or Modified version of the existing data

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

DataFrame.fillna(value={"Category":"Blank Cell"},inplace=True)

DataFrame.to_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

print("Data Overwritten Successfully")