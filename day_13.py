#!/usr/bin/env python3
""" module containing slution to day 13 tasks
"""


def your_vat():
    """ function that returns the price of
    an item including the vat
    """
    while True:
        try:
            item_price = int(input('enter the item price: '))
            vat_percentage = int(input('enter your vat(%): '))

            item_and_vat = item_price * (1 + (vat_percentage/100))
            return f'your item price including vat is: {item_and_vat}'
            break
        except ValueError as e:
            print(f'error: {e}, please enter a number')

if __name__ == "__main__":
    print(your_vat()) 
