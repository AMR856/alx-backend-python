#!/usr/bin/env python3
"""Do you think?"""
import asyncio
import time

async_comprehensionr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Nah, Blud needs a docs fr"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehensionr() for i in range(4)))
    return time.perf_counter() - start_time
