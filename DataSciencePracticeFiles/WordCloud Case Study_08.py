# Stemming :- Is the process of reducing a word to its base or root form,
# often by removing suffixes or prefixes. It is a crude technique that may not always produce a valid word.
# For example, the stem of "running" is "run", and the stem of "better" is "better".

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load the DataSet
DataFrame=pd.read_csv("C://Data Science Programs Practice/iphone.csv")

# Check for and handle missing values in the "reviewDescription" column
DataFrame['reviewDescription'].fillna('', inplace=True)

# Initialize the stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Function to tokenized, remove stopword and apply stemming
def stem_review(text): # ensure the text is a string
    if isinstance(text, str):
        # Tokenize the review text
        words=word_tokenize(text)

        # Remove stopwords and non alphabetic characters/words then apply stemming
        stemmed_words=[stemmer.stem(word) for word in words if word.isalpha() and word.lower() not in stop_words]

        # join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    else:
        return ''

# Apply the stemming function to the reviewDescription column
# This will create a new column 'stemmed_reviewDescription' in the DataFrame
DataFrame['stemmed_reviewDescription'] = DataFrame['reviewDescription'].apply(stem_review)

# Save the resulting DataFrame to a new CSV file
DataFrame.to_csv("C:\Data Science Programs Practice\iphone_stemmed_reviews.csv", index=False)

