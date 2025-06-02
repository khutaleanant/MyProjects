# Using DBSCAN to detect and remove noisy data

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

x=np.array([[1,2],[1,3],[2,3],[8,7],[8,8],[25,80]])

# apply the DBSCAN

Data1= DBSCAN(eps=3,min_samples=2)
# eps is the maximam distance between points and min_samples is the min number of points
# in a cluster.

labels=Data1.fit_predict(x) 
# Apply the DBSCAN alogrithm to the x and assign the each data point o the cluster labels.
# the result is stored in th labels which is an array of cluster assigments for each data point.
# Points that belong to cluster will get non negative label (0,1,3,3 etc...)
# Points consider as Noise (outliers) will be assign a label of -1
#

df = pd.DataFrame(x, columns=['X', 'Y'])
df['Cluster']=labels

# Visualizing the Cluster in table form
print(df)

# Visualizing the Cluster in Chart 
plt.scatter(x[:,0],x[:,1],c=labels,cmap="rainbow")

#Extract the X and Y coordinate of the points
# c=Labels parameters the colors the points based on there assign cluster labes and
# cmap="rainbow" specify the colore map for the different clustes
# Noise points (lable=-1) will be show in unique color indicatinf that they don't belong to any cluster.

# plt.title("DBSCAN Clustering-Noise Points Marked as -1")
# plt.show()

# Handling Noisy points (lables=-1 is noise)

Data2 = x[labels==-1]
print("Noise points by DBSCAN")
print(Data2)

plt.savefig("DBSCAN CLUSTERING.jpg")

