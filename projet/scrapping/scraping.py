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


def clean(descr):
    descr = descr.replace('&quot;','')
    descr = descr.replace('&#39;','')
    descr = descr.replace('&nbsp;','')
    return descr


def fetch_trends(country):
    doc = fetch_url(country)
    soup = BeautifulSoup(doc, "html.parser")

    for item in soup.find_all("item"):
        title=item.title
        approx_traffic=item.contents[3]
        description=item.contents[15]
        trend_time=item.pubdate
        db.trends.insert_one({"title":title.text,"approx_traffic":approx_traffic.text, "description":clean(description.contents[3].text), "trend_time":trend_time.text })

    approximate_traffic = soup.find_all("ht:approx_traffic")
    titles = soup.find_all("title")
    

    
    return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}




if __name__ == '__main__':
    trends = fetch_trends("US")
    # if you want to print the result
    print(trends)