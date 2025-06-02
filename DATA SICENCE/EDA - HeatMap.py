# EDA - HeatMap

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
# In Python seaborn is a popular data visualization library that is built on
# the top of matplotlib. It provides a high level interface for creating attractive 
# and informative statistical graphics. seaborn makes it is easier to generate complex
# visualization with less code compared to matplotlib specially for statistical
# and data analysis tasks.


DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

DATA1=DataFrame.corr()

# Plot a HeatMap of the correlation matrix

plt.figure(figsize=(10,8))
# This sets the size of the figure(or the ploting area) to be 10 inches wide by 8 inches tall

sns.heatmap(DATA1,annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)

plt.title("Correlation Matrix")

plt.show()
