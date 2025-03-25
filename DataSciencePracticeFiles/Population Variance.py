# Populatioins Variance

import pandas as pd
import numpy as np

Dataframe=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

DATA1=Dataframe["YearsExperience"]

DATA2=np.var(DATA1)

print(f"Population Variance = {DATA2}")