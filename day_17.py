""" module containig solution to day 17 task """
import random


def user_name():
    """ function that creates username for a user
    by taking their name as inpu and adding a random
    integer at the end of the reversed input
    """

    name = input("enter your name: ")
    rand_num = random.choice(range(10))
    return f'{name[::-1]}' + str(rand_num)

if __name__ == '__main__':
    print(user_name())