#!/usr/bin/env python3
""" 6. Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  returns their sum as a float """
    add: float = 0
    for i in mxd_lst:
        add += i
    return add
