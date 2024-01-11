#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes k and v and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    This returns tuple consisting of k and the square of v.
    '''
    return (k, v * v)
