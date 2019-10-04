import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_authentication():
    
    try:
        twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        twitter_consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
        twitter_access_secret = os.environ['TWITTER_ACCESS_SECRET']

    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)

    return auth

def get_twitter_client():
    
    auth = get_twitter_authentication()
    client = API(auth)
	
    return client
