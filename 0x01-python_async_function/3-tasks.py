#!/usr/bin/env python3
"""
function task_wait_random that takes an integer and returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int = 10) -> asyncio.Task[float]:
    '''
    This creates and returns an asyncio.Task object for wait_random.

    Parameters:
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - asyncio.Task[float]: Task object representing async execution.
    '''
    return asyncio.create_task(wait_random(max_delay))
