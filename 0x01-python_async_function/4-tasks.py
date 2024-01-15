#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List, Any
import asyncio
import random
my_module = __import__('3-tasks')
task_wait_random = my_module.task_wait_random


async def execute_tasks(n: int, max_delay: int = 10) -> List[float]:
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
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
