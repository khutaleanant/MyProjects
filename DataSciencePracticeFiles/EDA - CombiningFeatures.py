# For a dataset with Height and Weight columns, a new feature (column) such as BMI can be created.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\SOCR-HeightWeight.csv")

# BMI (Body Mass Index) = Weight/(Height^2)

DataFrame["BMI"]=DataFrame["Weight(Pounds)"]/DataFrame["Height(Inches)"]**2

DataFrame.to_csv("DataSet With BMI Column.csv")
