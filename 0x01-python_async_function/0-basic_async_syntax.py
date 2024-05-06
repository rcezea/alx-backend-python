#!/usr/bin/env python3
"""Basic async syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function to show an asynchronous coroutine"""
    time: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(time)
    return time
