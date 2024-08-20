#!/usr/bin/env python3
"""solution"""


def index_range(page: int, page_size: int) -> tuple:
    """Function index_range"""
    return ((page - 1) * page_size, page_size * page)
