


def decorator(func):
    def wrapper(a, b):
        print('inside the wrapper')
        new_sum = func(a, b) + 9
        return new_sum
    return wrapper


@decorator
def sumed(a, b):
    return a + b




print(sumed(43, 5))
