#!/usr/bin/env python3
"""Do you think?"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Ashely, Look at me"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
