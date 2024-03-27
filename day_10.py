#!/usr/bin/env python3
""" module containing solution to day 10 task """


def hide_password():
    """ function that takes an input
    from the user and returns a hidden
    password
    """

    password = input("enter your password: ")
    hidden_password = '*' * len(password)
    return f'{hidden_password} your password is {len(password)} characters long\n\
    thank you'
    
from typing import List
def convert_numbers(list_arg: List[int]) -> List[str]:
    """ function that receives a list of integers
    and convert it to a list of string
    with comma seperation
    """

    comma_sep_list = list()
    
    for i in list_arg:
        str_val = ''
        count = 0
        i_string = str(i)
        i_string_rev = i_string[::-1]
        for j in i_string_rev:
            count += 1
            if count % 3 == 0:
                str_val += j
                str_val += ','
            else:
                str_val += j
        
        
        last_rev = str_val[::-1]
        comma_sep_list.append(last_rev)
if __name__ == '__main__':


    print(hide_password())
    print(convert_numbers([100000, 20000000, 23440000]))