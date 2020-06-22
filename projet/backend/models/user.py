from mongoengine import Document, ReferenceField, ListField
from mongoengine.fields import StringField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

class User(Document):
    meta = {'collection': 'users'}
    username = StringField()
    password = StringField()
    email = StringField()

    

