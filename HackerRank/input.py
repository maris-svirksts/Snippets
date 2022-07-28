#! python

# https://www.hackerrank.com/challenges/input/problem

import re

variable, end_result = input().split()

calculation = re.sub('x', variable, input())

result = eval(calculation)

if int(result) == int(end_result):
    print('True')
else:
    print('False')