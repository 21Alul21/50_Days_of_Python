#!/usr/bin/env python3
""" module containing solutions to day 11 tasks """


def equal_strings(str1: str, str2: str) -> bool:
    """ takes two strings as arguments, compares
    them and returns true if they have the same
    characters and length, else returns false
    """
    
    if len(str1) == len(str2):
        for i in str1:
            if i in str2:
                continue
                
            else:
                break
        else:
            return True
                    
        
    return False
                
if __name__ == '__main__':
    print(equal_strings('live', 'vole'))