import pandas as pd                        
from pytrends.request import TrendReq


def get_keywords(keyword):
    pytrend = TrendReq()
    suggest=[]
    pytrend.build_payload(kw_list=[keyword])
    related_queries = pytrend.related_queries()
    liste=list(related_queries.values())[0]
    for y in liste.values():
        n=y.values.tolist()
        suggest.append(n)

    return suggest
    

def related_topic(keyword):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword])
    related_topic=pytrend.related_topics()
    topics=[]
    liste=list(related_topic.values())[0]
    for y in liste.values():
        n=y.values.tolist()
        topics.append(n)

    return topics


def intrest_by_time(keyword,year_start=2020,year_end=2020):
    pytrend = TrendReq()
    kw_list=[keyword]
    df=pytrend.get_historical_interest(kw_list, year_start=year_start, month_start=1, day_start=1, hour_start=0, year_end=year_end, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
    bf=[df.columns.tolist()] + df.reset_index().values.tolist()
    return bf[1:]

