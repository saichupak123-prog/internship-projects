import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download lexicon
nltk.download("vader_lexicon")

# Read dataset
df = pd.read_csv("reviews.csv")

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def sentiment(review):

    score = sia.polarity_scores(review)["compound"]

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(sentiment)

# Save results
df.to_csv("sentiment_results.csv", index=False)

# Print results
print(df)

# Count sentiment
counts = df["Sentiment"].value_counts()

print("\nSentiment Count")
print(counts)

# Visualization
plt.figure(figsize=(7,5))

plt.bar(counts.index, counts.values)

plt.title("Book Review Sentiment Analysis")

plt.xlabel("Sentiment")

plt.ylabel("Number of Reviews")

plt.savefig("sentiment_chart.png")

plt.show()

print("\nTask 4 Completed Successfully")
