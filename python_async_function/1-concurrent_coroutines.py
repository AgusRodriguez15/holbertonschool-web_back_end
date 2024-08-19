#!/usr/bin/env python3
"""solution"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """function async wain_n"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
