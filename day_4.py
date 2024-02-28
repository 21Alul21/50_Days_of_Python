#!/usr/bin/python3
""" Day three task """


def only_floats(a: (float | int | str), b: (float | int | str)) -> int:
    """ function that takes two arguments and determine
     whether any or all of the arguments are floats
    """
    if isinstance(a, float) and isinstance(b, float):
        return 2
    if isinstance(a, float) or isinstance(b, float):
        return 1
    if not isinstance(a, float) and not isinstance(b, float):
        return 0
   

#testing the function for desired output    
print(only_floats(1.1, 2))
print(only_floats(1, 2))
print(only_floats(1.1, 2.0))
print(only_floats('S', 2.0))



#Extra Challenge: Index of the Longest Word

from typing import List

def word_index(lst_of_string: [List[str]]) -> int:
    """ function that takes a list of strings as
    argument and returns index of the longest word
    """
    
    unique_index = set()
    for element in lst_of_string:
        unique_index.add(len(element))
    
    if len(unique_index) == 1: #all the elments are of same length
        return 0
    else:
        new_copy = lst_of_string.copy() #made a copy of the list argument that was passed to the function
        new_list = [len(i) for i in new_copy] #using list comprehension to create a new list containing only the length values
        for i in new_list:
            if i == max(new_list):
                return new_list.index(i)
            
#testing the function to ensure that the desired outcome is achieved
print(word_index(["ioo", "er", "re"]))