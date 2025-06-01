# EDA - Data Quality Assessment 
import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

# Firstly Fill Empty cell in specific column with specific value

DataFrame["Dislikes"]=DataFrame["Dislikes"].fillna(10101010)

DataFrame.to_csv("Find Modified Data.csv")

Duplicate_Rows=DataFrame[DataFrame.duplicated(subset=["Likes","Dislikes"])]

Duplicate_Rows.to_csv("Find Duplicate Data_02.csv")