import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import date, timedelta
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import json
import tweepy

client = MongoClient('127.0.0.1', 27017)
db = client.test1
countries={}
db.countries.drop()

def fetch_places_url(code):
    url = f"https://trendogate.com/place/{code}"
    response = requests.get(url)
    return response.content

def fetch_countries_url():
    url = f"https://trendogate.com/placeslist"
    response = requests.get(url)
    return response.content


def fetch_countries():
    doc = fetch_countries_url()
    soup = BeautifulSoup(doc, "html.parser")
    ul = soup.find('ul',{'class':'list-group'})
    lis = ul.findChildren('li' , recursive=False)
    tmp={}
    for li in lis:
        children = li.findChildren("a" , recursive=False)
        for child in children:
            tmp[child.text[5:]]=child['href'].replace('/place/','')

    return tmp



def fetch_places(code):
    doc=fetch_places_url(code)
    soup = BeautifulSoup(doc, "html.parser")
    uls = soup.find_all('ul',{'class':'list-group'})
    ul=None
    for ul in uls:
        pass
    lis = ul.findChildren('li' , recursive=False)
    tmp={}
    for li in lis:
        children = li.findChildren("a" , recursive=False)
        for child in children:
            tmp[child.text[1:]]=child['href'].replace('/place/','')

    return tmp

def registerCountries():
    countries=fetch_countries()
    for country,code in countries.items():
        db.countries.insert_one({"name":country,"code":code,"is_country":True,"country":''})

def registerplaces(country,code):
    places=fetch_places(code)
    for place,code in places.items():
        db.countries.insert_one({"name":place,"code":code,"is_country":False,"country":country})

def getAllplaces():
    countries=fetch_countries()
    for country,code in countries.items():
        registerplaces(country,code)

def cleanDatabase():
    myquery = { "code": {"$regex": "^/"} }
    mycol = db["countries"]
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")


if __name__ == '__main__':
    countries=fetch_countries()
    registerCountries()
    getAllplaces()
    cleanDatabase()

