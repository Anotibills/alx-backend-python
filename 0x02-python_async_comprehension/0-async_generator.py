#!/usr/bin/env python3
"""
a coroutine called async_generator that takes no arguments.
"""
from asyncio import sleep
from random import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Asynchronous generator that yields a random value between 0 and 10 every
    '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()


async def main():
    async for value in async_generator():
        print(value)

import asyncio
asyncio.run(main())