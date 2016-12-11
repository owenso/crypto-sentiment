from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import sys
import tweepy
from tweepy import OAuthHandler

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search, q=sys.argv[1], count=100,lang="en").items(5):
        print (tweet.created_at, tweet.text)

