#!/usr/bin/env python3
"""Basic async syntax"""
import asyncio
import random


async def wait_random(max_delay=10):
    """A function to show an asynchronous coroutine"""
    time = random.uniform(0, max_delay + 1)
    await asyncio.sleep(time)
    return time
