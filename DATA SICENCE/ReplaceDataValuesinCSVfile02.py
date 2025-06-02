# Replace multipal values in specific column of a CSV file.

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame.replace({"Music":"Music Video",None:"Comedy Video"},inplace=True)

with open("DataReplace2.txt","w",encoding="utf-8") as file:
    file.write(DataFrame.to_string())
