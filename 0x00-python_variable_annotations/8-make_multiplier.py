#!/usr/bin/env python3
"""
a program that multiplies a float by
a multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that multiplies a float
    """
    return lambda x: x * multiplier
