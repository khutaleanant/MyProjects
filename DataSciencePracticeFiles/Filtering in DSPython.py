# Applying filter in Python
# Filtering is a technique for selecting a subset of elements from a sequence based on certain criteria.

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/Most popular 1000 Youtube videos.csv")

# Filtering the data based on the condition

DataFrame=DataFrame[DataFrame["published"]>2016]

DataFrame.to_csv("FilteredData.csv")
