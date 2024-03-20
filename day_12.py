#!/usr/bin/env python3
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


#Extra Challenge: Your Age in minutes
from datetime import datetime

def age_in_minutes():
    while True:
        try:
            birth_year = input('enter your birth year: ')
            if len(birth_year) != 4:
                print('invalid input, enter 4 digits for birth year')
            if int(birth_year) < 1900:
                print('your input is invalid, enter a birth year that is \
                        greater than or equal to 1900')
            if int(birth_year) > int(datetime.now().strftime('%Y')):
                print('input a valid year, you are ahead of time')
            
        except Exception as e:
            print(f'erorr: {e}')
        
        else:
                age = (int(datetime.now().strftime('%Y'))) - int(birth_year) 
                return f' You are {age * 525600} mins old'
                break


if __name__ == '__main__':
    print(count_dots('a..s'))   # outputs 2
    print(age_in_minutes())     # outputs your age in mins

