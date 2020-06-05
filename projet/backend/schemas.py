import graphene
from flask import Blueprint
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .models.trends import Trend as TrendModel
from .extensions import mongo


class Trend(MongoengineObjectType):
    class Meta:
        model = TrendModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    trends = graphene.List(Trend)
    trds = MongoengineConnectionField(Trend)
    def resolve_trends(self, info):
    	return list(TrendModel.objects.all())

schema = graphene.Schema(query=Query)