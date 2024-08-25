#!/usr/bin/env python3
"""solution"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic"""

    return [doc for doc in mongo_collection.find()
            if (topics := doc.get('topics')) and topic in topics]
