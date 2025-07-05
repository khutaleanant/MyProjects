
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.decomposition import PCA
import seaborn as sns

# Load the dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\BankNoteAuthentication.csv")

# Inspect the first few rows of the dataset
print(DataFrame.head())

# Data Visualization
# 1) Pairplot to visualize feature relationships colored by the class
sns.pairplot(DataFrame,hue="class",diag_kind="kde",markers=["o","s"])
plt.suptitle("Pairplot of Features colored by Class", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(DataFrame.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# ---Prepare the data---
X = DataFrame[["variance", "skewness", "curtosis", "entropy"]]
y = DataFrame["class"]

# Split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---Train the SVM model---
svm=SVC(kernel="rbf",random_state=42)
svm.fit(X_train_scaled,y_train)

# ---Make predictions---
y_pred = svm.predict(X_test_scaled)

# ---Evaluate the model---
print("Accuracy:", accuracy_score(y_test, y_pred))
print("/nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 9))
sns.heatmap(cm,annot=True,fmt="d",cmap="Blues",xticklabels=["0","1"],yticklabels=["0","1"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("True")
plt.show()

# ---Visualize decision boundaries (Using PCA to reduce to 2D)---

# Reduce Features to 2 principal components for visualization
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Train SVM on PCA-reduced data for visualization purpose
svm_pca = SVC(kernel="rbf", random_state=42)
svm_pca.fit(X_train_pca, y_train)

# Create a mesh grid for plotting decision boundaries
x_min, x_max = X_train_pca[:, 0].min() - 1, X_train_pca[:, 0].max() + 1
y_min, y_max = X_train_pca[:, 1].min() - 1, X_train_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = svm_pca.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")

# plot the training points
scatter = plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, edgecolors='k', marker='o', label='Training Data',cmap="coolwarm")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("SVM Decision Boundary with PCA-reduced Training Data")
plt.legend(*scatter.legend_elements(), title="Classes")
plt.show()