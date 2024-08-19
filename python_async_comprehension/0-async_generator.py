#!/usr/bin/env python3
"""solution"""

import random
import asyncio


async def async_generator ():
    i = random.randit(0, 10)
    for i in range(10):
        await asyncio.sleep(1)
        yield i 