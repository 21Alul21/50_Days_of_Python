#!/usr/bin/env python3
""" module that contains solutions to day 7 tasks """


def string_range(num: int) -> str:
    """ function that takes a single number and and returns a
    string of it's range
    """
    range_value = [str(i) for i in range(num)]
    modified_string = ".".join(range_value)
    return (modified_string)


#Extra Challenge:   Dictionary of names
names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jubulani",
         "Sera", "Patel", "Sera"]
# the solution should return -> {"Sasha": 1, "Sera": 2} which is a 
# dictionary containing names starting with S and the number of times
# it occurs

from typing import List

def dictionary_of_names(list_arg: List[str]) -> dict[str]:
    """ function that returns a dictionary of names 
    from a list passed to it
    """

    s_names = {name:list_arg.count(name) for name in list_arg if name[0] == 'S'}
    return s_names

if __name__ == '__main__':
    print(string_range(5))   # outputs "0.1.2.3.4"
    print(dictionary_of_names(names))     # ouputs {'Sasha': 1, 'Sera': 2}
