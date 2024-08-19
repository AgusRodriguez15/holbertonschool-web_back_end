#!/usr/bin/env python3
"""solution"""


import typing
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """function task_wait_n"""

    delay_list = []
    tasks = []

    async def adder(delay):
        """function adder"""
        delay_list.append(await task_wait_random(delay))

    for _ in range(n):
        tasks.append(asyncio.create_task(adder(max_delay)))

    for task in tasks:
        await task

    return delay_list
