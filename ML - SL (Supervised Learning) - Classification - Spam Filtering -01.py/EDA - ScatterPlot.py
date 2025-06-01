import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

# Scatter plot (Relationship between years exp and Salary)

plt.figure(figsize=(10,12))
sns.scatterplot(x=DataFrame["YearsExperience"],y=DataFrame["Salary"])
plt.title("YearExp vs Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()