#!/usr/bin/python3
"""module doc"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function doc"""

    ans: Tuple[str, float] = (k, float(v**2))
    return ans
