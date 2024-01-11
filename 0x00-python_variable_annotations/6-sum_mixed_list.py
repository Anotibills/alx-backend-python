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


if __name__ == '__main__':
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)

    print(sum_mixed_list.__annotations__)
    print(ans == sum(mixed))
    print(f"sum_mixed_list(mixed) returns {ans} "
          f"which is a {type(ans)}")
