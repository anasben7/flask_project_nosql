from mongoengine import Document
from mongoengine.fields import StringField

class Trend(Document):
    meta = {'collection': 'trends'}

    title = StringField()
    approx_traffic = StringField()
    description = StringField()
    trend_time = StringField()
