#!/usr/bin/env python3
"""
This module contains an async generator function called async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine called async_generator that takes no arguments.
    The coroutine loops 10 times, each time asynchronously waiting for 1 second
    then yield a random number between 0 and 10.
    Args:

    Return:

    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
