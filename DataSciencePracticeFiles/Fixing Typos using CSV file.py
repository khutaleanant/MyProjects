# Fixing Typo Error in CSV file using the Pandas

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for Gender Correction.csv")

DataFrame["Gender"]=DataFrame["Gender"].replace({"MalE":"MALE","M":"MALE","MAle":"MALE","MALE":"MALE","Male":"MALE","Female":"FEMALE","F":"FEMALE","Feml":"FEMALE","FEMALE":"FEMALE"})


DataFrame.to_excel("Corrrected Dataset for Gender_02.xlsx",index=False)

