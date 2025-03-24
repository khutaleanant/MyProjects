# Label Encoding converts each unique catogory in cloumn into corresponding numrical Label.

import pandas as pd

from sklearn.preprocessing import LabelEncoder

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for Gender Correction.csv")

DATA1=LabelEncoder()

DataFrame["Gender_Encoded"]=DATA1.fit_transform(DataFrame["Gender"])

DataFrame.to_csv("Label Encoding.csv")