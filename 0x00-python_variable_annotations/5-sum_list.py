#!/usr/bin/python3
"""module doc"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function doc"""

    sum: float = 0
    for num in input_list:
        sum += num

    return sum
