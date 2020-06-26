from mongoengine import *
from mongoengine.fields import StringField,FloatField,DateTimeField,BooleanField
from datetime import datetime

connect("projet", host="mongodb://localhost:27017/test1", alias="default")

class TweetArchive(Document):
    meta = {'collection': 'toptrend'}

    _id = StringField()
    title = StringField()
    place = StringField()
    country = StringField()
    code = StringField()
    is_country=BooleanField()
    date=StringField()

    @queryset_manager
    def get(doc_cls, queryset,page,number,dates,code):
        kwargs = {}
        start=dates[0]
        end=dates[1]
        if code=="":
            places = TweetArchive.objects(__raw__={"date": { "$gte":start,"$lte": end}})[(page-1)*number:page*number]
        else :
            places = TweetArchive.objects(__raw__={"date": { "$gte":start,"$lte": end},"code":code})[(page-1)*number:page*number]
        return places
    
    @queryset_manager
    def getCount(doc_cls, queryset,dates,code):
        kwargs = {}
        start=dates[0]
        end=dates[1]
        if code=="":
            count = TweetArchive.objects(__raw__={"date": { "$gte":start,"$lte": end}}).count()
        else :
            count = TweetArchive.objects(__raw__={"date": { "$gte":start,"$lte": end},"code":code}).count()
        return count

print(TweetArchive.get(2,20,["2020-01-01","2020-01-03"],""))

