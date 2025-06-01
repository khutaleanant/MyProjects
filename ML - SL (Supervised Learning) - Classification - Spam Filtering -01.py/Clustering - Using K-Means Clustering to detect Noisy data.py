# Clustering - Using K-Means Clustering to detect Noisy data

from sklearn.cluster import KMeans

import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1,2],[1,3],[2,3],[8,7],[8,8],[25,80],[30,45],[15,20]])

y=KMeans(n_clusters=2)

y.fit(x)

labels=y.labels_
centroids=y.cluster_centers_

# Calculate distance from each point to it's cluster's centroid

distances=np.linalg.norm(x-centroids[labels],axis=1)

# Define a threshhold to identify outliers

threshold=np.percentile(distances,75)   #Upper 25% of distances are considered outliars

# identify noisy points

Data1=x[distances>threshold]

#visualised cluster and noisy points

plt.scatter(x[:,0],x[:,1],c=labels,cmap="rainbow")
plt.scatter(Data1[:,0],Data1[:,1],color="red",label="Noisy Points")
plt.legend()
plt.title("K-Means Clustering - Noisy Points in Red")
plt.show()

# print Noisy points

print("Noisy Points detected by K-Means")
print(Data1)
