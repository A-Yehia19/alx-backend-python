#!/usr/bin/env python3
"""module doc"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function doc"""
    return [(i, len(i)) for i in lst]
