from mongoengine import Document, ReferenceField, ListField
from mongoengine.fields import StringField


    
class User(Document):
    meta = {'collection': 'users'}
    username = StringField()
    password = StringField()
    email = StringField()

    

