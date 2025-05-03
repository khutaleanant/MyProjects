# Sentence tokenization:- Is the process of splitting a block of text into 
# individual sentences.

import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

# load the dataset
DataFrame=pd.read_csv("C:\Data Science Programs Practice\iphone.csv")

# Drop rows where reviewDescription is missing
DataFrame = DataFrame.dropna(subset=['reviewDescription'])

# Tokenize (apply sentence tokenization to each review)
DataFrame['Tokenized_Sentences'] = DataFrame['reviewDescription'].apply(sent_tokenize)

# Save output to a new CSV file
DataFrame.to_csv("C:\Data Science Programs Practice\iphone_tokenized_sentences.csv", index=False)

print("Tokenization complete. The tokenized sentences have been saved to 'iphone_tokenized_sentences.csv'.")
