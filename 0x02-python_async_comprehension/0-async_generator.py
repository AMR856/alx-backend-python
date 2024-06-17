#!/usr/bin/env python3
"""Do you think?"""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """Ashely, Look at me"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
