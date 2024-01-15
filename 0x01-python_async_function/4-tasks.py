#!/usr/bin/env python3
"""
A new function task_wait_n. except task_wait_random is being called.
"""
from typing import List
import asyncio

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
    task_list = []
    delay_list = []

    # Create a list of tasks
    for _ in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(
            lambda x, delays=delay_list: delays.append(x.result())
        )
        task_list.append(task)

    await asyncio.gather(*task_list)

    return sorted(delay_list)


if __name__ == '__main__':
    print(execute_tasks.__doc__)
    asyncio.run(execute_tasks(3, 4))
