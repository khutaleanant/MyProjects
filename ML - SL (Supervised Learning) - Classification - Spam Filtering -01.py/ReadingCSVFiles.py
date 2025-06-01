# Reading CSV Files where data is uncleaned or empty cells are present.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\most_subscribed_youtube_channels.csv")
# DataFrame=DataFrame.dropna() # Drop Rows with Empty Cells

# print(DataFrame.to_string())

# # Max Rows (Showing Fisrt Five Rows and last Five Rows)
# print(DataFrame.to_string(max_rows=10))

# # Max Cols (Showing Fisrt Three Columns and last two Columns)

# print(DataFrame.to_string(max_cols=5))

# Max columns

# print(DataFrame.to_string(columns=DataFrame.columns[:5]))

## Header parameter

# print(DataFrame.to_string(max_rows=10,max_cols=5,header=False))

## Index parameter

# print(DataFrame.to_string(max_rows=10,max_cols=5,index=False)

## Line Width

# print(DataFrame.to_string(max_rows=10,max_cols=5,line_width=50))


# with open("data.txt","w",encoding="UTF-8") as file:
#     file.write(DataFrame.to_string())



