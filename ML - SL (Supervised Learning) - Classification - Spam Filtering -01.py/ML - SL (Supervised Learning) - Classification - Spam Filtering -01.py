# ML - SL (Supervised Learning) - Classification - Spam Filtering
# Spam Filtering is a task of automatically identifying and separating
# unwanted email messages ("SPAM") from legitimate ones ("HAM").
# The goal is to classify incoming emails as SPAM or Not SPAM.

from h11 import Data
from matplotlib.pylab import multinomial
from numpy import vectorize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

# Load the dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Spam.csv",encoding="latin-1")[["v1","v2"]]
DataFrame.columns=["label","message"]

# Display first five rows from the selected dataset
DataFrame.head()

# Convert Labels to Binary (HAM=0, SPAM=1)
DataFrame["label"]=DataFrame["label"].map({"ham":0,"spam":1})

# Add a column for msg length
DataFrame["message_length"]=DataFrame["message"].apply(len)

# Data Visualization
# Countplot of HAM vs SPAM
plt.figure(figsize=(12,12))
sns.countplot(x="label",data=DataFrame)
plt.xticks([0,1],["HAM","SPAM"])
plt.title("Distribution of HAM and SPAM Messages")
plt.xlabel("Message Type")
plt.ylabel("Count")
plt.show()

# Distribution of msg lengths
plt.figure(figsize=(12,12))
sns.histplot(data=DataFrame,x="message_length",hue="label",bins=50,palette="husl",kde=True)
plt.xlabel("MSG LENGTH")
plt.ylabel("Frequency")
plt.legend(labels=["HAM","SPAM"])
plt.show()

# Train-Test split
X_train,X_test,y_train,y_test=train_test_split(DataFrame["message"],DataFrame["label"],test_size=0.2,random_state=42)

# TF-IDF vectorization
vectorizer=TfidfVectorizer(stop_words="english")
X_train_vec=vectorizer.fit_transform(X_train)
X_test_vec=vectorizer.transform(X_test)

# Train Naive Bayes classifier
model=MultinomialNB()
model.fit(X_train_vec,y_train)

# Predictions and Evaluation
y_pred=model.predict(X_test_vec)

# Accuracy
print("Accuracy:",accuracy_score(y_test,y_pred))

# Plotting the confusion matrix
conf_mat=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(12,10))
sns.heatmap(conf_mat,annot=True,fmt="d",cmap="Blues",xticklabels=["HAM","SPAM"],yticklabels=["HAM","SPAM"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print("\nClassification Report\n",classification_report(y_test,y_pred))