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
names = ["peter", "John", "Andrew"]
def sort_length(str_lst: List[str]) -> List[str]:
    for i in range(len(str_lst) -1):
        if len(str_lst[i]) > len(str_lst[i + 1]):
            str_lst[i], str_lst[i + 1] = str_lst[i + 1], str_lst[i]
    return str_lst



if __name__ == '__main__':
    print(user_name())
    print(sort_length(names))