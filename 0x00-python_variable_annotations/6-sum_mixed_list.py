#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    add: float = 0
    for i in mxd_lst:
        add += i
    return add
