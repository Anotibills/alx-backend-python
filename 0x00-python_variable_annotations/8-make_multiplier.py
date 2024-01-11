#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes multiplier and returns it
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    This returns `multiplier`
    '''
    return lambda x: x * multiplier
