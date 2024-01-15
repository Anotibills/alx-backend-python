#!/usr/bin/env python3
"""
function with integers and arguments that measures the total execution time
"""
from time import time
from typing import Callable
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int, run_func: Callable) -> float:
    '''
    Return average execution time for wait_n given `n` and `max_delay`.

    Parameters:
    - n (int): Number of times to run wait_n.
    - max_delay (int): Maximum delay for wait_n.
    - run_func (Callable): Function to run (e.g., asyncio.run).

    Returns:
    - float: Average execution time per call to wait_n.
    '''
    total_time = 0

    for _ in range(n):
        time_0 = time()
        run_func(wait_n(1, max_delay))
        time_1 = time()
        elapsed_time = time_1 - time_0
        total_time += elapsed_time

    return total_time / n
