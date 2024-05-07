#!/usr/bin/env python3
"""Some async here"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Do you think I'm a joke to you"""
    return asyncio.create_task(wait_random(max_delay))
