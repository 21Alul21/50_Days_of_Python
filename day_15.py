#!/usr/bin/env python3
""" module containing solution for the
day 15 task
"""

def same_in_reverse(string_arg: str) -> bool:
    """ function returns True or False if 
    the argument(string) reads same in reverse
    """

    str_reverse = string_arg[::-1]
    if str_reverse == string_arg:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(same_in_reverse('dal'))  # outputs True