#!/usr/bin/python3
"""module doc"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """function doc"""

    sum: float = 0
    for num in mxd_list:
        sum += num

    return sum
