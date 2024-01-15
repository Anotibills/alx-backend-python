#!/usr/bin/env python3
"""
function task_wait_random that takes an integer and returns a asyncio.Task
"""
import asyncio
from typing import Any


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    This creates and returns an asyncio.Task object for wait_random.

    Parameters:
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - asyncio.Task[float]: Task object representing async execution.
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    max_delay = 5
    task = task_wait_random(max_delay)
    print(f'Task created: {task.__class__}')
