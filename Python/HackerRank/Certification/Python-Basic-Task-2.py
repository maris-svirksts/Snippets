#!/bin/python3

import os
from string import ascii_lowercase

#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    letters = ascii_lowercase
    missing_letters = "".join([i for i in letters if i not in s])
    missing_digits  = "".join([str(i) for i in range(10) if str(i) not in s])
    
    return(missing_digits + missing_letters)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
