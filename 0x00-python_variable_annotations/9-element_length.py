#!/usr/bin/env python3
"""
Annotated function that return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    This returns list of tuples.
    '''
    return [(i, len(i)) for i in lst]
