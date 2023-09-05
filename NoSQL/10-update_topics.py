#!/usr/bin/env python3
"""update_topics module"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    query = {"name": name}
    newvalues= {"$set": {"topics": topics}}
    return mongo_collection.update_many(query, newvalues)
