# Equal Frequency Binning

import pandas as pd

DataFrame = [1,2,3,4,5,6,7,8,9,10]

Obj1=pd.qcut(DataFrame,q=4,labels=["Bin1", "Bin2", "Bin3", "Bin4"])

print(Obj1)