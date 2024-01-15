#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    Execute task_wait_random 'n' times and return a sorted list of delays.

    Parameters:
    - n (int): Number of times to execute task_wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: Sorted list of delays.
    '''
    spawn_ls = []
    delay_ls = []

    for _ in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(
            lambda x, delay_list=delay_ls: delay_list.append(x.result())
        )
        spawn_ls.append(delayed_task)
    await asyncio.gather(*spawn_ls)

    return sorted(delay_ls)
