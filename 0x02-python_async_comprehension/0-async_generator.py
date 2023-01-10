#!/usr/bin/env python3
"""
a program that loops asynchronously
with a second wait time
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    an asynchronous function
    that loops 10 times
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
