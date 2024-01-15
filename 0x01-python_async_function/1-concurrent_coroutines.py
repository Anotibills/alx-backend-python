#!/usr/bin/env python3
"""
A function that creates integers n and max_delay as arguments, the return total
"""
import asyncio
from typing import List
from typing_extensions import Literal
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    This waits for random delays, then returns list of actual delays.

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
