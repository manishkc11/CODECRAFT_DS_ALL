import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load datasets
train_df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task4_twitter\twitter_training.csv", header=None, names=["ID", "Entity", "Sentiment", "Tweet"])
valid_df = pd.read_csv(r"C:\Users\dell\Desktop\codecraft_internship_tasks\task4_twitter\twitter_validation.csv", header=None, names=["ID", "Entity", "Sentiment", "Tweet"])

# Combine both datasets
df = pd.concat([train_df, valid_df], ignore_index=True)

# Clean tweet text
def clean_text_safe(text):
    if isinstance(text, str):
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"#\w+", "", text)
        text = re.sub(r"[^A-Za-z\s]", "", text)
        return text.lower().strip()
    return ""

df["Clean_Tweet"] = df["Tweet"].apply(clean_text_safe)

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment", hue="Sentiment", palette="Set2", legend=False)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("task04_sentiment_distribution.png")
plt.close()

# Word Clouds for each sentiment
for sentiment in df["Sentiment"].unique():
    text = " ".join(df[df["Sentiment"] == sentiment]["Clean_Tweet"])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    wordcloud.to_file(f"task04_wordcloud_{sentiment}.png")

print("Task 4 completed. Outputs saved as PNGs.")
