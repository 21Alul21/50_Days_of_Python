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


# Extra Challenge: What's My Age?
def your_age():
    name_age = {'jane': 23, 'kerry': 45, 'tim': 34, 'peter': 27}
    name = input('enter your name: ').lower()
    

    if name in name_age:
        return f'Hi, {name.title()}, you are {name_age[name]} years old' 
    else:
        try:
            print("your name is not in the dictionary")
            new_user_age = int(input("enter your age: "))
            name_age[name] = new_user_age  #alternatively do: new_age.update({name: new_user_age})
            return f'Hi, {name.title()}, you are {new_user_age} years old'
        except ValueError as e:
            return f'error: {e}'
        
    
if __name__ == "__main__":
    print(same_in_reverse('dad'))  # outputs True
    print(your_age())
    