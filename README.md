# EngageAI-Intelligent-Twitter-X-Community-Engagement-Bot

An AI-powered bot that helps brands or creators enhance community interaction on Twitter/X. It auto-replies to mentions with meaningful, sentiment-aware, and tone-personalized responses using OpenAI and VADER Sentiment Analysis.

---

## 📌 Features

- **Auto-Reply to Mentions:** Detects and responds to recent mentions on Twitter/X.
- **Sentiment Analysis:** Uses VADER to classify tweets as Positive, Neutral, or Negative.
- **GPT-Powered Responses:** Generates intelligent replies tailored to sentiment and tone.
- **Manual Testing Mode:** Test responses manually without accessing Twitter.
- **Configurable Responses:** Easy setup for static/customized responses if desired.

---

## 🛠️ Tech Stack

- Python 🐍
- [Tweepy](https://www.tweepy.org/) – Twitter API
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) – Sentiment Analysis
- [OpenAI GPT](https://platform.openai.com/) – Language Generation

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/twitter-engageai-bot.git
cd twitter-engageai-bot
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Add Your API Keys

Create a file named `config.py` and paste the following (replace with your keys):

```python
API_KEY = 'your-twitter-api-key'
API_SECRET = 'your-twitter-api-secret'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'
OPENAI_API_KEY = 'your-openai-api-key'
```

---

## ▶️ Running the Bot

To run the bot and reply to mentions automatically:

```bash
python bot.py
```

---

## 🧪 Manual Testing

To manually test how the bot replies to sample inputs without Twitter:

```bash
python test_manual.py
```

---

## 📁 Project Structure

```
├── bot.py                # Main Twitter reply bot
├── config.py             # API keys and credentials
├── test_manual.py        # Manual input testing script
├── sample_dataset.csv    # Optional: dataset for testing or training
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 💡 Future Improvements

- Dashboard for analytics (e.g., sentiment over time)
- RLHF (Reinforcement Learning from Human Feedback)
- CRM integration to track brand-user interactions
- Content planning and tweet scheduling features

---

## 🧠 Inspiration

Built as part of a hackathon under the challenge:

> **"AI Social – Design an AI Community Engagement Bot for Twitter/X"**

The goal: not just automate, but **connect meaningfully** using AI.

---

## 🪪 License

MIT License. Free to use and modify.
