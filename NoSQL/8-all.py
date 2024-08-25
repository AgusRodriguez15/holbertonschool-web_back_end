#!/usr/bin/env python3
"""solution"""
import pymongo


def list_all(mongo_collection):
    """lists_all"""
    if not mongo_collection:
        return []
    else:
        return list(mongo_collection.find())
