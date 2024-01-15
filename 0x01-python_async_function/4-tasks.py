#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List, Any
import asyncio


async def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Execute task_wait_random 'n' times and return a sorted list of delays.

    Parameters:
    - n (int): Number of times to execute task_wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: Sorted list of delays.
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[Any]:
    '''
    This Runs an async function for n times and adds the results into a list
    '''
    task_wait_random_func = task_wait_random
    delay_list = []

    for _ in range(n):
        delay_list.append(await task_wait_random_func(max_delay))

    return sorted(delay_list)


if __name__ == '__main__':
    print(task_wait_n.__doc__)
    asyncio.run(task_wait_n(3, 4))
