""" module containing solution for day 19 task
"""


def count_words(str_: str) -> int:
    """ function that takes a string of words
     and returns the number of words are in the string
    """

    string_list = str_.split(' ')
    return (len(string_list))

def count_elements(str__: str) -> int:
    """ takes a string of words and counts
    how many elements are in the string
    """

    concat_string = ''
    for char in str__:
        if char == ' ':
            continue
        else:
            concat_string += char
    print(len(concat_string)) 

if __name__ == '__main__':
    count_words('I love learning') # returns 3
    count_elements('I love learning') # returns 13