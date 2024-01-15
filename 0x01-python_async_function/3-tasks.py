#!/usr/bin/env python3
"""
function task_wait_random that takes an integer and returns a asyncio.Task
"""
import asyncio


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
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
    return asyncio.create_task(wait_random(max_delay))
