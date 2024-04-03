""" module containig solution to day 17 task """
import random


def user_name() -> str:
    """ function that creates username for a user
    by taking their name as inpu and adding a random
    integer at the end of the reversed input
    """

    name = input("enter your name: ")
    rand_num = random.choice(range(10))
    return f'{name[::-1]}' + str(rand_num)


from typing import List
# Extra Challenge: Sort by Length
names = ["peter", "John", "Andrew", 'ft', 'g']
def sort_length(str_lst: List[str]) -> List[str]:
    """ function that takes a list of strings as an
    argument and sorts the strings in ascending order
    acording to their length 
    """

    for i in range(len(names)):
        for j in range((len(names) -1) ):
            if len(names[j]) > len(names[j + 1]):
                names[j], names[j + 1] = names[j + 1], names[j]
    return names


if __name__ == '__main__':
    #print(user_name())
    print(sort_length(names)) 