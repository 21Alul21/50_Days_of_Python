#!/usr/bin/env python3
""" module containing solution to day 16 tasks """
from typing import List


def sum_list(nested_list: List[List[int]]) -> str:
    """ function that accepts nested list of integers
    as argument and returns the sum
    """

    sum_val = 0
    for each_list in nested_list:
        sum_val += sum(each_list)
    return sum_val

if __name__ == '__main__':
    print(sum_list([[2,4,5,6], [2,3,5,6]])) #outputs 33