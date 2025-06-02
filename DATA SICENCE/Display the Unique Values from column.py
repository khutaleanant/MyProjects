# Display the unique values from a particular Column in peraticular dataset.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

# Check unique values in the "YearsExperience"

print("Unique Values in YearsExperience Column")

if "YearsExperience" in DataFrame.columns:
    print(f"YearsExperience={DataFrame["YearsExperience"].nunique()}unique Values.")
else:
    print("YearsExperience column not found in the Dataset.")