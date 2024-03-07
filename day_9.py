#!/usr/bin/env python3
""" module containing solution to day 9 task """


def biggest_odd(num_str: str) -> int:
    """ function that takes a string of numbers 
     and returns the biggest odd number in the list
    """

    biggest_odd = [i for i in num_str if int(i) % 2 != 0]
    return max(biggest_odd)

if __name__ == "__main__":
    print(biggest_odd("23569"))