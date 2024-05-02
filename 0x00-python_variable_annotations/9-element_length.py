#!/usr/bin/env python3
"""A file to function something that can be functioned"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst: an interable of a sequence
        Return:
            A list of tuples of somethings
    """
    return [(i, len(i)) for i in lst]
