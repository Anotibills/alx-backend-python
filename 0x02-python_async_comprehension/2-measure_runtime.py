#!/usr/bin/env python3
"""
A coroutine that will execute four times in parallel.
"""

from asyncio import gather, run
from time import time

from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of async_comprehension executed 4 times in parallel.
    '''
    first_time = time()
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    next_time = time()

    return next_time - first_time
