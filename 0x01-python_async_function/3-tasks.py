#!/usr/bin/env python3
"""python module to create a function to return asyncio task"""
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Return an asyncio task"""
    return Task(wait_random(max_delay))
