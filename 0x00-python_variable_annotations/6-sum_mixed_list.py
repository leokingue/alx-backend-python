#!/usr/bin/env python3
''' mixed list '''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    returns sum as a float
    '''
    return float(sum(mxd_list))
