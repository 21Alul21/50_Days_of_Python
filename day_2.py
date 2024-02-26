#!/usr/bin/python3
""" solution for day two """
from typing import List


def convert_add (list_param: [List[str]]) -> int:
    """ function that accepts list containing string as argument
     and converts the elements to integer and returns the sum
    """

    try:
        converted_list = [int(i) for i in list_param]
        print(converted_list)
        sum = 0
        for i in converted_list:
            sum += i
        return sum
    except ValueError as e:
        print('your list must only contain string literals: ', str(e))
    


#testing the function
print(convert_add(['1', '8']))

#testing the function, a ValueError is raised
print(convert_add(['1', 'b']))



#Extra challenge:
def check_duplicates(list_param: [List[str]]) -> str:
    """ checks if a list argument contains duplicate string values,
     if it does, return the duplicates, else, it should return
    'no duplictes'
    """

    for i in list_param:
        if list_param.count(i) >= 2:
            return i
        else:
            return 'no duplicates'

#testing the second function
print(check_duplicates(['boy', 'hello']))