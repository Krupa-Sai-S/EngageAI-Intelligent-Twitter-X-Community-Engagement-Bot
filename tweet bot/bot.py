import pandas as pd
import openai
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# === Sentiment Analysis Function ===
analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment[
        "compound"
    ]  # Returns a score between -1 (negative) and 1 (positive)


# === Function to generate reply ===
def generate_reply(prompt, sentiment_score):
    try:
        # Adjust tone based on sentiment
        if sentiment_score >= 0.05:
            tone = "positive and friendly"
        elif sentiment_score <= -0.05:
            tone = "empathetic and soothing"
        else:
            tone = "neutral and helpful"

        # OpenAI response with adjusted tone
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You're a {tone} Twitter bot that responds to tweets.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=80,
        )
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"❌ Error: {str(e)}"


# === Load CSV dataset ===
df = pd.read_csv("sample.csv")

# === Step 1: Respond to dataset tweets ===
print("\n📄 Responding to tweets from dataset...\n")
for i in range(min(5, len(df))):
    tweet = df.iloc[i]["text"]
    print(f"👤 Tweet: {tweet}")

    # Get sentiment score before generating a reply
    sentiment_score = get_sentiment(tweet)

    # Generate reply based on sentiment
    bot_reply = generate_reply(tweet, sentiment_score)
    print(f"🤖 Reply: {bot_reply}\n")

# === Step 2: Allow manual testing ===
print("💬 Now you can test a manual input! Type your question:")
manual_input = input("👤 You: ")
manual_sentiment = get_sentiment(manual_input)
manual_reply = generate_reply(manual_input, manual_sentiment)
print(f"🤖 Bot Reply: {manual_reply}")
