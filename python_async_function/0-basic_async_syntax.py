#!/usr/bin/env python3
"""solution"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
