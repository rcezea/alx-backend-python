#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    add: float = 0
    times = [await asyncio.gather(*(async_comprehension() for _ in range(4)))]
    for i in times:
        add += i[0][0]
    return add
