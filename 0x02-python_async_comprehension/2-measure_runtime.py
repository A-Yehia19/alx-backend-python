#!/usr/bin/env python3
"""module doc"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function doc"""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()

    return end - start
