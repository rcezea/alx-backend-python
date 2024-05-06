#!/usr/bin/env python3
"""Python that that creates a function to measure the average time"""
from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the average waiting time"""
    start: float = time()
    asyncio.run(wait_n(n, max_delay))
    stop: float = time()
    value: float = (stop - start) / n
    return value
