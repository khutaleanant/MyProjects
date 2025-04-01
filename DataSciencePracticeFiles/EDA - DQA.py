# Data Quality Assessments
# keep="first" >>> keeps the first occurrence of each unique combination of values in column1 and column2.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\First Occurrence.csv")

DataFrame_Cleaned=DataFrame.drop_duplicates(subset=["Likes","Dislikes"],keep="first")

DataFrame_Cleaned.to_csv("Clean DataFrame_01.csv",index=False)