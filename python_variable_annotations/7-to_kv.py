#!/usr/bin/env python3
"""to_v module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """reutrn a tuple w first elem and sec elem**2"""
    return k, v ** 2
