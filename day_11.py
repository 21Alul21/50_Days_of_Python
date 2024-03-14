#!/usr/bin/env python3
""" module containing solutions to day 11 tasks """


def equal_strings(str1: str, str2: str) -> bool:
    """ takes two strings as arguments, compares
    them and returns true if they have the same
    characters and length, else returns false
    """
    
    if len(str1) == len(str2):
        for i in str1:
            if i in str2:
                continue
                
            else:
                break
        else:
            return True
                    
        
    return False

# Extra Challenge: Swap Values
from typing import List
def swap_values(list_arg: List[int]) -> List[int]:
    """" function that takes list of numbers and
    swaps the first element with the last element
    """

    first_int = list_arg[0]
    last_int = list_arg[-1]
    list_arg.pop(0)
    list_arg.pop(-1)
    list_arg.insert(0, last_int)
    list_arg.append(first_int)
    
    
    return list_arg
                
if __name__ == '__main__':
    print(equal_strings('love', 'volt'))    # outoputs false
    print(swap_values([1,23,5,6]))          # outputs [6, 23, 5, 1]
