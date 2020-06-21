import pandas as pd                        
from pytrends.request import TrendReq
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test1
pytrend = TrendReq()


pytrend.build_payload(kw_list=['Taylor Swift'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)
print(df.shape)
df.reset_index().plot(x='geoName', y='Taylor Swift', figsize=(120, 10), kind ='bar')

df = pytrend.trending_searches(pn='united_states')
df = pytrend.today_searches(pn='US')

print(df)

keywords = pytrend.suggestions(keyword='Car')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid') 

print(df)
kw_list=['FSTT']
pytrend.build_payload(kw_list=['Car'])
related_queries = pytrend.related_queries()
related_queries.values()

print(related_queries.values())

related_topic = pytrend.related_topics()
print(related_topic.values())

idk = pytrend.interest_over_time()
print(idk)
print("laaast one ")
print(pytrend.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0))
