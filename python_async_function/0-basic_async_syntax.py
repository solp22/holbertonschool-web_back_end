#!/usr/bin/env python3
"""basic_async_sytanx module"""
import random
import asyncio


async def wait_random(max_delay=10):
    """wait random number and then return"""
    wait = random.unifrom(0, max_delay)
    await asyncio.sleep(wait)
    return wait
