#!/usr/bin/env python3
"""
This module contains a python async coroutine function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine function that takes in an integer argument that
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it
    args:
        max_delay: The upper bound of the random value
    return: The random number of secs that is generated
    """
    secs = random.uniform(0, max_delay)
    await asyncio.sleep(secs)
    return secs
