#!/usr/bin/env python3
"""solution"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function measure_runtime"""
    start = time.time()
    result = await asyncio.gather(
        *[async_comprehension() for i in range(4)]
    )
    end = time.time()
    return end - start
