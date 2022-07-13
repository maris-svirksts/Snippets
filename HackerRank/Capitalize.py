#!/bin/python3

# https://www.hackerrank.com/challenges/capitalize/problem

import os

# Complete the solve function below.
def solve(s):
    s_as_list = s.split(" ")
    
    for idx, word in enumerate(s_as_list):
        s_as_list[idx] = s_as_list[idx].capitalize()
    
    return " ".join(s_as_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

