# How sentiment polarity is calculated

## 1) Lexicon based scoring : Textblob use a predefined dictionary of words where
# each word is assigned:-
# 1. A polarity score between -1 and 1
# 2. A subjectivity score between 0 and 1

## 2) Word Level Polarity:
# Each word in the text is checked against this dictionary:-
# 1. Postive words like "Great","Excellent" have a positive polarity score (+0.8)
# 2. Negative words like "Bad","Poor","Terrible" have a negative polarity score (-0.9)
# 3. Neutral words  have a score of 0 or are ignored.

## 3) Modifiers are considered:
# 1. Negations like "not good" reduce or flip the polarity score of the word
# 2. Intensifiers like "very happy" increase the polarity score of the word

## 4) Sentence Level Aggregation:
# The polarity scores of all the words and phrases in a sentences or multiple sentences is averaged to give
# one final polarity score for the entire text.

import pandas as pd
from textblob import TextBlob

# Read the CSV file
DataFrame = pd.read_csv("C:\Data Science Programs Practice\iphone.csv")

# Combine title and description
DataFrame["Full_Review"]= DataFrame["reviewTitle"] + " " + DataFrame["reviewDescription"].fillna("")

# Compute sentiment polarity
DataFrame["sentiment"] = DataFrame["Full_Review"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Save the result to a new CSV file
DataFrame.to_csv("Sentiment_Polarity_Of_FullReview_Column.csv", index=False)

