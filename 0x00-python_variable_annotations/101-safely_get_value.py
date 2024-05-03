#!/usr/bin/env python3
"""A file to function something that can be functioned"""
from typing import TypeVar, Any, Union, Mapping

T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default : Union[T, None] = None) -> Union[Any, T]:
    """Here we do stuff ain't gonna lie"""
    if key in dct:
        return dct[key]
    else:
        return default
