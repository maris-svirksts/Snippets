#!python

# https://www.hackerrank.com/challenges/balanced-brackets/problem

import os

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    while True:
        initial_lenght = len(s)
        s.replace("()", '')
        s.replace("[]", '')
        s.replace("{}", '')
        if len(s) == initial_lenght:
            break
    
    if len(s) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
