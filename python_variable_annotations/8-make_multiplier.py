#!/usr/bin/env python3
"""make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return func that mul 'multiplier' by float"""
    def mul(num: float) -> float:
        """multiply 'multiplier' by float"""
        return num * multiplier
    return mul
