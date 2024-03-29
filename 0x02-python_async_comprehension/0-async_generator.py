#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""

from asyncio import sleep
from random import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields a random value between 0 and 10.
    """
    for i in range(10):
        await sleep(1)
        yield 10 * random()
