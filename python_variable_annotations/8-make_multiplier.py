#!/usr/bin/env python3
"""solution"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """function make_multiplier"""

    def mul(i: float) -> float:
        return i * multiplier

    return mul
