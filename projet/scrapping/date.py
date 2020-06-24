from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test1
collection = db['places']
cursor = collection.find({})
countries={}
for document in cursor:
    countries[document['name']]=document['wo']

