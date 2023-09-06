#!/usr/bin/env python3
"""log_stats module"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx
gets = collection.find({"method": "GET"}).count()
posts = collection.find({"method": "POST"}).count()
puts = collection.find({"method": "PUT"}).count()
patches = collection.find({"method": "PATCH"}).count()
deletes = collection.find({"method": "DELETE"}).count()
status = collection.find({"method": "GET"}, 
                         {"path": "/status"}).count()


print (f"{collection.find().count()} logs")
print ("Methods:")
print (f"\tmethod GET: {gets}")
print (f"\tmethod POST: {posts}")
print (f"\tmethod PUT: {puts}")
print (f"\tmethod PATCH: {patches}")
print (f"\tmethod DELETE: {deletes}")
print (f"{status} status check")
