# Using DBSCAN to detect and remove noisy data

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Mall_Customers.csv")

print(DataFrame.head())

Data1=DataFrame[["Age","Annual Income (k$)","Spending Score (1-100)"]]

print(Data1.head())

Data1=Data1.fillna(Data1.mean())

# Standarize the fetures

X = StandardScaler()
Y = X.fit_transform(Data1)

# Apply DBSCAN clustering

Z = DBSCAN(eps=0.5,min_samples=4)
Z_labels = Z.fit_predict(Y)

# Add DBSCAN labels to the original dataset

DataFrame["DBSCAN_Cluster"]=Z_labels

# Count how many points are labeled as noise (-1 indicate noise)

NoisyPoints=np.sum(Z_labels==-1)

print (f"Number of Noisy Points Detected by DBSCAN ={NoisyPoints}")

# plot the clusters

plt.figure(figsize=(8,6))
plt.scatter(Y[:,0],Y[:,1],c=Z_labels,cmap="viridis",marker="o")
plt.title("DBSCAN Clustering of Mall Customers")
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
plt.colorbar(label="Cluster Label")
plt.show()

# calculate the silhouette score (only if there are at list two clusters)
if len(np.unique(Z_labels))>1:
    #DBSCAN can sometimes result in a single cluster or noise
    SCORE=silhouette_score(Y,Z_labels)
    print(f"Silhouette Score : {SCORE}")
else:
    print("DBSCAN found only one Cluster or only one Noise.")

# Group By DBSCAN Cluster Lables and examin the Cluster centers

Group=DataFrame.groupby("DBSCAN_Cluster").agg({"Age":["mean","std"],"Spending Score (1-100)":["mean","std"]})

print(Group)

Group.to_csv("Clustering of mall customers dataset.csv")


