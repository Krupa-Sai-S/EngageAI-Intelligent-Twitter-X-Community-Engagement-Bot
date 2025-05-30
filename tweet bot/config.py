# config.py

from dotenv import load_dotenv
import os
import tweepy
import openai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create the API object
api = tweepy.API(auth)

# Test the authentication
try:
    mentions = api.mentions_timeline(count=5, tweet_mode='extended')
    print(f"Latest mentions: {mentions}")
except tweepy.errors.Unauthorized:
    print("Authentication failed! Please check your tokens.")
