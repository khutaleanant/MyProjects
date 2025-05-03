# Word tokenization:- Splits the text into individual words.

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer models if not already done.
nltk.download('punkt_tab')

# Read the CSV file into a DataFrame
DataFrame=pd.read_csv("C:\Data Science Programs Practice\iphone.csv")

# Drop rows where reviewDescription is missing
DataFrame = DataFrame.dropna(subset=['reviewDescription'])

# Tokenize each reviewDescription
DataFrame['tokens'] = DataFrame['reviewDescription'].apply(word_tokenize)

# Save the DataFrame with tokens to a new CSV file
DataFrame.to_csv("C:\Data Science Programs Practice\iphone_tokenized.csv", index=False)

print("Tokenization complete. The tokenized data has been saved to 'iphone_tokenized.csv'.")
