#!/usr/bin/env python3
from typing import List
"""A file to function something that can be functioned"""


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list: A list of floats
    Return:
        float
    """
    sum: float = 0
    for elm in input_list:
        sum = sum + elm
    return sum
