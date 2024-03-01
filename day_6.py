#!/usr/bin/python3
""" module containing solution to day 6 tasks"""
from sys import argv 


def user_name() -> str:
    """function that generates username from the user's
    email
    """

    email = input('enter your email address: ')
    username = ''
    for char in email:
        if char == '@':
            break
        else:
            username += char
    return username

from typing import List
#Extra Challenge: Zero Both Ends
def zeroed(list_of_numbers: List[int]) -> list:
    """ function thst accepts a list of numbers
    as argument and returns a list with the first
    and last elements zeroed
    """

    list_of_numbers[0] = 0
    list_of_numbers[-1] = 0
    return list

if __name__ == '__main__':
      print(user_name())
      print(zeroed([1,2,3,4]))     # outputs [0,1,2,3,0]
     
