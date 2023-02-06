#!/usr/bin/env python3
'''Task 1
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Execute multiple coroutines at the same time with async
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return delays
