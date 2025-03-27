import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

# PairPlot (Scatter Plot Matrix)
# Visualize the pairvise relationship between numrical columns

sns.pairplot(DataFrame,hue="YearsExperience")

plt.show()

