# Remove all Rows with NULL Values in a file

import pandas as pd

DataFram=pd.read_csv("C:\Data Science Programs Practice\most_subscribed_youtube_channels.csv")
DataFram.dropna(inplace=True)#Removes any rows with missing values in the DataFrame.
# print(DataFram.to_string())


with open("DataFileRemoveNUll.txt","w",encoding="UTF-8") as file:
    file.write(DataFram.to_string())