#!/usr/bin/env python3
""" module containing solution to day 9 task """


def biggest_odd(num_str: str) -> int:
    """ function that takes a string of numbers 
     and returns the biggest odd number in the list
    """

    biggest_odd = [i for i in num_str if int(i) % 2 != 0]
    return max(biggest_odd)


from typing import List


# Extra Challenge: Zeros to the end
def zeroes_last(list_arg: list) -> List[int] | int: 
    """ function that takes a list as argument,
    and moves the zeros in the list to the front,
    else, it returns the list in acsending
    order
    """

    
    for i in list_arg:
        if list_arg.count(0) == 0:
            list_arg.sort(reverse=True)
            return list_arg
        else:
            zero_count = list_arg.count(0)
            list_copy = list_arg.copy()
            list_copy.remove(0)
            for i in range(zero_count):
                list_copy.append(0)
            return list_copy



if __name__ == "__main__":
    print(biggest_odd("123459"))         # returns 9   
    print(zeroes_last([2,1,0,0,4,76,0])) # returns [2, 1, 0, 4, 76, 0, 0, 0, 0]
    print(zeroes_last([2,1,4,76]))       # returns [76, 4, 2, 1]