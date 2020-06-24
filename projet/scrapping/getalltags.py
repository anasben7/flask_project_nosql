import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import json
import tweepy
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test1

#Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "4518193835-XGOBCZibmnUdgkPZM3CGLL6JFKqoAktx1VimWYD"
ACCESS_TOKEN_SECRET = "GQrGPwhJehHwhQiw7pTC4CzXMioRLBFNWSpiwqIzkZAjA"
CONSUMER_KEY = "XRuZQD2Sq8Ojtvo3dbe1Z2U0M"
CONSUMER_SECRET = "FRjWoFHTSxWKIYfRZCsifD6jRJRjTJBunet8JUj4pJOiZp2y4x"

countries={}

def clean_tweets(x):
    x = x.replace('#','')
    return x

def replace_null(x):
    if x is None:
        x=0 
    return x

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tags = api.trends_available()
print(tags[0])

for x in tags:
    countries[x['name']]=[x['woeid'],x['country'],x['countryCode']]

for key,value in countries.items():
    db.places.insert_one({"name":key,"woeid":value[0],"country":value[1],"countryCode":value[2]})

for key,value in countries.items():
    tags = api.trends_place(value[0])
    if value[1]=='':
        value[1]=key
        key=''
    for a in tags :
        for b in a["trends"]:
            db.tweets.insert_one({"tweet":clean_tweets(b["name"]),"url":b["url"],"tweet_volume":replace_null(b["tweet_volume"]),"place":key,"Country":value[1],"as_of":datetime.datetime.now()})
