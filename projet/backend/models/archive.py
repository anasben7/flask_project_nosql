from mongoengine import Document
from mongoengine.fields import StringField,FloatField,DateTimeField,BooleanField

class TweetArchive(Document):
    meta = {'collection': 'toptrend'}

    _id = StringField()
    title = StringField()
    place = StringField()
    Country = StringField()
    is_country=BooleanField()
    date=DateTimeField()
