# Color schema :- Word Clouds often use color to enhance visualization.
# The colors may be be assigned randomly or they can be based on the word frequency,sentiment or
# even categories within the text.

from sys import exception
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Download neccesary NLTK data files
nltk.download('vader_lexicon')

# Try reading the CSV file with some error handling
try:
    DataFrame=pd.read_csv("C:\Data Science Programs Practice\iphone.csv")
    print("CSV file loaded successfully.")
except Exception as e:
    print(f"Error loading CSV file: {e}")

# If the file loaded successfully, proceed with the sentiment analysis
if not DataFrame.empty:
    # Initialize the Sentiment Intensity Analyzer
    sia = SentimentIntensityAnalyzer()

    # Function to ensure all values are strings and handle NaN values
    def preprocess_text(text):
        # If the text is Nan or not a string, return an empty string
        if pd.isna(text):
            return ""
        return str(text)
    
    # Apply the preprocessing function to the 'reviewDescription' column
    DataFrame['reviewDescription'] = DataFrame['reviewDescription'].apply(preprocess_text)

    # Funtion to assign colors based on sentiment
    def assign_color(sentiment_score):
        if sentiment_score > 0.1:
            return 'green'  # Positive sentiment
        elif sentiment_score < -0.1:
            return 'red'    # Negative sentiment
        else:
            return 'gray'   # Neutral sentiment
        
    # Apply the sentiment analysis to each review and assign color
    DataFrame['sentiment_score'] = DataFrame['reviewDescription'].apply(lambda x: sia.polarity_scores(x)['compound'])
    DataFrame['color'] = DataFrame['sentiment_score'].apply(assign_color)

    # Save the output to a new CSV file
    DataFrame.to_csv("C:\Data Science Programs Practice\iphone_sentiment_analysis.csv", index=False)
    print("Sentiment analysis results saved to 'iphone_sentiment_analysis.csv'.")

    # Plot the bar chart for showing the sentiment distribution
    sentiment_counts = DataFrame['color'].value_counts()
    
    # Use the Bar plot to with color column as hue to avoid the deprecation warning
    plt.figure(figsize=(10, 9))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, hue=sentiment_counts.index, dodge=False, palette="Set2")
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.legend(title='Sentiment', loc='upper right')
    plt.show()