#!/usr/bin/env python3
"""Some async here"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """Check by yourself"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
