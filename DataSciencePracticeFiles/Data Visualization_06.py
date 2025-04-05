from multiprocessing import connection
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn= sqlite3.connect('C:\\Data Science Programs Practice\\olist.sqlite')

query="SELECT shipping_limit_date from order_items"

DataFrame= pd.read_sql_query(query,conn)


# Convert the 'shipping_limit_date' column to datetime format

DataFrame['shipping_limit_date'] = pd.to_datetime(DataFrame['shipping_limit_date'])

# Resample to hourly counts (Counting the number of records per hour with "h")

DataFrame_Hourly = DataFrame.resample('h', on='shipping_limit_date').size()

# Plot time series with hourly resolution.
plt.figure(figsize=(12, 6))
plt.plot(DataFrame_Hourly.index, DataFrame_Hourly.values, marker='x')
plt.title('Shipping Limit Date Over Time')
plt.xlabel('Date & Time')
plt.ylabel('Number of Shippments')
plt.grid(True)
plt.show()

conn.close()