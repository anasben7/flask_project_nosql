import pandas as pd                        
from pytrends.request import TrendReq
from pymongo import MongoClient

pytrend = TrendReq()


pytrend.build_payload(kw_list=['Football'])
# Interest by Region
df = pytrend.interest_by_region(resolution='COUNTRY',inc_low_vol=True)
bf=df.reset_index().values.tolist()[0:]
print(df)
