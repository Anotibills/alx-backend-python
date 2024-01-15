#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument and returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Async function that waits for random amount of time up

    Parameters:
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - float: Actual delay that occurred.
    '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
