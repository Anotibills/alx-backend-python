#!/usr/bin/env python3
"""
Type-annotated function sum_list that takes input_list and returns their sum
"""
from typing import List


def sum_list(input_list: List[float]):
    '''
    This returns sum of all elements in input_list.
    '''
    return sum(input_list)
