# Lemmatization:- is the process in natural language processing (NLP) of reducing a word to its base or dictionary form, known as a lemma,
# while taking into account the context and part of the speech of the word.

from tkinter import READABLE
from unittest import result
import pandas as pd
import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

#Download the NLTK data files
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')  # ✅ corrected name
nltk.download('punkt')
nltk.download('stopwords')


# Load the dataset
DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\iphone.csv")

# Handle the missing values
DataFrame["reviewDescription"]=DataFrame["reviewDescription"].fillna("")

# Initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Map short pos tags to full descriptions
def map_pos(tag):
    if tag.startswith('J'):
        return 'Adjective'  # Adjective
    elif tag.startswith('V'):
        return 'Verb'  # Verb
    elif tag.startswith('N'):
        return 'Noun'  # Noun
    elif tag.startswith('R'):
        return 'Adverb'  # Adverb
    else:
        return "Noun"

# Helper function to map nltk POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ # Adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # Verb
    elif tag.startswith('N'):
        return wordnet.NOUN  # Noun
    elif tag.startswith('R'):
        return wordnet.ADV  # Adverb
    else:
        return wordnet.NOUN  # Default to noun if no match found
    
# process all reviews and collect results
rows=[]

for review in DataFrame["reviewDescription"]:
    if isinstance(review, str):
        
        # Tokenize the review
        tokens = word_tokenize(review)
    
        # Get the part of speech tags for each token
        tagged = pos_tag(tokens)
      
        for word,pos in tagged:
            wordnet_pos = get_wordnet_pos(pos)  # Get the WordNet POS tag
            lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)  # Lemmatize with the correct POS tag
            readable_pos  = map_pos(pos)
            rows.append([word,lemma,readable_pos])

# Create a DataFrame from the results
result_df = pd.DataFrame(rows, columns=["Original Word", "Lemma", "POS"])


# Save the DataFrame with lemmatized reviews to a new CSV file
result_df.to_csv("C:\Data Science Programs Practice\iphone_lemmatized_reviews.csv", index=False)

print("lemmatization completed successfully and saved to iphone_lemmatized_reviews.csv")

