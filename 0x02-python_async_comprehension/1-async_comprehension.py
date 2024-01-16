#!/usr/bin/env python3
"""
This module contains a coroutine called async_comprehension
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine called async_comprehension that takes no arguments.
    The coroutine collects 10 random numbers using an async comprehension over
    async_generator, then return the 10 random numbers.

    Args:

    Return:
    """
    return [i async for i in async_generator()]
