import pandas as pd                        
from pytrends.request import TrendReq

pytrend = TrendReq()

def get_keywords(keyword):
    suggest=[]
    pytrend.build_payload(kw_list=[keyword])
    related_queries = pytrend.related_queries()
    liste=list(related_queries.values())[0]
    for y in liste.values():
        n=y.values.tolist()
        suggest.append(n)

    return suggest
    
