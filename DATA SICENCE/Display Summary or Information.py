# Display Summary or Information
# .info () method is used to get a concise summary of the DataFrame. It comes really handy when doing exploratory analysis of the data.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")

print(DataFrame.info())

# Output:

with open("Datafileinfo.txt", "w") as file:
    file.write(str(DataFrame.info()))
