#!/usr/bin/env python3
"""Some async here"""


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """Some things here"""
    my_delay_list = []
    for _ in range(n):
        my_delay_list.append(await wait_random(max_delay))
    return sorted(my_delay_list)
