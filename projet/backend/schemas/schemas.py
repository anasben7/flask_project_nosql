import graphene
from flask import Blueprint
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models.trends import Trend as TrendModel
from ..models.tweets import Tweet as TweetModel
from ..extensions import mongo
from ..models.keywords import get_keywords

class Trend(MongoengineObjectType):
    class Meta:
        model = TrendModel
        interfaces = (Node,)
        
class Tweet(MongoengineObjectType):
    class Meta:
        model = TweetModel
        interfaces = (Node,)

class Keyword(graphene.ObjectType):
    keyword=graphene.String()
    value=graphene.Int()
    tp=graphene.String()

class Query(graphene.ObjectType):
    trends = graphene.List(Trend)
    tweets = graphene.List(Tweet,first=graphene.Int())
    trds = MongoengineConnectionField(Trend)
    test = graphene.List(Trend)
    total = graphene.Int()
    kyrd=graphene.List(Keyword,k=graphene.String())
    # this trd is not working cz the PyMongo return a dictionary so we will be using the Mongoengine OK
    trd= graphene.List(Trend)

    def resolve_kyrd(self,info,k):
        kyrds=[]
        rlt=get_keywords(k)
        tp="Top"
        for x in rlt:
            for y in x:
                kyrds.append(Keyword(y[0],y[1],tp))
            tp="Rising"     
        return kyrds

    def resolve_tweets(self, info,first):
        tweets=list(TweetModel.objects.all())
        total=0
        for x in tweets:
            t=x.tweet_volume
            if t is not None:
                total+=t

        for x in tweets:
            if x.tweet_volume is not None:
                x.percentage=(x.tweet_volume*100.0/total)
        print(type(tweets))
        return tweets[0:first]
    
    def resolve_trd(self, info):
        return mongo.db.trends.find()
        
    #helper fuction to return to graphql total type " calculate total of traffic"
    def resolve_total(self, info):
        trends=list(TrendModel.objects.all())
        total=0
        for x in trends:
            traffic=x['approx_traffic'][:-1].replace(',','')
            total+=int(traffic)
            print(int(traffic))
            print("total is : ",total)
        trends.append(total)
        return total
    #helper fuction to return to graphql test type
    def resolve_test(self, info):
        trends=list(TrendModel.objects.all())
        total=0
        for x in trends:
            traffic=x['approx_traffic'][:-1].replace(',','')
            total+=int(traffic)
            print(int(traffic))
            print("total is : ",total)
        return trends

schema = graphene.Schema(query=Query)