#!/usr/bin/env python3
"""log_stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
   
    count_logs = collection.count_documents({})
    print(f"{count_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_methods = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_methods}")

    status = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status} status check")
