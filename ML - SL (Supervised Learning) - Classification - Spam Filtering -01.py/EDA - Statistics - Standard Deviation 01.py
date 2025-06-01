# EDA Practice - Statistics - Standard Deviation

import numpy as np

# # Data
# DATASET = [4,11,7,14]

# SDValue=np.std(DATASET)

# print(SDValue)

####----- Using CSV File

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for EDA - RANGE.csv")

STD_DEV=DataFrame["Family Size"].std()

print(STD_DEV)

