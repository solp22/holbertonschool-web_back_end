#!/usr/bin/env python3
"""measure_runtime module"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n : int, max_delay: int) -> float:
    """measure execution time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
