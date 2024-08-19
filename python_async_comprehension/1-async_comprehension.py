#!/usr/bin/env python3
"""solution"""

import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> None:
    """function async_comprehension"""
    lst = [i async for i in async_generator() if i % 2]
    return lst
