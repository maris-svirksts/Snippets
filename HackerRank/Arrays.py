#!python

# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    return numpy.flip(numpy.array(arr, float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)