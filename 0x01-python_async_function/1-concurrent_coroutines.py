#!/usr/bin/env python3
"""This module demonstrates executing multiple coroutines using async."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of all the delays (float values).
    """
    arr = ()
    for i in range(n):
        arr += (await asyncio.gather(
            *(wait_random(max_delay))
        ))
    return sorted(arr)
