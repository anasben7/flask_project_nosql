from flask import Blueprint
from .extensions import mongo
import json
from bson import json_util

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

# @main.route('/tweets')
# def get():
#     curs=mongo.db.tweets
#     tweets = curs.find()
#     response = []
#     for document in tweets:
#         document['_id'] = str(document['_id'])
#         response.append(document)

#     return json.dumps(response,indent=4, sort_keys=True, default=str)       

