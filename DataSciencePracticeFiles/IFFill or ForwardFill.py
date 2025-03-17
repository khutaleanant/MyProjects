import pandas as pd

DataFrame1=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")
DataFrame2=pd.read_csv("C:\Data Science Programs Practice\Most popular 1000 Youtube videos.csv")


DataFrame1["Dislikes"]=DataFrame1["Dislikes"].ffill()
DataFrame2["Dislikes"]=DataFrame2["Dislikes"].bfill()

DataFrame1.to_csv("Fill_Ffill01.csv")
DataFrame2.to_csv("Fill_Bfill02.csv")