"""
Sentiment Analysis (Text)
------------------------
Classifies text as positive or negative using TextBlob.

Steps for Beginners:
1. Import TextBlob from textblob.
2. Get user input for a sentence.
3. Use TextBlob to analyze sentiment.
4. Print polarity and classification.
"""

from textblob import TextBlob

# 2. Get user input
text = input("Enter a sentence: ")

# 3. Analyze sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# 4. Print result
print(f"Polarity: {polarity}")
if polarity > 0:
    print("Sentiment: Positive")
elif polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
