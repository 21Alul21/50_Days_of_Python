""" module containing solution to day 14
task
"""
from typing import List


def flat_list(n_list: List[List]) -> List[int]:
    """ function that takes a nested list and flatten
    it to a 1D list
    """
    # flat_list = list(flat_list)
    # first = flat_list.pop(0)
    # last = flat_list.pop[-1]
    return n_list[0]

if __name__ == '__main__':
    print(flat_list([[1,2,3,4]]))