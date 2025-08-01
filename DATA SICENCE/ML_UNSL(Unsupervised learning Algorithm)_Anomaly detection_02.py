
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\validation_score.csv")
print("dataset shape : ",DataFrame.shape)
print("First Few Rows : ")
print(DataFrame.head())

# Visualized Data Distributions
plt.figure(figsize=(14, 8))
median_cols = [col for col in DataFrame.columns if "median" in col and "_h" not in col]
DataFrame[median_cols].hist(figsize=(14,10),bins=30)
plt.suptitle("Distributions of Median Columns",fontsize=16)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(DataFrame.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap", fontsize=16)
plt.tight_layout()
plt.show()

# Prepare the data for anomaly detection
features = ["median7", "median14","median28", "median35", "median42", "median49", "median7_h", "median14_h", "median21_h", "median28_h", "median35_h", "median42_h", "median49_h", "holiday", "holiday_log", "yearly_log"]
X = DataFrame[features].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
DataFrame["anomaly"]= model.fit_predict(X_scaled)
DataFrame["anomaly"] = DataFrame["anomaly"].map({1: 0, -1: 1})  # Convert to binary (0 for normal, 1 for anomaly)

# Count of Anomalies
plt.figure(figsize=(10,10))
sns.countplot(data=DataFrame, x='anomaly', palette={'0': 'blue', '1': 'red'})
plt.title("Count of Anomalies", fontsize=16)
plt.xlabel("Class", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(ticks=[0, 1], labels=["Normal", "Anomaly"], fontsize=12)
plt.tight_layout()
plt.show()

# Visualize anomalies in Feature space
plt.figure(figsize=(14, 10))
sns.scatterplot(x="median7", y="median7_h", hue="anomaly", data=DataFrame, palette={'0': "blue", '1': "red"}, alpha=0.6)
plt.title("Anomalies in Feature Space (median7 vs median7_h)", fontsize=16)
plt.xlabel("Median 7", fontsize=14)
plt.ylabel("Median 7 (Holiday)", fontsize=14)
plt.legend(title="Anomaly", loc="upper right", fontsize=12,labels=["Normal", "Anomaly"])
plt.tight_layout()
plt.show()

# Pairplot of sampled data
sample = DataFrame.sample(300) if len(DataFrame)>300 else DataFrame.copy()
sns.pairplot(sample, hue="anomaly", vars=['median7', 'median14', 'median7_h', 'median14_h'], palette={0: "blue", 1: "red"}, markers=["o", "X"], height=2.5)
plt.suptitle("Pairplot of Sampled Data", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# Save the DataFrame with anomalies
anomalies = DataFrame[DataFrame["anomaly"] == 1]
anomalies.to_csv("C:\\Data Science Programs Practice\\anomalies_detected.csv", index=False)
print(f"Anomalies saved to 'anomalies_detected.csv' ({len(anomalies)} rows).")

