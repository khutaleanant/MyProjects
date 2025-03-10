import pandas as pd

Dataframe=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

DuplicateResult=Dataframe.duplicated()
print(DuplicateResult.to_csv("C:\Data Science Programs Practice\DuplicateResult2.csv"))

print(DuplicateResult.to_string())