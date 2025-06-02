import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

print(DataFrame.tail(n=15))

with open ("TailData2.txt","w",encoding="utf-8") as file:
    file.write((DataFrame.tail(n=15).to_string()))
