import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import tweepy
import time
import seaborn as sns
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "iYisNscmJz071KRSMNevSFwEK"
consumer_secret = "60mFgvKBgrYZjEfhCkAaTm6jEYq3iDBdrnF11AeEgoC5GtR0Jn"
access_token = "2513453952-mkhs7Urv559Bzt6DVquYiFXriIuO7XJ3YHBlWde"
access_token_secret = "srNiXKJaABUz1FyHD15eKnYv6BnsiWYkqvjvO4ekxXW6H"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Account
#target = "@CNN"
target_terms = ("@BBCWorld", "@CNN", "@FoxNews",
                "@CBSNews", "@nytimes")

# Counter
counter = 1

# Variables for holding sentiments
source_sentiments = []

# Loop through 5 pages of tweets (total 100 tweets)
for target in target_terms:
  sentiments = []
  # Get all tweets from home feed
  public_tweets = api.user_timeline(target, count=100)

  # Loop through all tweets
  for tweet in public_tweets:

    # Print Tweets
    # print("Tweet %s: %s" % (counter, tweet["text"]))

    # Run Vader Analysis on each tweet
    compound = analyzer.polarity_scores(tweet["text"])["compound"]
    pos = analyzer.polarity_scores(tweet["text"])["pos"]
    neu = analyzer.polarity_scores(tweet["text"])["neu"]
    neg = analyzer.polarity_scores(tweet["text"])["neg"]
    tweets_ago = counter

    # Add sentiments for each tweet into an array
    sentiments.append({"Date": tweet["created_at"],
                       "Compound": compound,
                       "Positive": pos,
                       "Negative": neu,
                       "Neutral": neg,
                       "Tweets Ago": counter,
                       "Target": target})

    # Add to counter
    counter = counter + 1

  source_sentiments.append(sentiments)
#prt_this = sentiments[0]
# print(sentiments[4])
# print(len(sentiments[4]))

sentiment_dataframes = []

for sentiments in source_sentiments:
  # to do: set the color of the target points

  sentiments_pd = pd.DataFrame(sentiments)
  # print(sentiments)
  target = ""
  time = ""
  for sentiment in sentiments:
    print(sentiment)
    target = sentiment['Target']
    time = sentiment['Date']
    sentiments_pd.append(sentiments)

 # sentiment_dataframes.append(sentiments_pd)

# for df in sentiment_dataframes:

#print(sentiments_pd['Tweets Ago'].head())
  plt.scatter(np.arange(len(sentiments_pd["Compound"])),
              sentiments_pd["Compound"], marker="o", linewidth=0.5, alpha=0.8)

# # Incorporate the other graph properties
  plt.title("Sentiment Analysis of News Tweets 03/07/18")
  plt.ylabel("Tweet Polarity")
  plt.xlabel("Tweets Ago")
plt.legend(target_terms)
plt.show()

#y = np.arange(sentiments_pd['Compound'])
#N = len(y)
#x = len(y)
#width = 1/1.5
#plt.bar(x, y, width, color="blue")
#plt.show()
 
