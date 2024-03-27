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


# Extra Challenge: Unpack A Nest
def unpack_a_nest():
    """ code that generates a list of the numbers;
    34, 67, 78 from the nested list given below
    """
    nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    new_set = set()
    for i in nested_list:
        for j in i:
            if j == 34 or j == 67 or j ==78:
                new_set.add(j)
    return list(new_set)


if __name__ == '__main__':
    print(sum_list([[2,4,5,6], [2,3,5,6]]))   # outputs 33
    print(unpack_a_nest())                    # outputs [34, 67,  ]
