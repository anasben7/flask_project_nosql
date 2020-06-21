from mongoengine import Document
from mongoengine.fields import StringField,FloatField,DateTimeField

class Tweet(Document):
    meta = {'collection': 'tweets'}

    tweet = StringField()
    url = StringField()
    tweet_volume = FloatField()
    Country = StringField()
    as_of=DateTimeField()
    percentage=FloatField()