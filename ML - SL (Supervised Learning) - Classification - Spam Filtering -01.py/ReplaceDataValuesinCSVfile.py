# Replace a single value in specific column of a CSV file.

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

# Replacing the value in the specific column

# DataFrame.replace(np.nan,"Blank Cell",regex=True,inplace=True)

DataFrame.replace({None: "Blank Cell", "Blank Cell": "Balnk Cell"}, inplace=True)

DataFrame.to_csv("DataReplace15.csv")