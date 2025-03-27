# EDA - Data Quality Assessment (DQA)- Check for the Missing Data

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

# Check for the missing values

MD=DataFrame.isnull().sum()

# Percentage of the missing data

MP=(MD/len(DataFrame))*100
MP = MP.apply(lambda x: "{:.2f} %".format(x)) # for % simbol

# Display missing data

print("Missing Data =",MD)
print("Missing Data Percentage =",MP)