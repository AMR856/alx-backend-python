#!/usr/bin/env python3
"""Some async here"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Things here ain't gonna lie"""
    s = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
