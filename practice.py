
""" Extra challenge for day 1"""
def longest_value(dict_arg: dict) -> str:
    """ function that takes a dictionary as an argument
    and returns the first longest value of the dictionary
    """

    max_value = max(dict_arg.values(), key=len)
    return max_value




print(longest_value({"hi": "alll", "hey": "everyone"}))