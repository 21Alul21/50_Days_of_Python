""" module containing solution to day 18 task
"""


def any_number(*args: int|float):
    """ function that receives any number
    of arguments and returns the average
    of the numbers
    """

    sum = 0
    for arg in args:
        sum += arg
    return sum/len(args)

if __name__ == '__main__':
    print(any_number(34, 45, 45, 45))
