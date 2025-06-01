# Binning for Noise Reduction
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', for grouped analysis.
# Binning can be used for both continuous numerical variables and discrete numerical variables.
# In this section, we will use the pandas cut function for binning.

import pandas as pd
# DataFrame=["Kolhapur","Pune","Mumbai","Nagpur","Delhi"]

DataFrame=[1,2,3,4,5,6,7,8,9,10]

Data1=pd.qcut(DataFrame,q=4,labels=["Bin1","Bin2","Bin3","Bin4"])

Data2=pd.DataFrame({"Original Data":DataFrame,"Binned Data":Data1})

print(Data2)


import pandas as pd

# Sample numerical data corresponding to cities (e.g., population in millions)
DataFrame = [1,2,3,4,5]  # Numeric data for cities

# Binning the numerical data into 4 quantiles
Data1 = pd.qcut(DataFrame, q=4,labels=["Bin1","Bin2","Bin3","Bin4"])

# Creating a DataFrame with the original and binned data
Data2 = pd.DataFrame({"Original Data": ["Kolhapur", "Pune", "Mumbai", "Nagpur", "Delhi"], "Binned Data": Data1})

# Display the result
print(Data2)
