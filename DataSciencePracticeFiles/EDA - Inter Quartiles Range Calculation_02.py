# EDA - Inter Quartiles Range Calculation

import pandas as pd


DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for EDA - RANGE.csv")

Q1=DataFrame["Work Experience"].quantile(0.25)
Q3=DataFrame["Work Experience"].quantile(0.75)

#Q1 (First Quartile): The median of the lower half of the data (25th percentile).
#Q3 (Third Quartile): The median of the upper half of the data (75th percentile).

IQR2=Q3-Q1

print(IQR2)

##===============================================##
# Calucluate with diffrent way.
# import numpy as np
# from scipy import stats

# Dataset=[10,25,24,30,40,25,67,27]

# IQR=stats.iqr(Dataset)

# print(IQR)