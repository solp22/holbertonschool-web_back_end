#!/usr/bin/env python3
"""async_comprehension module"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() ->  List[float]:
    """collect 10 numbers from generator"""
    generator_list = []
    async for item in async_generator():
        generator_list.append(item)
    return generator_list
