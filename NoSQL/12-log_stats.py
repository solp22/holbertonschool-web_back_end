#!/usr/bin/env python3
"""log_stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx
    gets = collection.count_documents({"method": "GET"})
    posts = collection.count_documents({"method": "POST"})
    puts = collection.count_documents({"method": "PUT"})
    patches = collection.count_documents({"method": "PATCH"})
    deletes = collection.count_documents({"method": "DELETE"})
    status = collection.count_documents({"method": "GET"}, 
                                        {"path": "/status"})

    print (f"{collection.count_documents({})} logs")
    print ("Methods:")
    print (f"\tmethod GET: {gets}")
    print (f"\tmethod POST: {posts}")
    print (f"\tmethod PUT: {puts}")
    print (f"\tmethod PATCH: {patches}")
    print (f"\tmethod DELETE: {deletes}")
    print (f"{status} status check")
