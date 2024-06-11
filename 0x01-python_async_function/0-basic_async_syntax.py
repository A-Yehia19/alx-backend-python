#!/usr/bin/env python3
"""module doc"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """function doc"""

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
