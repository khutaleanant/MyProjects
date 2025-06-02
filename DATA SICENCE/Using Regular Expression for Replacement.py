# Using Regular Expression for Replacement 

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame.replace(to_replace=r"2,393",value="5555",regex=True,inplace=True)

#print(DataFrame["Dislikes"].dtype)

DataFrame.to_csv("DataReplace10.csv")



