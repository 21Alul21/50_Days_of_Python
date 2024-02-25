#!/usr/bin/python3
"""day 1 challenge
"""
from math import sqrt


def divide_or_square(number: int) -> float:
    """function that takes one numeric argument and returns
    square root of the number if it is divisible 5 else 
    returns its reminder if it is not divisible by 5
    """

    if number % 5 == 0:
        return sqrt(number)
    else:
        return number % 5
    

""" Extra challenge for day 1"""
def longest_value(dict_arg: dict) -> str:
    """ function that takes a dictionary as an argument
    and returns the first longest value of the dictionary
    """

    max_value = max(dict_arg.values(), key=len)
    return max_value