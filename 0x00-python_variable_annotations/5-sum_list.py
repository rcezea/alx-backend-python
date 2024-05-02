#!/usr/bin/env python3
""" 5. Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns their sum as a float """
    add: float = 0
    for i in input_list:
        add += i
    return add
