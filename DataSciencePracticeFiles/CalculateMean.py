## Calculate Mean of the data
import pandas as pd

Dataframe=pd.read_csv("C:\Data Science Programs Practice\most_subscribed_youtube_channels_01.csv")
X=Dataframe["video count"].mean()
Dataframe["video count"].fillna(X,inplace=True)
print(X)
# print(Dataframe.to_string())
with open("DataFileMean.txt","w",encoding="UTF-8") as file:
    file.write(Dataframe.to_string())

    