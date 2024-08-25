#!/usr/bin/env python3
"""solution"""


def list_all(mongo_collection):
    """list_all"""
    if not mongo_collection:
        return []
    else:
        return list(mongo_collection.find())
