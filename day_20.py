""" module containing solution to day 20
    task
"""


def capitaliz(str_: str) -> str:
    """ function that takes a string as an argument
    and capitalizes the first letter of each word
    """

    return str_.title()

if __name__ == '__main__':
    print(capitaliz('i love learning')) # outputs: I Love Learning


#Extra Challenge

# code that prints a list from a string, the list should contain
# only words with capital letter(s) and in reversed order

str1 = 'leArning is hard, bUt if You appLy youRself '\
    'you can achieVe success'
upper_list = list()

str_list = str1.split(' ')
for word in str_list:
    for char in word:
        if char.isupper():
            rev_word = word[::-1]
            upper_list.append(rev_word)
print(upper_list)   # outputs: ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
    
