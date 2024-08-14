#!/usr/bin/env python3
"""solution"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """function sum_mixed_list"""
    sum = 0
    for i in mxd_lst:
        sum = i + sum
    return sum
