from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# matplotlib.use("Agg")

x=np.array([[1,2],[1,3],[2,3],[8,7],[8,8],[25,80],[30,45],[15,20]])

# Apply Agglomerative Clustering

DataFrame=AgglomerativeClustering(n_clusters=2)
# The Agglomerative clustering algorithem is innitialized with the parameter n_cluster=2
# This means that we want algorithem to find to clusters in the data
# Agglomerative clustering is bottom - as approch to clustering
    # 1) Start with each data point as its own cluster
    # 2) Iteratively merggerd two closest cluster untile the desired number of clusters is reached.

labels=DataFrame.fit_predict(x)
# This method fits the model to the data x and returns the cluster labels for each data points
# The result labels is an array of the cluster assigment of each points
# The array contains the cluster assigments (example 0 or 1) where each number represent the cluster that the point belongs to.


# Visualize the Clusters

plt.scatter(x[:,0],x[:,1],c=labels,cmap="viridis")
# x[:,0] and x[:,1] extract the first and second columns of x (x and y coordinates of the dat points.)
# c=labels paramettes assign the color to each data points based on the cluster label
# cmap="viridis" sprcifies the color maps to be used for the cloring the custer.
plt.title("Agglomerative Cluster")
plt.show()

plt.savefig("Agglomerative Clustering.jpg")


