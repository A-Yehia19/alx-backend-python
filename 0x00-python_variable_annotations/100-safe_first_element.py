#!/usr/bin/env python3
"""module doc"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """dunction doc"""
    if lst:
        return lst[0]
    else:
        return None
