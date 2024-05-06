#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List, Tuple

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple coroutines in one module"""
    delay = [wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*delay)
    return sorted(delay)
