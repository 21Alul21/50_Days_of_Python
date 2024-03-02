#!/usr/bin/env python3
""" module containing day 8 solution """
from typing import List


def odd_even(number_list: List[int]) -> int:
    """ function that returns the difference
    between the largest even number in the list
    and the smallest odd number
    """
 
    
    
    odd_list = list()
    even_list = list()

    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
             odd_list.append(num)

    max_even = max(even_list)
    min_odd = min(odd_list)         
  
    return max_even - min_odd

    
if __name__ == "__main__":
      print(odd_even([2,3,4,5,6,7])) # outputs 3


