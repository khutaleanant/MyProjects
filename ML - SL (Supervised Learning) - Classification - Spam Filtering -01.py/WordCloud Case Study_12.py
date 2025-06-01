# Text frequency visualization :- Is the process of representing the frequency (Count or Importance)
# of words or terms in a body of text data using visual elements such as word clouds, bar charts, or histograms.

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import re

# Load CSV file
DataFrame = pd.read_csv("C:\Data Science Programs Practice\iphone.csv")

# Drop NA values in reviewDescription column
DataFrame = DataFrame[DataFrame["reviewDescription"].notna()]

# Combine all reviews into a single string
text = " ".join(DataFrame["reviewDescription"].astype(str).tolist())

# Convert to lowercase and remove punctuation and numbers
text = text.lower()
text = re.sub(r"[^a-z\s]", "", text)
    # Above line uses python's regular expression library (re) to remove all characters that are not lowercase letters or whitespace.
    # The pattern [^a-z\s] matches any character that is not a lowercase letter (a-z) or whitespace (\s).

# Remove stop words
stop_words = set(stopwords.words("english"))

# Add custom stop words related to the iphone reviews that to generic words
custom_stop_words = {"iphone","apple","device","one","get","got","use","using"}
all_stopwords = stop_words.union(custom_stop_words)

# Filter out stop words from the text
filtered_words = [word for word in text.split() if word not in all_stopwords]

# Rejoin the filtered words into a single string
cleaned_text = " ".join(filtered_words)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis",max_words=200).generate(cleaned_text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of iPhone Reviews",fontsize=20, fontweight="bold")
plt.show()

# Above scource code generates a word cloud from the reviews of iPhone products.
# The word cloud visually represents the most frequently used words in the reviews,
# with larger words indicating higher frequency.