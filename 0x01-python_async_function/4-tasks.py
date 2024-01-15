#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    Execute task_wait_random 'n' times and return a sorted list of delays.

    Parameters:
    - n (int): Number of times to execute task_wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: Sorted list of delays.
    '''
    tasks = []

    delay_list = []

    for _ in range(n):
        task = task_wait_random(max_delay)

        task.add_done_callback(lambda x: delay_list.append(x.result()))

        tasks.append(task)

    await asyncio.gather(*tasks)

    return sorted(delay_list)
