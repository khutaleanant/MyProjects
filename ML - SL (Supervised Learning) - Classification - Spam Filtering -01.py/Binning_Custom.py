# Custom binning function

import pandas as pd

DataFrame=[10,20,30,40,50,60,70,80,90,100]

bins=[20,30,40,50,60]

labels=["Low","Mid","High","Very High"]

BinData=pd.cut(DataFrame,bins=bins,labels=labels)

print(BinData)