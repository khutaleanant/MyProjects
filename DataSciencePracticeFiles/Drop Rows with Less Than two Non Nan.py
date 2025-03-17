import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Fortune_1000.csv")

DataFrame=DataFrame.dropna(thresh=2) # You can increase or decrease numbers

with open("DropRows With Less Than Two Non Nan.txt","w",encoding="utf-8") as file:
    file.write(DataFrame.to_string())

DataFrame.to_csv("DropRows With Less Than Two Non Nan.csv") 