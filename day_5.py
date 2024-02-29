#!/usr/bin/python3
""" module containing solution to
day 5 task
"""


def my_discount() -> float:
    """ function that prompts the user to input
    the price and the discount(percentage) of the 
    product and then calculates the price after 
    discount  
    """
    
    price =  int(input("enter the price: "))
    discount = int(input("enter discount: "))
    new_price = price - (discount/100 * price)
    return new_price


# EXtra Challenge: Tuple of Student Sex
# return a list of tuplas that counts number
# of female and male seperately

from typing import List
students = ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']
def students_counter(students_list) ->List[tuple]:
    """ function that takes in a list of students as agument
    and returns a list of tuple that groups the students in
    into male and female and their count
    """
    optimised_list =[i.lower() for i in students_list] 
    male_count = optimised_list.count('male')
    female_count = optimised_list.count('female')
   
    list_of_tuples = f"[('Male', {male_count}), ('female', {female_count})]"
    return list_of_tuples

if __name__ == "__main__":
    print(my_discount())
    print(students_counter(students))