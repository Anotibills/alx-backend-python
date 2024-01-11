#!/usr/bin/env python3
"""
Adding type annotations to the function provided
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    This returns dct[key] if it exists, otherwise return `default`.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
