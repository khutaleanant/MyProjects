# How to read data from .sqlite dataset
# Importing the required libraries
import sqlite3
import pandas as pd

# Establishing a connection to the SQLite database
conn = sqlite3.connect("C:\Data Science Programs Practice\olist.sqlite")

# Query the orders_payments table using sql
query="select * from order_payments"

# Load the Data into a pandas DataFrame

DataFrame=pd.read_sql(query,conn)

# Close the connection to the database
conn.close()

DataFrame.to_csv("SQLITE DATA using Pandas.csv")