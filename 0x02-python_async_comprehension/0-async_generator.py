#!/usr/bin/env python3
"""Python module to practice async comprehensions"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ function to yield a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
