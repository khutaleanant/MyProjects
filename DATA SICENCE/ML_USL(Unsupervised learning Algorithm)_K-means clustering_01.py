# K-Means clustering is an unsupervised machine learning algorithm used to 
# partition a dataset into K distinct, non-overlapping clusters based on feature similarity.
# The algorithm assigns each data point to the cluster with the nearest centroid (mean) 
# and iteratively updates the centroids to minimize the within-cluster variance (inertia).

# K: The number of clusters to form.
# Centroid: The center of a cluster.
# Inertia: The sum of squared distances between each point and its assigned cluster center.

# How K-Means Works (Step-by-Step):
# 1. Choose the number of clusters 𝐾
# 2. Randomly initialize 𝐾 centroids.
# 3. Assign each data point to the nearest centroid.
# 4. Compute new centroids as the mean of the points in each cluster.
# 5. Repeat steps 3 and 4 until centroids no longer change significantly or 
#    a maximum number of iterations is reached.

# -------------------------------------------------------
# K-Means Clustering on Country Data with Visualization
# -------------------------------------------------------
# Purpose: To group countries based on socio-economic features using K-Means clustering.
# Steps:
#   1. Load and clean the dataset
#   2. Scale the features for uniformity
#   3. Use Elbow method to determine optimal K
#   4. Apply KMeans clustering
#   5. Visualize clusters in 2D using PCA
#   6. Save results to CSV for analysis
# -------------------------------------------------------

# -------------------- Import Required Libraries --------------------
import pandas as pd                      # For data manipulation
import matplotlib.pyplot as plt          # For static plots
import seaborn as sns                    # For stylish visualizations
from sklearn.cluster import KMeans       # K-Means Clustering algorithm
from sklearn.preprocessing import StandardScaler  # Feature Scaling
from sklearn.decomposition import PCA    # For dimensionality reduction

# -------------------- Load Dataset --------------------
# CSV file contains country-wise socio-economic indicators
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\Country-Data.csv")

# Display the first 5 rows to understand the structure
print("Initial data preview:")
print(DataFrame.head())

# -------------------- Preprocessing --------------------
# Store country names for later use in labeling the final output
countries = DataFrame["country"]

# Drop the 'country' column to use only numerical features for clustering
X = DataFrame.drop(columns=["country"])

# -------------------- Feature Scaling --------------------
# Why: Different features have different units. K-Means uses distance.
# Scaling helps bring all features to same scale (mean=0, std=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------- Elbow Method --------------------
# Purpose: Find the optimal number of clusters (K)
inertia = []  # Stores inertia values for different K
K_range = range(1, 11)  # Try K from 1 to 10

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)  # Inertia: Sum of squared distances to centroids

# Plotting Elbow Curve to visually identify the best K
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, "bo-")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (Within-cluster sum of squares)")
plt.title("Elbow Method - Optimal K")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------- Apply KMeans with Optimal K --------------------
# Set number of clusters based on elbow plot (you can change this)
optimal_k = 3

# Run KMeans clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to original DataFrame
DataFrame['Cluster'] = cluster_labels

# View updated data with assigned cluster
print("\nDataFrame with assigned cluster labels:")
print(DataFrame[['country', 'Cluster']].head())

# -------------------- PCA for 2D Visualization --------------------
# PCA = Principal Component Analysis
# Goal: Reduce 10D features to 2D for plotting
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Add the 2D coordinates to the DataFrame
DataFrame["PCA1"] = X_pca[:, 0]
DataFrame["PCA2"] = X_pca[:, 1]

# -------------------- Visualize Clusters with Country Labels --------------------
plt.figure(figsize=(14, 10))

# Scatter plot with different colors for each cluster
sns.scatterplot(
    data=DataFrame,
    x="PCA1", y="PCA2",
    hue="Cluster",             # Cluster number as hue
    palette="Set1",            # Color set
    s=100,                     # Point size
    alpha=0.9,                 # Transparency
    edgecolor='black'         # Border around points
)

# Add country names on the plot near each point
for i in range(DataFrame.shape[0]):
    plt.text(
        DataFrame['PCA1'][i] + 0.1,
        DataFrame['PCA2'][i] + 0.1,
        DataFrame['country'][i],
        fontsize=9,
        alpha=0.75
    )

# Plot cluster centers (converted to PCA space)
centroids_pca = pca.transform(kmeans.cluster_centers_)
sns.scatterplot(
    x=centroids_pca[:, 0],
    y=centroids_pca[:, 1],
    color='black',
    s=300,
    label='Centroids',
    marker='X'
)

# Final formatting of plot
plt.title("K-Means Clustering of Countries (PCA 2D Projection)", fontsize=16)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------- View Countries in Each Cluster --------------------
# Print out the list of countries in each cluster
for i in range(optimal_k):
    print(f"\nCountries in Cluster {i}:")
    print(DataFrame[DataFrame["Cluster"] == i]["country"].values)

# -------------------- Save Results --------------------
# Save the final DataFrame with cluster and PCA info for further analysis
DataFrame.to_csv("C:\\Data Science Programs Practice\\Clustered_Country_Data.csv", index=False)
print("\nClustered data saved to 'Clustered_Country_Data.csv'")