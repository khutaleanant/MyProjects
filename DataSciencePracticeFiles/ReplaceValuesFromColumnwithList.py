# Replace Values from specific column with a list

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame.replace([2017,"Entertainment"],[2010,"Movie"],inplace=True)

DataFrame.to_csv("DataReplace08.csv")
