#!/usr/bin/env python3
"""A file to function something that can be functioned"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        float
    Return:
        A function that takes a float as a
        parameter and returns a float
    """
    def myfunction(my_number: float) -> float:
        """
        Args:
            float
        Return:
            float
        """
        return multiplier * my_number
    return myfunction
