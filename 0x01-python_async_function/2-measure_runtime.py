#!/usr/bin/env python3
"""
function with integers and arguments that measures the total execution time
"""
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


async def run_wait_n(n: int, max_delay: int):
    """Wrapper function to run wait_n."""
    await wait_n(n, max_delay)


def measure_time(n: int, max_delay: int) -> float:
    '''
    Return average execution time for wait_n given `n` and `max_delay`.

    Parameters:
    - n (int): Number of times to run wait_n.
    - max_delay (int): Maximum delay for wait_n.
    - run_func (Callable): Function to run (e.g., asyncio.run).

    Returns:
    - float: Average execution time per call to wait_n.
    '''
    time_0 = time()
    run(run_wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n
