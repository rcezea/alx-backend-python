#!/usr/bin/env python3
"""Create a new function to alter wait_n"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple coroutines in one module"""
    arr: List[float] = []
    for _ in range(n):
        arr.append(await wait_random(max_delay))
    task_wait_random(max_delay)
    return sorted(arr)
