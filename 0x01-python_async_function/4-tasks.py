#!/usr/bin/env python3
"""Some async here"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Some things here"""
    my_delay_list = []
    for _ in range(n):
        my_delay_list.append(await task_wait_random(max_delay))
    return sorted(my_delay_list)
