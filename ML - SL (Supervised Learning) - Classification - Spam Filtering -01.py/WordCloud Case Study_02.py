#Frequency Analysis
# Counting the number of times each word appears
# Frequency determines the size of the word in the word cloud

# Frequency analysis plus word cloud code

import pandas as pd
import nltk
from wordcloud import WordCloud

#nltk : Natural Language Toolkit.It is use to work with human language data.
# nltk: You can use nltk's predfined modules to pre process the text before
# generating a wordcloud.For Example, to remove stop words, perform tokenization
# and normalized words through stemming or lemmatization.
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string

# Download the stopwords
nltk.download('stopwords')

# Load the Dataset
DataFrame=pd.read_csv("C:\Data Science Programs Practice\iphone.csv")

#Drop NaN values in reviewDescription column
DataFrame.dropna(subset=['reviewDescription'], inplace=True)

#Combine all review description 
text=" ".join(DataFrame["reviewDescription"].astype(str))

# Convert text to lower case and remove punctuation
text=text.lower()
text=text.translate(str.maketrans("", "", string.punctuation))

# Remove stopwords
stop_words=set(stopwords.words("english"))
words=text.split()
filtered_words=[word for word in words if word not in stop_words]

# Join the filtered words back into a string
filtered_text="".join(filtered_words)

# Generate the wordcloud
wordcloud=WordCloud(width=800, height=400, background_color="white").generate(filtered_text)

# Display the wordcloud
plt.figure(figsize=(10, 9))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Frequent words in iphone reviews",fontsize=20)
plt.show()



