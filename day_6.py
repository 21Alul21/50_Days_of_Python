#!/usr/bin/python3
""" module containing solution to day 6 tasks"""
from sys import argv 


def user_name():
    """function that generates username from the user's
    email
    """

    email = input('enter your email address: ')
    username = ''
    for char in email:
        if char == '@':
            break
        username += char
    return username

if __name__ == '__main__':
	print(user_name())
