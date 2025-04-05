# Verify whether the review_score column is normally distributed or not.

import sqlite3
from cv2 import line
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


Connection=sqlite3.connect("C:\Data Science Programs Practice\olist.sqlite")
Query="SELECT review_score FROM order_reviews"

# Read the data from SQLite database into a DataFrame
DataFrame=pd.read_sql_query(Query,Connection)
Connection.close()

# Check the first few rows of the DataFrame
print(DataFrame.head())

# Calculate kurtosis of the review_score column
KURTOSIS=stats.kurtosis(DataFrame["review_score"].dropna())
print(f"KURTOSIS of review_score: {KURTOSIS}")

# Check if the distribution is mesokurtic (normal distribution or  kurtosis close to 0)

if -1<KURTOSIS<1:
    print("The Distribution is Mesokurtic (Normal Distribution)")
else:
    print("The Distribution is not Mesokurtic (Normal Distribution)")

# plot the KDE of the review_score column
plt.figure(figsize=(10,9))
sns.kdeplot(DataFrame["review_score"],fill=True,color="green",linewidth=2)
plt.title("KDE of review_score")
plt.xlabel("Review Score")
plt.ylabel("Density")
plt.show()