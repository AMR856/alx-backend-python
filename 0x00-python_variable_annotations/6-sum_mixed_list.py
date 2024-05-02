#!/usr/bin/env python3
from typing import List, Union
"""A file to function something that can be functioned"""


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    Args:
        mxd_lst: A list of floats or integers
    Return:
        float
    """
    sum: float = 0
    for elm in mxd_lst:
        sum = sum + elm
    return sum
