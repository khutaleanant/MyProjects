# If user is working with Time-Series Data in python using pandas then user can create new 
# features derived from Date Column like - Day of the Week, Month, Year,Hour,minute,Seconds,WeekDay,Quarter,etc

from tkinter.font import BOLD
import pandas as pd

DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\Ecommerce_Delivery_Data_Multiple_Years_2018_2025.csv")

# print(DataFrame.dtypes) # Check data types

####### Convert "Delivery Date" column to datetime
DataFrame["Delivery Date"] = pd.to_datetime(DataFrame["Delivery Date"])
DataFrame["Delivery Time"] = pd.to_datetime(DataFrame["Delivery Time"], format='%H:%M:%S')

# Create New Features
# Extract the Day of the week

DataFrame["Day Of the Week"]=DataFrame["Delivery Date"].dt.day_name()

# Extract the Month
DataFrame["Month"]=DataFrame["Delivery Date"].dt.month

#Extract the Year
DataFrame["Year"]=DataFrame["Delivery Date"].dt.year

#Extract the WeekDay
DataFrame["WeekDay"]=DataFrame["Delivery Date"].dt.weekday


# Extract the Quarter
DataFrame["Quarter"]=DataFrame["Delivery Date"].dt.quarter


# Extract the Hour
DataFrame["Hour"]=DataFrame["Delivery Time"].dt.hour

# Extract the Minute
DataFrame["Minute"]=DataFrame["Delivery Time"].dt.minute

# Extract the Second
DataFrame["Second"]=DataFrame["Delivery Time"].dt.second


DataFrame.to_csv("Find Day_Month_OTR_Weekday_01.csv")










