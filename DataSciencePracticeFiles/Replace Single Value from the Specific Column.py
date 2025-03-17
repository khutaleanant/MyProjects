# Replace single value or Insert new value in all dataset where the cells are empty or contain missing values

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

DataFrame.replace([None],"Balnk Cells",inplace=True)

DataFrame.to_csv("DataReplace17.csv")