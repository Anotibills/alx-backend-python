#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list that takes mxd_lst and returns their sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]):
    '''
    This returns sum of elements of mxd_list.
    '''
    return sum(mxd_lst)
