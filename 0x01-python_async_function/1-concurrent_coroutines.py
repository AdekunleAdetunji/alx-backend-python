#!/usr/bin/env python3
"""
This module contains an async coroutine function
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that takes in 2 int arguments. Spawns wait_random n times
    with the specified max_delay.
    args:
        n: The number of times to spawn wait_random
        max_delay: The argument to be supplied to the spawned function
    return:
        List of all the delays (float values). The list of the
        delays should be in ascending order without using sort() because of
        concurrency.
    """
    ls = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(ls)
