#!/usr/bin/env python3
"""solution"""

import random
import asyncio


async def async_generator ():
    yield random.random()
    await asyncio.sleep(1)
    for i in range(10):
        yield i == random.random()