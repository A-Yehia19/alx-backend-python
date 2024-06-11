#!/usr/bin/env python3
"""module doc"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """function doc"""
    if key in dct:
        return dct[key]
    else:
        return default
