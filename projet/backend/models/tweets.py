from mongoengine import Document
from mongoengine.fields import StringField

class Tweet(Document):
    meta = {'collection': 'tweets'}

    tweet = StringField()
    url = StringField()
    tweet_volume = StringField()
    Country = StringField()
    as_of=StringField()