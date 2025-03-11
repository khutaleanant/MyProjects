import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data (customer spending and purchases)
data = {
    'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Total Spend ($)': [100, 150, 200, 300, 50, 400, 250, 60, 120, 90],
    'Number of Purchases': [10, 15, 20, 30, 5, 50, 25, 7, 12, 8],
    'Product Categories Purchased': [3, 4, 5, 6, 2, 7, 5, 3, 4, 2],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Select relevant numerical features for clustering
X = df[['Total Spend ($)', 'Number of Purchases', 'Product Categories Purchased']]

# Apply K-Means clustering (let's assume we want 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Visualizing the clustering result
plt.figure(figsize=(8, 6))
plt.scatter(df['Total Spend ($)'], df['Number of Purchases'], c=df['Cluster'], cmap='viridis', s=100)

# Marking cluster centers (centroids)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=300, c='red', marker='X', label='Centroids')

# Title and labels
plt.title('Customer Segments Based on Purchase Behavior')
plt.xlabel('Total Spend ($)')
plt.ylabel('Number of Purchases')
plt.legend()

# Display plot
plt.show()
