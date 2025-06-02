# Using the CSV file, Creating and Calculating the New "AGE" & "AGE-GROUP" Columns

from calendar import Day, month
import pandas as pd
from datetime import datetime

# Load the dataset
DataFrame=pd.read_csv("C:\Data Science Programs Practice\Employee_Data_01.csv")

# Display the first few rows of the dataset
# print(DataFrame.head())


# 1. Convert 'Birthdate' column to datetime format
DataFrame["Date of birth"] = pd.to_datetime(DataFrame["Date of birth"], format="%d-%m-%Y")

# Display the first few rows of the dataframe to verify the result
print(DataFrame.head())

# 2. Calculate the 'Age' column based on the 'Birthdate' column
Today=datetime.today()
print(Today)

# Calculate the age of each employee
# Calculate the age of each employee
DataFrame["Age Of Employee"] = Today.year - DataFrame["Date of birth"].dt.year - \
    ((DataFrame["Date of birth"].dt.month > Today.month) | 
     ((DataFrame["Date of birth"].dt.month == Today.month) & (DataFrame["Date of birth"].dt.day > Today.day)))

# Display the modified DataFrame with the new 'Age' column
print("\nData with Age Calculated:")
print(DataFrame)

DataFrame.to_csv("New Employee Data with Age.csv")