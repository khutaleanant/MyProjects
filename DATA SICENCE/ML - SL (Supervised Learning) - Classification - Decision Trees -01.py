# A Decision Tree algorithm is a supervised learning method used for classification and regression tasks. It models decisions and their possible consequences as a tree-like structure, 
# where:
# Each internal node represents a test on an attribute (feature),
# Each branch represents the outcome of that test,
# Each leaf node represents a class label (for classification) or a continuous value (for regression).
# The algorithm works by recursively splitting the dataset into subsets based on the
# feature that results in the highest information gain (or lowest impurity) until a stopping condition is met.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import classification_report,accuracy_score

# Load your dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Diabetes_Prediction_Dataset.csv")

# Check for nulls
print("Missing Values\n",DataFrame.isnull().sum())

# check Somedata
print(DataFrame.head(10))

