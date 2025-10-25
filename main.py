import matplotlib.pyplot as plt
from textblob import TextBlob

# Sample headlines to simulate real-time data
texts = [
    "Boston plans new climate initiative",
    "Traffic delays cause frustration downtown",
    "Community garden opens in Roxbury",
    "Storm cleanup efforts continue",
    "Local artist wins major grant"
]

sentiments = {"positive":0, "neutral":0, "negative":0}
for text in texts:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        sentiments["positive"] += 1
    elif polarity < -0.1:
        sentiments["negative"] += 1
    else:
        sentiments["neutral"] += 1

plt.bar(sentiments.keys(), sentiments.values())
plt.title("Community Mood Map")
plt.ylabel("Count")
plt.savefig("mood_map.png")
print("Sentiments:", sentiments)
print("Saved as mood_map.png")
