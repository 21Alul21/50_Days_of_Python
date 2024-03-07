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


# Extra Challenge: List of Prime numbers
from typing import List


def prime_numbers() -> List[int]:
    """ function that asks the user for
    input and returns a list of prime numbers
    within its range
    """
    prime_list = list()
    try:
        value = int(input("enter a number: "))
        for i in range(0, value + 1):   # looping through the elements in the value/input range
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                    else:
                        prime_list.append(i)
        return prime_list
                    

    except ValueError as e:
        return f"please enter a number, {e}"

    
if __name__ == "__main__":
      print(odd_even([2,3,4,5,6,7])) # outputs 3
      print(prime_numbers())


