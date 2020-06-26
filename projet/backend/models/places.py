from mongoengine.fields import StringField,FloatField,DateTimeField,BooleanField
from mongoengine import *

connect("projet", host="mongodb://localhost:27017/test1", alias="default")

class Places(Document):
    meta = {'collection': 'countries'}

    _id = StringField()
    name = StringField()
    code = StringField()
    Country = StringField()
    is_country=BooleanField()
    
    @queryset_manager
    def get(doc_cls, queryset,c):
        return queryset.filter(country=c)

print(Places.get("United States"))
