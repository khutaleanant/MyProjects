import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DataFrame=pd.read_excel("C:/Data Science Programs Practice/Online Retail.xlsx")

# CHeck the first few rows of the DataFrame to understand the data structure
print(DataFrame.head())
# Check the data types of the columns
print(DataFrame.dtypes)

# Check for missing values in the Quantity column
print(f"Missing Values in Quantity Column:{DataFrame["Quantity"].isnull().sum()}")

# Drop rows where Quantity is NaN
DataFrame.dropna(subset=["Quantity"], inplace=True)

# Ensure Quantity is of integer/Numeric type
DataFrame["Quantity"] = pd.to_numeric(DataFrame["Quantity"], errors="coerce")

# Check Skewness of the Quantity column

qs=DataFrame["Quantity"].skew()
print(f"Skewness of Quantity Column:{qs}")

# Display Skewness interpretation
if qs<0:
    print("The Distribution is Negatively Skewed (Left Skewed)")
elif qs>0:
    print("The Distribution is Positively Skewed (Right Skewed)")
else:
    print("The Distribution is Symmetrical (No Skewness or Normal Distribution or Skewness close to 0)")

# Plot the KDE to visualize the distribution of the Quantity column
plt.figure(figsize=(10, 6))
sns.kdeplot(DataFrame["Quantity"], fill=True, color="blue", linewidth=2)
plt.title("KDE of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Density")  
plt.show()