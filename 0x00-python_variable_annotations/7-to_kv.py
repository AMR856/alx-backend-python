#!/usr/bin/env python3
"""A file to function something that can be functioned"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: a string ngl
        v: an integer or a float
    Return:
        a tuple of a string and an integer
    """
    myTuple: Tuple[str, float] = tuple()
    myTuple = k, v ** 2
    return myTuple
