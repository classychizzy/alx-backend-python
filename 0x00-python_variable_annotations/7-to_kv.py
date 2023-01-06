#!/usr/bin/env python3
"""
a program that returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """
    a function that returns a tuple of
    a string and a number
    """
    square = v * v
    tup1 = (k, square)
    return tup1
