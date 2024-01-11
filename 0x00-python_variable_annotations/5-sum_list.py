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


if __name__ == '__main__':
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)

    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print(f"sum_list(floats) returns {floats_sum} "
          f"which is a {type(floats_sum)}")
