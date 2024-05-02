#!/usr/bin/env python3
"""A file to function something that can be functioned"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Here we do stuff ain't gonna lie"""
    if lst:
        return lst[0]
    else:
        return None
