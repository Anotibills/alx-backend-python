#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.
"""
from typing import List

from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    '''
    Return list of values yielded by async_generator.
    '''
    return [value async for value in async_generator()]
