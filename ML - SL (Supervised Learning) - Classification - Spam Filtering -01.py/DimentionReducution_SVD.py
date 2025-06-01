# Singular Value Decomposition (SVD) is a matrix factorization method used to reduce
# the number of features (Dimensions) in a dataset while retaining most of the
# important information(Variance). It is especially useful when the data has 
# high dimensionality and you want to compress or simplify it.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

#Load Dataset
data=load_breast_cancer()
X=data.data
y=data.target
target_names=data.target_names

# Standardize the features
scaler=StandardScaler()
X_scaled= scaler.fit_transform(X)

# Compute SVD
U,S,VT=np.linalg.svd(X_scaled,full_matrices=False)

# Project the data onto the first two singular vectors
X_reduced =np.dot(U[:, :2],np.diag(S[:2]))

# Plot the first two components
plt.figure(figsize=(12,12))
colors=["navy","darkorange"]
for i,target_name in enumerate(target_names):
    plt.scatter(X_reduced[y==i,0],X_reduced[y==i,1],alpha=0.7,color=colors[i],label=target_name)
plt.title("SVD of Breast Cancer Dataset (Top Two Components)")
plt.xlabel("First Singular Vector")
plt.ylabel("Second Singular Vector")
plt.legend()
plt.grid(True)
plt.show()

# Save to CSV file
output_df=pd.DataFrame(X_reduced,columns=["SVD1","SVD2"])
output_df["Target"]=y
output_df["TargetName"]=[target_names[label] for label in y]
output_df.to_csv("Breast_Cancer_SVD_output.csv",index=False)
