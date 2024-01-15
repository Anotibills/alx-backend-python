#!/usr/bin/env python3
"""
function task_wait_random that takes an integer and returns a asyncio.Task
"""
import asyncio
from 0-basic_async_syntax import wait_random


async def task_wait_random(max_delay: int = 10) -> asyncio.Task[float]:
    '''
    Creates and returns an asyncio.Task object for wait_random.

    Parameters:
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - asyncio.Task[float]: Task object representing asyncexecution of wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))