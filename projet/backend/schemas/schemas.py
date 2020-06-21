import graphene
from flask import Blueprint
from ..models.user import User
from textblob import TextBlob
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models.trends import Trend as TrendModel
from ..models.tweets import Tweet as TweetModel
from ..extensions import mongo
from ..models.keywords import get_keywords
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required
)


class UserObject(MongoengineObjectType):    
    class Meta:
       model = User
       interfaces = (graphene.relay.Node, )


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserObject)

    class Arguments:
        username =graphene.String(required=True)
        password =graphene.String(required=True)
        email =graphene.String(required=True)

    def mutate(self, info, username, password , email):
        user = User(username=username,password=password,email=email)
        user.save()
        return CreateUser(user)

class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info , username, password) :
        user = User(username=username,password=password)
        print(user)
        if not user:
            raise Exception('Authenication Failure : User is not registered')
        return AuthMutation(
            access_token = create_access_token(username),
            refresh_token = create_refresh_token(username)
        )

class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))

class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    create_user = CreateUser.Field()
    refresh = RefreshMutation.Field()




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
    
    # def resolve_trd(self, info):
    #     return mongo.db.trends.find()
        
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
    def resolve_trd(self, info):
        trends=list(TrendModel.objects.all())
        total=0
        positivity = 0
        negativity = 0
        etat=" "


        for descr in trends:
            
            descr_content=descr['description']
            blob_test=TextBlob(descr_content)
            if blob_test.sentiment.polarity > 0 :
                descr.etat="positive"
                positivity += 1
            else : 
                negativity += 1
                descr.etat="negative"

                


        return trends

schema = graphene.Schema(query=Query, mutation=Mutation)
