#!/usr/bin/env python3
"""solution"""


def sum_list(input_list) -> float:
    """function sum_list"""
    sum = 0
    for i in input_list:
        sum = i + sum
    return sum
