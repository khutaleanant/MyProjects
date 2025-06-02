# One Hot Encoding is used for nominal catogorical veriables where there is no inherent order
# It create new binnary column for each catogoery and assign 1 or 0 to indicate the presence or absence of that category in the row

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

DataFrame_Encoding=pd.get_dummies(DataFrame["Category"],prefix="Category")

# Concatenate the encoded columns back to the origianl dataframe
DataFrame=pd.concat([DataFrame,DataFrame_Encoding],axis=1)

DataFrame.to_csv("One-Hot Encoding.csv")
