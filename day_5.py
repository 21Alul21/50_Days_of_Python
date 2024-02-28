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

if __name__ == "__main__":
    print(my_discount())
