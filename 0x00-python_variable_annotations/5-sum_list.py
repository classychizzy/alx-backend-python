#!/usr/bin/env python3
"""
a program that annotates type
to a list
"""

from typing import List


def sum_list(input_list: List[float]):
    """
    a function that returns the
    sum of a list
    """
    sum = 0
    for i in range(0, len(input_list)):
        sum = sum + input_list[i]
    return sum
