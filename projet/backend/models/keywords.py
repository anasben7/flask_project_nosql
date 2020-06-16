from mongoengine import Document
from mongoengine.fields import StringField


class Keyword():
    name=StringField()
    keyword=StringField()
    country=StringField()
        

