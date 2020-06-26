from mongoengine.fields import StringField,FloatField,DateTimeField,BooleanField
from mongoengine import *

connect("projet", host="mongodb://localhost:27017/test1", alias="default")

class Places(Document):
    meta = {'collection': 'countries'}

    _id = StringField()
    name = StringField()
    code = StringField()
    country = StringField()
    is_country=BooleanField()
    
    @queryset_manager
    def get(doc_cls, queryset,c):
        return queryset.filter(country=c)
    @queryset_manager
    def getCountries(doc_cls, queryset):
        return queryset.filter(is_country=True)
    

