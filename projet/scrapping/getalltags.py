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
#db.toptrend.drop()

def generateDate():
    sdate = date(2020, 4, 15)   # start date
    edate = date.today()  # end date

    delta = edate - sdate       # as timedelta
    days=[]
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        days.append(day)
    return days

def fetch_url_test():
    url = f"https://trendogate.com/placebydate/1118108/2015-04-01"
    response = requests.get(url)
    return response.content

def fetch_url(country,date):
    url = f"https://trendogate.com/placebydate/{country}/{date}"
    response = requests.get(url)
    return response.content

def clean(descr):
    descr = descr.replace('&quot;','')
    descr = descr.replace('&#39;','')
    descr = descr.replace('&nbsp;','')
    return descr

def fetch_trends(country,date):
    doc=fetch_url(country,date)
    tmp=[]
    try:
        soup = BeautifulSoup(doc, "html.parser")
        ul = soup.find('ul',{'class':'list-group'})
        lis = ul.findChildren('li' , recursive=False) 
        for li in lis:
            children = li.findChildren("a" , recursive=False)
            for child in children:
                txt=child.text
                tmp.append(txt[1:])
    except :
        return tmp
        print("error Nonetype")
    return tmp

def registerTop(place,country,is_country,code,date):
    tops=fetch_trends(code,date)
    if tops:
        for top in tops:
            print(top)
            db.toptrend.insert_one({"title":top,"place":place,"code":code,"is_country":is_country,"country":country,'date':date})

def getAllplaces():
    collection = db['countries']
    cursor = collection.find({})
    countries={}
    for document in cursor:
        countries[document['name']]={"code":document['code'],"is_country":document['is_country'],"country":document['country']}
    return countries

def getAllTopsTrends():
    countries=getAllplaces()
    days=generateDate()
    for day in days:
        day=str(day)
        for place,value in countries.items():
            if value['is_country']:
                registerTop(place,place,value['is_country'],value['code'],day)
            else :
                registerTop(place,value['country'],value['is_country'],value['code'],day)
            

if __name__ == '__main__':
    getAllTopsTrends()      
    #registerTop("United State",True,'23424977','2020-06-23')
    # if you want to print the result
