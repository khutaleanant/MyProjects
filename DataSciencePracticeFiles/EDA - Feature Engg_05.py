#EDA - Feature Engg
# Categorical Encoding >> Frequency or Count Encoding >> This encoding method replaces
# categories with their respective frequency or count in the dataset.

import pandas as pd

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Color-Concrete-Objects.csv")

# Get the Frequency (Count) of each category in the "color" column

DATA1=DataFrame["color"].value_counts()

# Replace the categories with their respective frequencies.

DataFrame["color_encoded"]=DataFrame["color"].map(DATA1)

DataFrame.to_csv("Encoded_File2.csv",index=False)