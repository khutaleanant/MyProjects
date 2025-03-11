# Display Described Information

import pandas as pd

DataFrame = pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

# print(DataFrame.describe())

with open ("DisplayDiscribedInfo.txt","w",encoding="utf=8") as file:
            file.write(DataFrame.describe().to_string())
