# Data Visualization
# Platykurtic Distribution

from turtle import title
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew,kurtosis

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Sales_Data.csv")

# Assume "Sales_Amount" is the column we are interested in

Sales_Data=DataFrame["Sales_Amount"]

# plot skewness visualization (KDE plot-curve form)

def plot_kde_curve (Data,title):
    plt.figure(figsize=(10,9))
    sns.kdeplot(Data,fill=True,color="purple",linewidth=2)
    plt.title(f"{title}-KDE Plot")
    plt.xlabel("Sales Amount")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()

# Visualize Skewness using KDE Plot
plot_kde_curve(Sales_Data,"Sales Data Skewness")

# Calculate Skewness of the sales data
Sales_Skewness=skew(Sales_Data)
print(f"Skewness of Sales Data = {Sales_Skewness}")

# Calculate KURTOSIS of Sales Data
Sales_KURTOSIS=kurtosis(Sales_Data)
print(f"KURTOSIS of Sales Data = {Sales_KURTOSIS}")

#Interpret the KURTOSIS
if Sales_KURTOSIS>3:
    print("The Distribution is leptokurtic (More Peaked With Heavy Tails)")
elif Sales_KURTOSIS<3:
    print("The Distribution is platykurtic (Flatter Distribution)")
else:
    print("The Distribution is mesokurtic (Normal Tailedness)")






