#!/usr/bin/env python3
"""list of all the delays"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    arr: List[float] = []
    for _ in range(n):
        result = (await asyncio.gather(task_wait_random(max_delay)))[0]
        if isinstance(result, float):
            arr.append(result)
    return sorted(arr)