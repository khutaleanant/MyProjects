# ✅ Python Program: Time Series + Word Cloud on Customer Reviews

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
from collections import Counter
import nltk
import re

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ----------------------------
# 1. Load or Simulate Data
# ----------------------------
# Simulated review dataset
data = {
    'timestamp': pd.date_range(start='2022-01-01', periods=100, freq='15D'),
    'review': [
        "Battery life is amazing. Totally worth the price!" if i % 2 == 0 else
        "Not durable. I had to return it. Poor quality battery." for i in range(100)
    ]
}
df = pd.DataFrame(data)

# Convert to datetime and month
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.to_period('M')

# ----------------------------
# 2. Preprocessing Functions
# ----------------------------
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word not in stop_words]
    return " ".join(filtered)

df['cleaned'] = df['review'].apply(clean_text)

# ----------------------------
# 3. Sentiment Analysis
# ----------------------------
df['polarity'] = df['review'].apply(lambda x: TextBlob(x).sentiment.polarity)
sentiment_over_time = df.groupby('month')['polarity'].mean()

# ----------------------------
# 4. Keyword Frequency Analysis
# ----------------------------
keywords = ['battery', 'price', 'quality', 'durable', 'return']
def count_keywords(text, keywords):
    words = text.split()
    count = Counter(word for word in words if word in keywords)
    return dict(count)

df['keyword_counts'] = df['cleaned'].apply(lambda x: count_keywords(x, keywords))
keyword_df = pd.DataFrame(df['keyword_counts'].tolist())
keyword_df['month'] = df['month']
keyword_time_series = keyword_df.groupby('month').sum()

# ----------------------------
# 5. Plot Sentiment Over Time
# ----------------------------
plt.figure(figsize=(10, 4))
sentiment_over_time.plot(marker='o', title="Average Sentiment Over Time")
plt.xlabel("Month")
plt.ylabel("Average Sentiment Polarity")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------
# 6. Plot Keyword Frequency
# ----------------------------
keyword_time_series.plot(kind='line', figsize=(10, 5), title="Keyword Frequency Over Time")
plt.xlabel("Month")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------
# 7. Generate Word Clouds by Month
# ----------------------------
for month in df['month'].unique():
    text = " ".join(df[df['month'] == month]['cleaned'])
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud - {month}")
    plt.tight_layout()
    plt.show()