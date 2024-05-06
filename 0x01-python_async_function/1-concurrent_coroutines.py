#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    arr: List[float] = []
    for _ in range(n):
        result = (await asyncio.gather(wait_random(max_delay)))[0]
        if isinstance(result, float):
            arr.append(result)
    return sorted(arr)
