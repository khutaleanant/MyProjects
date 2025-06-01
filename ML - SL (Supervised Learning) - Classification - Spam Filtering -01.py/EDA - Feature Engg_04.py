# EDA - Feature Engg
# Binary Encoding >> is a compromise between one-hot encoding and label encoding.
# Each category is first assigned an integer which is then converted into binary code.
# The Binary digits(0s and 1s) are split into separate columns.

import pandas as pd
import category_encoders as ce

DataFram=pd.read_csv("C:\Data Science Programs Practice\Color-Concrete-Objects.csv")

# Apply binary encoding to the "color" column.

encoder=ce.BinaryEncoder(cols=["color"])

DataFram_encoded=encoder.fit_transform(DataFram)

DataFram_encoded.to_csv("Encoded_File.csv",index=False)






