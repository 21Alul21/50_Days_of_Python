#!/usr/bin/env python3\
""" module containing solution to day 12
task
"""

def count_dots(dotted_string: str) -> str:
    """ function that takes a string 
    seperated by dots as argument and
    conunts number of dots in the string
    """
    count = 0
    for i in dotted_string:
        if i == '.':
            count +=1
    
    return f'{count} dots'



if __name__ == '__main__':
    print(count_dots('a..s'))   # outputs 