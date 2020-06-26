import graphene
from flask import Blueprint
from ..models.user import User
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models.trends import Trend as TrendModel
from ..models.tweets import Tweet as TweetModel
from ..models.user import User as UserModel
from ..extensions import mongo
from ..models.keywords import get_keywords,intrest_by_time,related_topic,intrest_by_time2,intrest_by_time3,related_topic2,intrestByCountry
from ..models.keywords import get_keywords,clustring
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    get_raw_jwt,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required
)


class UserObject(MongoengineObjectType):    
    class Meta:
       model = UserModel
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
        user = UserModel.objects(username=username).first()
        if not user:
            raise Exception('Authenication Failure : User is not registered')
        elif user.password==password:
            return AuthMutation(
                access_token = create_access_token(username),
                refresh_token = create_refresh_token(username)
            )
        else :
            raise Exception('Authenication Failure : Credentials are false')

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
    timestamp=graphene.String()

class keywordIntrest(graphene.ObjectType):
    nm=graphene.String()
    intrest=graphene.List(Keyword)

class Dictionnary(graphene.ObjectType):
    key = graphene.String()
    value = graphene.Int()

class Topic(graphene.ObjectType):
    value= graphene.Int()
    formattedvalue=graphene.String()
    link=graphene.String()
    topic_mid = graphene.String()
    topic_title=graphene.String()
    topic_type=graphene.String()
    key=graphene.String()

class DictionnaryTopics(graphene.ObjectType):
    key = graphene.String()
    value = graphene.List(Topic)

class Query(graphene.ObjectType):
    trends = graphene.List(Trend)
    tweets = graphene.List(Tweet,first=graphene.Int())
    trds = MongoengineConnectionField(Trend)
    test = graphene.List(Trend)
    total = graphene.Int()
    total_sentiment= graphene.List(Dictionnary)
    kyrd=graphene.List(Keyword,k=graphene.String())
    kyrd_intrest=graphene.List(Keyword,k=graphene.String(),start=graphene.String(),dend=graphene.String())
    # this trd is not working cz the PyMongo return a dictionary so we will be using the Mongoengine OK
    trd= graphene.List(Trend)
    intrest=graphene.List(keywordIntrest,k=graphene.String(),start=graphene.String(),dend=graphene.String())
    topics=graphene.List(DictionnaryTopics,k=graphene.String())
    intrestbyRegion=graphene.List(Dictionnary,k=graphene.String())
    cluster=graphene.List(Keyword,k=graphene.String())


    def resolve_cluster(self,info,k):
        tmp=clustring(k)
        liste=[]
        for x in tmp:
            liste.append(Keyword(keyword=x))
        return liste

    def resolve_intrestbyRegion(self,info,k):
        tmp=intrestByCountry(k)
        liste=[]
        for x in tmp:
            liste.append(Dictionnary(key=x[0],value=x[1]))
        return liste

    def resolve_topics(self,info,k):
        kyrds=[]
        rlt=related_topic2(k)	
        topics=[]
        for n,x in rlt.items():
            for y in x:	
                kyrds.append(Topic(
                    value= y[1],
                    formattedvalue=y[2],
                    link=y[3],
                    topic_mid = y[4],
                    topic_title=y[5],
                    topic_type=y[6],
                    key=n
                    )
                    )
            topics.append(DictionnaryTopics(key=n,value=kyrds))
            kyrds=[]
        return topics
        
    def resolve_intrest(self,info,k,start,dend):
        kyrds=[]
        words=[]
        intrest=[]
        startdate=start.split("-")
        enddate=dend.split("-")
        words=k.split(",")
        rlt=intrest_by_time3(words[0:4],startdate,enddate)
        for key,value in rlt.items():
            for x in value:
                kyrds.append(Keyword(timestamp=x[0],value=x[1]))
            intrest.append(keywordIntrest(nm=key,intrest=kyrds))
            kyrds=[]
        return intrest

    def resolve_kyrd(self,info,k):
        kyrds=[]
        rlt=get_keywords(k)	
        tp="Top"	
        for x in rlt:	
            for y in x:	
                kyrds.append(Keyword(y[0],y[1],tp))	
            tp="Rising"     	
        return kyrds

    def resolve_kyrd_intrest(self,info,k,start="2020",dend="2020"):
        kyrds=[]
        startdate=start.split("-")
        enddate=dend.split("-")
        rlt=intrest_by_time(k)	
        for x in rlt:
            kyrds.append(Keyword(timestamp=x[0],value=x[1]))	
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
            else:
                 x.percentage=0   
        return tweets[0:first]
    
    #helper fuction to return to graphql total type " calculate total of traffic"
    def resolve_total(self, info):
        trends=list(TrendModel.objects.all())
        total=0
        for x in trends:
            traffic=x['approx_traffic'][:-1].replace(',','')
            total+=int(traffic)
        trends.append(total)
        return total

    def resolve_total_sentiment(self, info):
        trends=list(TrendModel.objects.all())
        total_positive=0
        total_negative=0
        for descr in trends:     
            descr_content=descr['description']
            blob_test=TextBlob(descr_content)
            if blob_test.sentiment.polarity > 0 :
                descr.etat="positive"
                total_positive += 1
            else : 
                total_negative += 1

        return [Dictionnary("Positive",total_positive),Dictionnary("Negative",total_negative)]

    def resolve_trd(self, info):
        trends=list(TrendModel.objects.all())
        doc=[]
        total=0
        positivity = 0
        negativity = 0
        etat=" "
        for descr in trends:  
            descr_content=descr['description']
            doc.append(descr.description)
            blob_test=TextBlob(descr_content)
            if blob_test.sentiment.polarity > 0 :
                descr.etat="positive"
                positivity += 1
            else : 
                negativity += 1
                descr.etat="negative"    
        
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(doc)
        true_k = 4
        model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
        model.fit(X)
        print("Top terms per cluster:")
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        for i in range(true_k):
            print("Cluster %d:" % i),
            for ind in order_centroids[i, :10]:
                print(' %s' % terms[ind])

        print("\n")
        print("Prediction")

        Y = vectorizer.transform(["Justin"])
        prediction = model.predict(Y)
        print(prediction)
        

        return trends
    

schema = graphene.Schema(query=Query, mutation=Mutation)
