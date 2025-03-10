import pandas as pd

Dataframe=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")
# Dataframe.drop("published",axis=1,inplace=True)
Dataframe.drop(["published","Video views"],axis=1,inplace=True)

print(Dataframe.columns)
# print(Dataframe.to_string())

with open("ColumnRemove.txt","w",encoding="UTF-8") as file:
    file.write(Dataframe.to_string())