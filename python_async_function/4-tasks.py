#!/usr/bin/env python3
"""tasks module"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """call wait random n times"""
    delay_list = []
    for i in range(n):
        delay = await(task_wait_random(max_delay))
        delay_list.append(delay)
    return sorted(delay_list)