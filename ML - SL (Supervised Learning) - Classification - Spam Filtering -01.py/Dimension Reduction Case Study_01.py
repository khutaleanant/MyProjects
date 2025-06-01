# Principal Component Analysis (PCA) - Is an unsupervised algorithm used to reduce
# dimemisnality of large dataset while preserving as much variance (information) as possible.

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

DataFrame=pd.read_csv("C:/Data Science Programs Practice/mnist_test.csv")

# Separate features and labels
X=DataFrame.drop(columns=["label"])
y=DataFrame["label"]

# Standardize the features
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

# Apply PCA to reduce to two components
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_scaled)

# Combine PCA results and labels into one DataFrame
pca_dataframe=pd.DataFrame(X_pca,columns=["PC1","PC2"])
pca_dataframe["label"]=y

# Save PCA result in CSV file
pca_dataframe.to_csv("C:/Data Science Programs Practice/Mnist_PCA_Output.csv",index=False)
print("PCA output saved to 'Mnist_PCA_Output.csv'")

# Visualize PCA result
plt.figure(figsize=(10,10))
scatter=plt.scatter(pca_dataframe["PC1"],pca_dataframe["PC2"],c=pca_dataframe["label"])
plt.colorbar(scatter,label="Digital Label")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization Of MNIST Test Set")
plt.grid(True)
plt.show()
