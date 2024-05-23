#!/usr/bin/env python3
""" module containing solution to day 14
task
"""
from typing import List


def flat_list(n_list: List[List]) -> List[int]:
    """ function that takes a nested list and flatten
    it to a 1D list
    """
  
    return n_list[0]



# Extra Challenge: Teacher's Salary
def your_salary():
    while True:
        try:
            name_teacher = input('enter the teacher\'s name: ' )
            period_number = int(input('number of periods taught in a month: '))
            rate = float(input('enter rate per period: '))
        except ValueError as e:
            print (f'error: {e}')
        else:
            if period_number > 100:
                extra_time = period_number - 100
                extra_time_sum = extra_time * 25
                gross = (100 * 20) + extra_time_sum
                return f'Teacher: {name_teacher},\n Period: {period_number}\n\
                    Gross salary: {gross}'
                
            else:
                gross = period_number * 20
                return f'Teacher: {name_teacher},\n Period: {period_number}\n\
                Gross salary: {gross}'
                



if __name__ == '__main__':
    print(flat_list([[1,2,3,4]]))

    print(your_salary())