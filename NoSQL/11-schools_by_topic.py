#!/usr/bin/env python3
"""schools_by_topic module"""



def schools_by_topic(mongo_collection, topic):
    """returns the list of schools having a specific topic"""
    schools_list = []
    query =  mongo_collection.find({"topic": topic})
    for school in query:
        schools_list.append(school)
    return schools_list
