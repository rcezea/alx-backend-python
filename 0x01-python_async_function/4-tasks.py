#!/usr/bin/env python3
"""list of all the delays"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    # Create a list to store coroutine objects
    coroutines: List[asyncio.Task] = []

    # Generate coroutine objects for each task_wait_random call
    for _ in range(n):
        coroutine: asyncio.Task = task_wait_random(max_delay)
        coroutines.append(coroutine)

    # Wait for all coroutines to complete and gather their results
    results: List[float] = []
    for result in await asyncio.gather(*coroutines):
        if isinstance(result, float):
            results.append(result)

    # Sort the results in ascending order
    sorted_results: List[float] = sorted(results)

    # Return the sorted list of delays
    return sorted_results