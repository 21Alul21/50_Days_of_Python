#!/usr/bin/env python3
""" module containing slution to day 13 tasks
"""


def your_vat():
    """ function that returns the price of
    an item including the vat
    """
    while True:
        try:
            item_price = int(input('enter the item price($): '))
            vat_percentage = int(input('enter your vat(%): '))

        except ValueError as e:
            print(f'error: {e}, please enter a number')
        
        else:
            item_and_vat = item_price * (1 + (vat_percentage/100))
            return f'your item price including vat is: {item_and_vat}'
            break


# Extra Challenge: Pyramid of Snakes
def python_snakes(num):
    """ function that an argument and 
    and creates a shape using the range
    """
    for i in range(1, num):
        print('*' * i)

if __name__ == "__main__":
    print(your_vat())
    python_snakes(7) 
