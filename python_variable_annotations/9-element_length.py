#!/usr/bin/env python3
"""solution"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function element_length"""
    return [(i, len(i)) for i in lst]
