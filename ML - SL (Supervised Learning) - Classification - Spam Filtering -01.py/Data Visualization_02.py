# Leptokurtic Distribution
from turtle import color
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pyparsing import alphas
from scipy.stats import kurtosis

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Coin_Aave.csv")

# Check first few rows of the dataset to understand its structure
print(DataFrame.head())

# Check the column names to find the numerical columns
print(DataFrame.columns)

# Check datatypes of the columns
print(DataFrame.dtypes)

# Assuming "Volume" column exists in the dataset
if "Volume" in DataFrame.columns:
    column=DataFrame["Volume"]
else:
    print("Volume Column does not found in Dataset.")

# Calculate the KURTOSIS of the "Volume" column.
kurt_value=kurtosis(column)

# print the KURTOSIS value
print(f"KURTOSIS for the 'Volume' column = {kurt_value}")

# Check if the distribution is Leptokurtic
if kurt_value>3:
    print("The Distribution is Leptokurtic(Heavy tails)")
else:
    print("The Distribution is not Leptokurtic")

# Plot the KDE of the "Volume" column
plt.figure(figsize=(10,9))
sns.kdeplot(column,fill=True,color="blue",alpha=0.7)
plt.title(f"KDE of Volume(KURTOSIS={kurt_value:.2f})")
plt.xlabel("Volume")
plt.ylabel("Density")
plt.grid(True)
plt.show()

