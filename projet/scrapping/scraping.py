import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test1


def fetch_url(country):
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={country}"
    response = requests.get(url)
    return response.content

def fetch_trends(country):
    doc = fetch_url(country)
    soup = BeautifulSoup(doc, "html.parser")
    titles = soup.find_all("title")
    descriptions=soup.find_all("description")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    trend_dates = soup.find_all("pubdate")
    
    for title, traffic, description, trend_date in zip(titles[1:], approximate_traffic, descriptions[1:], trend_dates):
        db.trends.insert_one({"title":title.text,"approx_traffic":traffic.text, "description":description.text, "trend_time":trend_date.text })

    
    return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}

def fetch_trends2(country):
    doc = fetch_url(country)
    soup = BeautifulSoup(doc, "html.parser")
    titles = soup.find_all("title")
    descriptions=soup.find_all("description")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    trend_dates = soup.find_all("pubdate")

    
    return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}


if __name__ == '__main__':
    trends = fetch_trends("US")
    # if you want to print the result
    print(trends)