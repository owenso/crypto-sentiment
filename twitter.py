from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import sys
import tweepy
import time
from tweepy import OAuthHandler
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)['compound']
    return snt

custom_negative_words = ["sell", "tanked", "tanking"]
custom_positive_words = ["moon", "lambo", "mooon", "mooning", "moooon", "fuck yeah", "buy", "ath"]


total_score = 0
num_returned = 0

for tweet in tweepy.Cursor(api.search, q="$IOTA", count=100, lang="en", result_type='recent').items(100):
        num_returned = num_returned + 1
        # print("-------------------------")
        # print(tweet.text)
        if any(ext in tweet.text.lower() for ext in custom_negative_words):
                # print("bad")
                total_score = total_score + -1
        elif any(ext in tweet.text.lower() for ext in custom_positive_words):
                # print("good")
                total_score = total_score + 1
        else:
                # print(print_sentiment_scores(tweet.text))
                total_score = total_score + print_sentiment_scores(tweet.text)
        # print("-------------------------")


print(total_score/num_returned)
