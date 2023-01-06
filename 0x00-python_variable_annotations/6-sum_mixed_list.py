#!/usr/bin/env python3
"""
a program that converts all
arguments in a list to float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function that calculates the sum
    of a list of mixed types
    """

    total = 0

    for i in range(0, len(mxd_lst)):
        total = total + mxd_lst[i]
    return total
