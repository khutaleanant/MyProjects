# Replace Multipal values in the specific column

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

# Replace Multipal values in the specific column
DataFrame["Category"]=DataFrame["Category"].replace({"Film & Animation":"Film","Music":"Music & Dance"})
                ## OR ##
# DataFrame["Category"].replace({"Film & Animation":"Film","Music":"Music & Dance"},inplace=True)

DataFrame.to_csv("DataReplace7.csv")