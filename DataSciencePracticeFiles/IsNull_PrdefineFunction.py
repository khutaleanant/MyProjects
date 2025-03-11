# IsNull predefine function in pandas

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

# Data=DataFrame.isnull()

# Data.to_csv("IsNull.csv",index=False)

Data2=DataFrame.isnull().sum()

Data2.to_csv("IsNull2.csv",index=False)


