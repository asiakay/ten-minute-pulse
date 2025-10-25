import feedparser
from textblob import TextBlob
import matplotlib.pyplot as plt
import json

# --- 1. Fetch live data (Boston.com RSS feed) ---
feed = feedparser.parse("https://www.boston.com/tag/news/feed/")
texts = [entry.title for entry in feed.entries]

# --- 2. Sentiment analysis ---
sentiments = {"positive": 0, "neutral": 0, "negative": 0}
for text in texts:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        sentiments["positive"] += 1
    elif polarity < -0.1:
        sentiments["negative"] += 1
    else:
        sentiments["neutral"] += 1

# --- 3. Save data for front end ---
with open("mood_data.json", "w") as f:
    json.dump(sentiments, f)
print("Wrote mood_data.json:", sentiments)

# --- 4. Also save chart image (optional) ---
plt.bar(sentiments.keys(), sentiments.values(), color=["#00b7b3", "#efe7d8", "#ff1e8a"])
plt.title("Boston News Mood Map")
plt.ylabel("Count")
plt.savefig("mood_map.png")
print("Saved mood_map.png")