#!/usr/bin/env python3
"""solution"""

import random
import asyncio


async def async_generator ():
    await asyncio.sleep(1)
    i =random.sample(range(0, 10), 10)
    yield i