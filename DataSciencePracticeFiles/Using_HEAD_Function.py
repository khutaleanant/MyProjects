# HEAD functionally use
import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\most_subscribed_youtube_channels.csv")
DataFrame=DataFrame.dropna()
print(DataFrame.head(n=9)) # Default value of n is 5


