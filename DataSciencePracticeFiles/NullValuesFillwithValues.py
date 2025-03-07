import pandas as pd

Dataframe=pd.read_csv(("C:\Data Science Programs Practice\most_subscribed_youtube_channels.csv"))
Dataframe.fillna("Error",inplace=True) #replace NaN values with 'Error'

# print(Dataframe.to_string(max_rows=10))
with open("CLeanedData.txt",'w',encoding="UTF-8") as file:
    file.write(Dataframe.to_string())
    file.close()