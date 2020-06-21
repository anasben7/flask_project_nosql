from flask import Blueprint
from .extensions import mongo
import json
from bson import json_util
from flask import render_template
import atexit
from apscheduler.scheduler import Scheduler

main= Blueprint('main',__name__)

cron = Scheduler(daemon=True)


@main.route('/')
def index():
   return render_template("index.html")

# @main.route('/tweets')
# def get():
#     curs=mongo.db.tweets
#     tweets = curs.find()
#     response = []
#     for document in tweets:
#         document['_id'] = str(document['_id'])
#         response.append(document)

#     return json.dumps(response,indent=4, sort_keys=True, default=str)       

