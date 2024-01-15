#!/usr/bin/env python3
"""

"""
import asyncio
from typing import List
from 0-basic_async_syntax.py import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for random delays up to max_delay 'n' times, returns list of actual delays.

    Parameters:
    - n (int): Number of delays to wait for.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: List of actual delays that occurred.
    """
    tasks = []

    delay_list = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))

        task.add_done_callback(lambda x: delay_list.append(x.result()))

        tasks.append(task)

    await asyncio.gather(*tasks)

    return delay_list
