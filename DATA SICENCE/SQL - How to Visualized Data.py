# How to visualize data from stored data in tables.
# Importing the required libraries
from pickle import TRUE
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Establishing a connection to the SQLite database
conn = sqlite3.connect("C:\Data Science Programs Practice\olist.sqlite")

query = "select payment_value from order_payments"

# Load the Data into a pandas DataFrame

DataFrame = pd.read_sql(query, conn)

conn.close()

# Visualizing the data using matplotlib and seaborn
# Ploting the histogram of payment_value
plt.figure(figsize=(10, 6))
sns.histplot(DataFrame["payment_value"], bins=30, kde=True,color="purple")
plt.title("Distribution of Payment Value")
plt.xlabel("Payment Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()