#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Execute task_wait_random 'n' times and return a sorted list of delays.

    Parameters:
    - n (int): Number of times to execute task_wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: Sorted list of delays.
    '''
    modified_random = __import__('3-tasks').task_wait_random

    delay_list = []

    for _ in range(n):
        delay_list.append(await modified_random(max_delay))

    return sorted(delay_list)


if __name__ == '__main__':
    import asyncio

    print(task_wait_n.__doc__)
    print(asyncio.run(task_wait_n(3, 4)))
