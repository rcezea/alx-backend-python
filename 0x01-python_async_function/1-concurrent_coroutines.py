#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function to show an asynchronous coroutine"""
    time: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(time)
    return time


async def wait_n(n: int, max_delay: int) -> list:
    """Run multiple coroutines in one module"""
    arr: list = []
    for i in range(n):
        delay: tuple = await asyncio.gather(wait_random(max_delay))
        arr.append(*delay)

    for x in range(len(arr)):
        for i in range(x + 1, len(arr)):
            if arr[x] > arr[i]:
                arr[x], arr[i] = arr[i], arr[x]
    return arr
