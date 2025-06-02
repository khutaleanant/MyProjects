# EDA - Data Quality Assessment
# Sometimes user might only want to check for the duplicates in certain column rather than the entire row.


import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

DupliCate_Rows=DataFrame[DataFrame.duplicated(subset=["Likes"])]

DupliCate_Rows.to_csv("Find Duplicates Data_01.csv")
