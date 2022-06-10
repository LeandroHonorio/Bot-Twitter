import config
import tweepy
from os import environ


# API_KEY = config.API_KEY
# API_SECRET = config.API_SECRET
# BEARER_TOKEN = config.BEARER_TOKEN
# ACCESS_TOKEN = config.ACCESS_TOKEN
# ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET


API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
BEARER_TOKEN = environ['BEARER_TOKEN']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

def api_v1_oauth1():
    """ V1.1 authentication - OAuth 1.0a User Context"""
    auth = tweepy.OAuth1UserHandler(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
        )
    api = tweepy.API(auth)
    return api

def api_v2_oauth1():
    """ V2 authentication - OAuth 1.0a User Context"""
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
        )
    return client

def api_v2_oauth2():
    """ API V2 - OAuth 2.0 Bearer Token (App-Only) """
    client = tweepy.Client(config.BEARER_TOKEN)
    return client