# Using K-Mean clustering to detect noisy data

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Mall_Customers.csv")

print(DataFrame.head())

# Selecting relavent columns for Clustering

Data1=DataFrame[["Age","Annual Income (k$)","Spending Score (1-100)"]]

# Normalise the data for better clusterring

SCELAR=StandardScaler()
Data_SCALED=SCELAR.fit_transform(Data1)

# Elbow method to find the optimal numbers of clusters
wcss=[]
for i in range (1,11):
    KMEANS=KMeans(n_clusters=i,init="k-means++",max_iter=300,n_init=10,random_state=42)
    KMEANS.fit(Data_SCALED)
    wcss.append(KMEANS.inertia_)

# ploting the elbow method graph

plt.figure(figsize=(10,6))
plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("Number Of Cluster")
plt.ylabel("WCSS")
plt.show()

# apply KMeans with optimal number of clusters

DATA2=KMeans(n_clusters=5,init="k-means++",max_iter=300,n_init=100,random_state=42)

# adding cluster cloumn to the original data

DataFrame["Cluster"]=DATA2.fit_predict(Data_SCALED)

# Visualizing the clusters

plt.figure(figsize=(10,6))
plt.scatter(DataFrame["Age"],DataFrame["Annual Income (k$)"],c=DataFrame["Cluster"],cmap="viridis")
plt.title(" Clustering of Mall Customers")
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
plt.colorbar()
plt.show()

