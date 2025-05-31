# Linear Discriminant Analysis (LDA) is a supervised dimensionality reduction
# technique used in data science. Unlike PCA or SVD (Which are unsupervised),
# LDA uses class labels to reduce dimensions while maximizing class separability.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Load Dataset
data=load_iris()
X=data.data
y=data.target
target_names=data.target_names

# Standardize the Features
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

# Apply LDA 
lda=LDA(n_components=2) #Reduce to 2 dimensions for visualization
X_lda=lda.fit_transform(X_scaled,y)

# Plot the LDA result
plt.figure(figsize=(10,10))
colors=["red","green","blue"]
for i,target_name in enumerate(target_names):
    plt.scatter(X_lda[y==i,0],X_lda[y==i,1],alpha=0.7,color=colors[i],label=target_name)
plt.title("LDA of iris dataset (Two Components)")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.legend()
plt.grid(True)
plt.show()

# Save LDA results to CSV file
output_df=pd.DataFrame(X_lda,columns=["LD1","LD2"])
output_df["Target"]=y
output_df["TargetName"]=[target_names[label] for label in y]
output_df.to_csv("Iris_LDA_Output.csv",index=False)


