#!/usr/bin/env python3
"""solution"""


def index_range(page: int, page_size: int) -> tuple:
    """Function index_range"""
    x = page - 1
    return (x * page_size, page_size * page)
