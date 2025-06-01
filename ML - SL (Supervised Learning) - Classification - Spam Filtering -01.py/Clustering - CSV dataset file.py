# Clustering create on the Dataset CSV file

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# Load the CSV file into a pandas DataFrame
Dataframe=pd.read_csv("C:\Data Science Programs Practice\Cities DataSet for Clustering.csv")

# Check the first few rows of the dataset
# print(Dataframe.head())

# If necessary, handle missing values (this depends on your dataset)
df = Dataframe.dropna()  # Remove rows with missing values, or you can fill them using df.fillna()

# Drop the categorical column 'CITY' for clustering
df_numeric = Dataframe.drop(columns=['CITY'])

# Preprocess the data (normalize/standardize the numerical features)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

# Preprocess the data (normalize/standardize the numerical features)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

# Apply DBSCAN clustering
# The parameters are 'eps' (maximum distance between two samples to be considered neighbors)
# and 'min_samples' (minimum number of samples in a neighborhood for a point to be considered as a core point)
dbscan = DBSCAN(eps=0.5, min_samples=2)  # Adjust eps and min_samples as needed

# Fit the DBSCAN model
dbscan.fit(X_scaled)

# Add the cluster labels to the original dataframe
df['Cluster'] = dbscan.labels_

# Display the table with the cluster labels along with the original data
print(df)

# Optionally, save the results to a new CSV with cluster labels
df.to_csv('dbscan_clustered_data.csv', index=False)