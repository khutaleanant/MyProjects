# Analysis on the Ecommerce_Delivery_Analytics_New.csv file from Kaggle
# This file contains the data of an e-commerce company's delivery data
# The data is about the delivery of products to the customers
# The data contains the following columns:
## Order ID	Customer ID	Platform	Order Date & Time	
## Delivery Time (Minutes)	Product Category	Order Value (INR)	
## Customer Feedback	Service Rating	Delivery Delay	Refund Requested

#1) Importing the required libraries

import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

DataFrame = pd.read_csv("C:/Data Science Programs Practice/Ecommerce_Delivery_Analytics_New.csv")
# print(DataFrame.head())
# print(DataFrame.columns)
# print(DataFrame.shape)
# print(DataFrame.describe())
# print(DataFrame.dtypes)

#2) Data Cleaning
# Checking for missing values
# print(DataFrame.isnull().sum())
# Dropping the missing values
# DataFrame = DataFrame.dropna()

# #3) Data Analysis
# # Finding the total number of orders
# total_orders = DataFrame['Order ID'].nunique()
# print("Total Order: ",total_orders)

# # Finding the total number of customers
# total_customers = DataFrame['Customer ID'].nunique()
# print("Total Customer: ",total_customers)

# # Finding the total number of platforms
# total_platforms = DataFrame['Platform'].nunique()
# print("Total Platforms: ",total_platforms)

# # Finding the total number of product categories
# total_product_categories = DataFrame['Product Category'].nunique()
# print("Total Product Categories: ",total_product_categories)

# Finding the customers list who have requested for refund
# customers_with_refund = DataFrame[DataFrame['Refund Requested'] == 'Yes']

# # Finding the total number of customers who have requested for refund
# total_customers_with_refund = customers_with_refund['Customer ID'].nunique()
# print("Total Customers with Refund Requested: ",total_customers_with_refund)
# customers_with_refund.to_csv("Ecommerce_Delivery_Analytics_New_01.csv")

# # Finding the customers list who have given feedback
customers_with_feedback = DataFrame[DataFrame['Customer Feedback'] == 'Yes']

DataFrame.to_csv("Ecommerce_Delivery_Analytics_New_04.csv")


