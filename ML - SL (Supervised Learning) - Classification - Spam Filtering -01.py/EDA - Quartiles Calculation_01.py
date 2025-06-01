# Exploratory Data Analysis (EDA) Quartiles Calculation

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Customers Data for EDA - RANGE.csv")

Quartiles01="Spending Score (1-100)"

# Calculate the Quartiles
Q1=DataFrame["Spending Score (1-100)"].quantile(0.25) #25% Quartiles
Q2=DataFrame["Spending Score (1-100)"].quantile(0.50) #50% Quartiles
Q3=DataFrame["Spending Score (1-100)"].quantile(0.75) #75% Quartiles

print("Q1(25th percentile of",Quartiles01,"is",Q1)
print("Q2(50th percentile of",Quartiles01,"is",Q2)
print("Q3(75th percentile of",Quartiles01,"is",Q3)