# Replace values using the column name

import pandas as pd


DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame["Category"]=DataFrame["Category"].replace("Music",5555)

DataFrame.to_csv("DataReplace4.csv")

