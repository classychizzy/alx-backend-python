#!/usr/bin/env python3
"""
a program that annotates type
to a list
"""

input_list: float = []

def sum_list(input_list) -> float:
    """
    a function that returns the
    sum of a list
    """
    sum = 0
    for i in range (0, len(input_list)):
        sum = sum + input_list[i]
    return sum
