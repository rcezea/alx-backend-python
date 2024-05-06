#!/usr/bin/env python3
"""python module to create a function to return asyncio task"""
import asyncio
from asyncio import Task
from typing import Type, Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[Any]:
    """Return an asyncio task"""
    return asyncio.Task(wait_random(max_delay))
