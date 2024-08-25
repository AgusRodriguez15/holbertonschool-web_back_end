#!/usr/bin/env python3
"""Solution"""


def list_all(mongo_collection):
    """list_all"""
    return [doc for doc in mongo_collection.find()]
