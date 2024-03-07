#!/usr/bin/env python3
""" module containing solution to day 10 task """


def hide_password():
    """ function that takes an input
    from the user and returns a hidden
    password
    """

    password = input("enter your password: ")
    hidden_password = '*' * len(password) 
    return f'{hidden_password} your password is {len(password)} characters long\n\
    thank you'
    

if __name__ == '__main__':
    print(hide_password())