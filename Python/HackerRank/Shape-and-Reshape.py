#!python

# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

input_data = numpy.array(input().split(), int)
print(numpy.reshape(input_data, (3, 3)))