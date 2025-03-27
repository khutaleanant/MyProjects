import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Ecommerce_Delivery_Analytics_New.csv")

# VIOLIN plot to compare distrubutions (Compairing Platform and Delivery Time)\

plt.figure(figsize=(10,10))
sns.boxplot(x="Platform",y="Delivery Time (Minutes)",data=DataFrame)
plt.title("Delivery Time Distribustion Accross Pltform")
plt.show()