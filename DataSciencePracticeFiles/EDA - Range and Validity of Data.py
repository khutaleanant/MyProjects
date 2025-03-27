# Identification:- Check if numerical data values fall within expected ranges

# Example 1

from numpy import maximum
import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Salary DataSet.csv")

# For salary, it should be greater than 50000

Minimum_Salary=50000

Salary_Outliers=DataFrame[DataFrame["Salary"]<Minimum_Salary]

# Displaying the Outlier in the Salary column

print(Salary_Outliers)

##################################################3

# Example 2

DataFrame2=pd.read_csv("C:\Data Science Programs Practice\Mall_Customers.csv")

# For Age, it should be greater than 20

Minimum_Age=20
Maximum_Age=60

Age_Outliers=DataFrame2[(DataFrame2["Age"]<Minimum_Age)|(DataFrame2["Age"]>Maximum_Age)]

# Displaying the Outlier in the Salary column

print(Age_Outliers)





