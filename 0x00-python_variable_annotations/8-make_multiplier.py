#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function"""
    def mul(n: float) -> float:
        return n * multiplier
    return mul
