import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.decomposition import PCA
import numpy as np

# Load the dataset
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\BankNoteAuthentication.csv")

# Inspect the first few rows of the dataset
print("First five rows of the dataset:")
print(DataFrame.head())

# Data Visualization
# Pairplot to visualize relationships between features colored by class
sns.pairplot(DataFrame, hue="class",diag_kind="kde",markers=["o", "s"])
plt.suptitle("Pairplot of Features colored by Class", y=1.02)
plt.show()

# Correlation heatmap to visualize feature correlations
plt.figure(figsize=(10, 10))
sns.heatmap(DataFrame.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Heatmap of Features")
plt.show()

# Prepare the data
X = DataFrame[["variance","skewness","curtosis","entropy"]]
y = DataFrame["class"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the SVM classifier
svm=SVC(kernel='rbf', C=1.0, random_state=42)
svm.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm.predict(X_test_scaled)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Accuracy Score:")
print(accuracy_score(y_test, y_pred))

# Visualize the confusion matrix
cm= confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Class 0", "Class 1"], yticklabels=["Class 0", "Class 1"])
plt.xlabel("Predicted Class")
plt.ylabel("True Class")
plt.title("Confusion Matrix")
plt.show()

# Visualization of Decision Boundaries (Using PCA to reduce to 2D)
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Train SVM on PCA-reduced data for visualization
svm_pca = SVC(kernel='rbf', C=1.0, random_state=42)
svm_pca.fit(X_train_pca, y_train)

# Create a mesh to plot decision boundaries
x_min, x_max = X_train_pca[:, 0].min() - 1, X_train_pca[:, 0].max() + 1
y_min, y_max = X_train_pca[:, 1].min() - 1, X_train_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = svm_pca.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10,6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')

# plot training points
scatter = plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, edgecolors="k", marker="o", label="Train")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("SVM Decision Boundary (PCA-reduced Data)")
plt.legend(*scatter.legend_elements(), title="Classes")
plt.show()
