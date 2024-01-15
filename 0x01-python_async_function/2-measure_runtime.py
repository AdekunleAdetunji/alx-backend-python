#!/usr/bin/env python3
"""
This module contains an async coroutine function
"""
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A functions that measures the total execution time for wait_n(n, max_delay)

    Args:
        n: The first positional argument to be supplied to wait_n function
        max_delay: The second position argument to be supplied to the wait_n
            function
    Return: total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed/n
