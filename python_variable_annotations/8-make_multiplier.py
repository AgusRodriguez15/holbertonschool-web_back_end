#!/usr/bin/env python3
"""solution"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier"""
    def mul(multiplier: float) -> float:
        return multiplier * multiplier
    return mul
