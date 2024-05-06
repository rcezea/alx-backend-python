#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Run multiple coroutines in one module"""
    arr: list[float] = [float]
    for i in range(n):
        delay: tuple[float] = await asyncio.gather(wait_random(max_delay))
        arr.append(*delay)

    return sorted(arr)
