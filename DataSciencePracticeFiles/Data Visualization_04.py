# Positve Skewness

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Titanic-Dataset.csv")

if "Fare" in DataFrame.columns:
    column=DataFrame["Fare"]
else:
    column=DataFrame.select_dtypes(include=[np.number]).columns[0]

skew_value=skew(column)
print(f"Skewness of {column.name}={skew_value}")

if skew_value>0:
    print("The distribution of the FARE column is positively skewed")
else:
    print("The distribution of the FARE column is not positively skewed")

# plot a KDE curve to visualize the distribution
sns.kdeplot(column,fill=True,color="yellow",alpha=0.7)
plt.title(f"Distribution of {column.name} (skewness:{skew_value:.2f})")
plt.xlabel(column.name)
plt.ylabel("Density")
plt.grid(True)
plt.show()