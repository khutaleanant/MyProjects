# To check Data Type of the perticular Column

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

print(DataFrame["published"].dtype)
print(DataFrame.dtypes)