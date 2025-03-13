# Eqaul width binning or range binning

import pandas as pd

DataFrame=[1,2,3,4,5,6,7,8,9]
A=pd.cut(DataFrame,bins=4,labels=["Bin1","Bin2","Bin3","Bin4"])

print(A)

 
