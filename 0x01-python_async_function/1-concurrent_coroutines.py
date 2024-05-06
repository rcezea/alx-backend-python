#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
import importlib

module_name = importlib.import_module("0-basic_async_syntax")
wait_random = module_name.wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Run multiple coroutines"""
    arr: list = []
    for i in range(n):
        delay: tuple = await asyncio.gather(wait_random(max_delay))
        arr.append(*delay)

    for x in range(len(arr)):
        for i in range(x + 1, len(arr)):
            if arr[x] > arr[i]:
                arr[x], arr[i] = arr[i], arr[x]
    return arr
