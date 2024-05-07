#!/usr/bin/env python3
"""Create an async comprehension"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of random numbers using async comprehension"""
    return [i async for i in async_generator()]
