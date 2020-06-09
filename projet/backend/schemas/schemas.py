import graphene
from flask import Blueprint
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models.trends import Trend as TrendModel
from ..extensions import mongo

class Trend(MongoengineObjectType):
    class Meta:
        model = TrendModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    trends = graphene.List(Trend)
    trds = MongoengineConnectionField(Trend)
    test = graphene.List(Trend)
    total = graphene.Int()
    # this trd is not working cz the PyMongo return a dictionary so we will be using the Mongoengine OK
    trd= graphene.List(Trend)
    
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