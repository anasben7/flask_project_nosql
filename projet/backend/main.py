from flask import Blueprint
from .extensions import mongo
import json

main= Blueprint('main',__name__)

@main.route('/')
def get():
    curs=mongo.db.trends
    trends = curs.find()
    response = []
    for document in trends:
        document['_id'] = str(document['_id'])
        response.append(document)

    return json.dumps(response)