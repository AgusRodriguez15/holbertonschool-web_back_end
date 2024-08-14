#!/usr/bin/env python3
"""solution"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list"""
    sum = 0
    for i in input_list:
        sum = i + sum
    return sum
