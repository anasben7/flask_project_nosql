import pandas as pd                        
from pytrends.request import TrendReq


pytrends = TrendReq()

df=pytrends.trending_searches(pn='united_states')
print(df)